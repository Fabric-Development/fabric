import gi
import base64
from enum import Enum
from loguru import logger
from dataclasses import dataclass
from typing import cast, Literal, TypedDict, Any
from fabric.core.service import Service, Signal, Property
from fabric.utils.helpers import load_dbus_xml, get_enum_member

gi.require_version("Gtk", "3.0")
from gi.repository import Gio, GLib, GdkPixbuf


NOTIFICATIONS_BUS_NAME = "org.freedesktop.Notifications"
NOTIFICATIONS_BUS_PATH = "/org/freedesktop/Notifications"
NOTIFICATIONS_BUS_IFACE_NODE = load_dbus_xml(
    "../dbus_assets/org.freedesktop.Notifications.xml",
)


class NotificationCloseReason(Enum):
    """A reason for which a notification was closed"""

    EXPIRED = 1
    DISMISSED_BY_USER = 2
    CLOSED_BY_APPLICATION = 3
    UNKNOWN = 4


class NotificationImagePixmap:
    """A class for storing image data associated with a notification"""

    @classmethod
    def deserialize(
        cls, data: tuple[int, int, int, bool, int, int, str]
    ) -> "NotificationImagePixmap":
        """Load image data from a serialized data tuple (using the `serialize` method) and return the newly created Pixmap object

        :param data: the tuple which is holding the image's data
        :type data: tuple[int, int, int, bool, int, int, str]
        :return: the newly loaded image pixmap
        :rtype: NotificationImagePixmap
        """
        self = cls.__new__(cls)

        (
            self.width,
            self.height,
            self.rowstride,
            self.has_alpha,
            self.bits_per_sample,
            self.channels,
            pixmap_data,
        ) = data

        # if this doesn't work, please report.
        loader = GdkPixbuf.PixbufLoader.new_with_type("png")
        decoded_data = base64.b64decode(pixmap_data)
        bytes_data = GLib.Bytes.new(decoded_data)
        loader.write_bytes(bytes_data)  # type: ignore
        loader.close()

        self._pixbuf = loader.get_pixbuf()  # type: ignore
        self.byte_array = None

        return self

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
        """Load a `Pixbuf` variant of this pixmap

        :return: the newly created pixbuf in which it has the contents of this pixmap
        :rtype: GdkPixbuf.Pixbuf
        """
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

    def serialize(self) -> tuple[int, int, int, bool, int, int, str]:
        """Serialize this pixmap image into a tuple for ease of carrying and saving

        :return: the serialized pixmap image data
        :rtype: tuple[int, int, int, bool, int, int, str]
        """
        return (
            self.width,
            self.height,
            self.rowstride,
            self.has_alpha,
            self.bits_per_sample,
            self.channels,
            base64.b64encode(
                cast(bytes, self.as_pixbuf().save_to_bufferv("png", [], [])[1])
            ).decode(),
        )


@dataclass
class NotificationAction:
    """A notification action that can be invoked"""

    identifier: str
    label: str

    parent: "Notification"

    def invoke(self):
        "Invoke this action"
        return self.parent.invoke_action(self.identifier)


NotificationSerializedData = TypedDict(
    "NotificationSerializedData",
    {
        "id": int,
        "replaces-id": int,
        "app-name": str,
        "app-icon": str,
        "summary": str,
        "body": str,
        "timeout": int,
        "urgency": int,
        "actions": list[tuple[str, str]],
        "image-file": str | None,
        "image-pixmap": tuple[int, int, int, bool, int, int, str] | None,
    },
)


class Notification(Service):
    """The notification class holds all the data of a specific notification (such as actions, images and sender's info)"""

    @Signal
    def closed(self, reason: object) -> None: ...

    @Signal
    def action_invoked(self, action: str) -> None: ...

    @Property(str, "readable")
    def app_name(self) -> str:
        """The display name of the application sent this notification

        :return: sender's display name
        :rtype: str
        """
        return self._app_name

    @Property(str, "readable")
    def app_icon(self) -> str:
        """An optional application icon name

        :return: sender's named icon (or None)
        :rtype: str
        """
        return self._app_icon

    @Property(str, "readable")
    def summary(self) -> str:
        return self._summary

    @Property(str, "readable")
    def body(self) -> str:
        """A multi-line body of text given by the sender (might contain markup)

        :return: this notification's body text
        :rtype: str
        """
        return self._body

    @Property(int, "readable")
    def id(self) -> int:
        """The uniuqe identifier of this notification

        :return: this notification's id
        :rtype: int
        """
        return self._id

    @Property(int, "readable")
    def replaces_id(self) -> int:
        """An optional ID of an existing notification that this notification is intended to replace

        :return: the id of the targeted notification (or None)
        :rtype: int
        """
        return self._replaces_id

    @Property(int, "readable")
    def timeout(self) -> int:
        """
        Expiration timeout (in milliseconds) since the display of the notification
        at which the notification should automatically get closed

        :return: timeout in milliseconds, -1 means whatever the user decides, 0 means the notification is supposed to never get closed
        :rtype: int
        """
        return self._timeout

    @Property(int, "readable")
    def urgency(self) -> int:
        """Urgency level of this notification

        :return: the urgency level as an integer, 0 for low, 1 for normal, 2 for critical
        :rtype: int
        """
        return self._urgency

    @Property(list[NotificationAction], "readable")
    def actions(self) -> list[NotificationAction]:
        """A list of all the action this notification has

        :return: a list of notification actions
        :rtype: list[NotificationAction]
        """
        return self._actions

    @Property(NotificationImagePixmap, "readable")
    def image_pixmap(self) -> NotificationImagePixmap:
        """Raw image data supplied by the sender (if any)

        :return: raw image data stored in a pixmap object
        :rtype: NotificationImagePixmap
        """
        return self._image_pixmap  # type: ignore

    @Property(str, "readable")
    def image_file(self) -> str:
        """The image file path provided by the sender for this notification (if any)

        :return: the image file path
        :rtype: str
        """
        return self._image_file  # type: ignore

    @Property(GdkPixbuf.Pixbuf, "readable")
    def image_pixbuf(self) -> GdkPixbuf.Pixbuf:
        """A `Pixbuf` loaded from either `image-pixmap` or the `image-file` property

        :return: the newly loaded image pixbuf
        :rtype: GdkPixbuf.Pixbuf
        """
        if self.image_pixmap:
            return self.image_pixmap.as_pixbuf()
        if self.image_file:
            return GdkPixbuf.Pixbuf.new_from_file(self.image_file)
        return None  # type: ignore

    @classmethod
    def deserialize(cls, data: NotificationSerializedData, **kwargs) -> "Notification":
        """Deserialize a given serialized notification data into a newly created notification object

        :param data: the serialized data to consume and covert to an object
        :type data: NotificationSerializedData
        :return: the newly created notification object
        :rtype: Notification
        """
        self = cls.__new__(cls)
        Service.__init__(self, **kwargs)

        self._id = data["id"]
        self._app_name = data["app-name"]
        self._replaces_id = data["replaces-id"]
        self._app_icon = data["app-icon"]

        self._summary = data["summary"]
        self._body = data["body"]

        self._timeout = data["timeout"]
        self._urgency = data["urgency"]

        self._actions = [
            NotificationAction(action[0], action[1], self) for action in data["actions"]
        ]

        self._image_file = data["image-file"]
        self._image_pixmap = (
            NotificationImagePixmap.deserialize(data["image-pixmap"])
            if data["image-pixmap"]
            else None
        )

        return self

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

        self._urgency: int = self.do_get_hint_entry("urgency") or 1  # type: ignore

        self._image_file: str | None = self.do_get_hint_entry(
            "image-path"
        ) or self.do_get_hint_entry("image_path")  # type: ignore

        self._image_pixmap: NotificationImagePixmap | None = None
        if raw_image_data := (
            self.do_get_hint_entry("image-data", False)
            or self.do_get_hint_entry("icon_data", False)
        ):
            self._image_pixmap = NotificationImagePixmap(raw_image_data)

    def do_get_hint_entry(
        self, entry_key: str, unpack: bool = True
    ) -> GLib.Variant | Any | None:
        variant = self._hints.lookup_value(entry_key)
        if not unpack or not variant:
            return variant
        return variant.unpack()  # type: ignore

    def serialize(self) -> NotificationSerializedData:
        """Serialize this notification into a dictionary that can easily get converted into JSON

        :return: the serialized notification data (dict)
        :rtype: NotificationSerializedData
        """
        return {
            "id": self._id,
            "replaces-id": self._replaces_id,
            "app-name": self._app_name,
            "app-icon": self._app_icon,
            "summary": self._summary,
            "body": self._body,
            "timeout": self._timeout,
            "urgency": self._urgency,
            "actions": [(action.identifier, action.label) for action in self._actions],
            "image-file": self._image_file,
            "image-pixmap": self._image_pixmap.serialize()
            if self._image_pixmap
            else None,
        }

    def invoke_action(self, action: str):
        """Invoke an action via its name"""
        return self.action_invoked(action)

    def close(
        self,
        reason: Literal[
            "expired", "dismissed-by-user", "closed-by-application", "unknown"
        ]
        | NotificationCloseReason = NotificationCloseReason.DISMISSED_BY_USER,
    ):
        """Close this notification and notify the sender with a reason

        :param reason: the reason behind the close of this notification, defaults to NotificationCloseReason.DISMISSED_BY_USER
        :type reason: Literal["expired", "dismissed-by-user", "closed-by-application", "unknown"] | NotificationCloseReason, optional
        """
        return self.closed(get_enum_member(NotificationCloseReason, reason))


class Notifications(Service):
    """A server for watching in-coming notifications from running applications, in order for it to work, other notification daemons must be NOT running on the system"""

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
        """A list of all the notifications received by this server

        :return: the list of notifications
        :rtype: dict[int, Notification]
        """
        return self._notifications

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._notifications: dict[int, Notification] = {}
        self._connection: Gio.DBusConnection | None = None

        self._counter = 0

        # all aboard...
        self.do_register()

    def do_register(self) -> int:  # the bus id
        return Gio.bus_own_name(
            Gio.BusType.SESSION,
            NOTIFICATIONS_BUS_NAME,
            Gio.BusNameOwnerFlags.NONE,
            self.on_bus_acquired,
            None,
            lambda *_: logger.warning(
                "[Notifications] couldn't own the DBus name, another notifications daemon is probably running."
            ),
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
                    on_closed=self.do_handle_notification_closed,
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

    def new_notification_id(self) -> int:
        """Get the next notification id and increase the internal counter

        :return: the next id
        :rtype: int
        """
        self._counter += 1
        return self._counter

    def do_handle_notification_action_invoke(
        self, notification: Notification, action: str
    ):
        # a pointer to a function is better than a new lambda on every notification
        return self.invoke_notification_action(notification.id, action)

    def do_handle_notification_closed(
        self, notification: Notification, reason: NotificationCloseReason
    ):
        return self.close_notification(notification.id, reason)

    def get_notification_from_id(self, notification_id: int) -> Notification | None:
        """Lookup a notification via its identifier

        :param notification_id: the notification's id (gotten from the `notification-added` signal)
        :type notification_id: int
        :return: the desired notification object (if found)
        :rtype: Notification | None
        """
        return self._notifications.get(notification_id)

    def invoke_notification_action(self, notification_id: int, action: str):
        """Invoke a named action on a notification

        :param notification_id: the notification id of in which the action should be triggered
        :type notification_id: int
        :param action: the name of the action
        :type action: str
        """
        return self.do_emit_bus_signal(
            "ActionInvoked", GLib.Variant("(us)", (notification_id, action))
        )

    def remove_notification(self, notification_id: int):
        """Remove a notification (without closing it) from the server

        :param notification_id: the id of the notification
        :type notification_id: int
        """
        return self.notification_removed(notification_id)

    def close_notification(
        self,
        notification_id: int,
        reason: NotificationCloseReason = NotificationCloseReason.DISMISSED_BY_USER,
    ):
        """Close a notification and remove it from the server

        .. note::
            Consider using `Notification.close` instead of this, this method is intended for internal usage and it is a subject to change.

        :param notification_id: the id of the notification
        :type notification_id: int
        :param reason: the reason behind this notification begin closed, defaults to NotificationCloseReason.DISMISSED_BY_USER
        :type reason: NotificationCloseReason, optional
        """
        return self.notification_closed(notification_id, reason)

    def serialize(self) -> list[NotificationSerializedData]:
        """Similar to `Notification.serialize` but it serializes all the notifications in the server instead

        :return: a list with all the serialized notifications in this server
        :rtype: list[NotificationSerializedData]
        """
        return [notif.serialize() for notif in self._notifications.values()]

    def deserialize(self, data: list[NotificationSerializedData]):
        """Load a list of serialized notifications data

        :param data: the list with serialized notifications
        :type data: list[NotificationSerializedData]
        """
        for notif_data in data:
            self._notifications[notif_data["id"]] = Notification.deserialize(
                data=notif_data,
                on_closed=self.do_handle_notification_closed,
                on_action_invoked=self.do_handle_notification_action_invoke,
            )
            self.notification_added(notif_data["id"])

        # just to make sure we don't break newcoming notifications
        # yet this doesn't fix "overwritten" notifications in the above loop
        # all "overwritten" notifications are going to meet the VOID one day or another
        # so this method _shall_ be used once the class is initialized
        # TODO: a fix for this might be by randomizing the notification id
        self._counter += max(self._notifications.keys() or (1,))
        return
