import fabric
from loguru import logger
from fabric.widgets import (
    Box,
    Label,
    Image,
    Button,
    Window,
    CenterBox,
    ScrolledWindow,
)
from fabric.bluetooth import BluetoothClient, BluetoothDevice
from fabric.utils import set_stylesheet_from_file, get_relative_path


class BtDeviceBox(CenterBox):
    def __init__(self, device: BluetoothDevice, **kwargs):
        super().__init__(spacing=2, name="bt-device-box", **kwargs)
        self.device = device
        self.device.connect("closed", lambda _: self.destroy())

        self.connect_button = Button()
        self.connect_button.connect(
            "clicked", lambda _: self.device.set_connection(not self.device.connected)
        )
        self.device.connect("connecting", self.on_device_connecting)
        self.device.connect("notify::connected", self.on_device_connect)

        self.add_start(Image(icon_name=device.icon, icon_size=6))  # type: ignore
        self.add_start(Label(label=device.name))  # type: ignore
        self.add_end(self.connect_button)

    def on_device_connecting(self, device, connecting):
        self.connect_button.set_label(
            "connecting..."
        ) if connecting else self.connect_button.set_label("failed to connect")

    def on_device_connect(self, *args):
        self.connect_button.set_label(
            "connected"
        ) if self.device.connected else self.connect_button.set_label("disconnected")


class BtConnectionsList(Box):
    def __init__(self, **kwargs):
        super().__init__(
            orientation="vertical",
            spacing=5,
            name="bt-box",
            **kwargs,
        )

        self.client = BluetoothClient()
        self.client.connect("device-added", self.new_device)
        self.scan_button = Button()
        self.scan_button.connect("clicked", lambda _: self.client.toggle_scan())
        self.client.connect(
            "notify::scanning",
            lambda *args: self.scan_button.set_label("stop")
            if self.client.scanning
            else self.scan_button.set_label("scan"),
        )
        self.toggle_button = Button()
        self.toggle_button.connect("clicked", lambda _: self.client.toggle_power())
        self.client.connect(
            "notify::enabled",
            lambda *args: self.toggle_button.set_label("bluetooth on")
            if self.client.enabled
            else self.toggle_button.set_label("bluetooth off"),
        )

        self.paired_box = Box(orientation="vertical")
        self.available_box = Box(orientation="vertical")

        self.add(
            CenterBox(start_children=self.scan_button, end_children=self.toggle_button)
        )
        self.add(Label("Paired Devices"))
        self.add(self.paired_box)
        self.add(Label("Available Devices"))
        self.add(
            ScrolledWindow(
                min_content_height=400,
                children=self.available_box,
            )
        )

    def new_device(self, client: BluetoothClient, address):
        device: BluetoothDevice = client.get_device_from_addr(address)
        if device.paired:
            self.paired_box.add(BtDeviceBox(device))
        else:
            self.available_box.add(BtDeviceBox(device))


class BluetoothWidget(Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer="top",
            anchor="top right",
            name="main-window",
            visible=False,
            all_visible=False,
            exclusive=True,
        )
        self.btbox = BtConnectionsList()
        self.add(self.btbox)
        self.show_all()


def apply_style(*args):
    logger.info("[Bluetooth Widget] CSS applied")
    return set_stylesheet_from_file(get_relative_path("bluetooth_widget.css"))


if __name__ == "__main__":
    bt = BluetoothWidget()
    apply_style()
    fabric.start()
