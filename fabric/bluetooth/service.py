import gi
from typing import Callable, Dict, List
from loguru import logger
from fabric.service import Service, Signal, SignalContainer, Property
from fabric.utils import bulk_connect
from gi.repository import Gio, GLib


class GnomeBluetoothImportError(ImportError):
    def __init__(self, *args):
        super().__init__(
            "gnome-bluetooth-3 is not installed, please install it first",
            *args,
        )


try:
    gi.require_version("GnomeBluetooth", "3.0")
    from gi.repository import GnomeBluetooth
except ValueError:
    raise GnomeBluetoothImportError()


class BluetoothDevice(Service):
    __gsignals__ = SignalContainer(
        Signal("connecting", "run-first", None, (bool,)),
        Signal("changed", "run-first", None, ()),  # type: ignore
        Signal("closed", "run-first", None, ()),  # type: ignore
    )

    def __init__(
        self, device: GnomeBluetooth.Device, client: GnomeBluetooth.Client, **kwargs
    ):
        self._device: GnomeBluetooth.Device = device
        self._client: GnomeBluetooth.Client = client
        self._signal_connectors: dict = {}
        for sn in [
            "battery-percentage",
            "battery-level",
            "connected",
            "trusted",
            "address",
            "paired",
            "alias",
            "icon",
            "name",
        ]:
            self._signal_connectors[sn] = self._device.connect(
                f"notify::{sn}", lambda *args, sn=sn: self.notifier(sn, args)
            )
        super().__init__(**kwargs)
        # To get the current state of connection
        GLib.idle_add(lambda: self.notify("connected"))

    @Property(value_type=object, flags="readable")
    def device(self) -> GnomeBluetooth.Device:
        return self._device

    @Property(value_type=str, flags="readable")
    def address(self) -> str:
        return self._device.props.address

    @Property(value_type=str, flags="readable")
    def alias(self) -> str:
        return self._device.props.alias

    @Property(value_type=str, flags="readable")
    def name(self) -> str:
        return self._device.props.name

    @Property(value_type=str, flags="readable")
    def icon(self) -> str:
        return self._device.props.icon

    @Property(value_type=str, flags="readable")
    def type(self) -> str:
        return GnomeBluetooth.type_to_string(self._device.type)  # type: ignore

    @Property(value_type=bool, default_value=False, flags="readable")
    def paired(self) -> bool:
        return self._device.props.paired

    @Property(value_type=bool, default_value=False, flags="readable")
    def trusted(self) -> bool:
        return self._device.props.trusted

    @Property(value_type=bool, default_value=False, flags="readable")
    def connected(self) -> bool:
        return self._device.props.connected

    @Property(value_type=int, flags="readable")
    def battery_level(self) -> int:
        return self._device.props.battery_level

    @Property(value_type=float, flags="readable")
    def battery_percentage(self) -> float:
        return self._device.props.battery_percentage

    def set_connection(self, connect: bool):
        self.emit("connecting", True)
        self.connect_device(connect, lambda *args: self.emit("connecting", False))

    def connect_device(self, connection: bool, callback: Callable):
        def inner_callback(client: GnomeBluetooth.Client, res: Gio.AsyncResult):
            try:
                finish = client.connect_service_finish(res)
                logger.info(f"[Bluetooth] Connected to device {self.address}")
                callback(finish)
            except Exception:
                logger.warning(
                    f"[Bluetooth] Failed to connect to device {self.address}"
                )
                callback(False)

        self._client.connect_service(
            self._device.get_object_path(),
            connection,
            None,
            inner_callback,
        )

    def close(self):
        for id in self._signal_connectors.values():
            try:
                self._device.disconnect(id)
            except Exception:
                pass
        self.emit("closed")

    def notifier(self, name: str, args=None):
        self.notify(name)
        self.emit("changed")
        return


class BluetoothClient(Service):
    __gsignals__ = SignalContainer(
        Signal("device-added", "run-first", None, (str,)),
        Signal("device-removed", "run-first", None, (str,)),
        Signal("changed", "run-first", None, ()),  # type: ignore
        Signal("closed", "run-first", None, ()),  # type: ignore
    )

    def __init__(self, **kwargs):
        self._client: GnomeBluetooth.Client = GnomeBluetooth.Client.new()  # type: ignore
        self._devices: Dict[str, GnomeBluetooth.Device] = {}
        bulk_connect(
            self._client,
            {
                "device-added": self.on_device_added,
                "device-removed": self.on_device_removed,
                "notify::default-adapter-state": lambda *args: self.notifier("state"),
                "notify::default-adapter-powered": lambda *args: self.notifier(
                    "enabled"
                ),
                "notify::default-adapter-setup-mode": lambda *args: self.notifier(
                    "scanning"
                ),
            },
        )
        for device in self._get_devices():
            self.on_device_added(self._client, device)  # type: ignore
        super().__init__(**kwargs)

    def toggle_power(self):
        GLib.idle_add(
            lambda: self._client.set_property(
                "default_adapter_powered",
                not self._client.props.default_adapter_powered,
            )
        )

    def toggle_scan(self):
        GLib.idle_add(
            lambda: self._client.set_property(
                "default_adapter_setup_mode",
                not self._client.props.default_adapter_setup_mode,
            )
        )

    def _get_devices(self):
        devices = []
        device_store: Gio.ListStore = self._client.get_devices()  # type: ignore
        for i in range(device_store.get_n_items()):
            device: GnomeBluetooth.Device = device_store.get_item(i)  # type: ignore
            if device.props.paired or device.props.trusted:
                devices.append(device)
        return devices

    def on_device_added(
        self, client: GnomeBluetooth.Client, device: GnomeBluetooth.Device
    ):
        if device.props.address in self._devices.keys():
            return
        # This may be a mistake, it fixed an issue with me but might not be the right choice
        #  We should probably let the user choose what to do with devices with no name
        if device.props.name is None:
            return
        logger.info(f"[Bluetooth] Device added: {device.props.address}")
        bluetooth_device: BluetoothDevice = BluetoothDevice(device, self._client)
        bluetooth_device.connect("changed", lambda _: self.emit("changed"))
        bluetooth_device.connect(
            "notify::connected", lambda *args: self.notify("connected-devices")
        )
        self._devices[device.props.address] = bluetooth_device
        self.notifier("devices")
        self.emit("device-added", device.props.address)

    def on_device_removed(self, client: GnomeBluetooth.Client, object_path: str):
        addr = object_path.split("/")[-1][4:].replace("_", ":")
        if addr not in self._devices.keys():
            return
        logger.info(f"[Bluetooth] Device removed: {addr}")
        was_connected: bool = self._devices[addr].connected
        self._devices[addr].close()
        self._devices.pop(addr)
        self.notifier("devices")
        if was_connected:
            self.notifier("connected-devices")
        self.emit("device-removed", addr)

    def get_device_from_addr(self, address: str) -> BluetoothDevice:
        return self._devices[address]

    def notifier(self, name: str, args=None):
        self.notify(name)
        self.emit("changed")
        return

    @Property(value_type=object, flags="readable")
    def devices(self) -> List:
        return list(self._devices.values())

    @Property(value_type=object, flags="readable")
    def connected_devices(self) -> List:
        ret = []
        for device in self._devices.values():
            if device.connected:
                ret.append(device)
        return ret

    @Property(value_type=str, flags="readable")
    def state(self) -> str:
        return {
            GnomeBluetooth.AdapterState.ABSENT: "absent",
            GnomeBluetooth.AdapterState.ON: "on",
            GnomeBluetooth.AdapterState.TURNING_ON: "turning-on",
            GnomeBluetooth.AdapterState.TURNING_OFF: "turning-off",
            GnomeBluetooth.AdapterState.OFF: "off",
        }.get(self._client.props.default_adapter_state, "unknown")

    @Property(value_type=int, flags="read-write")
    def scanning(self) -> int:  # type: ignore[no-redef]
        return self._client.props.default_adapter_setup_mode

    @scanning.setter
    def scanning(self, value):
        GLib.idle_add(
            lambda: self._client.set_property("default_adapter_setup_mode", value)
        )

    @Property(value_type=bool, default_value=False, flags="read-write")
    def enabled(self) -> bool:  # type: ignore[no-redef]
        return True if self.props.state in ["on", "turning-on"] else False

    @enabled.setter
    def enabled(self, value: bool):
        GLib.idle_add(
            lambda: self._client.set_property("default_adapter_powered", value)
        )
