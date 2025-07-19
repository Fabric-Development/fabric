import os
import json

from dataclasses import dataclass
from typing import ParamSpec, Concatenate, Any
from collections.abc import Callable
from loguru import logger
from gi.repository import Gio, GLib

from fabric.core.service import Service, Signal, Property
from fabric.utils.helpers import idle_add

P = ParamSpec("P")
NIRI_COMMAND_BUFFER_SIZE = 1_048_576  # 1MB

class NiriError(Exception): ...
class NiriSocketNotFoundError(Exception): ...

@dataclass(frozen=True)
class NiriReply:
    command: str
    reply: dict
    is_ok: bool

@dataclass(frozen=True)
class NiriEvent:
    name: str
    data: dict
    raw: str

class Niri(Service):
    """
    A Fabric-compatible service to interact with the Niri window manager via its IPC socket.
    """

    SOCKET_PATH = ""

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
        self.lookup_socket()

        # if not self.socket_path or not os.path.exists(self.socket_path):
        #     raise NiriSocketNotFoundError("NIRI_SOCKET not found or invalid.")

        if not commands_only:
            self.event_socket_thread = GLib.Thread.new(
                "niri-event-thread", self.event_socket_task, None
            )

        self._ready = True
        self.ready.emit()

    @staticmethod
    def lookup_socket() -> str:
        if not os.path.exists(os.getenv("NIRI_SOCKET")):
            raise NiriSocketNotFoundError("NIRI_SOCKET not found or invalid.")

    @staticmethod
    def send_command(command: str | dict) -> NiriReply:
        """
        Send a command (e.g. "Workspaces") to the Niri IPC socket.
        """
        response = {}
        try:
            address = Niri.lookup_socket()

            client = Gio.SocketClient()
            conn: Gio.SocketConnection = client.connect(address)
            stream: Gio.OutputStream = conn.get_output_stream()

            # ostream = conn.get_output_stream()
            # istream = Gio.DataInputStream.new(conn.get_input_stream())

            if isinstance(command, dict):
                stream.write((json.dumps(command) + "\n").encode())
            else:
                stream.write((f'"{command}"\n').encode())

            stream.flush()

            input_stream = Gio.DataInputStream.new(conn.get_input_stream())
            raw_data = input_stream.read_line_utf8(None)[0]
            response = json.loads(raw_data)
        except Exception as e:
            logger.error(f"[NiriService] Failed to send command '{command}': {e}")

        return NiriReply(command=command, reply=response, is_ok="Ok" in response)

    @staticmethod
    def send_command_async(
        command: str,
        callback: Callable[Concatenate[NiriReply, P], Any],
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> None:
        address = Niri.lookup_socket()
        client = Gio.SocketClient()

        def reader_callback(input_stream: Gio.DataInputStream, res: Gio.AsyncResult, *_):
            try:
                raw_data = input_stream.read_line_finish_utf8(res)[0]
                reply = NiriReply(command=command, reply=json.loads(raw), is_ok="Ok" in data)
            except Exception as e:
                logger.error(f"[NiriService] Async command error: {e}")
                reply = NiriReply(command=command, reply={}, is_ok=False)

            callback(reply, *args, **kwargs)

        def client_callback(client: Gio.SocketClient, res: Gio.AsyncResult, *_):
            try:
                conn: Gio.SocketConnection = client.connect_finish(res)
                stream: Gio.OutputStream = conn.get_output_stream()
                input_stream = Gio.DataInputStream.new(conn.get_input_stream())

                stream.write_async(
                    f'"{command}"\n'.encode(),
                    NIRI_COMMAND_BUFFER_SIZE,
                    None, None, None, None
                )
                stream.flush_async(1, None, None, None)
                input_stream.read_line_async(1, None, reader_callback, conn)
            except Exception as e:
                logger.error(f"[NiriService] Async connect error: {e}")

        client.connect_async(address, None, client_callback, None)
        return None

    def event_socket_task(self, _) -> bool:
        """
        Listens for events using Niri's 'EventStream' mechanism.
        """
        try:
            address = Niri.lookup_socket()
            client = Gio.SocketClient()
            conn: Gio.SocketConnection = client.connect(address)
            ostream = conn.get_output_stream()
            istream = Gio.DataInputStream.new(conn.get_input_stream())

            # Tell Niri to start streaming events
            ostream.write((f'"EventStream"\n').encode())
            ostream.flush()

            while not ostream.is_closed():
                raw = istream.read_line_utf8(None)
                if raw is None or raw[0] is None:
                    continue

                try:
                    raw_str = raw[0]
                    event_data = json.loads(raw_str)
                    event_name = next(iter(event_data))
                    event_obj = NiriEvent(name=event_name, data=event_data[event_name], raw=raw_str)

                    idle_add(self.emit, f"event::{event_name}", event_obj)
                except Exception as e:
                    logger.error(f"[NiriService] Event parse error: {e}")
        except Exception as e:
            logger.error(f"[NiriService] Event socket error: {e}")

        return False

