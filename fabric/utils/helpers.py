import gi
import re
import os
import time
import shlex
import inspect
from enum import Enum
from typing import Callable, Literal, Iterable, Generator, Union, Any

gi.require_version("Gtk", "3.0")
gi.require_version("GtkLayerShell", "0.1")
from gi.repository import Gtk, Gdk, GObject, Gio, GLib, GtkLayerShell


class ValueEnum(Enum):
    @classmethod
    def get_member(cls, name):
        return cls[name].value


class Validator:
    def __init__(
        self,
        func: Callable,
        exception_to_raise: Exception = None,
        assertion: bool = False,
        **kwargs,
    ):
        if not callable(func):
            raise ValueError("func must be a callable (a function, method or a lambda)")
        if exception_to_raise is not None and not isinstance(
            exception_to_raise, Exception
        ):
            raise ValueError("exception_to_raise must be an Exception")
        if assertion and not isinstance(assertion, bool):
            raise ValueError("assertion must be a bool")
        self.func = func
        self.func_data = kwargs
        self.exception_to_raise = exception_to_raise
        self.assertion = assertion

    def __call__(self, value: object, exception_to_raise: Exception = None, *args):
        if exception_to_raise is None or not isinstance(exception_to_raise, Exception):
            exception_to_raise = self.exception_to_raise
        if self.assertion is True:
            try:
                assert self.func(value, *args, **self.func_data)
            except AssertionError as e:
                if self.exception_to_raise is not None:
                    raise Exception(self.exception_to_raise) or e
                return False
        elif self.func(value, *args, **self.func_data) is False:
            if self.exception_to_raise is not None:
                raise self.exception_to_raise
            return False
        return True


def get_gdk_rgba(color: str | Iterable) -> Gdk.RGBA:
    """
    get a Gdk.RGBA from a hexdecimal color string or an iterable of RGBA/RGB values

    :param color: the input color/data
    :type color: str | Iterable
    :raises ValueError: Invalid color format
    :return: the Gdk.RGBA generated
    :rtype: Gdk.RGBA
    """
    if isinstance(color, Iterable) and (len(color) == 3 or len(color) == 4):
        return Gdk.RGBA(*[c / 255.0 for c in color])
    if isinstance(color, str) and (
        len(color.lstrip("#")) == 6 or len(color.lstrip("#")) == 8
    ):
        color = color.lstrip("#")
        return Gdk.RGBA(
            *[int(color[i : i + 2], 16) / 255.0 for i in range(0, len(color), 2)]
        )
    raise ValueError("Invalid color format")


def compile_css(css_string: str) -> str:
    """
    compile a CSS string to GTK's CSS syntax
    issues might happen, this thing uses a chain of regex

    :param css_string: the CSS string
    :type css_string: str
    :return: the compiled CSS string
    :rtype: str
    """
    vars_selector_pattern = re.compile(r":vars\s*{\s*([^}]+)\s*}")
    vars_declaration_pattern = re.compile(r"--([\w-]+)\s*:\s*([^;]+)\s*;")
    vars_reference_pattern = re.compile(r"var\(--([\w-]+)\)")

    # special selector for variables
    match = vars_selector_pattern.search(css_string)
    if match is not None:
        css = f"{match.group(1)}\n\n{css_string.replace(match.group(0), '')}"
    else:
        css = css_string

    # variable declarations
    css = vars_declaration_pattern.sub(
        lambda m: f"@define-color {m.group(1)} {m.group(2)};", css
    )

    # variable references
    css = vars_reference_pattern.sub(r"@\1", css)
    return css


def set_stylesheet_from_file(file_path: str, compiled: bool = True) -> None:
    """
    set the global stylesheet for the application from a file

    :param file_path: the path to the CSS file
    :type file_path: str
    :return: None
    """
    provider = Gtk.CssProvider()
    with open(file_path, "r") as f:
        file = f.read()
    if compiled:
        provider.load_from_data(bytearray(compile_css(file), "utf-8"))
    else:
        provider.load_from_path(file)
    screen = Gdk.Screen.get_default()
    context = Gtk.StyleContext()
    context.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
    return


def set_stylesheet_from_string(css_string: str, compiled: bool = True) -> None:
    """
    same as set_stylesheet_from_file but sets the global stylesheet from a string

    :param css_string: the CSS string
    :type css_string: str
    :return: None
    """
    provider = Gtk.CssProvider()
    if compiled:
        provider.load_from_data(bytearray(compile_css(css_string), "utf-8"))
    else:
        provider.load_from_data(bytearray(css_string, "utf-8"))
    screen = Gdk.Screen.get_default()
    context = Gtk.StyleContext()
    context.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
    return


def bulk_replace(
    input_str: str, texts: list[str], replacements: list[str], regex: bool = False
) -> str:
    """
    Replaces occurrences of multiple texts in a string with corresponding replacements.

    :param input_str: the input string in which replacements will be made.
    :type input_str: str
    :param texts: the texts to be replaced, this can be a list of strings or a list of regular expressions.
    :type texts: list[str]
    :param replacements: the replacements for each text.
    :type replacements: list[str]
    :param regex: Whether to interpret the texts as regular expressions. Defaults to False.
    :type regex: bool, optional

    :return: the string with replacements made.
    :rtype: str

    :raises ValueError: If the lengths of texts and replacements are not the same.
    """
    if len(texts) != len(replacements):
        raise ValueError("texts and replacements must be the same length.")

    for text, replacement in zip(texts, replacements):
        if regex:
            input_str = re.sub(text, replacement, input_str)
        else:
            input_str = input_str.replace(text, replacement)

    return input_str


def bulk_connect(
    connectable: GObject.Object | object, mapping: dict[str:Callable], *args
) -> list[Union[object, int]]:
    """connects a list of signals to a list of callbacks to an object

    :param connectable: the object to connect the signals to
    :type connectable: GObject.Object | object
    :param mapping: the mapping of signals to callbacks, example: `{"signal-name": lambda *args: ...}`
    :type mapping: dict[str: Callable]
    :rtype: list[Union[object, int]]
    """
    rlist = []
    rlist.extend(
        [
            connectable.connect(signal, callback)
            for signal, callback in zip(mapping.keys(), mapping.values())
        ]
    )
    if len(args) > 1 and len(args) % 2:
        raise ValueError(
            f"extra passed arguments must follow this syntax (connectable, mapping, connectable, mapping, ...) but got {args}"
        )
    for index, item in enumerate(args):
        if isinstance(item, GObject.Object):
            rlist.extend(bulk_connect(item, args[index + 1]))
    return rlist


def bulk_disconnect(
    disconnectable: GObject.Object | object,
    signals_or_funcs: list[Union[str, Callable]],
) -> list[int]:
    """does the opposite of bulk_connect

    :param disconnectable: the object to disconnect the signals from
    :type disconnectable: GObject.Object | object
    :param signals_or_funcs: the list of signals/callbacks to disconnect
    :type signals: list[Union[str, Callable]]
    :return: a list of return values from the `disconnect` function
    :rtype: list[int]
    """
    return [
        (
            disconnectable.disconnect(x)
            if callable(x) is False
            else disconnectable.disconnect_by_func(x)
        )
        for x in signals_or_funcs
    ]


def clamp(value, min_value, max_value):
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


def extract_css_values(css_string: str) -> tuple[int]:
    """
    extracts and returns a tuple of four CSS values from a given CSS string.

    :param css_string: the CSS string from which to extract the values.
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
        return tuple(values)
    else:
        return default_values


def extract_anchor_values(string: str) -> list[str]:
    """
    extracts the geometry values from a given geometry string.

    :param string: the string containing the geometry values.
    :type string: str
    :return: a list of unique directions extracted from the geometry string.
    :rtype: list
    """
    direction_map = {"l": "left", "t": "top", "r": "right", "b": "bottom"}
    pattern = re.compile(r"\b(left|right|top|bottom)\b", re.IGNORECASE)
    matches = pattern.findall(string)
    directions = [direction_map[match.lower()[0]] for match in matches]
    unique_directions = list(set(directions))
    return unique_directions


def extract_edges_from_string(string: str) -> dict[GtkLayerShell.Edge, bool]:
    anchor_values = extract_anchor_values(string.lower())
    return {
        GtkLayerShell.Edge.TOP: "top" in anchor_values,
        GtkLayerShell.Edge.RIGHT: "right" in anchor_values,
        GtkLayerShell.Edge.BOTTOM: "bottom" in anchor_values,
        GtkLayerShell.Edge.LEFT: "left" in anchor_values,
    }


def extract_margin_from_string(string: str) -> dict[GtkLayerShell.Edge, int]:
    margins = extract_css_values(string)
    return {
        GtkLayerShell.Edge.TOP: margins[0],
        GtkLayerShell.Edge.RIGHT: margins[1],
        GtkLayerShell.Edge.BOTTOM: margins[2],
        GtkLayerShell.Edge.LEFT: margins[3],
    }


def monitor_file(
    file_path: str,
    flags: Literal[
        "none",
        "watch-mounts",
        "send-moved",
        "watch-hard-links",
        "watch-moves",
    ]
    | Gio.FileMonitorFlags = None,
) -> Gio.FileMonitor:
    """
    creates a file monitor for the specified file path

    :param file_path: the path of the file to be monitored
    :type file_path: str
    :param flags: the flags to configure the file monitor. Defaults to None.
    :type flags: Literal["none", "watch-mounts", "send-moved", "watch-hard-links", "watch-moves"], optional
    :return: the file monitor for the specified file
    :rtype: Gio.FileMonitor
    """
    file_path = (
        "file://" + file_path if not file_path.startswith("file://") else file_path
    )
    file = Gio.File.new_for_uri(file_path)
    monitor = file.monitor_file(
        flags
        if isinstance(flags, Gio.FileMonitorFlags)
        else {
            "none": Gio.FileMonitorFlags.NONE,
            "watch-mounts": Gio.FileMonitorFlags.WATCH_MOUNTS,
            "send-moved": Gio.FileMonitorFlags.SEND_MOVED,
            "watch-hard-links": Gio.FileMonitorFlags.WATCH_HARD_LINKS,
            "watch-moves": Gio.FileMonitorFlags.WATCH_MOVES,
        }.get(flags, Gio.FileMonitorFlags.NONE)
    )
    return monitor


def cooldown(cooldown_time: int, error: Callable = None, return_error: bool = False):
    """
    Decorator function that adds a cooldown period to a given function

    :param cooldown_time: the time in seconds to wait before calling the function again
    :type cooldown_time: int
    :param error: the function to call if the cooldown period has not been reached yet. Defaults to None
    :type error: Callable, optional
    :rtype: decorator
    """

    def decorator(func):
        last_call_time = 0

        def wrapper(*args, **kwargs):
            nonlocal last_call_time
            current_time = time.time()
            elapsed_time = current_time - last_call_time
            if elapsed_time >= cooldown_time:
                result = func(*args, **kwargs)
                last_call_time = current_time
                return result
            else:
                if return_error is True and error is not None:
                    return error((cooldown_time - elapsed_time), *args, **kwargs)
                elif error is not None:
                    error((cooldown_time - elapsed_time), *args, **kwargs)

        return wrapper

    return decorator


def exec_shell_command(cmd: str) -> str | bool:
    """
    executes a shell command and returns the output

    :param cmd: the shell command to execute
    :type cmd: str
    :return: the output of the command
    :rtype: str | bool
    """
    if isinstance(cmd, str) is True:
        try:
            result, output, error, status = GLib.spawn_command_line_sync(cmd)
            if status != 0:
                return error.decode()
            return output.decode()
        except:
            return False
    else:
        return False


def exec_shell_command_async(
    cmd: str | list[str],
    callback: Callable[[str], None],
) -> tuple[Gio.Subprocess | None, Gio.DataInputStream]:
    """
    executes a shell command and returns the output asynchronously

    :param cmd: the shell command to execute
    :type cmd: str
    :param callback: a function to retrieve the result at
    :type cmd: Callable[[str], None]
    :return: a Gio.Subprocess object which holds a referance to your process and a Gio.DataInputStream object for stdout
    :rtype: tuple[Gio.Subprocess | None, Gio.DataInputStream]
    """
    process = Gio.Subprocess.new(
        shlex.split(cmd) if isinstance(cmd, str) else cmd,
        Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_PIPE,
    )
    stdout = Gio.DataInputStream(
        base_stream=process.get_stdout_pipe(),
        close_base_stream=True,
    )

    def reader_loop(stdout: Gio.DataInputStream):
        def _callback(stream: Gio.DataInputStream, res):
            output, _ = stream.read_line_finish_utf8(res)
            if isinstance(output, str):
                callback(output)
                reader_loop(stream)

        stdout.read_line_async(GLib.PRIORITY_DEFAULT, None, _callback)

    reader_loop(stdout)

    return process, stdout


def invoke_repeater(interval: int, func: Callable, *args) -> int | list[int]:
    """
    invokes a function repeatedly with a given interval

    :param interval: the interval in milliseconds to invoke the function
    :type interval: int
    :param func: the function to invoke
    :type func: Callable
    :param args: extra pairs of (interval, func, ...) to get registered as well

    :return: the result of the function
    :rtype: int | list[int]
    """
    rlist = []
    o = GLib.timeout_add(interval, func)
    if len(args) > 1 and len(args) % 2:
        raise ValueError(
            f"extra passed arguments must follow this syntax (interval, func, interval, func, ...) but got {args}"
        )
    elif len(args) > 1:
        rlist.append(o)
    for index, item in enumerate(args):
        if isinstance(item, (int, float)):
            # item is a interval, get the callback
            callback = args[index + 1]
            rlist.append(GLib.timeout_add(item, callback))
    return rlist if len(rlist) > 1 else o


def get_relative_path(path: str, level: int = 1) -> str:
    """
    converts a path to a relative path according to callers `__file__` variable
    NOTE: This function only works if the caller `__file__` variable is set
    means only if you're running a python FILE (not using IDLE)
    else it will fallback to the current working directory as `__file__`

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


def get_ixml(path_to_xml: str, interface_name: str):
    path_to_xml = get_relative_path(path_to_xml, level=2)
    with open(path_to_xml, "r") as f:
        file = f.read()
    return interface_name, Gio.DBusNodeInfo.new_for_xml(file)


def kebab_case_to_snake_case(string: str) -> str:
    return string.replace("-", "_").lower()


def snake_case_to_kebab_case(string: str) -> str:
    return string.replace("_", "-").lower()


def snake_case_to_pascal_case(string: str) -> str:
    return string.replace("_", " ").title().replace(" ", "")


def pascal_case_to_snake_case(string: str) -> str:
    return "_".join(
        map(
            str.lower,
            re.findall(r"[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+", string),
        )
    )


def get_connectable_names_from_kwargs(kwargs: dict[str, Callable]) -> Generator:
    for key, value in zip(kwargs.keys(), kwargs.values()):
        if key.startswith("on_"):
            yield [snake_case_to_kebab_case(key[3:]), value]
        elif key.startswith("notify_"):
            # yield a connectable property
            yield [f"notify::{snake_case_to_kebab_case(key[7:])}", value]


def get_enum_member(
    cls, name: str | Any, custom_mapping: dict[str, str] = {}
) -> Any | None:
    """
    get an enum member from a enum class (usually for GEnums)

    :param name: the name of the enum member (if the value was passed instead it will be returned)
    :type name: str
    :param custom_mapping: a mapping of name to name replacement, defaults to {}
    :type custom_mapping: dict[str, str], optional
    :return: the enum member or None
    :rtype: Any | None
    """
    if isinstance(name, cls):
        return name

    if not isinstance(name, str):
        return None

    for n, r in custom_mapping.items():
        if name == n:
            name = r
            break

    return getattr(cls, kebab_case_to_snake_case(name).upper())


def bridge_signals(
    source: GObject.Object,
    target: GObject.Object,
    exclude: list[str] = [],
    custom_mapping: dict[str, str] = {},
) -> None:
    """
    bridges signals from one object to another

    :param source: the source object to bridge from
    :type source: GObject.Object
    :param target: the target object to bridge to
    :type target: GObject.Object
    :param exclude: a list of signal names to exclude connecting from, defaults to []
    :type exclude: list[str], optional
    :param custom_mapping: a mapping of name to name replacement, defaults to {}
    :type custom_mapping: dict[str, str], optional
    :return: None
    """

    def do_emit_bridge_signal(signal_name, *args):
        rv = []
        for arg in args:
            rv.append(arg) if not arg is source else None
        return target.emit(signal_name, *rv)

    for signal_name in GObject.signal_list_names(source):
        if signal_name in exclude:
            continue
        source.connect(
            signal_name,
            lambda *args, signal_name=signal_name: do_emit_bridge_signal(
                custom_mapping.get(signal_name, signal_name), *args
            ),
        )


def idlify(func: Callable, *args) -> int:
    """add a function to be invoked in the main thread, useful for multi-threaded code

    :param func: the function to be queued
    :type func: Callable
    :param args: arguments will be passed to the given function
    """
    return GLib.idle_add(func, *args)
