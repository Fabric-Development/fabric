import dbus
import dbus.service
import inspect
from inspect import FrameInfo
from types import FrameType
from typing import TypedDict
from dis import Positions
from dbus.mainloop.glib import DBusGMainLoop, threads_init
from loguru import logger
from fabric.service import *
from fabric.utils.enum import ValueEnum

FABRIC_BUS_NAME = "org.Fabric.fabric"
FABRIC_BUS_PATH = "/org/Fabric/fabric"

threads_init()
DBusGMainLoop(set_as_default=True)


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
        Signal("exec", "run-first", None, (object, object))
        # args: source-code: str (i guess), exception: if any else none
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
    ) -> tuple[str, Exception | None]:
        """executes python code within this hook scopes (globals and locals)
        this method emits the `exec` siganl
        the siganl function will receive the code and the exception (if any, if not then None)

        :param source: the python code to execute
        :type source: str
        :param raise_on_exception: whether you want this method to raise the exception from the `exec` function or just return the exception, defaults to False (return the exception)
        :type raise_on_exception: bool, optional
        :raises exc: if an exception has happened and the `raise_on_exception` arg is set to True
        :return: a tuple that contains the given string of code and the exception (if any)
        :rtype: tuple[str, Exception | None]
        """
        exc = None
        try:
            exec(
                source,
                self.global_scope if self.global_scope is not None else {},
                self.local_scope if self.local_scope is not None else {},
            )
            self.emit("exec", source, None)
        except Exception as e:
            exc = e
            self.emit("exec", source, e)
        if raise_on_exception is True and exc is not None:
            raise exc
        return source, exc

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
            return {
                "line": 0,
                "line_end": 0,
                "col": 0,
                "col_offset": 0,
            }

        return {
            "line": positions.lineno if positions.lineno is not None else 0,
            "line_end": positions.end_lineno if positions.end_lineno is not None else 0,
            "col": positions.col_offset if positions.col_offset is not None else 0,
            "col_offset": positions.end_col_offset
            if positions.end_col_offset is not None
            else 0,
        }


class DbusClient(dbus.service.Object):
    def __init__(self, client: Service, **kwargs):
        self.client: Service = client
        self.bus = dbus.SessionBus()
        self.bus_name = dbus.service.BusName(FABRIC_BUS_NAME, bus=dbus.SessionBus())
        super().__init__(self.bus_name, FABRIC_BUS_PATH, self.bus)

    @dbus.service.method(FABRIC_BUS_NAME, in_signature="sb", out_signature="s")
    def execute(self, source: str, raise_on_exception: bool | int = False) -> str:
        data = self.client.execute(
            source,
            raise_on_exception
            if isinstance(raise_on_exception, bool)
            else True
            if raise_on_exception == 1
            else False
            if raise_on_exception == 0
            else False,
        )
        data = (str(data[0]), data[1].__repr__() if data[1] is not None else "")
        return str(data)

    @dbus.service.method(FABRIC_BUS_NAME, in_signature="si", out_signature="s")
    def log(self, data: str, level: int | str = 0):
        if isinstance(level, str):
            level = LogLevel.get_member(level.upper())
        return str(
            logger.debug(data)
            if level == 0
            else logger.info(data)
            if level == 1
            else logger.warning(data)
            if level == 2
            else logger.error(data)
            if level == 3
            else logger.info(data)
        )

    @dbus.service.method(FABRIC_BUS_NAME, signature="s")
    def file(self) -> str:
        # TODO: use property instead
        return str(self.client.hook.file)


class Client(Service):
    hook = Property(value_type=Service, flags="read")
    dbus_client = Property(value_type=object, flags="read")
    __gsignals__ = SignalContainer(
        Signal(
            "exec",
            "run-first",
            None,
            (object, object, object),
            # ^^^^^^ pass the hook to callback
        )
    )

    def __init__(self, hook: Hook, **kwargs):
        super().__init__(**kwargs)
        self.hook: Hook = hook
        self.dbus_client = DbusClient(self)
        self.hook.connect("exec", lambda *args: self.emit("exec", *args))

    def execute(
        self, source: str, raise_on_exception: bool = False
    ) -> tuple[str, Exception | None]:
        return self.hook.execute(source, raise_on_exception)


def get_fabric_session_bus() -> dbus.Interface | None:
    try:
        session_bus = dbus.SessionBus()
        obj = session_bus.get_object(FABRIC_BUS_NAME, FABRIC_BUS_PATH)
        iface = dbus.Interface(obj, FABRIC_BUS_NAME)
        return iface
    except dbus.exceptions.DBusException:
        return None


def get_hook() -> Hook:
    frame_info = inspect.stack()[-1]
    hook = Hook(frame_info)
    return hook


def get_client() -> Client:
    return Client(get_hook())
