import json
from dataclasses import dataclass
from typing import ParamSpec, cast

from gi.repository import Gio, GLib
from loguru import logger

from fabric.core.service import Property, Service, Signal
from fabric.utils.helpers import (
    idle_add,
    pascal_case_to_snake_case,
    snake_case_to_kebab_case,
)

P = ParamSpec("P")


# exceptions
class NiriError(Exception): ...


class NiriSocketError(NiriError): ...


class NiriSocketNotFoundError(NiriSocketError): ...


# dataclasses with frozen flag
# to avoid unexpected changes
@dataclass(frozen=True)
class NiriEvent:
    name: str
    "the name of the received event"
    data: dict | list | str
    "data gathered from the event's body"
    raw_data: bytes
    "the data as is from the socket event"


@dataclass(frozen=True)
class NiriReply:
    command: dict | list | str
    "the command fed to get this reply"
    reply: bytes
    "the reply line raw bytes raw bytes are given to avoid deserializing commands that the user typically ignores its output"
    is_ok: bool
    "if the command ran successfuly or not, this is infered through a basic check (if reply has `'Err'` in it then `is_ok` is `False`)"


class Niri(Service):
    """
    a connection to a running Niri instance's socket
    """

    # refs
    # https://github.com/niri-wm/niri/wiki/IPC
    # https://niri-wm.github.io/niri/niri_ipc/enum.Event.html

    SOCKET: Gio.UnixSocketAddress | None = None
    SOCKET_PATH: str = ""

    @Property(bool, "readable", "is-ready", default_value=False)
    def ready(self) -> bool:
        return self._ready

    @Signal
    def ready(self):
        return self.notify("ready")

    @Signal("event", flags="detailed")
    def event(self, event: object): ...

    def __init__(self, commands_only: bool = False, **kwargs):
        super().__init__(**kwargs)
        self._ready = False
        self.lookup_socket()  # set the above constants

        self._command_conn = Gio.SocketClient().connect(
            cast(Gio.UnixSocketAddress, self.SOCKET)
        )
        self._command_writer = Gio.DataOutputStream.new(
            self._command_conn.get_output_stream()
        )
        self._command_reader = Gio.DataInputStream.new(
            self._command_conn.get_input_stream()
        )

        self._event_conn: Gio.SocketConnection = Gio.SocketClient().connect(
            cast(Gio.UnixSocketAddress, self.SOCKET)
        )
        self._event_writer = Gio.DataOutputStream.new(
            self._event_conn.get_output_stream()
        )
        self._event_reader = Gio.DataInputStream.new(
            self._event_conn.get_input_stream()
        )

        # all aboard...
        if not commands_only:
            self.event_socket_thread = GLib.Thread.new(
                "niri-socket-service", self.do_handle_event_socket_task
            )

        self._ready = True
        self.ready.emit()

    @staticmethod
    def lookup_socket() -> tuple[Gio.UnixSocketAddress, str]:
        if Niri.SOCKET and Niri.SOCKET_PATH:  # this _should_ handle "" as None
            return (Niri.SOCKET, Niri.SOCKET_PATH)

        if not (socket_path := GLib.getenv("NIRI_SOCKET")) and GLib.file_test(
            socket_path, GLib.FileTest.EXISTS
        ):
            raise NiriSocketNotFoundError("couldn't find Niri socket, is Niri running?")

        Niri.SOCKET = Gio.UnixSocketAddress.new(socket_path)
        Niri.SOCKET_PATH = socket_path

        return (Niri.SOCKET, Niri.SOCKET_PATH)

    def do_handle_event_socket_task(self) -> bool:
        self._event_writer.put_string('"EventStream"\n', None)
        self._event_conn.get_output_stream().flush(None)

        raw_reply, length = self._event_reader.read_line()

        if length <= 0 or (b"Ok" not in raw_reply):
            raise NiriSocketError(
                "Niri closed the event socket before acknowledging EventStream"
            )

        while not self._event_reader.is_closed():
            raw_data, _ = cast(tuple[bytes, int], self._event_reader.read_line())  # type: ignore

            idle_add(self.do_handle_raw_event, raw_data)

        logger.warning("[NiriService] events socket thread ended")
        return False

    def do_handle_raw_event(
        self, raw_event: bytes
    ):  # shall not be called from a threads
        decoded_event: dict[str, dict | list | str] = json.loads(raw_event)
        ((event_name, event_body),) = decoded_event.items()

        event = NiriEvent(
            snake_case_to_kebab_case(pascal_case_to_snake_case(event_name)),  # sick
            event_body,
            raw_event,
        )

        return self.emit(f"event::{event.name}", event)

    def send_command(self, command: dict | list | str):
        encoded_command = (
            json.dumps(
                command,
                separators=(",", ":"),
            ).encode("utf-8")
            + b"\n"
        )

        self._command_writer.write_all(
            encoded_command,
            None,
        )

        self._command_writer.flush(None)

        raw_reply, _ = self._command_reader.read_line()

        return NiriReply(command, raw_reply, b'"Err":' not in raw_reply)

    # TODO: send_command_async
