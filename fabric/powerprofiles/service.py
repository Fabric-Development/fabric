import gi
from fabric.core.service import Property, Service, Signal
from gi.repository import Gio, GLib
from loguru import logger

gi.require_version("Gtk", "3.0")

POWER_PROFILES_BUS_NAME = "net.hadess.PowerProfiles"
POWER_PROFILES_BUS_PATH = "/net/hadess/PowerProfiles"


class PowerProfiles(Service):
    """Service to interact with the PowerProfiles service via GIO."""

    @Signal
    def changed(self) -> None: ...

    @Property(str, "read-write")
    def active_profile(self) -> str:
        prop = self._proxy.get_cached_property("ActiveProfile")
        return prop.unpack() if prop else "balanced"

    @active_profile.setter
    def active_profile(self, profile: str) -> None:
        try:
            self.call_method(
                bus_name=POWER_PROFILES_BUS_NAME,
                object_path=POWER_PROFILES_BUS_PATH,
                interface_name="org.freedesktop.DBus.Properties",
                method_name="Set",
                parameters=GLib.Variant(
                    "(ssv)",
                    (
                        POWER_PROFILES_BUS_NAME,
                        "ActiveProfile",
                        GLib.Variant("s", profile),
                    ),
                ),
            )
            logger.info(f"[PowerProfile] Power profile set to {profile}")
        except Exception as e:
            logger.exception(
                f"[PowerProfile] Could not change power level to {profile}: {e}"
            )

    @Property(list, "read-write")
    def profiles(self) -> list[str]:
        prop = self._proxy.get_cached_property("Profiles")
        return prop.unpack() if prop else []

    @Property(bool, "read-write", default_value=False)
    def performance_degraded(self) -> bool:
        prop = self._proxy.get_cached_property("PerformanceDegraded")
        return prop.unpack() if prop else False

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
            POWER_PROFILES_BUS_NAME,
            POWER_PROFILES_BUS_PATH,
            POWER_PROFILES_BUS_NAME,
            None,
        )

        logger.info("[PowerProfiles] Proxy initialized")

        # Listen for PropertiesChanged signals
        self._bus.signal_subscribe(
            POWER_PROFILES_BUS_NAME,
            "org.freedesktop.DBus.Properties",
            "PropertiesChanged",
            POWER_PROFILES_BUS_PATH,
            arg0=None,
            flags=Gio.DBusSignalFlags.NONE,
            callback=self.handle_property_change,
        )

    def handle_property_change(self, *_):
        self.emit("changed")

    def call_method(
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
