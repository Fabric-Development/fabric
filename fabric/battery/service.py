import gi
from fabric.core.service import Property, Service, Signal
from gi.repository import Gio, GLib
from loguru import logger

gi.require_version("Gtk", "3.0")


BATTERY_BUS_NAME = "org.freedesktop.UPower"
BATTERY_BUS_PATH = "/org/freedesktop/UPower/devices/DisplayDevice"
BATTERY_INTERFACE = "org.freedesktop.UPower.Device"

DEVICE_STATE = {
    0: "UNKNOWN",
    1: "CHARGING",
    2: "DISCHARGING",
    3: "EMPTY",
    4: "FULLY_CHARGED",
    5: "PENDING_CHARGE",
    6: "PENDING_DISCHARGE",
}


class Battery(Service):
    """A service for interacting with the battery's DBus"""

    @Signal
    def changed(self) -> None: ...

    @Property(type=bool, default=False)
    def available(self) -> bool:
        return self.do_get_cached_property("IsPresent") or False

    @Property(type=str, default="")
    def vendor(self) -> str:
        return self.do_get_cached_property("Vendor") or ""

    @Property(type=int, default=0)
    def percent(self) -> int:
        return self.do_get_cached_property("Percentage") or 0

    @Property(type=bool, default=False)
    def charging(self) -> bool:
        val = self.do_get_cached_property("Charging")
        if val is None:
            return False
        return val == DEVICE_STATE.get("CHARGING", 1)

    @Property(type=bool, default=False)
    def charged(self) -> bool:
        val = self.do_get_cached_property("FullyCharged")
        if val is None:
            return False
        return val == DEVICE_STATE.get("FULLY_CHARGED", 4)

    @Property(type=str, default="")
    def icon_name(self) -> str:
        return self.do_get_cached_property("IconName") or ""

    @Property(type=int, default=0)
    def time_remaining(self) -> int:
        return self.do_get_cached_property("TimeToEmpty") or 0

    @Property(type=int, default=0)
    def time_to_full(self) -> int:
        return self.do_get_cached_property("TimeToFull") or 0

    @Property(type=float, default=0.0)
    def energy(self) -> float:
        return self.do_get_cached_property("Energy") or 0.0

    @Property(type=float, default=0.0)
    def energy_full(self) -> float:
        return self.do_get_cached_property("EnergyFull") or 0.0

    @Property(type=float, default=0.0)
    def energy_rate(self) -> float:
        return self.do_get_cached_property("EnergyRate") or 0.0

    @Property(type=float, default=0.0)
    def temperature(self) -> float:
        return self.do_get_cached_property("Temperature") or 0.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._bus: Gio.DBusConnection | None = None
        self.do_register()

    def do_register(self) -> None:
        self._bus = Gio.bus_get_sync(Gio.BusType.SYSTEM)
        self._proxy = Gio.DBusProxy.new_sync(
            self._bus,
            Gio.DBusProxyFlags.NONE,
            None,
            BATTERY_BUS_NAME,
            BATTERY_BUS_PATH,
            BATTERY_INTERFACE,
            None,
        )

        logger.info("[Battery] Proxy initialized")

        # Listen for PropertiesChanged signals
        self._bus.signal_subscribe(
            BATTERY_BUS_NAME,
            "org.freedesktop.DBus.Properties",
            "PropertiesChanged",
            BATTERY_BUS_PATH,
            None,
            Gio.DBusSignalFlags.NONE,
            self.do_handle_property_change,
        )

    def do_handle_property_change(self, *_):
        self.emit("changed")

    def do_call_proxy_method(
        self,
        bus_name,
        object_path,
        interface_name,
        method_name,
        parameters=None,
        timeout=-1,
    ):
        if parameters is None:
            parameters = GLib.Variant("()", ())
        result = self._bus.call_sync(
            bus_name,
            object_path,
            interface_name,
            method_name,
            parameters,
            None,
            Gio.DBusCallFlags.NONE,
            timeout,
            None,
        )
        return result.unpack()

    def do_get_cached_property(self, property_name):
        result = self._proxy.get_cached_property(property_name)
        return result.unpack() if result is not None else None
