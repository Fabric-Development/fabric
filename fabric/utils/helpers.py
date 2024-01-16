import gi
import re
import time

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject, Gio, GLib
from typing import Callable, Literal, Iterable


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
    if compiled:
        with open(file_path, "r") as f:
            file = f.read()
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
    connecable: GObject.Object | object, signals: list[str], callbacks: list[Callable]
) -> list[object | int]:
    """connects a list of signals to a list of callbacks to an object

    :param connecable: the object to connect the signals to
    :type connecable: GObject.Object | object
    :param signals: the list of signals
    :type signals: list[str]
    :param callbacks: the list of callbacks
    :type callbacks: list[Callable]
    :return: a list of return values from the connect function
    :rtype: list[object | int]
    """
    return_list = []
    for signal, callback in zip(signals, callbacks):
        return_list.append(connecable.connect(signal, callback))
    return return_list


def bulk_disconnect(
    disconnecable: GObject.Object | object, signals: list[str]
) -> list[int]:
    """does the opposite of bulk_connect

    :param disconnecable: the object to disconnect the signals from
    :type disconnecable: GObject.Object | object
    :param signals: the list of signals
    :type signals: list[str]
    :return: a list of return values from the disconnect function
    :rtype: list[int]
    """
    return_list = []
    for signal in signals:
        return_list.append(disconnecable.disconnect(signal))
    return return_list


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


def extract_css_values(css_string: str):
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


def extract_anchor_values(geometry_string: str):
    """
    extracts the geometry values from a given geometry string.

    :param geometry_string: the string containing the geometry values.
    :type geometry_string: str
    :return: a list of unique directions extracted from the geometry string.
    :rtype: list
    """
    direction_map = {"l": "left", "t": "top", "r": "right", "b": "bottom"}
    pattern = re.compile(r"\b(left|right|top|bottom)\b", re.IGNORECASE)
    matches = pattern.findall(geometry_string)
    directions = [direction_map[match.lower()[0]] for match in matches]
    unique_directions = list(set(directions))
    return unique_directions


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


def cooldown(cooldown_time: int, error: Callable = None):
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
                error((cooldown_time - elapsed_time)) if error is not None else None

        return wrapper

    return decorator


def exec_shell_command(cmd: str | list[str]) -> str | list[str]:
    """
    executes a shell command and returns the output

    :param cmd: the command to execute
    :type cmd: str or list of str
    :return: the output of the command
    :rtype: str or list of str
    """
    if isinstance(cmd, str):
        result, output, error, status = GLib.spawn_command_line_sync(cmd)
        if status != 0:
            return error.decode()
        return output.decode()
    elif isinstance(cmd, list):
        for c in cmd:
            result, output, error, status = GLib.spawn_command_line_sync(" ".join(c))
            if status != 0:
                yield error.decode()
            yield output.decode()


def invoke_repeater(interval: int, func: Callable, *args, **kwargs) -> int:
    """
    invokes a function repeatedly with a given interval

    :param interval: the interval in milliseconds to invoke the function
    :type interval: int
    :param func: the function to invoke
    :type func: Callable

    *args and **kwargs are passed to the function

    :return: the result of the function
    :rtype: int
    """
    return GLib.timeout_add(interval, func, *args, **kwargs)
