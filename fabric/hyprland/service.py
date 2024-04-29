import os
import asyncio
from loguru import logger
from dataclasses import dataclass
from fabric.service import *
from gi.repository import (
    Gio,
    GLib,
)


# exceptions
# TODO: use the rest of 'em
class HyprlandError(Exception):
    ...


class HyprlandSocketError(Exception):
    ...


class HyprlandSocketNotFoundError(Exception):
    ...


# dataclasses with frozen flag
# to avoid unexpected changess
@dataclass(frozen=True)
class HyprlandEvent:
    name: str
    data: dict | str | None
    raw_data: bytes | str | None
    service: object


@dataclass(frozen=True)
class HyprlandReply:
    """
    NOTE: if is_ok is `None` that means the socket did not returned ok as the response
    so commands that returns a json object for example will cause is_ok to be `None`
    make sure you have some way to handle this or ignoring is_ok at all.
    """

    command: str
    reply: dict | str | bytes | None
    service: object
    is_ok: bool = None


HYPRLAND_SIGNALS = [
    # custom helper signals.
    Signal(name="ready", flags="run-first", rtype=None, args=()),
    Signal(name="error", flags="deprecated", rtype=None, args=(str,)),  # TODO: remove
    Signal(name="any", flags="run-first", rtype=None, args=(object,)),
    # actual hyprland events.
    # https://wiki.hyprland.org/IPC for more info.
    Signal(name="workspace", flags="run-first", rtype=None, args=(object,)),
    Signal(name="workspacev2", flags="run-first", rtype=None, args=(object,)),
    Signal(name="focusedmon", flags="run-first", rtype=None, args=(object,)),
    Signal(name="activewindow", flags="run-first", rtype=None, args=(object,)),
    Signal(name="activewindowv2", flags="run-first", rtype=None, args=(object,)),
    Signal(name="fullscreen", flags="run-first", rtype=None, args=(object,)),
    Signal(name="monitorremoved", flags="run-first", rtype=None, args=(object,)),
    Signal(name="monitoradded", flags="run-first", rtype=None, args=(object,)),
    Signal(name="monitoraddedv2", flags="run-first", rtype=None, args=(object,)),
    Signal(name="createworkspace", flags="run-first", rtype=None, args=(object,)),
    Signal(name="createworkspacev2", flags="run-first", rtype=None, args=(object,)),
    Signal(name="destroyworkspace", flags="run-first", rtype=None, args=(object,)),
    Signal(name="destroyworkspacev2", flags="run-first", rtype=None, args=(object,)),
    Signal(name="moveworkspace", flags="run-first", rtype=None, args=(object,)),
    Signal(name="moveworkspacev2", flags="run-first", rtype=None, args=(object,)),
    Signal(name="renameworkspace", flags="run-first", rtype=None, args=(object,)),
    Signal(name="activespecial", flags="run-first", rtype=None, args=(object,)),
    Signal(name="activelayout", flags="run-first", rtype=None, args=(object,)),
    Signal(name="openwindow", flags="run-first", rtype=None, args=(object,)),
    Signal(name="closewindow", flags="run-first", rtype=None, args=(object,)),
    Signal(name="movewindow", flags="run-first", rtype=None, args=(object,)),
    Signal(name="movewindowv2", flags="run-first", rtype=None, args=(object,)),
    Signal(name="openlayer", flags="run-first", rtype=None, args=(object,)),
    Signal(name="closelayer", flags="run-first", rtype=None, args=(object,)),
    Signal(name="submap", flags="run-first", rtype=None, args=(object,)),
    Signal(name="changefloatingmode", flags="run-first", rtype=None, args=(object,)),
    Signal(name="urgent", flags="run-first", rtype=None, args=(object,)),
    Signal(name="minimize", flags="run-first", rtype=None, args=(object,)),
    Signal(name="screencast", flags="run-first", rtype=None, args=(object,)),
    Signal(name="windowtitle", flags="run-first", rtype=None, args=(object,)),
    Signal(name="ignoregrouplock", flags="run-first", rtype=None, args=(object,)),
    Signal(name="lockgroups", flags="run-first", rtype=None, args=(object,)),
    Signal(name="configreloaded", flags="run-first", rtype=None, args=(object,)),
    Signal(name="pin", flags="run-first", rtype=None, args=(object,)),
]


class Hyprland(Service):
    """
    a connection to the hyprland's socket
    this can be used for ONLY sending commands or both sending and receiving events
    """

    __gsignals__ = SignalContainer(*HYPRLAND_SIGNALS)

    def __init__(self, commands_only: bool = False, **kwargs):
        """
        :param commands_only: set to `True` if you're going to use this connection for sending commands only, defaults to False
        :type commands_only: bool, optional
        """
        super().__init__(**kwargs)
        self.HYPRLAND_SIGNATURE = os.getenv("HYPRLAND_INSTANCE_SIGNATURE")
        self.BASE_SOCKET_PATH = (
            new_path
            if os.path.isdir(
                (
                    new_path
                    := f"{os.getenv('XDG_RUNTIME_DIR')}/hypr/{self.HYPRLAND_SIGNATURE}"
                )
            )
            else f"/tmp/hypr/{self.HYPRLAND_SIGNATURE}"
        )
        if not os.path.isdir(self.BASE_SOCKET_PATH):
            # hyprland is not running.
            raise HyprlandSocketNotFoundError(
                "Hyprland socket doenst seem to be found, Hyprland is running?"
            )
        # all aboard
        self.HYPRLAND_EVENTS_SOCKET = f"{self.BASE_SOCKET_PATH}/.socket2.sock"
        self.HYPRLAND_COMMANDS_SOCKET = f"{self.BASE_SOCKET_PATH}/.socket.sock"
        if not commands_only:
            self.event_socket_thread = GLib.Thread.new(
                "hyprland-socket-service",
                self.event_socket_task,
                self.HYPRLAND_EVENTS_SOCKET,
            )
        GLib.idle_add(lambda: (self.emit("ready"), True))

    def send_command(self, command: str) -> HyprlandReply:
        """
        to send hyprctl-like commands over hyprland socket

        example usage:
        ```python
        # next workspace...
        send_command("/dispatch workspace e+1")
        ```

        :param command: the command to send
        :type command: str
        :return: a command reply object contains the reply data from hyprland
        :rtype: HyprlandReply
        """

        return asyncio.run(self.send_command_async(command))

    async def send_command_async(self, command: str) -> HyprlandReply:
        """same as send_command but async"""
        try:
            reader, writer = await asyncio.open_unix_connection(
                self.HYPRLAND_COMMANDS_SOCKET
            )
            writer.write(command.encode())
            await writer.drain()
            resp = await reader.read(-1)
            writer.close()
        except Exception as e:
            return logger.error(f"[HyprlandService] socket Error, {e}")
        return HyprlandReply(
            command=command,
            reply=resp,
            service=self,
            is_ok=True if resp == b"ok" else None,
        )

    def event_socket_task(self, socket_path: str) -> bool:
        addr: Gio.UnixSocketAddress = Gio.UnixSocketAddress.new(
            socket_path,  # the path to the events socket.
        )
        client = Gio.SocketClient()
        conn: Gio.SocketConnection = client.connect(addr)
        stream: Gio.InputStream = conn.get_input_stream()
        input_stream = Gio.DataInputStream.new(stream)
        while True:
            raw_data: list[bytes, object] | bytearray = input_stream.read_line(
                None,
            )
            if not b">>" in raw_data[0]:
                # hyprland is broken, it does happen.
                logger.error(
                    f"[HyprlandService] hyprland returned wrong data ({raw_data})"
                )
                continue
            raw_listed = str((raw_data[0]).decode()).split(">>")
            if not raw_listed[0] in [x.name for x in HYPRLAND_SIGNALS]:
                logger.warning(
                    f"got an unknown event from hyprland ({raw_listed}), probably a new event added to hyprland, report this."
                )
                continue
            event_object = HyprlandEvent(
                name=raw_listed[0],
                data=raw_listed[1].split(",") if len(raw_listed) > 1 else None,
                raw_data=raw_data,
                service=self,
            )
            self.emit(
                event_object.name,
                event_object,
            )
            self.emit(
                "any",
                event_object,
            )
        logger.warning("[HyprlandService] events socket thread ended")
        return False
