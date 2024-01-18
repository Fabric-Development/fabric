from typing import Any
from typing import Callable
from typing import Optional

from gi.repository import Gio
from gi.repository import GObject

ATTR_APPLICATION_ICON: str = "application.icon"
ATTR_APPLICATION_ICON_NAME: str = "application.icon_name"
ATTR_APPLICATION_ID: str = "application.id"
ATTR_APPLICATION_LANGUAGE: str = "application.language"
ATTR_APPLICATION_NAME: str = "application.name"
ATTR_APPLICATION_PROCESS_BINARY: str = "application.process.binary"
ATTR_APPLICATION_PROCESS_HOST: str = "application.process.host"
ATTR_APPLICATION_PROCESS_ID: str = "application.process.id"
ATTR_APPLICATION_PROCESS_USER: str = "application.process.user"
ATTR_APPLICATION_VERSION: str = "application.version"
ATTR_CANBERRA_CACHE_CONTROL: str = "canberra.cache-control"
ATTR_CANBERRA_ENABLE: str = "canberra.enable"
ATTR_CANBERRA_FORCE_CHANNEL: str = "canberra.force_channel"
ATTR_CANBERRA_VOLUME: str = "canberra.volume"
ATTR_CANBERRA_XDG_THEME_NAME: str = "canberra.xdg-theme.name"
ATTR_CANBERRA_XDG_THEME_OUTPUT_PROFILE: str = "canberra.xdg-theme.output-profile"
ATTR_EVENT_DESCRIPTION: str = "event.description"
ATTR_EVENT_ID: str = "event.id"
ATTR_EVENT_MOUSE_BUTTON: str = "event.mouse.button"
ATTR_EVENT_MOUSE_HPOS: str = "event.mouse.hpos"
ATTR_EVENT_MOUSE_VPOS: str = "event.mouse.vpos"
ATTR_EVENT_MOUSE_X: str = "event.mouse.x"
ATTR_EVENT_MOUSE_Y: str = "event.mouse.y"
ATTR_MEDIA_ARTIST: str = "media.artist"
ATTR_MEDIA_FILENAME: str = "media.filename"
ATTR_MEDIA_ICON: str = "media.icon"
ATTR_MEDIA_ICON_NAME: str = "media.icon_name"
ATTR_MEDIA_LANGUAGE: str = "media.language"
ATTR_MEDIA_NAME: str = "media.name"
ATTR_MEDIA_ROLE: str = "media.role"
ATTR_MEDIA_TITLE: str = "media.title"
ATTR_WINDOW_DESKTOP: str = "window.desktop"
ATTR_WINDOW_HEIGHT: str = "window.height"
ATTR_WINDOW_HPOS: str = "window.hpos"
ATTR_WINDOW_ICON: str = "window.icon"
ATTR_WINDOW_ICON_NAME: str = "window.icon_name"
ATTR_WINDOW_ID: str = "window.id"
ATTR_WINDOW_NAME: str = "window.name"
ATTR_WINDOW_VPOS: str = "window.vpos"
ATTR_WINDOW_WIDTH: str = "window.width"
ATTR_WINDOW_X: str = "window.x"
ATTR_WINDOW_X11_DISPLAY: str = "window.x11.display"
ATTR_WINDOW_X11_MONITOR: str = "window.x11.monitor"
ATTR_WINDOW_X11_SCREEN: str = "window.x11.screen"
ATTR_WINDOW_X11_XID: str = "window.x11.xid"
ATTR_WINDOW_Y: str = "window.y"
_namespace: str = "GSound"
_version: str = "1.0"

def error_quark() -> int: ...

class Context(GObject.Object, Gio.Initable):
    def cache(self, attrs: dict[str, str]) -> bool: ...
    @classmethod
    def new(cls, cancellable: Optional[Gio.Cancellable] = None) -> Context: ...
    def open(self) -> bool: ...
    def play_full(
        self,
        attrs: dict[str, str],
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def play_full_finish(self, result: Gio.AsyncResult) -> bool: ...
    def play_simple(
        self, attrs: dict[str, str], cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def set_attributes(self, attrs: dict[str, str]) -> bool: ...
    def set_driver(self, driver: str) -> bool: ...

class ContextClass(GObject.GPointer): ...

class Error(GObject.GEnum):
    ACCESS = -13
    CANCELED = -11
    CORRUPT = -7
    DESTROYED = -10
    DISABLED = -16
    DISCONNECTED = -18
    FORKED = -17
    INTERNAL = -15
    INVALID = -2
    IO = -14
    NODRIVER = -5
    NOTAVAILABLE = -12
    NOTFOUND = -9
    NOTSUPPORTED = -1
    OOM = -4
    STATE = -3
    SYSTEM = -6
    TOOBIG = -8
