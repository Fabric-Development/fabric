import gi
import re
import os
import time
import math
import cairo
import shlex
import string
import random
import inspect
from enum import Enum
from loguru import logger
from functools import wraps
from dataclasses import dataclass
from collections.abc import Callable, Iterable, Generator
from typing import (
    cast,
    Literal,
    NamedTuple,
    Union,
    TypeAlias,
    Generic,
    TypeVar,
    ParamSpec,
    Any,
)

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject, Gio, GLib

P = ParamSpec("P")
T = TypeVar("T")
E = TypeVar("E", bound=Enum)
MISSING = TypeVar("MISSING")
Number: TypeAlias = int | float


class __DeprecationHook__:
    def __init__(self, deprecated_to_replacement: dict[str, str]):
        self.lookup_table = deprecated_to_replacement

    def __call__(self, additional_message: str | None = None):
        if replacement := self.lookup_table.get(
            (caller := inspect.currentframe().f_back.f_code.co_name),  # type: ignore
            None,
        ):
            return logger.warning(
                f"the function `{caller}` is deprecated and will removed in later versions of Fabric, consider using `{replacement}` instead"
            )
        return


__deprecation_table = __DeprecationHook__(
    {
        "idlify": "idle_add",
        "set_stylesheet_from_string": "Application.add_stylesheet_from_string",
        "set_stylesheet_from_file": "Application.add_stylesheet_from_file",
        "get_gdk_rgba": "Gdk.RGBA.parse OR parse_color",
    }
)


class PixbufUtils:
    @staticmethod
    def from_cairo_surface(
        surface: cairo.ImageSurface,
        x_offset: int = 0,
        y_offset: int = 0,
        target_width: int | None = None,
        target_height: int | None = None,
    ) -> GdkPixbuf.Pixbuf:
        return Gdk.pixbuf_get_from_surface(
            surface,  # type: ignore
            x_offset,
            y_offset,
            target_width or surface.get_width(),
            target_height or surface.get_height(),
        )

    @staticmethod
    def set_cairo_source(
        pixbuf: GdkPixbuf.Pixbuf,
        cr: cairo.Context,
        x_offset: int = 0,
        y_offset: int = 0,
    ):
        return Gdk.cairo_set_source_pixbuf(cr, pixbuf, x_offset, y_offset)  # type: ignore

    @staticmethod
    def rotate(pixbuf: GdkPixbuf.Pixbuf, angle: float) -> GdkPixbuf.Pixbuf:
        """return a rotated version of the given `GdkPixbuf.Pixbuf` to a given angle

        :param pixbuf: the input pixbuf
        :type pixbuf: GdkPixbuf.Pixbuf
        :param angle: the desired rotation angle in degrees
        :type angle: float
        :return: the newly rotated pixbuf
        :rtype: GdkPixbuf.Pixbuf
        """
        r = math.radians(angle)
        w, h = pixbuf.get_width(), pixbuf.get_height()

        nw = round(abs(w * math.cos(r)) + abs(h * math.sin(r)))
        nh = round(abs(w * math.sin(r)) + abs(h * math.cos(r)))

        surface = cairo.ImageSurface(cairo.Format.ARGB32, nw, nh)
        cr = cairo.Context(surface)

        cr.translate(nw / 2, nh / 2)
        cr.rotate(r)
        PixbufUtils.set_cairo_source(pixbuf, cr, round(-w / 2), round(-h / 2))
        cr.paint()

        return PixbufUtils.from_cairo_surface(
            surface, target_width=nw, target_height=nh
        )


class FormattedString:
    """simple string formatter made to be baked mid-runtime"""

    class FormatDict(dict):
        def __init__(self, *args, **kwargs):
            super(FormattedString.FormatDict, self).__init__(*args, **kwargs)

        def __missing__(self, key):
            try:
                rkey = eval(key, globals(), self)
            except Exception as e:
                logger.warning(
                    f"[FormattedString] couldn't format string expression ({key}), raised exception is\n {str(e)}"
                )
                rkey = key.join("{}")
            return rkey

    def __init__(self, string: str, **kwargs) -> None:
        self.__string__ = string
        self.__format_map__ = kwargs

    def __call__(self, **kwargs) -> str:
        return self.format(**kwargs)

    def format(self, **kwargs) -> str:
        return self.__string__.format_map(
            FormattedString.FormatDict(self.__format_map__ | kwargs)
        )


@dataclass(init=False)
class DesktopApp:
    name: str
    generic_name: str | None
    display_name: str | None
    description: str | None
    window_class: str | None
    executable: str | None
    command_line: str | None
    icon: (
        Gio.Icon
        | Gio.ThemedIcon
        | Gio.FileIcon
        | Gio.LoadableIcon
        | Gio.EmblemedIcon
        | None
    )
    icon_name: str | None
    hidden: bool

    def __init__(
        self, app: Gio.DesktopAppInfo, icon_theme: Gtk.IconTheme | None = None
    ):
        self._app: Gio.DesktopAppInfo = app
        self._icon_theme = icon_theme or Gtk.IconTheme.get_default()
        self._pixbuf: GdkPixbuf.Pixbuf | None = None
        self.name = app.get_name()  # type: ignore
        self.generic_name = app.get_generic_name()  # type: ignore
        self.display_name = app.get_display_name()  # type: ignore
        self.description = app.get_description()  # type: ignore
        self.window_class = app.get_startup_wm_class()  # type: ignore
        self.executable = app.get_executable()  # type: ignore
        self.command_line = app.get_commandline()  # type: ignore
        self.icon = app.get_icon()  # type: ignore
        self.icon_name = self.icon.to_string() if self.icon is not None else None  # type: ignore
        self.hidden = app.get_is_hidden()

    def launch(self):
        return self._app.launch()  # type: ignore

    def get_icon_pixbuf(
        self,
        size: int = 48,
        default_icon: str | None = "image-missing",
        flags: Gtk.IconLookupFlags = Gtk.IconLookupFlags.FORCE_REGULAR
        | Gtk.IconLookupFlags.FORCE_SIZE,  # type: ignore
    ) -> GdkPixbuf.Pixbuf | None:
        """
        get a pixbuf from the icon (if any)

        :param size: the size of the icon, defaults to 48
        :type size: int, optional
        :param default_icon: the name of the default icon. pass None if you want to receive None upon failing, defaults to "image-missing"
        :type default_icon: str | None, optional
        :param flags: the Gtk.IconLookupFlags to use when fetching the icon
        :type flags: Gtk.IconLookupFlags, defaults to (Gtk.IconLookupFlags.FORCE_REGULAR | Gtk.IconLookupFlags.FORCE_SIZE), optional
        :return: the pixbuf
        :rtype: GdkPixbuf.Pixbuf | None
        """
        if self._pixbuf:
            return self._pixbuf  # already loaded
        try:
            if not self.icon_name:
                raise
            self.icon
            self._pixbuf = self._icon_theme.load_icon(
                self.icon_name,
                size,
                flags,
            )
        except Exception:
            self._pixbuf = (
                self._icon_theme.load_icon(default_icon, size, flags)
                if default_icon is not None
                else None
            )

        return self._pixbuf


def get_desktop_applications(include_hidden: bool = False) -> list[DesktopApp]:
    """
    get a list of all desktop applications
    this might be useful for writing application launchers

    :param include_hidden: whether to include applications unintended to be visible to normal users, defaults to false
    :type include_hidden: bool, optional
    :return: a list of all desktop applications
    :rtype: list[DesktopApp]
    """
    icon_theme = Gtk.IconTheme.get_default()
    return [
        DesktopApp(app, icon_theme)
        for app in Gio.DesktopAppInfo.get_all()
        if include_hidden or app.should_show()
    ]


def parse_color(color: str | Iterable[Number]) -> Gdk.RGBA:
    """parse a serialized color data over to a `Gdk.RGBA` object

    :param color: the color data, example of an iterable color; `(255, 255, 255) / (255, 255, 255, 255)`, for a list of parseable string formats head over to https://docs.gtk.org/gdk3/method.RGBA.parse.html
    :type color: str | Iterable[Number]
    :raises ValueError: if the passed in color data is unparsable
    :return: the newly created `Gdk.RGBA` (alpha is set to opaque if the passed in color data is RGB only)
    :rtype: Gdk.RGBA
    """
    if (
        isinstance(color, (tuple, list))
        and (color_len := len(color)) >= 3
        and color_len <= 4
    ):
        return Gdk.RGBA(*[c / 255.0 for c in color])
    elif isinstance(color, str):
        rgba = Gdk.RGBA()
        if rgba.parse(color):
            return rgba
    raise ValueError(f"{color} is an invalid color format")


def get_gdk_rgba(color: str | Iterable[Number]) -> Gdk.RGBA:
    __deprecation_table()
    return parse_color(color)


def compile_css(
    css_string: str,
    base_path: str = ".",
    exposed_functions: dict[str, Callable] | Iterable[Callable] | None = None,
) -> str:
    """
    preprocess and transpile a CSS string to GTK's CSS syntax.

    supports transpiling web-css like variables over to GTK's `@define-color` syntax.

    also supports having CSS macros. syntax example:
    .. code-block:: css
        /* define a macro */
        @define my-macro(--arg-1, --arg-2) {
            /* CSS body goes here. example body.. */
            color: --arg-1;
            background-color: --arg-2;
        }

        #my-widget {
            @apply my-macro(red, blue);
            /* compiles to
                color: --arg-1;
                background-color: --arg-2;
            */
        }

    **Note:** this function relies on a series of regular expressions for its processing, which may lead to potential issues in certain edge cases.

    :param css_string: the input CSS as a string.
    :type css_string: str
    :param base_path: for `@import` statements, used for relative imports.
    :type base_path: str, optional
    :param exposed_functions: a dictionary of macro functions or an iterable of callable functions to use as extra macros. if a dictionary is provided, the keys are macro names, and the values are the corresponding functions.
    :type exposed_functions: dict[str, Callable] | Iterable[Callable] | None, optional
    :return: the compiled CSS string converted to GTK's CSS syntax.
    :rtype: str
    """

    import_pattern = re.compile(r'@import\s+(?:url\()?["\']?([^"\')]+)["\']?\)?\s*;')

    vars_selector_pattern = re.compile(r":vars\s*{\s*([^}]+)\s*}")
    vars_declaration_pattern = re.compile(r"--([\w-]+)\s*:\s*([^;]+)\s*;")
    vars_reference_pattern = re.compile(r"var\(--([\w-]+)\)")

    constant_pattern = re.compile(r"@define\s+([\w-]+)\s+([^;]+);")
    constant_apply_pattern = re.compile(r"apply\(([\w-]+)\)")

    macro_pattern = re.compile(r"@define\s+([\w-]+)\(([^)]*)\)\s*{\s*([^}]+)\s*}")
    macro_apply_pattern = re.compile(r"@apply\s+([\w-]+)\(([^)]*)\)\s*;?")

    functions_map: dict[str, Callable] = (
        {}
        if not exposed_functions
        else (
            {
                snake_case_to_kebab_case(func.__name__): func
                for func in (
                    exposed_functions
                    if not isinstance(exposed_functions, Callable)
                    else (exposed_functions,)
                )
            }
            if isinstance(exposed_functions, (list, tuple, Callable))
            else exposed_functions
        )
    )  # type: ignore

    def resolve_imports(css_content: str) -> str:
        def import_replacement(match: re.Match) -> str:
            file_path = match.group(1)
            full_path = os.path.join(base_path, file_path)

            try:
                with open(full_path, "r") as imported_file:
                    imported_content = imported_file.read()
                return resolve_imports(imported_content)
            except Exception as e:
                logger.warning(
                    f"[FASS] couldn't find the imported file: {full_path}, Error: {e}"
                )
                return f"/* couldn't import file: {file_path} */"

        return import_pattern.sub(import_replacement, css_content)

    # resolve @import statements before passing over to the preprocessor
    css_output = resolve_imports(css_string)

    # color variables
    match = vars_selector_pattern.search(css_output)
    css_output = (
        f"{match.group(1)}\n\n{css_output.replace(match.group(0), '')}"
        if match
        else css_output
    )

    # this could be preprocessed as the original value not (a translation to Gtk's syntax)
    css_output = vars_declaration_pattern.sub(
        lambda m: f"@define-color {m.group(1)} {m.group(2)};", css_output
    )
    css_output = vars_reference_pattern.sub(r"@\1", css_output)

    # preprocessing
    constants: dict[str, str] = {
        m.group(1): m.group(2) for m in constant_pattern.finditer(css_output)
    }
    css_output = constant_pattern.sub("", css_output)
    css_output = constant_apply_pattern.sub(
        lambda m: constants.get(m.group(1), m.group(0)), css_output
    )

    # keys are macro names.
    # tuple's first item is a list of arguments
    # and last item is the macro's body
    macros: dict[str, tuple[tuple[str, ...], str]] = {
        cast(str, m.group(1)): (
            tuple(args_group.split(",")) if (args_group := m.group(2)) else (),
            m.group(3).strip(),
        )
        for m in macro_pattern.finditer(css_output)
    }
    css_output = macro_pattern.sub("", css_output)

    def apply_macro_replacement(match: re.Match) -> str:
        macro_name = match.group(1)
        macro_func = functions_map.get(macro_name, None)
        macro_args, macro_body = macros.get(macro_name, (None, ""))
        if not macro_args and not macro_body and not macro_func:
            logger.warning(f"[FASS] couldn't find a macro with name {macro_name}")
            return match.group(0)  # like nothing has happened

        logger.info(f"[FASS] applying a macro with name {macro_name}")

        # passed in parameters
        passed_params: list[str] = (
            [arg_name.strip() for arg_name in args_group.split(",")]
            if (args_group := match.group(2))
            else []
        )

        if macro_func:
            return macro_func(*passed_params)

        for param, arg in zip(cast(tuple[str, ...], macro_args), passed_params):
            macro_body = macro_body.replace(param.strip(), arg)

        return macro_body

    css_output = macro_apply_pattern.sub(apply_macro_replacement, css_output)

    # clean up
    css_output = re.sub(r"\n\s*\n", "\n", css_output).strip()

    return css_output


def bulk_replace(
    string: str,
    patterns: Iterable[str],
    replacements: Iterable[str],
    regex: bool = False,
) -> str:
    """
    Replaces occurrences of multiple patterns in a string with corresponding replacements.

    :param string: the input string in which replacements will be made.
    :type string: str
    :param patterns: the patterns to be replaced, this can be a list of strings or a list of regular expressions.
    :type patterns: Iterable[str]
    :param replacements: the replacements for each text.
    :type replacements: Iterable[str]
    :param regex: Whether to interpret the patterns as regular expressions. Defaults to False.
    :type regex: bool, optional

    :return: the string with replacements made.
    :rtype: str

    :raises ValueError: If the lengths of patterns and replacements are not the same.
    """
    if not (
        isinstance(patterns, (tuple, list)) and isinstance(replacements, (tuple, list))
    ):
        return ""

    if len(patterns) != len(replacements):
        raise ValueError("patterns and replacements must be the same length.")

    for text, replacement in zip(patterns, replacements):
        if regex:
            string = re.sub(text, replacement, string)
        else:
            string = string.replace(text, replacement)

    return string


def bulk_connect(
    connectable: GObject.Object, mapping: dict[str, Callable]
) -> tuple[int, ...]:
    """connects a list of signals to a list of callbacks to an object

    :param connectable: the object to connect the signals to
    :type connectable: GObject.Object
    :param mapping: the mapping of signals to callbacks, example: `{"signal-name": lambda *args: ...}`
    :type mapping: dict[str, Callable]
    :rtype: tuple[int, ...]
    """

    return tuple(
        connectable.connect(signal, callback)  # type: ignore
        for signal, callback in mapping.items()
    )


def bulk_disconnect(
    disconnectable: GObject.Object,
    signals_or_funcs: Iterable[Union[str, Callable]],
) -> tuple[int, ...]:
    """does the opposite of bulk_connect

    :param disconnectable: the object to disconnect the signals from
    :type disconnectable: GObject.Object | object
    :param signals_or_funcs: iterable of signals/callbacks to disconnect
    :type signals: Iterable[Union[str, Callable]]
    :return: a list of return values from the `disconnect` function
    :rtype: tuple[int]
    """

    def disconnect(signal_or_func) -> int:
        if callable(signal_or_func):
            return disconnectable.disconnect_by_func(signal_or_func)  # type: ignore
        return disconnectable.disconnect(signal_or_func)  # type: ignore

    return tuple(disconnect(x) for x in signals_or_funcs)


def clamp(value: Number, min_value: Number, max_value: Number) -> Number:
    """
    clamp a value between a minimum and maximum value

    :param value: the value to be clamped
    :type value: float or int
    :param min_value: the minimum value to clamp to
    :type min_value: float or int
    :param max_value: the maximum value to clamp to
    :type max_value: float or int
    :return: the clamped value
    :rtype: float or int
    """
    return max(min(value, max_value), min_value)


def extract_css_values(css_string: str) -> tuple[int, int, int, int]:
    """
    extracs and return a tuple of four CSS values from a given CSS string.

    :param css_string: the CSS string to extract the values from.
    :type css_string: str
    :return: a tuple of four integers representing the extracted CSS values. If the CSS string
        does not contain enough values, the missing values are filled with zeros.
    :rtype: tuple
    """
    pattern = re.compile(
        r"(-?\d+)(?:px)?(?:\s+(-?\d+)(?:px)?(?:\s+(-?\d+)(?:px)?(?:\s+(-?\d+)(?:px)?)?)?)?"
    )
    matches = pattern.match(css_string)
    default_values = (0, 0, 0, 0)
    if matches:
        values = [int(val) if val else 0 for val in matches.groups()]
        values.extend([values[-1]] * (4 - len(values)))
        return tuple(values)  # type: ignore
    else:
        return default_values


def monitor_file(
    path: str,
    *callbacks: Callable,
    flags: Literal[
        "none",
        "watch-mounts",
        "send-moved",
        "watch-hard-links",
        "watch-moves",
    ]
    | Gio.FileMonitorFlags = Gio.FileMonitorFlags.NONE,
    initial_call: bool = False,
) -> Gio.FileMonitor:
    """
    Monitor a specific file or directory for changes...

    :param path: path to the desired file or directory
    :type path: str
    :param callbacks: list of functions each assigned directly to the `"changed"` signal of the monitor
    :type callbacks: Callable
    :param flags: flags to configure the file monitor. Defaults to None.
    :type flags: Literal["none", "watch-mounts", "send-moved", "watch-hard-links", "watch-moves"], optional
    :param initial_call: whether should the given callbacks get called upon registering. Defaults to False
    :type initial_call: bool, optional
    :return: the monitor for the specified path
    :rtype: Gio.FileMonitor
    """
    file: Gio.File = Gio.File.new_for_uri(  # type: ignore
        ("file://" + os.path.expanduser(path)) if "://" not in path else path
    )
    monitor = file.monitor(
        get_enum_member(Gio.FileMonitorFlags, flags, default=Gio.FileMonitorFlags.NONE)
    )

    for f in callbacks:
        monitor.connect("changed", f)

    [f() for f in callbacks] if initial_call else None

    return monitor


def cooldown(
    cooldown_time:  int | float , error: Callable | None = None, return_error: bool = False
):
    """
    Decorator function that adds a cooldown period to a given function

    :param cooldown_time: the time in seconds to wait before calling the function again
    :type cooldown_time: int
    :param error: the function to call if the cooldown period has not been reached yet. Defaults to None
    :type error: Callable, optional
    :rtype: decorator
    """

    def decorator(func):
        last_call_delay = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call_delay
            current_time = time.time()
            elapsed_time = current_time - last_call_delay
            if elapsed_time >= cooldown_time:
                result = func(*args, **kwargs)
                last_call_delay = current_time
                return result
            else:
                if return_error is True and error is not None:
                    return error((cooldown_time - elapsed_time), *args, **kwargs)
                elif error is not None:
                    error((cooldown_time - elapsed_time), *args, **kwargs)

        return wrapper

    return decorator


def exec_shell_command(cmd: str) -> str | Literal[False]:
    """
    executes a shell command and returns the output

    :param cmd: the shell command to execute
    :type cmd: str
    :return: the output of the command or False if an error has occurred
    :rtype: str | Literal[False]
    """
    if not isinstance(cmd, str):
        raise ValueError  # FIXME: add error message

    try:
        result, output, error, status = GLib.spawn_command_line_sync(cmd)  # type: ignore
        if status != 0:
            return error.decode()
        return output.decode()
    except Exception:
        pass
    return False  # *unreachable*


def exec_shell_command_async(
    cmd: str | list[str],
    callback: Callable[[str], Any] | None = None,
) -> tuple[Gio.Subprocess | None, Gio.DataInputStream]:
    """
    executes a shell command and returns the output asynchronously

    :param cmd: the shell command to execute
    :type cmd: str
    :param callback: a function to retrieve the result at or `None` to ignore the result
    :type callback: Callable[[str], Any] | None, optional
    :return: a Gio.Subprocess object which holds a reference to your process and a Gio.DataInputStream object for stdout
    :rtype: tuple[Gio.Subprocess | None, Gio.DataInputStream]
    """
    process = Gio.Subprocess.new(
        shlex.split(cmd) if isinstance(cmd, str) else cmd,  # type: ignore
        Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_PIPE,  # type: ignore
    )

    stdout = Gio.DataInputStream(
        base_stream=process.get_stdout_pipe(),  # type: ignore
        close_base_stream=True,
    )

    def reader_loop(stdout: Gio.DataInputStream):
        def read_line(stream: Gio.DataInputStream, res: Gio.AsyncResult):
            output, *_ = stream.read_line_finish_utf8(res)
            if isinstance(output, str):
                callback(output) if callback else None
                reader_loop(stream)

        stdout.read_line_async(GLib.PRIORITY_DEFAULT, None, read_line)

    reader_loop(stdout)

    return process, stdout


def invoke_repeater(
    interval: int, func: Callable, *args, initial_call: bool = True
) -> int:
    """
    invokes a function repeatedly with a given interval

    :param interval: the interval in milliseconds to invoke the function
    :type interval: int
    :param func: the function to invoke
    :type func: Callable
    :param args: list of arguments passed directly to the given function
    :param initial_call: whether should the given function get called as soon as it is registered. Defaults to False
    :type initial_call: bool, optional
    """
    if initial_call:
        func(*args)
    return GLib.timeout_add(interval, func, *args)


def get_relative_path(path: str, level: int = 1) -> str:
    """
    converts a path to a relative path according to caller's `__file__` variable

    NOTE: This function only works if the caller `__file__` variable is set. means this will work only if you're calling from a python file (not a IDLE / REPL), else it will fallback to the current working directory as `__file__`

    :param path: the path to convert
    :type path: str
    :param level: the stack level to get the `__file__` variable from. Defaults to 1
    :type level: int, optional
    :return: the relative path
    :rtype: str
    """
    prev_globals = inspect.stack()[level][0].f_globals
    file_var = (
        os.path.dirname(os.path.abspath(prev_globals["__file__"]))
        if "__file__" in prev_globals
        else os.getcwd()
    )
    path = os.path.join(file_var, path)
    return path


def load_dbus_xml(path_to_xml: str):
    path_to_xml = get_relative_path(path_to_xml, level=2)
    with open(path_to_xml, "r") as f:
        file = f.read()
    return Gio.DBusNodeInfo.new_for_xml(file)


def snake_case_to_pascal_case(string: str) -> str:
    return string.replace("_", " ").title().replace(" ", "")


def pascal_case_to_snake_case(string: str) -> str:
    return "_".join(
        map(
            str.lower,
            re.findall(r"[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+", string),
        )
    )


def snake_case_to_kebab_case(string: str) -> str:
    return string.strip().lower().replace("_", "-")


def kebab_case_to_snake_case(string: str) -> str:
    return string.replace("-", "_").lower()


def get_connectables_for_kwargs(kwargs: dict[str, Callable]) -> Generator:
    __deprecation_table()
    for key, value in zip(kwargs.keys(), kwargs.values()):
        if key.startswith("on_"):
            yield [snake_case_to_kebab_case(key[3:]), value]
        elif key.startswith("notify_"):
            # yield a connectable property
            yield [f"notify::{snake_case_to_kebab_case(key[7:])}", value]


def get_enum_member(
    enum: type[E], member: str | E, mapping: dict[str, str] = {}, default: Any = MISSING
) -> E:
    if isinstance(member, enum):
        return member

    if not isinstance(member, str):
        raise ValueError  # FIXME: add exception message

    for name, replacement in mapping.items():
        if member.casefold() == name.casefold():
            member = replacement
            break

    try:
        return getattr(enum, kebab_case_to_snake_case(member).upper())
    except Exception:
        if default is MISSING:
            raise ValueError
        return default


def get_enum_member_name(
    member: Enum | Any, mapping: dict[str, str] = {}, default: Any = MISSING
) -> str:
    if isinstance(member, str):
        return member

    if isinstance(member, Enum):
        return member.name

    # GIR type enum...
    member_name: str | None = None
    if _name := getattr(member, "first_value_nick", None):
        member_name = _name
    elif _name := getattr(member, "value_nick", None):
        member_name = _name

    if not member_name and default is MISSING:
        raise ValueError
    elif not member_name:
        return default

    member_name = member_name.upper()
    return mapping.get(member_name, member_name)


def bridge_signal(
    source: GObject.Object,
    source_signal: str,
    target: GObject.Object,
    target_signal: str,
    notify: bool = False,
) -> int:
    def signal_handler(*args, **kwargs):
        return target.emit(target_signal, *args, **kwargs)  # type: ignore

    def notify_handler(*args, **kwargs):
        return target.notify(target_signal)  # type: ignore

    return source.connect(  # type: ignore
        source_signal if not notify else f"notify::{source_signal}",
        signal_handler if not notify else notify_handler,
    )


def generate_random_string(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))


class FunctionAnnotations(NamedTuple, Generic[T]):
    arguments: dict[str, type]
    return_type: T | None


def get_function_annotations(
    func: Callable[P, T],
) -> FunctionAnnotations[T]:
    args: dict[str, Any] = {}
    signature = inspect.signature(func)
    return_type: T | None = (
        signature.return_annotation
        if signature.return_annotation is not signature.empty
        else None
    )
    for arg_name, arg_pspec in signature.parameters.items():
        args[arg_name] = (
            arg_pspec.annotation if arg_pspec.annotation is not arg_pspec.empty else Any
        )
    return FunctionAnnotations(args, return_type)


def truncate(string: str, max_length: int, suffix: str = "...") -> str:
    return (
        string
        if len(string) <= max_length
        else string[: max_length - len(suffix)] + suffix
    )


def idle_add(func: Callable, *args, pin: bool = False) -> int:
    """
    add a function to be invoked in a lazy manner in the main thread, useful for multi-threaded code

    :param func: the function to be queued
    :type func: Callable
    :param args: arguments will be passed to the given function
    :param pin: whether the function should be invoked as long as it's return value is `True`, when the function returns `False` it won't be called again
    :type pin: bool, optional
    """
    if pin:
        return GLib.idle_add(func, *args)

    def idle_executor(*largs):
        func(*largs)
        return False

    return GLib.idle_add(
        idle_executor, *args
    )  # a hack to safely pass a pointer to user's data


def remove_handler(handler_id: int):
    return GLib.source_remove(handler_id)


# FIXME: deprecated (please don't use, there's a replacement of each function)
def set_stylesheet_from_file(file_path: str, compiled: bool = True) -> None:
    __deprecation_table()

    provider = Gtk.CssProvider()
    if compiled:
        with open(file_path, "r") as f:
            file = f.read()
        provider.load_from_data(bytearray(compile_css(file), "utf-8"))  # type: ignore
    else:
        provider.load_from_path(file_path)
    screen = Gdk.Screen.get_default()
    context = Gtk.StyleContext()
    context.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
    return


def set_stylesheet_from_string(css_string: str, compiled: bool = True) -> None:
    __deprecation_table()

    provider = Gtk.CssProvider()
    if compiled:
        provider.load_from_data(bytearray(compile_css(css_string), "utf-8"))
    else:
        provider.load_from_data(bytearray(css_string, "utf-8"))
    screen = Gdk.Screen.get_default()
    context = Gtk.StyleContext()
    context.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
    return


def idlify(func: Callable, *args) -> int:
    __deprecation_table()
    return idle_add(func, *args)
