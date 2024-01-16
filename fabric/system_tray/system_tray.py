# TODO: split this thing into a service and a widget, i have to go right now
# IDEA: implement this with another non-blocking dbus library, Gio is a bit broken
# NOTE: this is a work in progress, for now it works as a widget
import gi
import os
from loguru import logger
from fabric.widgets.box import Box
from fabric.widgets.button import Button

gi.require_version("Gtk", "3.0")
gi.require_version("DbusmenuGtk3", "0.4")
from gi.repository import (
    Gtk,
    Gdk,
    GLib,
    GdkPixbuf,
    DbusmenuGtk3,
    Gio,
)


def get_ixml(path_to_xml: str, interface: str):
    with open(path_to_xml, "r") as f:
        file = f.read()
    return interface, Gio.DBusNodeInfo.new_for_xml(file), file


DBUS_FOLDER_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "dbus")
)

(
    STATUS_NOTIFIER_WATCHER_IFACE,
    STATUS_NOTIFIER_WATCHER_NODE_INFO,
    STATUS_NOTIFIER_WATCHER_IFACE_XML,
) = get_ixml(
    f"{DBUS_FOLDER_PATH}/org.kde.StatusNotifierWatcher.xml",
    "org.kde.StatusNotifierWatcher",
)
(
    STATUS_NOTIFIER_ITEM_IFACE,
    STATUS_NOTIFIER_ITEM_NODE_INFO,
    STATUS_NOTIFIER_IFACE_XML,
) = get_ixml(
    f"{DBUS_FOLDER_PATH}/org.kde.StatusNotifierItem.xml", "org.kde.StatusNotifierItem"
)


class SystemTrayItem(Button):
    def __init__(
        self,
        dbus_name: str = None,
        dbus_object_path: str = None,
    ):
        super().__init__()
        self.dbus_name = dbus_name
        self.dbus_object_path = dbus_object_path
        self.proxy: Gio.DBusProxy = Gio.DBusProxy.new_for_bus_sync(
            Gio.BusType.SESSION,
            Gio.DBusProxyFlags.NONE,
            STATUS_NOTIFIER_ITEM_NODE_INFO.interfaces[0],
            dbus_name,
            dbus_object_path,
            STATUS_NOTIFIER_ITEM_IFACE,
            None,
        )
        self.connection = self.proxy.get_connection()
        self.dbus_menu = (
            self.create_menu(dbus_name, self.proxy.get_cached_property("Menu").unpack())
            if self.proxy.get_cached_property("Menu") is not None
            else None
        )
        self.icon_size = 18
        self.icon_theme = Gtk.IconTheme.get_default()
        self.set_image(Gtk.Image(pixbuf=self.icon)) if self.icon is not None else None
        self.set_tooltip_markup(
            self.tooltip_markup
        ) if self.tooltip_markup is not None else None
        self.connect("button-press-event", self.on_clicked)

    # i had to do that, sorry to myself.
    @property
    def id(self):
        return self.proxy.get_cached_property("Id").unpack()

    @property
    def title(self):
        return (
            self.proxy.get_cached_property("Title").unpack()
            if self.proxy.get_cached_property("Title") is not None
            else None
        )

    @property
    def status(self):
        return (
            self.proxy.get_cached_property("Status").unpack()
            if self.proxy.get_cached_property("Status") is not None
            else None
        )

    @property
    def category(self):
        return (
            self.proxy.get_cached_property("Category").unpack()
            if self.proxy.get_cached_property("Category") is not None
            else None
        )

    @property
    def is_menu(self):
        return (
            self.proxy.get_cached_property("ItemIsMenu").unpack()
            if self.proxy.get_cached_property("ItemIsMenu") is not None
            else None
        )

    @property
    def window_id(self):
        return (
            self.proxy.get_cached_property("WindowId").unpack()
            if self.proxy.get_cached_property("WindowId") is not None
            else None
        )

    @property
    def tooltip_markup(self):
        if self.proxy.get_cached_property("ToolTip") is None:
            return self.title if self.title is not None else self.id
        tooltip_raw = self.proxy.get_cached_property("ToolTip").unpack()
        tooltip = tooltip_raw[2]
        if tooltip_raw[3] != "":
            tooltip += "\n" + tooltip_raw[3]
        return tooltip

    @property
    def icon(self) -> GdkPixbuf.Pixbuf:
        icon_name: str | None = (
            self.proxy.get_cached_property("AttentionIconName").unpack()
            if (
                self.proxy.get_cached_property("NeedsAttention") is not None
                and self.proxy.get_cached_property("AttentionIconName") is not None
            )
            else self.proxy.get_cached_property("IconName").unpack()
            if self.proxy.get_cached_property("IconName") is not None
            else self.proxy.get_cached_property("Id").unpack()
            if self.proxy.get_cached_property("Id") is not None
            else None
        )
        icon_pixmap = (
            self.proxy.get_cached_property("AttentionIconPixmap").unpack()
            if (
                self.proxy.get_cached_property("NeedsAttention") is not None
                and self.proxy.get_cached_property("AttentionIconPixmap") is not None
            )
            else self.proxy.get_cached_property("IconPixmap").unpack()
            if self.proxy.get_cached_property("IconPixmap") is not None
            else None
        )
        icon_pixbuf = (
            self.pixbuf_from_pixmap_array(icon_pixmap, self.icon_size)
            if icon_pixmap is not None
            else self.pixbuf_from_icon_name(icon_name, self.icon_size)
            if icon_name is not None
            else None
        )
        return icon_pixbuf

    def create_menu(self, dbus_name: str, menu_object_path: str) -> DbusmenuGtk3.Menu:
        menu = DbusmenuGtk3.Menu().new(
            dbus_name,
            menu_object_path,
        )
        menu.show()
        return menu

    def on_clicked(self, button: Gtk.Button, event: Gdk.EventButton):
        if event.button == 1:
            try:
                self.proxy.Activate("(ii)", *event.get_root_coords())
            except Exception as e:
                logger.warning(e)
        elif event.button == 3:
            if self.dbus_menu is not None:
                self.dbus_menu.popup_at_widget(
                    button, Gdk.Gravity.SOUTH, Gdk.Gravity.NORTH, event
                )

    def pixbuf_from_pixmap_array(
        self, pix_map_array: list, icon_size: int = 22
    ) -> None | GdkPixbuf.Pixbuf:
        if not pix_map_array:
            return None

        pix_map = sorted(pix_map_array, key=lambda x: x[0])[-1]
        if not pix_map:
            return None

        array = bytearray(pix_map[2])
        for i in range(0, 4 * pix_map[0] * pix_map[1], 4):
            alpha = array[i]
            array[i] = array[i + 1]
            array[i + 1] = array[i + 2]
            array[i + 2] = array[i + 3]
            array[i + 3] = alpha

        bytes_data = GLib.Bytes.new(array)
        pixbuf = GdkPixbuf.Pixbuf.new_from_bytes(
            bytes_data,
            GdkPixbuf.Colorspace.RGB,
            True,
            8,
            pix_map[0],
            pix_map[1],
            pix_map[0] * 4,
        )
        return pixbuf.scale_simple(icon_size, icon_size, GdkPixbuf.InterpType.HYPER)

    def pixbuf_from_icon_name(
        self,
        icon_name: str,
        size: int,
        default_icon: str = "unknown",
    ) -> GdkPixbuf.Pixbuf:
        if self.icon_theme.has_icon(icon_name):
            icon_info = self.icon_theme.lookup_icon(icon_name, size, 0)
            if icon_info:
                pixbuf: GdkPixbuf.Pixbuf = icon_info.load_icon()
                return pixbuf
        else:
            icon_info = self.icon_theme.lookup_icon(default_icon, size, 0)
            if icon_info:
                pixbuf: GdkPixbuf.Pixbuf = icon_info.load_icon()
                return pixbuf
        return None


class SystemTray(Box):
    def __init__(
        self,
        spacing: int | None = None,
        orientation: Gtk.Orientation | str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_compiled: bool = True,
        style_append: bool = False,
        style_add_brackets: bool = True,
        name: str | None = None,
        size: tuple[int] | None = None,
        **kwargs,
    ):
        super().__init__(
            spacing,
            orientation,
            None,
            visible,
            all_visible,
            style,
            style_compiled,
            style_append,
            style_add_brackets,
            name,
            size,
            **kwargs,
        )
        self.connection: Gio.DBusConnection = None
        self.bus_owner_id: int = self.register_bus_name()
        self.items: list = []
        self.registered_tray_buttons: dict = {}

    def register_bus_name(self) -> int:
        return Gio.bus_own_name(
            Gio.BusType.SESSION,
            STATUS_NOTIFIER_WATCHER_IFACE,
            Gio.BusNameOwnerFlags.NONE,
            self.on_bus_acquired,
            None,
            lambda *args: print(
                "The bus is already registered before (or an error occured)"
            ),
        )

    def on_bus_acquired(
        self, conn: Gio.DBusConnection, name: str, user_data: object = None
    ):
        self.connection = conn
        # we're now the owner of the bus
        for interface in STATUS_NOTIFIER_WATCHER_NODE_INFO.interfaces:
            if interface.name == name:
                conn.register_object(
                    "/StatusNotifierWatcher", interface, self.on_signal
                )
        self.subscribe_to_signal(conn, "org.freedesktop.DBus", "NameOwnerChanged")

    def subscribe_to_signal(
        self, conn: Gio.DBusConnection, interface: str, signal: str = None
    ):
        return conn.signal_subscribe(
            None,  # sender
            interface,
            signal,
            None,  # path
            None,
            Gio.DBusSignalFlags.NONE,
            self.on_signal,
            None,  # user_data
        )

    def on_signal(
        self,
        conn: Gio.DBusConnection,
        sender: str,
        path: str,
        interface: str,
        signal: str,
        params: GLib.Variant | tuple,
        invocation: Gio.DBusMethodInvocation,
        user_data: object = None,
    ):
        props = {
            "RegisteredStatusNotifierItems": GLib.Variant("as", self.items),
            "IsStatusNotifierHostRegistered": GLib.Variant("b", True),
        }

        if signal == "NameOwnerChanged":
            if params[2] != "":
                return
            items = [item for item in self.items if item.startswith(params[0] + "/")]
            if not items:
                return
            for item in items:
                self.remove_item(item)
            return

        if signal == "Get" and params[1] in props:
            invocation.return_value(GLib.Variant("(v)", [props[params[1]]]))
            conn.flush()
        if signal == "GetAll":
            invocation.return_value(GLib.Variant("(a{sv})", [props]))
            conn.flush()
        elif signal == "RegisterStatusNotifierItem":
            if params[0].startswith("/"):
                path = params[0]
            else:
                path = "/StatusNotifierItem"
            self.create_item(conn, sender, path)
            invocation.return_value(None)
            conn.flush()

        logger.debug(
            f"STATUS NOTIFIER WATCHER:\n{sender} {path} {interface} {signal} {params} {invocation}\n",
        )

    def create_item(self, conn: Gio.DBusConnection, sender: str, path):
        self.items.append(sender + path)
        button = SystemTrayItem(sender, path)
        self.registered_tray_buttons[sender + path] = button
        self.add(button)
        button.show()

    def remove_item(self, item: str):
        button: Gtk.Button | None = self.registered_tray_buttons.get(item)
        self.remove(button)
        button.destroy()
        self.items.remove(item)
        self.registered_tray_buttons.pop(item)
