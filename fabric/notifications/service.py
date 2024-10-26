import gi
from enum import Enum
from typing import cast
from dataclasses import dataclass
from fabric.core.service import Service, Signal, Property
from fabric.utils.helpers import load_dbus_xml

gi.require_version("Gtk", "3.0")
from gi.repository import Gio, GLib, GdkPixbuf


NOTIFICATIONS_BUS_NAME = "org.freedesktop.Notifications"
NOTIFICATIONS_BUS_PATH = "/org/freedesktop/Notifications"
NOTIFICATIONS_BUS_IFACE_NODE = load_dbus_xml(
    "../dbus_assets/org.freedesktop.Notifications.xml",
)


class NotificationCloseReason(Enum):
    EXPIRED = 1
    DISMISSED_BY_USER = 2
    CLOSED_BY_APPLICATION = 3
    UNKNOWN = 4


class NotificationImagePixmap:
    def __init__(self, raw_variant: GLib.Variant):
        # manually unpack children so we don't lock up the interpreter
        # trying to unpack hugely sized object recursively
        self.width = raw_variant.get_child_value(0).unpack()  # type: ignore
        self.height = raw_variant.get_child_value(1).unpack()  # type: ignore
        self.rowstride = raw_variant.get_child_value(2).unpack()  # type: ignore
        self.has_alpha = raw_variant.get_child_value(3).unpack()  # type: ignore
        self.bits_per_sample = raw_variant.get_child_value(4).unpack()  # type: ignore
        self.channels = raw_variant.get_child_value(5).unpack()  # type: ignore
        self.byte_array = raw_variant.get_child_value(6).get_data_as_bytes()  # type: ignore

        self._pixbuf: GdkPixbuf.Pixbuf | None = None

    def as_pixbuf(self) -> GdkPixbuf.Pixbuf:
        if self._pixbuf is not None:
            return self._pixbuf

        self._pixbuf = GdkPixbuf.Pixbuf.new_from_bytes(
            self.byte_array,
            GdkPixbuf.Colorspace.RGB,
            self.has_alpha,
            self.bits_per_sample,
            self.width,
            self.height,
            self.rowstride,
        )
        return self._pixbuf


@dataclass
class NotificationAction:
    identifier: str
    label: str

    parent: "Notification"

    def invoke(self):
        return self.parent.invoke_action(self.identifier)


class Notification(Service):
    @Signal
    def action_invoked(self, action: str) -> None: ...

    @Property(str, "readable")
    def app_name(self) -> str:
        return self._app_name

    @Property(str, "readable")
    def app_icon(self) -> str:
        return self._app_icon

    @Property(str, "readable")
    def summary(self) -> str:
        return self._summary

    @Property(str, "readable")
    def body(self) -> str:
        return self._body

    @Property(int, "readable")
    def id(self) -> int:
        return self._id

    @Property(int, "readable")
    def replaces_id(self) -> int:
        return self._replaces_id

    @Property(int, "readable")
    def timeout(self) -> int:
        return self._timeout

    @Property(list[NotificationAction], "readable")
    def actions(self) -> list[NotificationAction]:
        return self._actions

    @Property(NotificationImagePixmap, "readable")
    def image_pixmap(self) -> NotificationImagePixmap:
        return self._image_pixmap  # type: ignore

    @Property(str, "readable")
    def image_file(self) -> str:
        return self._image_file  # type: ignore

    @Property(GdkPixbuf.Pixbuf, "readable")
    def image_pixbuf(self) -> GdkPixbuf.Pixbuf:
        if self.image_pixmap:
            return self.image_pixmap.as_pixbuf()
        if self.image_file:
            return GdkPixbuf.Pixbuf.new_from_file(self.image_file)
        return None  # type: ignore

    def __init__(self, id: int, raw_variant: GLib.Variant, **kwargs):
        super().__init__(**kwargs)
        self._id: int = id

        self._app_name: str = raw_variant.get_child_value(0).unpack()  # type: ignore
        self._replaces_id: int = raw_variant.get_child_value(1).unpack()  # type: ignore
        self._app_icon: str = raw_variant.get_child_value(2).unpack()  # type: ignore
        self._summary: str = raw_variant.get_child_value(3).unpack()  # type: ignore
        self._body: str = raw_variant.get_child_value(4).unpack()  # type: ignore

        raw_actions: list[str] = raw_variant.get_child_value(5).unpack()  # type: ignore
        self._actions: list[NotificationAction] = [
            NotificationAction(raw_actions[i], raw_actions[i + 1], self)
            for i in range(0, len(raw_actions), 2)
        ]

        self._hints: GLib.Variant = raw_variant.get_child_value(6)  # type: ignore
        self._timeout: int = raw_variant.get_child_value(7).unpack()  # type: ignore

        self._image_file: str | None = (
            image_file_raw := (
                self.do_get_hint_entry("image-path")
                or self.do_get_hint_entry("image_path")
            ),
            image_file_raw.unpack() if image_file_raw is not None else None,  # type: ignore
        )[1]

        self._image_pixmap: NotificationImagePixmap | None = None
        if image_data := (
            self.do_get_hint_entry("image-data") or self.do_get_hint_entry("icon_data")
        ):
            self._image_pixmap = NotificationImagePixmap(image_data)

    def do_get_hint_entry(self, entry_key: str) -> GLib.Variant | None:
        return self._hints.lookup_value(entry_key)

    def invoke_action(self, action: str):
        return self.action_invoked(action)


class Notifications(Service):
    @Signal
    def changed(self) -> None: ...

    @Signal
    def notification_added(self, notification_id: int) -> None:
        self.notify("notifications")
        self.changed()
        return

    @Signal
    def notification_removed(self, notification_id: int) -> None:
        self._notifications.pop(notification_id, None)
        self.notify("notifications")
        self.changed()
        return

    @Signal
    def notification_closed(self, notification_id: int, reason: object) -> None:
        self.notification_removed(notification_id)
        self.do_emit_bus_signal(
            "NotificationClosed",
            GLib.Variant(
                "(uu)", (notification_id, cast(NotificationCloseReason, reason).value)
            ),
        )
        return

    @Property(dict[int, Notification], "readable")
    def notifications(self) -> dict[int, Notification]:
        return self._notifications

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._notifications: dict[int, Notification] = {}
        self._connection: Gio.DBusConnection | None = None

        self._counter = 0

        # all aboard...
        self.do_register()

    def new_notification_id(self) -> int:
        self._counter += 1
        return self._counter

    def do_register(self) -> int:  # the bus id
        return Gio.bus_own_name(
            Gio.BusType.SESSION,
            NOTIFICATIONS_BUS_NAME,
            Gio.BusNameOwnerFlags.NONE,
            self.on_bus_acquired,
            # FIXME: add logging
            print,
            print,
        )

    def on_bus_acquired(
        self, conn: Gio.DBusConnection, name: str, user_data: object = None
    ) -> None:
        self._connection = conn
        # we now own the name
        for interface in NOTIFICATIONS_BUS_IFACE_NODE.interfaces:
            cast(Gio.DBusInterface, interface)
            if interface.name == name:
                conn.register_object(
                    NOTIFICATIONS_BUS_PATH,
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
        print(target)
        match target:
            case "Get":
                prop_name = params[1] if len(params) >= 1 else None
                match prop_name:
                    case _:
                        invocation.return_value(None)
            case "GetAll":
                invocation.return_value(GLib.Variant("(a{sv})", ({},)))

            case "CloseNotification":
                notif_id = int(params[0])

                self.notification_removed(notif_id)

                invocation.return_value(None)

            case "GetCapabilities":
                invocation.return_value(
                    GLib.Variant(
                        "(as)",
                        (
                            [
                                "action-icons",
                                "actions",
                                "body",
                                "body-hyperlinks",
                                "body-images",
                                "body-markup",
                                # "icon-multi",
                                "icon-static",
                                "persistence",
                                # "sound",
                            ],
                        ),
                    )
                )

            case "GetServerInformation":
                invocation.return_value(
                    GLib.Variant(
                        "(ssss)", ("fabric", "Fabric-Development", "0.0.2", "1.2")
                    )
                )

            case "Notify":
                notif_id = self.new_notification_id()

                self._notifications[notif_id] = Notification(
                    id=notif_id,
                    raw_variant=cast(GLib.Variant, params),
                    on_action_invoked=self.do_handle_notification_action_invoke,
                )
                self.notification_added(notif_id)

                invocation.return_value(GLib.Variant("(u)", (notif_id,)))

        return conn.flush()

    def do_emit_bus_signal(self, signal_name: str, params: GLib.Variant) -> None:
        self._connection.emit_signal(
            None,
            NOTIFICATIONS_BUS_PATH,
            NOTIFICATIONS_BUS_NAME,
            signal_name,
            params,
        ) if self._connection is not None else None
        return

    def do_handle_notification_action_invoke(
        self, notification: Notification, action: str
    ):
        # a pointer to a function is better than a new lambda on every notification
        return self.invoke_notification_action(notification.id, action)

    def invoke_notification_action(self, notification_id: int, action: str):
        return self.do_emit_bus_signal(
            "ActionInvoked", GLib.Variant("(us)", (notification_id, action))
        )

    def get_notification_from_id(self, notification_id: int) -> Notification | None:
        return self._notifications.get(notification_id)
