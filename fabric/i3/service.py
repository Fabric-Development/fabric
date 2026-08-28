import os
import json
import socket
import struct
from enum import IntEnum
from loguru import logger
from typing import ParamSpec
from dataclasses import dataclass
from fabric.core.service import Service, Signal, Property
from fabric.utils.helpers import exec_shell_command, idle_add
from gi.repository import GLib

P = ParamSpec("P")

SOCKET_MAGIC = b"i3-ipc"


# exceptions
class I3Error(Exception): ...


class I3SocketError(I3Error): ...


class I3SocketNotFoundError(I3SocketError): ...


class I3MessageType(IntEnum):
    # commands
    COMMAND = 0
    GET_WORKSPACES = 1
    SUBSCRIBE = 2
    GET_OUTPUTS = 3
    GET_TREE = 4
    GET_MARKS = 5
    GET_BAR_CONFIG = 6
    GET_VERSION = 7
    GET_BINDING_MODES = 8
    GET_CONFIG = 9
    SEND_TICK = 10
    SYNC = 11
    GET_BINDING_STATE = 12
    # sway only
    GET_INPUTS = 100
    GET_SEATS = 101

    # events
    WORKSPACE_EVENT = 0x80000000
    OUTPUT_EVENT = 0x80000001
    MODE_EVENT = 0x80000002
    WINDOW_EVENT = 0x80000003
    BARCONFIG_UPDATE_EVENT = 0x80000004
    BINDING_EVENT = 0x80000005
    SHUTDOWN_EVENT = 0x80000006
    TICK_EVENT = 0x80000007
    # sway only
    BAR_STATE_UPDATE_EVENT = 0x80000014
    INPUT_EVENT = 0x80000015


@dataclass(frozen=True)
class I3Event:
    name: str
    "the name of the received event"
    data: dict
    "the json data gotten from event's body"
    raw_data: bytes
    "the raw json data"


@dataclass(frozen=True)
class I3Reply:
    command: str
    "the passed in command"
    reply: dict | list
    "the raw reply from i3/sway as a dict or list"
    is_ok: bool
    "this indicates if the ran command has returned a success message"


class I3(Service):
    """
    A connection to the i3/Sway's IPC socket.
    This can be used for sending commands and receiving events.
    """

    SOCKET_PATH: str | None = None

    @Property(bool, "readable", "is-ready", default_value=False)
    def ready(self) -> bool:
        return self._ready

    @Signal("event", flags="detailed")
    def event(self, event: object): ...

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._ready = False
        self.lookup_socket()

        self.event_socket_thread = GLib.Thread.new(
            "i3-socket-service",
            self.event_socket_task,  # type: ignore
            self.SOCKET_PATH,
        )

        self._ready = True
        self.notify("ready")

    @staticmethod
    def lookup_socket() -> str:
        if I3.SOCKET_PATH:
            return I3.SOCKET_PATH

        for cmd in ("sway", "i3"):
            path = exec_shell_command(f"{cmd} --get-socketpath")
            if not path or not (path := path.strip()) or not os.path.exists(path):
                continue

            I3.SOCKET_PATH = path

            return I3.SOCKET_PATH

        raise I3SocketNotFoundError(
            "Couldn't find i3 or Sway socket, is either of them running?"
        )

    @staticmethod
    def pack(message_type: I3MessageType, payload: str = "") -> bytes:
        payload_bytes = payload.encode()
        header = struct.pack("<II", len(payload_bytes), message_type.value)
        return SOCKET_MAGIC + header + payload_bytes

    @staticmethod
    def unpack(connection: socket.socket) -> tuple[int, str]:
        header = connection.recv(14)
        if len(header) != 14:
            raise I3SocketError("Failed to read IPC header")

        magic, length, message_type = struct.unpack("<6sII", header)
        if magic != SOCKET_MAGIC:
            raise I3SocketError(f"Invalid IPC magic string ({magic}). Report this!")

        return message_type, connection.recv(length).decode()

    @staticmethod
    def send_command(
        command: str, message_type: I3MessageType = I3MessageType.COMMAND
    ) -> I3Reply:
        """
        Sends a command to the i3/sway socket.

        example usage:
        ```python
        # next workspace...
        I3.send_command("workspace next")
        ```
        :param command: The command to send.
        :type command: str
        :param message_type: The type of message to send.
        :type message_type: I3MessageType, optional
        :return: A reply object containing the data from i3/sway.
        :rtype: I3Reply
        """
        reply_data = {}
        is_ok = False
        try:
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
                sock.connect(I3.lookup_socket())
                sock.sendall(I3.pack(message_type, command))

                _, payload = I3.unpack(sock)
                reply_data = json.loads(payload)

                # results for any GET_* command is considered ok
                # other commands a success reply is a list of dicts with {"success": True}
                if (message_type != I3MessageType.COMMAND) or (
                    isinstance(reply_data, list)
                    and reply_data
                    and reply_data[0].get("success")
                ):
                    is_ok = True

        except Exception as e:
            logger.error(
                f"[I3Service] got error while sending command via socket ({e})"
            )

        return I3Reply(command=command, reply=reply_data, is_ok=is_ok)

    def event_socket_task(self, socket_addr: str) -> bool:
        try:
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
                sock.connect(socket_addr)

                # subscribe to all events
                sock.sendall(
                    self.pack(
                        I3MessageType.SUBSCRIBE,
                        json.dumps(
                            [
                                evnt_name.replace("_event", "")
                                for mt in I3MessageType
                                if (evnt_name := mt.name.lower()).endswith("_event")
                            ]
                        ),
                    )
                )
                self.unpack(sock)  # success reply

                while True:
                    idle_add(self.handle_raw_event, *self.unpack(sock))

        except Exception as e:
            logger.warning(f"[I3Service] events socket thread ended with an error: {e}")

        return False

    def handle_raw_event(self, message_type: int, payload: str):
        event_data = json.loads(payload)
        event_name = I3MessageType(message_type).name.lower().replace("_event", "")

        if "change" in event_data:  # subevents
            event_name = f"{event_name}::{event_data['change']}"

        return self.emit(
            f"event::{event_name}",
            I3Event(event_name, event_data, payload.encode()),
        )
