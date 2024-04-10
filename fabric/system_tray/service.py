import gi
from loguru import logger
from typing import NamedTuple
from fabric.service import *
from fabric.utils import (
    get_ixml,
    bulk_connect,
)

gi.require_version("Gtk", "3.0")
gi.require_version("DbusmenuGtk3", "0.4")
from gi.repository import (
    Gtk,
    Gio,
    Gdk,
    GdkPixbuf,
    DbusmenuGtk3,
    GLib,
)


(
    STATUS_NOTIFIER_WATCHER_BUS_NAME,
    STATUS_NOTIFIER_WATCHER_BUS_IFACE_NODE,
    STATUS_NOTIFIER_WATCHER_BUS_PATH,
) = (
    *get_ixml(
        "../dbus_assets/org.kde.StatusNotifierWatcher.xml",
        "org.kde.StatusNotifierWatcher",
    ),
    "/StatusNotifierWatcher",
)
(
    STATUS_NOTIFIER_ITEM_BUS_NAME,
    STATUS_NOTIFIER_ITEM_BUS_IFACE_NODE,
    STATUS_NOTIFIER_IFACE_BUS_PATH,
) = (
    *get_ixml(
        "../dbus_assets/org.kde.StatusNotifierItem.xml", "org.kde.StatusNotifierItem"
    ),
    None,
)


class SystemTrayItemPixmap(
    NamedTuple
):  # FIXME: i don't think it's good to use NamedTuple...
    width: int | None = None
    "icon width size in pixels"
    height: int | None = None
    "icon height size in pixels"
    data: bytearray | None = None
    "the actual data representing this icon"

    def as_pixbuf(
        self,
        size: int | None = None,
        resize_method: Literal[
            "hyper",
            "bilinear",
            "nearest",
            "tiles",
        ] = "nearest",
    ) -> GdkPixbuf.Pixbuf | None:
        if not (self.width and self.height and self.data):
            return None

        data_bytearray = bytearray(self.data)

        for i in range(0, 4 * self.width * self.height, 4):
            alpha = data_bytearray[i]
            data_bytearray[i] = data_bytearray[i + 1]
            data_bytearray[i + 1] = data_bytearray[i + 2]
            data_bytearray[i + 2] = data_bytearray[i + 3]
            data_bytearray[i + 3] = alpha
        pixbuf = GdkPixbuf.Pixbuf.new_from_bytes(
            GLib.Bytes.new(data_bytearray),
            GdkPixbuf.Colorspace.RGB,
            True,
            8,
            self.width,
            self.height,
            self.width * 4,
        )
        return (
            pixbuf.scale_simple(
                size,
                size,
                {
                    "hyper": GdkPixbuf.InterpType.HYPER,
                    "bilinear": GdkPixbuf.InterpType.BILINEAR,
                    "nearest": GdkPixbuf.InterpType.NEAREST,
                    "tiles": GdkPixbuf.InterpType.TILES,
                }.get(resize_method.lower(), GdkPixbuf.InterpType.NEAREST),
            )
            if size is not None and pixbuf is not None
            else pixbuf
        )


class SystemTrayItemToolTip(NamedTuple):
    icon_name: str | None = None
    "free-desktop compliant name for an icon"
    icon_pixmap: SystemTrayItemPixmap | None = None
    "icon data as a pixmap"
    title: str | None = None
    "title for this tooltip"
    description: str | None = None
    "descriptive text for this tooltip. It can contain also a subset of the HTML markup language"


class SystemTrayItem(Service):
    __gsignals__ = SignalContainer(
        Signal("changed", "run-first", None, ()),
        Signal("removed", "run-first", None, ()),
        Signal("title-changed", "run-first", None, ()),
        Signal("icon-changed", "run-first", None, ()),
        Signal("attention-icon-changed", "run-first", None, ()),
        Signal("overlay-icon-changed", "run-first", None, ()),
        Signal("tooltip-changed", "run-first", None, ()),
        Signal("status-changed", "run-first", None, (str,)),
    )

    def __init__(
        self,
        bus_name: str,
        bus_path: str,
        proxy: Gio.DBusProxy,
        connection: Gio.DBusConnection,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.bus_name = bus_name
        self.bus_path = bus_path
        self.identifier = bus_name + bus_path
        self._proxy = proxy
        self._connection = connection
        self._menu: DbusmenuGtk3.Menu | None = self.do_create_menu(
            self._proxy.get_name_owner(), self.get_menu_object_path()
        )
        self._icon_theme: Gtk.IconTheme | None = None
        bulk_connect(
            self._proxy,
            {
                "g-signal": lambda _, __, signal_name, args: [
                    self.do_cache_proxy_properties(),
                    self.emit(
                        {
                            f"New{x}": f"{y}-changed"
                            for x, y in zip(
                                [
                                    "Title",
                                    "Icon",
                                    "AttentionIcon",
                                    "OverlayIcon",
                                    "ToolTip",
                                    "Status",
                                ],
                                [
                                    "title",
                                    "icon",
                                    "attention-icon",
                                    "overlay-icon",
                                    "tooltip",
                                    "status",
                                ],
                            )
                        }.get(signal_name),
                        *args,
                    ),
                ],
                "g-properties-changed": lambda *args: self.emit("changed"),
                "notify::g-name-owner": lambda *args: self.emit("removed")
                if not self._proxy.get_name_owner()
                else None,
            },
        )

    def get_preferred_icon_pixbuf(
        self,
        size: int | None = None,
        resize_method: Literal[
            "hyper",
            "bilinear",
            "nearest",
            "tiles",
        ] = "nearest",
    ) -> GdkPixbuf.Pixbuf | None:
        icon_name = self.get_icon_name()
        attention_icon_name = self.get_attention_icon_name()

        icon_pixmap = self.get_icon_pixmap()
        attention_icon_pixmap = self.get_attention_icon_pixmap()

        if self.get_status() == "NeedsAttention" and (
            attention_icon_name is not None or attention_icon_pixmap is not None
        ):
            preferred_icon_name = attention_icon_name
            preferred_icon_pixmap = attention_icon_pixmap
        else:
            preferred_icon_name = icon_name
            preferred_icon_pixmap = icon_pixmap

        icon_theme = self.get_icon_theme()

        icon_theme_sizes: list | None = (
            icon_theme.get_icon_sizes(preferred_icon_name)
            if preferred_icon_name is not None
            else None
        )
        icon_theme_sizes = [] if not icon_theme_sizes else icon_theme_sizes
        icon_theme_sizes.append(size if size is not None else 24)

        pixbuf = (
            preferred_icon_pixmap.as_pixbuf()
            if preferred_icon_pixmap is not None
            else icon_theme.load_icon(
                preferred_icon_name,
                max(icon_theme_sizes),
                Gtk.IconLookupFlags.FORCE_SIZE,
            )
            if preferred_icon_name is not None
            else None
        )
        return (
            pixbuf.scale_simple(
                size,
                size,
                {
                    "hyper": GdkPixbuf.InterpType.HYPER,
                    "bilinear": GdkPixbuf.InterpType.BILINEAR,
                    "nearest": GdkPixbuf.InterpType.NEAREST,
                    "tiles": GdkPixbuf.InterpType.TILES,
                }.get(resize_method.lower(), GdkPixbuf.InterpType.NEAREST),
            )
            if size is not None and pixbuf is not None
            else pixbuf
        )

    # remote properties
    def get_id(self) -> int | None:
        return self.do_get_proxy_property("Id")

    def get_title(self) -> str | None:
        return self.do_get_proxy_property("Title")

    def get_status(self) -> str | None:
        return self.do_get_proxy_property("Status")

    def get_category(self) -> str | None:
        return self.do_get_proxy_property("Category")

    def get_window_id(self) -> int | None:
        return self.do_get_proxy_property("WindowId")

    def get_icon_theme_path(self) -> str | None:
        return self.do_get_proxy_property("IconThemePath")

    def get_icon_theme(self) -> Gtk.IconTheme | None:
        if not self._icon_theme:
            self._icon_theme = Gtk.IconTheme()
            search_path = self.get_icon_theme_path()
            self._icon_theme.set_search_path([search_path]) if not search_path in (
                None,
                "",
            ) else None
        return self._icon_theme

    def get_icon_name(self) -> str | None:
        return self.do_get_proxy_property("IconName")

    def get_icon_pixmap(self) -> SystemTrayItemPixmap | None:
        return self.do_extract_pixmap(self.do_get_proxy_property("IconPixmap"))

    def get_overlay_icon_name(self) -> str | None:
        return self.do_get_proxy_property("OverlayIconName")

    def get_overlay_icon_pixmap(self) -> SystemTrayItemPixmap | None:
        return self.do_extract_pixmap(self.do_get_proxy_property("OverlayIconPixmap"))

    def get_attention_icon_name(self) -> str | None:
        return self.do_get_proxy_property("AttentionIconName")

    def get_attention_icon_pixmap(self) -> SystemTrayItemPixmap | None:
        return self.do_extract_pixmap(self.do_get_proxy_property("AttentionIconPixmap"))

    def get_tooltip(self) -> SystemTrayItemToolTip:
        return self.do_unpack_tooltip(self.do_get_proxy_property("ToolTip"))

    def get_is_menu(self) -> bool | None:
        return self.do_get_proxy_property("ItemIsMenu")

    def get_menu_object_path(self) -> str | None:
        return self.do_get_proxy_property("Menu")

    def get_menu(self) -> DbusmenuGtk3.Menu | None:
        if self._menu is not None:
            return self._menu
        self._menu = self.do_create_menu(
            self._proxy.get_name_owner(), self.get_menu_object_path()
        )
        return self._menu

    # remote methods
    def context_menu(self, x: int, y: int) -> None:
        """to open a server-side context menu"""
        return self._proxy.ContextMenu("(ii)", x, y)

    def activate(self, x: int, y: int) -> None:
        return self._proxy.Activate("(ii)", x, y)

    def secondary_activate(self, x: int, y: int) -> None:
        return self._proxy.SecondaryActivate("(ii)", x, y)

    def invoke_menu_for_event(self, event: Gdk.Event) -> None:
        menu = self.get_menu()
        return (
            menu.popup_at_pointer(event)
            if menu is not None
            else self.context_menu_for_event(event)
        )

    def scroll(
        self, delta: int, orientation: Literal["vertical", "horizontal"]
    ) -> None:
        return self._proxy.Scroll("(is)", delta, orientation)

    # event methods
    def context_menu_for_event(self, event: Gdk.EventAny) -> None:
        return self.context_menu(*event.get_root_coords())

    def activate_for_event(self, event: Gdk.EventAny) -> None:
        return self.activate(*event.get_root_coords())

    def secondary_activate_for_event(self, event: Gdk.EventAny) -> None:
        return self.secondary_activate(*event.get_root_coords())

    def scroll_for_event(self, event: Gdk.EventScroll) -> None:
        direction = (
            "vertical" if event.direction == 0 or event.direction == 1 else "horizontal"
        )
        delta: int = event.delta_y if direction == "vertical" else event.delta_x
        return self.scroll(delta, direction)

    # privates
    def do_get_proxy_property(self, property_name: str) -> Any | None:
        value = self._proxy.get_cached_property(property_name)
        if value is None:
            return None
        return value.unpack()

    def do_extract_pixmap(
        self, pixmaps: list[tuple[int, int, bytearray]] | None
    ) -> SystemTrayItemPixmap | None:
        # only use the biggest icon and ignore all others

        if not pixmaps:  # to handle both None and []
            return None
        sorted_pixmap = sorted(pixmaps, key=lambda x: x[0])
        return (
            SystemTrayItemPixmap(*sorted_pixmap[-1])
            if len(sorted_pixmap) >= 1
            else None
        )

    def do_unpack_tooltip(
        self, tooltip: list[str, list[tuple[int, int, bytearray]], str, str] | None
    ) -> SystemTrayItemToolTip | None:
        if not tooltip or not len(tooltip) == 4:
            return None
        return SystemTrayItemToolTip(
            tooltip[0],
            self.do_extract_pixmap(tooltip[1]),
            tooltip[2],
            tooltip[3],
        )  # this should be fine

    def do_create_menu(self, bus_name: str, bus_path: str) -> DbusmenuGtk3.Menu | None:
        return (
            DbusmenuGtk3.Menu().new(bus_name, bus_path)
            if not bus_path in (None, "")
            else None
        )

    def do_cache_proxy_properties(self) -> None:
        return self._connection.call(  # "async"
            self._proxy.get_name(),
            self._proxy.get_object_path(),
            "org.freedesktop.DBus.Properties",
            "GetAll",
            GLib.Variant("(s)", [self._proxy.get_interface_name()]),
            GLib.VariantType("(a{sv})"),
            Gio.DBusCallFlags.NONE,
            -1,  # no timeout
            None,
            self.do_cache_proxy_properties_finish,
        )

    def do_cache_proxy_properties_finish(self, _, result: Gio.AsyncResult) -> None:
        try:
            props_var: GLib.Variant = self._connection.call_finish(result)
            if not props_var:
                raise RuntimeError("can't get the properties variant")
        except Exception as e:
            return logger.warning(
                f"[SystemTray][Item] can't update properties for item with identifier {self.identifier} ({e})"
            )

        def unpack_properties(variant: GLib.Variant) -> dict:
            res = {}
            variant = variant.get_child_value(0)
            if variant.get_type_string().startswith("a{"):
                for i in range(variant.n_children()):
                    v = variant.get_child_value(i)
                    res[v.get_child_value(0).unpack()] = v.get_child_value(1)
            return res

        for prop_name, prop_value in unpack_properties(props_var).items():
            prop_name: str
            prop_value: GLib.Variant
            self._proxy.set_cached_property(prop_name, prop_value.get_variant())
        return self.emit("changed")


class SystemTray(Service):
    __gsignals__ = SignalContainer(
        Signal("changed", "run-first", None, ()),
        Signal("item-added", "run-first", None, (str,)),
        Signal("item-removed", "run-first", None, (str,)),
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._items: dict[str, SystemTrayItem] = {}
        self._connection: Gio.DBusConnection | None = None
        self.do_register()

    def get_items(
        self,
    ) -> dict[str, SystemTrayItem]:
        return self._items

    def add_item(self, item: SystemTrayItem) -> None:
        self._items[item.identifier] = item
        self.do_notify_registered_item(item.identifier)
        return

    def remove_item(self, item: SystemTrayItem) -> None:
        try:
            self._items.pop(item.identifier)
            self.do_notify_unregistered_item(item.identifier)
        except:
            logger.warning(
                f"[SystemTray] can't remove tray item with identifier {item.identifier}"
            )
        return

    def do_register(self) -> int:  # the bus id
        return Gio.bus_own_name(
            Gio.BusType.SESSION,
            STATUS_NOTIFIER_WATCHER_BUS_NAME,
            Gio.BusNameOwnerFlags.NONE,
            self.on_bus_acquired,
            None,
            lambda *args: logger.warning(
                "[SystemTray] can't own the DBus name, another bar is probably running"
            ),
        )

    def on_bus_acquired(
        self, conn: Gio.DBusConnection, name: str, user_data: object = None
    ) -> None:
        self._connection = conn
        # we now own the name
        for interface in STATUS_NOTIFIER_WATCHER_BUS_IFACE_NODE.interfaces:
            interface: Gio.DBusInterface
            if interface.name == name:
                conn.register_object(
                    STATUS_NOTIFIER_WATCHER_BUS_PATH, interface, self.do_handle_bus_call
                )
        return

    def do_handle_bus_call(
        self,
        conn: Gio.DBusConnection,
        sender: str,
        path: str,
        interface: str,
        target: str,
        params: GLib.Variant | tuple,
        invocation: Gio.DBusMethodInvocation,
        user_data: object = None,
    ) -> None:
        props = {
            "ProtocolVersion": GLib.Variant("i", 1),
            "IsStatusNotifierHostRegistered": GLib.Variant("b", True),
            "RegisteredStatusNotifierItems": GLib.Variant("as", self._items.keys()),
        }

        match target:
            case "Get":
                prop_name = params[1] if len(params) >= 1 else None
                if not prop_name in props or not prop_name:
                    invocation.return_value(None)
                    conn.flush()
                    return
                invocation.return_value(GLib.Variant("(v)", [props.get(prop_name)]))
            case "GetAll":
                invocation.return_value(GLib.Variant("(a{sv})", [props]))
            case "RegisterStatusNotifierItem":
                self.do_create_item(sender, params[0] if len(params) >= 1 else "")
                invocation.return_value(None)
        return conn.flush()

    def do_create_item(self, bus_name: str, bus_path: str) -> None:
        # phase 1, validate
        if (
            bus_name is None
            or bus_path is None
            or not isinstance(bus_name, str)
            or not isinstance(bus_path, str)
            or self.get_items().get(bus_name + bus_path) is not None
        ):
            return  # FIXME: logging
        if not bus_path.startswith("/"):
            bus_path = "/StatusNotifierItem"
        return self.do_acquire_item_proxy(bus_name, bus_path)

    def do_acquire_item_proxy(self, bus_name: str, bus_path: str) -> None:
        # phase 2, get the proxy

        # some remote objects has a huge props size
        # so loading them in a async way is an ideal
        return Gio.DBusProxy.new_for_bus(
            Gio.BusType.SESSION,
            Gio.DBusProxyFlags.NONE,
            STATUS_NOTIFIER_ITEM_BUS_IFACE_NODE.interfaces[0],
            bus_name,
            bus_path,
            STATUS_NOTIFIER_ITEM_BUS_NAME,
            None,
            lambda *args: self.do_acquire_item_proxy_finish(bus_name, bus_path, *args),
            None,
        )

    def do_acquire_item_proxy_finish(
        self,
        bus_name: str,
        bus_path: str,
        proxy: Gio.DBusProxy,
        result: Gio.AsyncResult,
        *args,
    ) -> None:
        # phase 3, we might have gotten a proxy, if so create a new item
        proxy = proxy.new_for_bus_finish(result)
        if not proxy:
            return logger.warning(
                f"[SystemTray] can't acquire proxy object for tray item with identifier {bus_name + bus_path}"
            )
        connection = proxy.get_connection()
        # all aboard
        item = SystemTrayItem(bus_name, bus_path, proxy, connection)
        item.connect("removed", lambda *args: self.remove_item(item))
        return self.add_item(item)

    def do_emit_bus_signal(self, signal_name: str, variant: GLib.Variant) -> None:
        return (
            self._connection.emit_signal(
                None,
                STATUS_NOTIFIER_WATCHER_BUS_PATH,
                STATUS_NOTIFIER_WATCHER_BUS_NAME,
                signal_name,
                variant,
            )
            if self._connection is not None
            else None
        )

    def do_notify_registered_item(self, identifier: str) -> None:
        self.emit("changed")
        self.emit("item-added", identifier)
        return self.do_emit_bus_signal(
            "StatusNotifierItemRegistered", GLib.Variant("(s)", [identifier])
        )

    def do_notify_unregistered_item(self, identifier: str) -> None:
        self.emit("changed")
        self.emit("item-removed", identifier)
        return self.do_emit_bus_signal(
            "StatusNotifierItemUnregistered",
            GLib.Variant("(s)", [identifier]),
        )
