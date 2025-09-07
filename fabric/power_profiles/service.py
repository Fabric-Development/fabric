import gi
from fabric.core.service import Property, Service, Signal
from gi.repository import Gio, GLib
from loguru import logger

gi.require_version("Gtk", "3.0")

POWER_PROFILES_BUS_NAME = "net.hadess.PowerProfiles"
POWER_PROFILES_BUS_PATH = "/net/hadess/PowerProfiles"


class PowerProfiles(Service):
    """A service for interacting with PowerProfiles' DBus"""

    @Signal
    def changed(self) -> None: ...

    @Property(str, "read-write")
    def active_profile(self) -> str:
        prop = self._proxy.get_cached_property("ActiveProfile")
        return prop.unpack() if prop else "balanced"

    @active_profile.setter
    def active_profile(self, profile: str) -> None:
        try:
            self.do_call_proxy_method(
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
            logger.info(f"[PowerProfiles] Power profile set to {profile}")
        except Exception as e:
            logger.exception(
                f"[PowerProfiles] Could not change power level to {profile}: {e}"
            )

    @Property(list, "readable")
    def profiles(self) -> list[str]:
        prop = self._proxy.get_cached_property("Profiles")
        return prop.unpack() if prop else []

    @Property(bool, "readable", default_value=False)
    def battery_aware(self) -> bool:
        prop = self._proxy.get_cached_property("BatteryAware")
        return prop.unpack() if prop else False

    @Property(list, "readable")
    def actions(self) -> list[str]:
        prop = self._proxy.get_cached_property("Actions")
        return prop.unpack() if prop else []

    @Property(list, "readable")
    def actions_info(self) -> list[str]:
        prop = self._proxy.get_cached_property("ActionsInfo")
        return prop.unpack() if prop else []

    @Property(list, "readable")
    def active_profile_holds(self) -> list[str]:
        prop = self._proxy.get_cached_property("ActiveProfileHolds")
        return prop.unpack() if prop else []

    @Property(str, "readable")
    def icon_name(self) -> str:
        return f"power-profile-{self.active_profile}-symbolic"

    @Property(str, "readable")
    def performance_degraded(self) -> str:
        prop = self._proxy.get_cached_property("PerformanceDegraded")
        return prop.unpack() if prop else ""

    @Property(str, "readable")
    def performance_inhibited(self) -> str:
        prop = self._proxy.get_cached_property("PerformanceInhibited")
        return prop.unpack() if prop else ""

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
