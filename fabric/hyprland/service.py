import os
from loguru import logger
from dataclasses import dataclass
from collections.abc import Callable
from typing import ParamSpec, Concatenate, Any
from fabric.core.service import Service, Signal, Property

from fabric.utils.helpers import idle_add
from gi.repository import (
    Gio,
    GLib,
)

P = ParamSpec("P")
HYPRLAND_COMMAND_BUFFER_SIZE = 1_048_576  # 12mb -> binary bytes


# exceptions
# TODO: use the rest of 'em
class HyprlandError(Exception): ...


class HyprlandSocketError(Exception): ...


class HyprlandSocketNotFoundError(Exception): ...


# dataclasses with frozen flag
# to avoid unexpected changes
@dataclass(frozen=True)
class HyprlandEvent:
    name: str
    "the name of the received event"
    data: list[str]
    "the data gotten from event's body"
    raw_data: bytes
    "the data as it's from the socket's event, it may be formatted as following `event-name>>event-data1,event-data2`"


@dataclass(frozen=True)
class HyprlandReply:
    command: str
    "the passed in command"
    reply: bytes
    "the raw reply from Hyprland"
    is_ok: bool
    """
    this indicates if the ran command has returned `ok` or not
    if set to `False` this means either the command execution has failed
    or the command itself doesn't return a indication on if it failed or not
    (i.e commands that return data from Hyprland)
    """


class Hyprland(Service):
    """
    a connection to the Hyprland's socket
    this can be used for ONLY sending commands or both sending and receiving events
    """

    EVENTS_SOCKET = COMMANDS_SOCKET = None
    SOCKET_PATH = ""

    # refs
    # https://wiki.hyprland.org/IPC

    @Property(bool, "readable", "is-ready", default_value=False)
    def ready(self) -> bool:
        return self._ready

    @Signal
    def ready(self):
        return self.notify("ready")

    @Signal("event", flags="detailed")
    def event(self, event: object): ...

    def __init__(self, commands_only: bool = False, **kwargs):
        """
        :param commands_only: set to `True` if you're going to use this connection for sending commands only, defaults to False
        :type commands_only: bool, optional

        NOTE: since version v0.40.0 of Hyprland, the IPC socket path has been changed from `/tmp/hypr/` to `$XDG_RUNTIME_DIR/hypr/`

        this service is backward compaitible so this is just a friendly note
        """
        super().__init__(**kwargs)
        self._ready = False
        self.lookup_socket()  # set the above constants

        # all aboard...
        if not commands_only:
            self.event_socket_thread = GLib.Thread.new(
                "hyprland-socket-service", self.event_socket_task, self.EVENTS_SOCKET
            )

        self._ready = True
        self.ready.emit()

    @staticmethod
    def lookup_socket() -> tuple[Gio.UnixSocketAddress, Gio.UnixSocketAddress, str]:
        if (
            Hyprland.EVENTS_SOCKET and Hyprland.COMMANDS_SOCKET and Hyprland.SOCKET_PATH
        ):  # this _should_ handle "" as None
            return (
                Hyprland.EVENTS_SOCKET,
                Hyprland.COMMANDS_SOCKET,
                Hyprland.SOCKET_PATH,
            )

        runtime_dir = os.getenv("XDG_RUNTIME_DIR")
        hyprland_sig = os.getenv("HYPRLAND_INSTANCE_SIGNATURE")

        hyprland_dir = f"/tmp/hypr/{hyprland_sig}"
        if not os.path.isdir(hyprland_dir):
            # a new version of hyprland
            hyprland_dir = f"{runtime_dir}/hypr/{hyprland_sig}"

        if not os.path.isdir(hyprland_dir):
            # hyprland is not running
            raise HyprlandSocketNotFoundError(
                "couldn't find Hyprland socket, is Hyprland running?"
            )

        Hyprland.EVENTS_SOCKET = Gio.UnixSocketAddress.new(
            f"{hyprland_dir}/.socket2.sock"
        )
        Hyprland.COMMANDS_SOCKET = Gio.UnixSocketAddress.new(
            f"{hyprland_dir}/.socket.sock"
        )
        Hyprland.SOCKET_PATH = hyprland_dir

        return (
            Hyprland.EVENTS_SOCKET,
            Hyprland.COMMANDS_SOCKET,
            Hyprland.SOCKET_PATH,
        )

    @staticmethod
    def send_command(command: str) -> HyprlandReply:
        """
        send hyprctl-like commands over hyprland socket

        example usage:
        ```python
        # next workspace...
        Hyprland.send_command("/dispatch workspace e+1")
        ```

        :param command: the Hyprland command to send, see Hyprland's wiki for more info
        :type command: str
        :return: a command reply object contains the reply data from hyprland
        :rtype: HyprlandReply
        """
        resp = b""
        try:
            _, socket_addr, *__ = Hyprland.lookup_socket()

            # from Gio's docs:
            # > GSocketClient is a lightweight object, you don't need to cache it.
            # > You can just create a new one any time you need one.
            client = Gio.SocketClient()
            conn: Gio.SocketConnection = client.connect(socket_addr)
            stream: Gio.OutputStream = conn.get_output_stream()  # type: ignore

            # write command's content
            stream.write(command.encode())  # type: ignore
            stream.flush()  # type: ignore

            # read return data
            input_stream = Gio.DataInputStream.new(conn.get_input_stream())  # type: ignore
            raw_data: GLib.Bytes = input_stream.read_bytes(HYPRLAND_COMMAND_BUFFER_SIZE)
            resp: bytes = raw_data.get_data()  # type: ignore
        except Exception as e:
            logger.error(
                f"[HyprlandService] got error while sending command via socket ({e})"
            )

        return HyprlandReply(
            command=command,
            reply=resp,
            is_ok=True if resp == b"ok" else False,
        )

    @staticmethod
    def send_command_async(
        command: str,
        callback: Callable[Concatenate[HyprlandReply, P], Any],
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> None:
        """send hyprctl-like commands asynchronously
        this function will act same as `send_command` but in a asynchronous manner

        NOTE: `*args` and `**kwargs` are passed directly into your callback

        :param command: the Hyprland command to send, see Hyprland's wiki for more info
        :type command: str
        :param callback: the callback on where would you like to receive the reply of the command
        :type callback: Callable[[HyprlandReply], Any]
        """
        _, socket_addr, *_ = Hyprland.lookup_socket()

        # from Gio's docs:
        # > GSocketClient is a lightweight object, you don't need to cache it.
        # > You can just create a new one any time you need one.
        client = Gio.SocketClient()

        def reader_callback(
            input_stream: Gio.DataInputStream, res: Gio.AsyncResult, *_
        ):
            raw_data: GLib.Bytes = input_stream.read_bytes_finish(res)
            resp: bytes = raw_data.get_data()  # type: ignore
            print("data if any: ", resp)
            callback(
                HyprlandReply(
                    command=command,
                    reply=resp,
                    is_ok=True if resp == b"ok" else False,
                ),
                *args,
                **kwargs,
            )

        def client_callback(client: Gio.SocketClient, res: Gio.AsyncResult, *_):
            conn: Gio.SocketConnection = client.connect_finish(res)
            stream: Gio.OutputStream = conn.get_output_stream()  # type: ignore
            input_stream = Gio.DataInputStream.new(conn.get_input_stream())  # type: ignore

            # write command's content
            stream.write_async(  # type: ignore
                command.encode(),
                HYPRLAND_COMMAND_BUFFER_SIZE,
                None,  # type: ignore
                None,
                None,
                None,
            )
            stream.flush_async(1, None, None, None)  # type: ignore

            # the connection object must be have a living pointer
            # in our case it's passed over to reader_callback
            # if there's no references to the connection found
            # the GC will collect the connection object and thus the input stream
            # this will result in a undefined behaviour
            # this is a bug with PyGObject (or at least an issue with the ref counter)
            input_stream.read_bytes_async(
                HYPRLAND_COMMAND_BUFFER_SIZE, 1, None, reader_callback, conn
            )

        client.connect_async(socket_addr, None, client_callback, None)

        return None

    def event_socket_task(self, socket_addr: Gio.UnixSocketAddress) -> bool:
        client = Gio.SocketClient()
        conn: Gio.SocketConnection = client.connect(socket_addr)
        stream: Gio.InputStream = conn.get_input_stream()  # type: ignore
        input_stream = Gio.DataInputStream.new(stream)

        while not stream.is_closed():
            raw_data: list[bytes] = input_stream.read_line(None)  # type: ignore
            if b">>" not in raw_data[0]:
                # hyprland broke, it happens...
                logger.error(
                    f"[HyprlandService] hyprland returned wrong data ({raw_data})"
                )
                continue

            idle_add(self.handle_raw_event, raw_data[0])

        logger.warning("[HyprlandService] events socket thread ended")
        return False

    def handle_raw_event(self, raw_event: bytes):
        raw_listed = str((raw_event).decode()).split(">>")
        if len(raw_listed) < 1:
            return  # how?.. i mean Why?

        event_name: str = raw_listed[0]
        raw_event_body: str = "".join(raw_listed[1:])
        event_body: list[str] = raw_event_body.split(",")

        event = HyprlandEvent(event_name, event_body, raw_event)

        return self.emit(f"event::{event.name}", event)
