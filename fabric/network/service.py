import gi
from loguru import logger
from collections.abc import Callable
from typing import ParamSpec, Literal, Concatenate, Any
from fabric.core.service import Service, Signal, Property
from fabric.utils.helpers import (
    bulk_connect,
    get_enum_member_name,
    snake_case_to_kebab_case,
    bridge_signal,
)

from gi.repository import Gio

try:
    gi.require_version("GnomeBluetooth", "3.0")
    from gi.repository import NM as NetworkManager
except Exception:
    raise ImportError("gnome-bluetooth-3 is not installed, please install it first")


class Connection(Service):  # base block for both wlan & eth
    @Property(NetworkManager.ActiveConnection, flags="readable")
    def connection(self) -> NetworkManager.ActiveConnection:
        return self._connection

    @Property(str, flags="readable")
    def connection_type(self) -> Literal["wifi", "wired", "unknown"]:
        return self._connection_type  # type: ignore

    @Property(str, flags="readable")
    def status(
        self,
    ) -> Literal["connected", "connecting", "disconnected", "disconnecting", "unknown"]:
        return get_enum_member_name(
            self._connection.get_state(),
            {
                "ACTIVATING": "connecting",
                "ACTIVATED": "connected",
                "DEACTIVATING": "disconnecting",
                "DEACTIVATED": "disconnected",
            },
            default="unknown",
        ).lower()  # type: ignore

    def __init__(
        self,
        connection: NetworkManager.ActiveConnection,
        connection_type: str,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self._connection = connection
        self._connection_type = connection_type

        self._status = "unknown"


class Network(Service):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
