import gi
from loguru import logger
from typing import NamedTuple, Literal, Any, cast
from fabric.core.service import Service, Signal, Property
from fabric.utils.helpers import load_dbus_xml, bulk_connect, get_enum_member

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


STATUS_NOTIFIER_WATCHER_BUS_NAME = "org.kde.StatusNotifierWatcher"
STATUS_NOTIFIER_WATCHER_BUS_PATH = "/StatusNotifierWatcher"
STATUS_NOTIFIER_WATCHER_BUS_IFACE_NODE = load_dbus_xml(
    "../dbus_assets/org.kde.StatusNotifierWatcher.xml",
)

STATUS_NOTIFIER_ITEM_BUS_NAME = "org.kde.StatusNotifierItem"
STATUS_NOTIFIER_ITEM_BUS_IFACE_NODE = load_dbus_xml(
    "../dbus_assets/org.kde.StatusNotifierItem.xml"
)


class SystemTrayItemPixmap(
    NamedTuple
):  # TODO: i don't think it's good to use NamedTuple, use dataclass instead
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
            GLib.Bytes.new(data_bytearray),  # type: ignore
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
    @Signal
    def changed(self) -> None: ...
    @Signal
    def removed(self) -> None: ...

    def __init__(
        self,
        proxy: Gio.DBusProxy,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self._proxy = proxy
        self._connection = proxy.get_connection()
        self._bus_name = proxy.get_name()
        self._bus_path = proxy.get_object_path()
        self._identifier = self._bus_name + self._bus_path

        self._menu: DbusmenuGtk3.Menu | None = self.do_create_menu(
            self._proxy.get_name_owner(), self.menu_object_path
        )
        self._icon_theme: Gtk.IconTheme | None = None

        bulk_connect(
            self._proxy,
            {
                "g-signal": self.on_dbus_signal,
                "g-properties-changed": lambda *_: self.changed(),
                "notify::g-name-owner": lambda *_: (
                    self.removed() if not self._proxy.get_name_owner() else None
                ),
            },
        )

    def on_dbus_signal(self, _, __, signal_name: str, signal_args: tuple[str, ...]):
        self.do_cache_proxy_properties()
        signal_to_prop = {
            f"New{dsig}": dsig.lower()
            for dsig in [
                "Title",
                "Icon",
                "AttentionIcon",
                "OverlayIcon",
                "ToolTip",
                "Status",
            ]
        }.get(signal_name)
        if not signal_to_prop:
            return

        self.notify(signal_to_prop)
        return self.changed()

    def get_preferred_icon_pixbuf(
        self,
        size: int | None = None,
        resize_method: Literal[
            "hyper",
            "bilinear",
            "nearest",
            "tiles",
        ]
        | GdkPixbuf.InterpType = GdkPixbuf.InterpType.BILINEAR,
    ) -> GdkPixbuf.Pixbuf | None:
        icon_name = self.icon_name
        attention_icon_name = self.attention_icon_name

        icon_pixmap = self.icon_pixmap
        attention_icon_pixmap = self.attention_icon_pixmap

        if self.status == "NeedsAttention" and (
            attention_icon_name is not None or attention_icon_pixmap is not None
        ):
            preferred_icon_name = attention_icon_name
            preferred_icon_pixmap = attention_icon_pixmap
        else:
            preferred_icon_name = icon_name
            preferred_icon_pixmap = icon_pixmap

        icon_theme = self.icon_theme

        icon_theme_sizes: list | None = (
            icon_theme.get_icon_sizes(preferred_icon_name)
            if preferred_icon_name is not None
            else None
        )  # type: ignore
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
                get_enum_member(
                    GdkPixbuf.InterpType,
                    resize_method,
                    default=GdkPixbuf.InterpType.NEAREST,
                ),
            )
            if size is not None and pixbuf is not None
            else pixbuf
        )

    # remote properties
    @Property(int, "readable")
    def id(self) -> int:
        return self.do_get_proxy_property("Id")

    @Property(str, "readable")
    def identifier(self) -> str:
        return self._identifier

    @Property(str, "readable")
    def title(self) -> str:
        return self.do_get_proxy_property("Title")

    @Property(str, "readable")
    def status(self) -> str:
        return self.do_get_proxy_property("Status")

    @Property(str, "readable")
    def category(self) -> str:
        return self.do_get_proxy_property("Category")

    @Property(int, "readable")
    def window_id(self) -> int:
        return self.do_get_proxy_property("WindowId")

    @Property(str, "readable")
    def icon_theme_path(self) -> str:
        return self.do_get_proxy_property("IconThemePath")

    @Property(Gtk.IconTheme, "readable")
    def icon_theme(self) -> Gtk.IconTheme:
        if not self._icon_theme:
            self._icon_theme = Gtk.IconTheme()
            search_path = self.get_icon_theme_path()
            self._icon_theme.set_search_path([search_path]) if search_path not in (
                None,
                "",
            ) else None
        return self._icon_theme

    @Property(str, "readable")
    def icon_name(self) -> str:
        return self.do_get_proxy_property("IconName")

    @Property(SystemTrayItemPixmap, "readable")
    def icon_pixmap(self) -> SystemTrayItemPixmap:
        return self.do_extract_pixmap(self.do_get_proxy_property("IconPixmap"))

    @Property(str, "readable")
    def overlay_icon_name(self) -> str:
        return self.do_get_proxy_property("OverlayIconName")

    @Property(SystemTrayItemPixmap, "readable")
    def overlay_icon_pixmap(self) -> SystemTrayItemPixmap:
        return self.do_extract_pixmap(self.do_get_proxy_property("OverlayIconPixmap"))

    @Property(str, "readable")
    def attention_icon_name(self) -> str:
        return self.do_get_proxy_property("AttentionIconName")

    @Property(SystemTrayItemPixmap, "readable")
    def attention_icon_pixmap(self) -> SystemTrayItemPixmap:
        return self.do_extract_pixmap(self.do_get_proxy_property("AttentionIconPixmap"))

    @Property(SystemTrayItemToolTip, "readable")
    def tooltip(self) -> SystemTrayItemToolTip:
        return self.do_unpack_tooltip(self.do_get_proxy_property("ToolTip"))

    @Property(bool, "readable", default_value=False)
    def is_menu(self) -> bool:
        return self.do_get_proxy_property("ItemIsMenu")

    @Property(str, "readable")
    def menu_object_path(self) -> str:
        return self.do_get_proxy_property("Menu")

    @Property(DbusmenuGtk3.Menu, "readable")
    def menu(self) -> DbusmenuGtk3.Menu:
        if self._menu is not None:
            return self._menu
        self._menu = self.do_create_menu(
            self._proxy.get_name_owner(), self.get_menu_object_path()
        )
        return self._menu  # type: ignore

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
    def do_get_proxy_property(self, property_name: str) -> Any:
        value = self._proxy.get_cached_property(property_name)
        if value is None:
            return None
        return value.unpack()

    def do_extract_pixmap(
        self, pixmaps: list[tuple[int, int, bytearray]]
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
        self, tooltip: tuple[str, list[tuple[int, int, bytearray]], str, str] | None
    ) -> SystemTrayItemToolTip:
        if not tooltip or not len(tooltip) == 4:
            return SystemTrayItemToolTip()
        return SystemTrayItemToolTip(
            tooltip[0],
            self.do_extract_pixmap(tooltip[1]),
            tooltip[2],
            tooltip[3],
        )  # this should be fine

    def do_create_menu(self, bus_name: str, bus_path: str) -> DbusmenuGtk3.Menu | None:
        return (
            DbusmenuGtk3.Menu().new(bus_name, bus_path)
            if bus_path not in (None, "")
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
                f"[SystemTray][Item] can't update properties for item with identifier {self._identifier} ({e})"
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
        return self.changed()


class SystemTray(Service):
    @Signal
    def changed(self) -> None: ...
    @Signal
    def item_added(self, item_identifier: str) -> None: ...
    @Signal
    def item_removed(self, item_identifier: str) -> None: ...

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._items: dict[str, SystemTrayItem] = {}
        self._connection: Gio.DBusConnection | None = None

        # all aboard...
        self.do_register()

    @Property(dict[str, SystemTrayItem], "readable")
    def items(self) -> dict[str, SystemTrayItem]:
        return self._items

    def add_item(self, item: SystemTrayItem) -> None:
        self._items[item._identifier] = item
        self.do_notify_registered_item(item._identifier)
        return

    def remove_item(self, item: SystemTrayItem) -> None:
        try:
            self._items.pop(item._identifier)
            self.do_notify_unregistered_item(item._identifier)
        except:
            logger.warning(
                f"[SystemTray] can't remove tray item with identifier {item._identifier}"
            )
        return

    def do_register(self) -> int:  # the bus id
        return Gio.bus_own_name(
            Gio.BusType.SESSION,
            STATUS_NOTIFIER_WATCHER_BUS_NAME,
            Gio.BusNameOwnerFlags.NONE,
            self.on_bus_acquired,
            None,
            lambda *_: logger.warning(
                "[SystemTray] can't own the DBus name, another bar is probably running"
            ),
        )

    def on_bus_acquired(
        self, conn: Gio.DBusConnection, name: str, user_data: object = None
    ) -> None:
        self._connection = conn
        # we now own the name
        for interface in STATUS_NOTIFIER_WATCHER_BUS_IFACE_NODE.interfaces:
            cast(Gio.DBusInterface, interface)
            if interface.name == name:
                conn.register_object(
                    STATUS_NOTIFIER_WATCHER_BUS_PATH,
                    interface,
                    self.do_handle_bus_call,  # type: ignore
                )
        return

    def do_handle_bus_call(
        self,
        conn: Gio.DBusConnection,
        sender: str,
        path: str,
        interface: str,
        target: str,
        params: tuple,
        invocation: Gio.DBusMethodInvocation,
        user_data: object = None,
    ) -> None:
        match target:
            case "Get":
                prop_name = params[1] if len(params) >= 1 else None
                match prop_name:
                    case "ProtocolVersion":
                        invocation.return_value(
                            GLib.Variant("(v)", (GLib.Variant("i", 1),))
                        )
                    case "IsStatusNotifierHostRegistered":
                        invocation.return_value(
                            GLib.Variant("(v)", (GLib.Variant("b", True),))
                        )
                    case "RegisteredStatusNotifierItems":
                        invocation.return_value(
                            GLib.Variant(
                                "(v)", (GLib.Variant("as", self._items.keys()),)
                            ),
                        )
                    case _:
                        invocation.return_value(None)
            case "GetAll":
                all_properties = {
                    "ProtocolVersion": GLib.Variant("i", 1),
                    "IsStatusNotifierHostRegistered": GLib.Variant("b", True),
                    "RegisteredStatusNotifierItems": GLib.Variant(
                        "as", self._items.keys()
                    ),
                }

                invocation.return_value(GLib.Variant("(a{sv})", (all_properties,)))
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
            return

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

        item = SystemTrayItem(proxy)
        item.removed.connect(lambda *args: self.remove_item(item))

        # all aboard...
        self.add_item(item)
        return

    def do_emit_bus_signal(self, signal_name: str, params: GLib.Variant) -> None:
        self._connection.emit_signal(
            None,
            STATUS_NOTIFIER_WATCHER_BUS_PATH,
            STATUS_NOTIFIER_WATCHER_BUS_NAME,
            signal_name,
            params,
        ) if self._connection is not None else None
        return

    def do_notify_registered_item(self, identifier: str) -> None:
        self.do_emit_bus_signal(
            "StatusNotifierItemRegistered", GLib.Variant("(s)", (identifier,))
        )
        self.item_added(identifier)
        self.changed()
        return

    def do_notify_unregistered_item(self, identifier: str) -> None:
        self.changed()
        self.item_removed(identifier)
        self.do_emit_bus_signal(
            "StatusNotifierItemUnregistered",
            GLib.Variant("(s)", (identifier,)),
        )
        return
