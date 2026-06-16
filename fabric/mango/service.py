import os
import json
from loguru import logger
from dataclasses import dataclass
from collections.abc import Callable
from typing import ParamSpec, Concatenate, Any, Self, override
from fabric.core.service import Service, Signal, Property

from fabric.utils.helpers import idle_add, make_arguments_ignorable
from gi.repository import (
    Gio,
    GLib,
)

P = ParamSpec("P")
MANGO_INSTANCE_SIGNATURE = os.getenv("MANGO_INSTANCE_SIGNATURE")
MANGO_COMMAND_BUFFER_SIZE = 1_048_576

class MangoError(Exception): ...


class MangoSocketError(Exception): ...


class MangoSocketNotFoundError(Exception): ...



@dataclass(frozen=True)
class MangoEvent:
    name: str
    "the name of the received event"
    data: Any
    "the data gotten from event's body"
    raw_data: bytes
    "the data as it's from the socket's event, it may be formatted as a JSON object"


@dataclass(frozen=True)
class MangoReply:
    command: str
    "the passed in command"
    reply: bytes
    "the raw reply from Mango"
    parsed_reply: dict
    "the parsed JSON reply turned into a python dictionary for simplicity"
    is_ok: bool
    """
    indicates if the command executed successfully without errors.
    set to False if the mango returned an object containing an 'error' key.
    """


class Mango(Service):
    
    SOCKET_PATH: str | None = None
    SOCKET_ADDRESS: Gio.UnixSocketAddress | None = None
    
    @Property(bool, "readable", "is-ready", default_value=False)
    def ready(self) -> bool:
        return self._ready

    @Signal
    def ready(self):
        return self.notify("ready")

    @Signal("event", flags="detailed")
    def event(self, event: object): ...


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self._ready: bool = False
        self._active_streams: set[str] = set()
        
        self.lookup_socket()
        
        self._ready = True
        self.ready.emit()
    
    @override
    def connect(
        self,
        signal_name: str,
        callback: Callable[Concatenate[Self, P], Any] | Callable,
        *args,
        ignore_missing: bool = True,):
        
        
        if signal_name.startswith("event::"):
            
            watch_target = signal_name[7:]
            
            if watch_target not in self._active_streams and watch_target != "event":
                self._active_streams.add(watch_target)
                
                GLib.Thread.new(
                    f"mango-watch-{watch_target.replace(' ', '_')}", 
                    self.event_socket_task, 
                    watch_target
                )
        
        
        return super().connect(
            signal_name,
            make_arguments_ignorable(callback) if ignore_missing else callback,
            *args,
        )
        
    
    
    @staticmethod
    def lookup_socket():
        if Mango.SOCKET_ADDRESS and Mango.SOCKET_PATH:
            return Mango.SOCKET_PATH
    
        if (MANGO_INSTANCE_SIGNATURE is not None) and os.path.exists(MANGO_INSTANCE_SIGNATURE):
            Mango.SOCKET_PATH = MANGO_INSTANCE_SIGNATURE
            Mango.SOCKET_ADDRESS = Gio.UnixSocketAddress.new(Mango.SOCKET_PATH)
            return Mango.SOCKET_PATH
        
        raise MangoSocketNotFoundError("couldn't find mango socket, is mango running?")
    
    @staticmethod
    def send_command(command: str):
        
        resp = b""
        
        try:
            Mango.lookup_socket()
            
            client = Gio.SocketClient()
            conn: Gio.SocketConnection = client.connect(Mango.SOCKET_ADDRESS)
            stream: Gio.OutputStream = conn.get_output_stream()
            
            stream.write(command.encode())
            stream.flush() 
            
            
            input_stream = Gio.DataInputStream.new(conn.get_input_stream())
            raw_data: GLib.Bytes = input_stream.read_bytes(MANGO_COMMAND_BUFFER_SIZE)
            resp: bytes = raw_data.get_data()
            
            parsed_resp = json.loads(resp.decode('utf-8'))
            
            is_ok = "error" not in parsed_resp
            
            return MangoReply(
                command=command,
                reply=resp,
                parsed_reply=parsed_resp,
                is_ok=is_ok
            )
            
        except Exception as e:
            logger.error(
                f"[MangoService] got error while sending command via socket ({e})"
            )
            
            return MangoReply(
                command=command,
                reply=resp,
                parsed_reply={},
                is_ok=False
            )
    
    @staticmethod
    def send_command_async(command: str, callable: Callable[Concatenate[MangoReply, P], Any], *args: P.args, **kwargs: P.kwargs):
        
        Mango.lookup_socket()
        
        client = Gio.SocketClient()
        
        def reader_callback(input_stream: Gio.DataInputStream, res: Gio.AsyncResult, *_):
            try:
                raw_data: GLib.Bytes = input_stream.read_bytes_finish(res)
                resp: bytes = raw_data.get_data()
                
                parsed_resp = json.loads(resp.decode("utf-8"))
                is_ok = "error" not in parsed_resp
            except Exception as e:
                logger.error(f"[MangoService] Async payload unpacking failed: {e}")
                
                resp = b""
                parsed_resp = {}
                is_ok = False
            
            callable(
                MangoReply(
                    command=command,
                    reply=resp,
                    parsed_reply=parsed_resp,
                    is_ok=is_ok
                ),
                *args,
                **kwargs
            )
        
        def client_callback(client: Gio.SocketClient, res: Gio.AsyncResult, *_):
            try:
                conn: Gio.SocketConnection = client.connect_finish(res)
                stream: Gio.OutputStream = conn.get_output_stream()
                input_stream = Gio.DataInputStream.new(conn.get_input_stream()) 
                
                stream.write_async( 
                command.encode(),
                    MANGO_COMMAND_BUFFER_SIZE,
                    None,
                    None,
                    None,
                    None,
                )
                stream.flush_async(1, None, None, None)
                input_stream.read_bytes_async(
                    MANGO_COMMAND_BUFFER_SIZE, 1, None, reader_callback, conn
                )
            except Exception as e:
                logger.error(f"[MangoService] Async connection setup failed: {e}")
                
                callable(
                    MangoReply(
                        command=command,
                        reply=b"",
                        parsed_reply={},
                        is_ok=False
                    ),
                    *args,
                    **kwargs
                )
        client.connect_async(Mango.SOCKET_ADDRESS, None, client_callback, None)
    
    def event_socket_task(self, watch_target: str) -> bool:
        try:
            client = Gio.SocketClient()
            conn: Gio.SocketConnection = client.connect(Mango.SOCKET_ADDRESS)
            
            output_stream: Gio.OutputStream = conn.get_output_stream()
            watch_cmd = f"watch {watch_target}\n"
            output_stream.write(watch_cmd.encode())
            output_stream.flush()
            
            stream: Gio.InputStream = conn.get_input_stream()  # type: ignore
            input_stream = Gio.DataInputStream.new(stream)
            
            while not stream.is_closed():
                raw_data: tuple[bytes, int] = input_stream.read_line(None)
                line_bytes = raw_data[0]
    
                if not line_bytes:
                    break
    
                idle_add(self.handle_raw_event, watch_target, line_bytes)
            
            
            
        except Exception as e:
            logger.error(f"[MangoService] Event socket thread error: {e}")
        finally:
            if watch_target in self._active_streams:
                self._active_streams.remove(watch_target)
        
        logger.warning("[MangoService] events socket thread ended")
        return False
    
    def handle_raw_event(self, watch_target: str, raw_event: bytes):
        
        if not raw_event or raw_event.strip() == b"":
            return
        
        data = None
        try:
            data = json.loads(raw_event.decode("utf-8"))
        except Exception as e:
            logger.error(f"[MangoService] failed to decode json string: {e}")
            
            return
        
        
        event = MangoEvent(
            name=watch_target,
            data=data,
            raw_data=raw_event
        )
        
        self.emit(f"event::{watch_target}", event)
        
        return self.emit("event", event)
            
        
            