import gi
import re
import atexit
import inspect
from loguru import logger
from types import FrameType
from inspect import FrameInfo
from collections.abc import Iterable
from typing import overload, Literal, Self
from fabric.core.service import Service, Property
from fabric.utils.helpers import load_dbus_xml, compile_css

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, Gio


FABRIC_DBUS_INTERFACE_NAME = "org.Fabric.fabric"
FABRIC_DBUS_OBJECT_PATH = "/org/Fabric/fabric"
FABRIC_DBUS_INTERFACE_NODES = load_dbus_xml(
    f"../dbus_assets/{FABRIC_DBUS_INTERFACE_NAME}.xml"
)


class FileHook:
    file_path: str
    frame: FrameType
    frame_info: FrameInfo
    global_scope: dict
    local_scope: dict

    @classmethod
    def from_here(cls, depth: int = -1) -> Self:
        instance = cls.__new__(cls)
        instance.__init__(inspect.stack()[depth])
        return instance

    def __init__(self, frame_info: FrameInfo, **kwargs):
        super().__init__(**kwargs)
        self.frame_info: FrameInfo = frame_info
        self.frame: FrameType = frame_info.frame
        self.global_scope: dict = self.frame.f_globals if self.frame is not None else {}
        self.local_scope = self.frame.f_locals if self.frame is not None else {}
        self.file_path: str = (
            (
                frame_info.filename
                if frame_info is not None and frame_info.filename is not None
                else None
            )
            or (
                self.global_scope.get("__file__", "unknown")
                if self.global_scope is not None
                else None
            )
            or "unknown"
        )

    def execute(
        self, source: str, raise_on_exception: bool = False
    ) -> Exception | None:
        error = None
        try:
            exec(source, self.global_scope, self.local_scope)
        except Exception as e:
            error = e
        if raise_on_exception is True and error not in (None, ""):
            raise error
        return error

    def evaluate(self, code: str, raise_on_exception: bool = False):
        result = None
        error = None
        try:
            result = eval(
                code,
                self.global_scope,
                self.local_scope,
            )
        except Exception as e:
            error = e
        if raise_on_exception is True and error not in (None, ""):
            raise error
        return result, error

    def is_class(self, class_name: str | object):
        return inspect.isclass(self.global_scope.get(class_name, None))


class DBusClient:
    def __init__(
        self, config: "Application", connection: Gio.DBusConnection, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.config = config
        self.hook = FileHook.from_here()
        self.connection: Gio.DBusConnection = connection
        self.do_register()

    def do_register(self):
        for interface in FABRIC_DBUS_INTERFACE_NODES.interfaces:
            if interface.name == FABRIC_DBUS_INTERFACE_NAME:
                self.connection.register_object(
                    FABRIC_DBUS_OBJECT_PATH,
                    interface,
                    self.do_handle_bus_call,  # type: ignore
                )
        return self.connection.flush()

    def do_handle_bus_call(
        self,
        conn: Gio.DBusConnection,
        sender: str,
        path: str,
        interface: str,
        target: str,
        params: tuple,
        invocation: Gio.DBusMethodInvocation,
        user_data: object = None,
    ) -> None:
        # property accessing
        match target:
            case "Get":
                prop_name = params[1] if len(params) >= 1 else None
                match prop_name:
                    case "File":
                        invocation.return_value(
                            GLib.Variant(
                                "(v)", (GLib.Variant("s", self.hook.file_path),)
                            )
                        )
                    case "Windows":
                        invocation.return_value(
                            GLib.Variant(
                                "(v)",
                                (
                                    GLib.Variant(
                                        "a{sb}",
                                        self.do_serialize_windows(),
                                    ),
                                ),
                            )
                        )
                    case _:
                        invocation.return_value(None)
            case "GetAll":
                all_properties = {
                    "File": GLib.Variant("s", self.hook.file_path),
                    "Windows": GLib.Variant("a{sb}", self.do_serialize_windows()),
                }

                invocation.return_value(GLib.Variant("(a{sv})", (all_properties,)))

            # interface methods
            case "Log":
                level, message = params
                match level:
                    case 0:
                        logger.debug(message)
                    case 1:
                        logger.info(message)
                    case 2:
                        logger.warning(message)
                    case 3:
                        logger.error(message)
                invocation.return_value(None)
            case "Execute":
                source: str = params[0]
                exc = self.hook.execute(source)
                invocation.return_value(
                    GLib.Variant("(s)", (exc.__repr__() if exc is not None else "",))
                )
            case "Evaluate":
                code: str = params[0]
                result, exc = self.hook.evaluate(code)
                invocation.return_value(
                    GLib.Variant(
                        "(ss)",
                        (
                            str(result),
                            exc.__repr__() if exc is not None else "",
                        ),
                    )
                )
            case _:
                invocation.return_value(None)

        return conn.flush()

    def do_serialize_windows(self) -> dict[str, bool]:
        windows: dict[str, bool] = {}
        for window in self.config.windows:
            windows[window.get_name()] = window.is_visible()
        return windows


class Application(Gtk.Application, Service):
    activated = Property(bool, flags="read-write", default_value=False)
    name = Property(str, flags="read-write")

    @Property(list[Gtk.Window])
    def windows(self) -> list[Gtk.Window]:
        return self._windows

    @windows.setter
    def windows(self, windows: list[Gtk.Window]):
        for window in self._windows:
            self.remove_window(window)
        return self._windows.extend(windows)

    @overload
    def __init__(
        self,
        name: str = "default",
        *windows: Gtk.Window,
        open_client: bool = True,
        **kwargs,
    ): ...

    @overload
    def __init__(
        self,
        *windows: Gtk.Window,
        open_client: bool = True,
        **kwargs,
    ): ...

    def __init__(
        self,
        *args: str | Gtk.Window,
        open_client: bool = True,
        **kwargs,
    ):
        name: str
        windows: Iterable[Gtk.Window]

        name = "default"
        if len(args) < 1:
            windows = ()
        elif isinstance(args[0], str):
            name, *windows = args  # type: ignore
        elif isinstance(args[0], Gtk.Window):
            windows = args  # type: ignore
        else:
            raise ValueError  # FIXME: add a error message

        application_id = FABRIC_DBUS_INTERFACE_NAME + f".{name or 'default'}"

        if not self.validate_name(name):
            raise ValueError(
                f"`{name}` is an invalid name, consider using only English letters, numbers, and hyphens in the name"
            )

        if self.name_running(application_id):
            raise ValueError(
                f"there's already a Fabric application instance running with the name `{name}`"
            )

        Gtk.Application.__init__(
            self,  # type: ignore
            application_id=application_id,
        )

        Service.__init__(
            self,
            **kwargs,
        )

        self._windows: list[Gtk.Window] = []
        self._open_client = open_client

        self.name = name
        self.windows = [window for window in windows]

        GLib.set_application_name(name) if name else None

    def remove_window(self, window: Gtk.Window):
        self._windows.remove(window)
        if self.activated:
            super().remove_window(window)
        return

    def add_window(self, window: Gtk.Window):
        self._windows.append(window)
        if self.activated:
            super().add_window(window)
        return

    def dispatch_windows(self):
        if not self.activated:
            return
        for window in self.windows:
            super().add_window(window)
        return

    def do_activate(self):
        if self.activated:
            return
        self.activated = True
        self.hold()
        self.dispatch_windows()

        if self._open_client:
            logger.debug(
                f"[Fabric] opening a DBus client for Application with name {self.name}"
            )
            self.dbus_client = DBusClient(self, self.get_dbus_connection())
        else:
            self.dbus_client = None

    def quit(self, *_):
        self.activated = False
        return super().quit()

    def run(self, *args, **kwargs):
        def on_exit():
            # assuming clean exit (e.g. segfaults are considered dirty)
            return logger.info("[Fabric] exiting...")

        atexit.register(on_exit)
        try:
            super().run(*args, **kwargs)
        finally:
            # the application has quit (somehow in a bad way...)
            # we do nothing, just return thus print the at exit message
            return

    def open_inspector(self):
        return Gtk.Window.set_interactive_debugging(True)  # type: ignore

    @staticmethod
    def validate_name(name: str) -> bool:
        pattern = re.compile(r"^[A-Za-z0-9-]+$")
        return bool(pattern.match(name))

    @staticmethod
    def name_running(name: str) -> bool:
        return (
            Gio.bus_get_sync(Gio.BusType.SESSION)
            .call_sync(
                "org.freedesktop.DBus",
                "/org/freedesktop/DBus",
                "org.freedesktop.DBus",
                "NameHasOwner",
                GLib.Variant("(s)", (name,)),
                GLib.VariantType("(b)"),  # type: ignore
                Gio.DBusCallFlags.NONE,
                -1,
                None,
            )
            .get_child_value(0)
            .get_boolean()
        )

    @staticmethod
    def get_dbus_proxy(config_name: str | None = None) -> Gio.DBusProxy | None:
        proxy = Gio.DBusProxy.new_for_bus_sync(
            Gio.BusType.SESSION,
            Gio.DBusProxyFlags.NONE,
            None,
            FABRIC_DBUS_INTERFACE_NAME
            + (f".{config_name}" if config_name is not None else ""),
            FABRIC_DBUS_OBJECT_PATH,
            FABRIC_DBUS_INTERFACE_NAME,
            None,
        )
        return proxy

    @staticmethod
    def set_stylesheet(
        provider: Gtk.StyleProvider,
        priority: Literal["fallback", "theme", "settings", "application", "user"]
        | int = Gtk.STYLE_PROVIDER_PRIORITY_USER,
    ) -> None:
        # well, i have to manually bind this
        return Gtk.StyleContext.add_provider_for_screen(  # type: ignore
            Gdk.Screen.get_default(),
            provider,
            (
                {
                    "fallback": Gtk.STYLE_PROVIDER_PRIORITY_FALLBACK,
                    "theme": Gtk.STYLE_PROVIDER_PRIORITY_THEME,
                    "settings": Gtk.STYLE_PROVIDER_PRIORITY_SETTINGS,
                    "application": Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
                    "user": Gtk.STYLE_PROVIDER_PRIORITY_USER,
                }.get(priority, Gtk.STYLE_PROVIDER_PRIORITY_USER)
                if isinstance(priority, str)
                else priority
            ),
        )

    @staticmethod
    def set_stylesheet_from_file(
        file_path: str, compile: bool = True, *args, **kwargs
    ) -> None:
        if compile:
            with open(file_path, "r") as f:
                Application.set_stylesheet_from_string(f.read(), True)
            return
        provider = Gtk.CssProvider()
        provider.load_from_path(file_path)
        Application.set_stylesheet(provider, *args, **kwargs)
        return

    @staticmethod
    def set_stylesheet_from_string(
        style_string: str, compile: bool = True, *args, **kwargs
    ):
        provider = Gtk.CssProvider()
        provider.load_from_data(
            bytearray(compile_css(style_string) if compile else style_string, "utf-8")  # type: ignore
        )
        Application.set_stylesheet(provider, *args, **kwargs)
        return