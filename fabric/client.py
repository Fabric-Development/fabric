import inspect
from inspect import FrameInfo
from types import FrameType
from typing import TypedDict
from dis import Positions
from loguru import logger
from fabric.service import *
from fabric.utils import ValueEnum
from fabric.utils import get_ixml
from gi.repository import Gio, GLib


(FABRIC_BUS_NAME, FABRIC_BUS_IFACE_NODE, FABRIC_BUS_PATH) = (
    *get_ixml("dbus_assets/org.Fabric.fabric.xml", "org.Fabric.fabric"),
    "/org/Fabric/fabric",
)


class LogLevel(ValueEnum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3


class HookPositionDict(TypedDict):
    line: int
    line_end: int
    col: int
    col_offset: int


class Hook(Service):
    frame = Property(value_type=object, flags="read")
    frame_info = Property(value_type=object, flags="read")
    global_scope = Property(value_type=object, flags="read")
    local_scope = Property(value_type=object, flags="read")
    code_ctx = Property(value_type=str, flags="read")
    code_position = Property(value_type=object, flags="read")
    file = Property(value_type=str, flags="read")
    __gsignals__ = SignalContainer(
        Signal("execute", "run-first", None, (object, object)),
        Signal("execute-error", "run-first", None, (object, object)),
        Signal("evaluate", "run-first", None, (object, object)),
        Signal("evaluate-error", "run-first", None, (object, object)),
    )

    def __init__(
        self,
        frame_info: FrameInfo | None,
    ):
        super().__init__()
        self.frame_info: FrameInfo | None = frame_info
        self.frame: FrameType | None = (
            frame_info.frame if frame_info is not None else None
        )
        self.global_scope: dict | None = (
            self.frame.f_globals if self.frame is not None else None
        )
        self.local_scope = self.frame.f_locals if self.frame is not None else None
        self.code_ctx: str = (
            frame_info.code_context[0]
            if frame_info is not None and frame_info.code_context is not None
            else "unknown"
        )
        self.code_position: HookPositionDict | None = self.get_dict_from_position(
            frame_info.positions
        )
        self.file: str = (
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
        exc = None
        try:
            exec(
                source,
                self.global_scope if self.global_scope is not None else {},
                self.local_scope if self.local_scope is not None else {},
            )
            self.emit("execute", source, None)
        except Exception as e:
            exc = e
            self.emit("execute-error", source, e)
        if raise_on_exception is True and not exc in (None, ""):
            raise exc
        return exc

    def evaluate(
        self, code: str, raise_on_exception: bool = False
    ) -> tuple[str | None, Exception | None]:
        result = None
        exc = None
        try:
            result = eval(
                code,
                self.global_scope if self.global_scope is not None else {},
                self.local_scope if self.local_scope is not None else {},
            )
            self.emit("evaluate", code, None)
        except Exception as e:
            exc = e
            self.emit("evaluate-error", code, e)
        if raise_on_exception is True and not exc in (None, ""):
            raise exc
        return result, exc

    def get_global_scope_object_is_class(
        self, obj_reference: str | object
    ) -> bool | None:
        return (
            inspect.isclass(self.global_scope.get(obj_reference, None))
            if self.global_scope is not None
            else None
        )

    def get_dict_from_position(self, positions: Positions | None) -> HookPositionDict:
        if positions is None:
            return HookPositionDict(line=0, line_end=0, col=0, col_offset=0)

        return HookPositionDict(
            line=positions.lineno if positions.lineno is not None else 0,
            line_end=positions.end_lineno if positions.end_lineno is not None else 0,
            col=positions.col_offset if positions.col_offset is not None else 0,
            col_offset=positions.end_col_offset
            if positions.end_col_offset is not None
            else 0,
        )


class DBusClient(Service):
    def __init__(self, hook: Hook, **kwargs):
        super().__init__(**kwargs)
        self._hook = hook
        self._connection: Gio.DBusConnection | None = None
        self.do_register()

    def do_register(self):
        return Gio.bus_own_name(
            Gio.BusType.SESSION,
            FABRIC_BUS_NAME,
            Gio.BusNameOwnerFlags.NONE,
            self.on_bus_acquired,
            None,
            lambda *args: logger.warning(
                "[DBusClient] The bus is already registered (or an error occured), another fabric instance is probably running"
            ),
        )

    def on_bus_acquired(
        self, conn: Gio.DBusConnection, name: str, user_data: object = None
    ):
        self.bus_connection = conn
        for interface in FABRIC_BUS_IFACE_NODE.interfaces:
            if interface.name == name:
                conn.register_object(
                    FABRIC_BUS_PATH, interface, self.do_handle_bus_call
                )

    def do_handle_bus_call(
        self,
        conn: Gio.DBusConnection,
        sender: str,
        path: str,
        interface: str,
        target: str,
        params: GLib.Variant | tuple,
        invocation: Gio.DBusMethodInvocation,
        user_data: object = None,
    ) -> None:
        props = {
            "File": GLib.Variant("s", self._hook.file),
        }

        match target:
            case "Get":
                prop_name = params[1] if len(params) >= 1 else None
                if not prop_name in props or not prop_name:
                    invocation.return_value(None)
                    conn.flush()
                    return
                invocation.return_value(GLib.Variant("(v)", [props.get(prop_name)]))
            case "GetAll":
                invocation.return_value(GLib.Variant("(a{sv})", [props]))
            case "Log":
                level: int
                message: str
                level, message = params
                logger.level
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
                source: str
                source = params[0]
                exc = self._hook.execute(
                    source,
                )
                exc = exc.__repr__() if not exc in ("", None) else None
                invocation.return_value(GLib.Variant("(s)", (exc or "",)))
            case "Evaluate":
                code: str
                code = params[0]
                result, exc = self._hook.evaluate(
                    code,
                )
                exc = exc.__repr__() if not exc in ("", None) else None
                invocation.return_value(GLib.Variant("(ss)", (str(result), exc or "")))
        return conn.flush()


def get_fabric_dbus_proxy() -> Gio.DBusProxy | None:
    proxy = Gio.DBusProxy.new_for_bus_sync(
        Gio.BusType.SESSION,
        Gio.DBusProxyFlags.NONE,
        None,
        FABRIC_BUS_NAME,
        FABRIC_BUS_PATH,
        FABRIC_BUS_NAME,
        None,
    )
    return proxy


def get_hook() -> Hook:
    frame_info = inspect.stack()[-1]
    hook = Hook(frame_info)
    return hook


def get_dbus_client() -> DBusClient:
    return DBusClient(get_hook())
