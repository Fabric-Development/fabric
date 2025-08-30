from typing import cast
from os import path

from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.image import Image
from fabric.widgets.button import Button
from fabric.widgets.wayland import WaylandWindow
from fabric.notifications import Notifications, Notification
from fabric.utils import invoke_repeater, get_relative_path

from gi.repository import GdkPixbuf, Gtk


NOTIFICATION_WIDTH = 360
NOTIFICATION_IMAGE_SIZE = 64
NOTIFICATION_TIMEOUT = 10 * 1000  # 10 seconds


class NotificationWidget(Box):
    def __init__(self, notification: Notification, **kwargs):
        super().__init__(
            size=(NOTIFICATION_WIDTH, -1),
            name="notification",
            spacing=8,
            orientation="v",
            **kwargs,
        )

        self._notification = notification

        body_container = Box(spacing=4, orientation="h")

        if image_pixbuf := self._load_notification_pixbuf(self._notification):
            body_container.add(
                Image(
                    pixbuf=image_pixbuf.scale_simple(
                        NOTIFICATION_IMAGE_SIZE,
                        NOTIFICATION_IMAGE_SIZE,
                        GdkPixbuf.InterpType.BILINEAR,
                    )
                )
            )

        body_container.add(
            Box(
                spacing=4,
                orientation="v",
                children=[
                    # a box for holding both the "summary" label and the "close" button
                    Box(
                        orientation="h",
                        children=[
                            Label(
                                label=self._notification.summary,
                                ellipsization="middle",
                            )
                            .build()
                            .add_style_class("summary")
                            .unwrap(),
                        ],
                        h_expand=True,
                        v_expand=True,
                    )
                    # add the "close" button
                    .build(
                        lambda box, _: box.pack_end(
                            Button(
                                image=Image(
                                    icon_name="close-symbolic",
                                    icon_size=18,
                                ),
                                v_align="center",
                                h_align="end",
                                on_clicked=lambda *_: self._notification.close(),
                            ),
                            False,
                            False,
                            0,
                        )
                    ),
                    Label(
                        label=self._notification.body,
                        line_wrap="word-char",
                        v_align="start",
                        h_align="start",
                    )
                    .build()
                    .add_style_class("body")
                    .unwrap(),
                ],
                h_expand=True,
                v_expand=True,
            )
        )

        self.add(body_container)

        if actions := self._notification.actions:
            self.add(
                Box(
                    spacing=4,
                    orientation="h",
                    children=[
                        Button(
                            h_expand=True,
                            v_expand=True,
                            label=action.label,
                            on_clicked=lambda *_, action=action: action.invoke(),
                        )
                        for action in actions
                    ],
                )
            )

        # destroy this widget once the notification is closed
        self._notification.connect(
            "closed",
            lambda *_: (
                parent.remove(self) if (parent := self.get_parent()) else None,  # type: ignore
                self.destroy(),
            ),
        )

        # automatically close the notification after the timeout period
        invoke_repeater(
            NOTIFICATION_TIMEOUT,
            lambda: self._notification.close("expired"),
            initial_call=False,
        )

    def _load_notification_pixbuf(self, notification: Notification) -> GdkPixbuf.Pixbuf | None:
        try:
            if getattr(notification, "image_pixbuf", None):
                return notification.image_pixbuf

            if getattr(notification, "image_data", None):
                loader = GdkPixbuf.PixbufLoader()
                loader.write(notification.image_data)
                loader.close()
                return loader.get_pixbuf()

            if getattr(notification, "image_path", None) and path.exists(notification.image_path):
                return GdkPixbuf.Pixbuf.new_from_file_at_scale(
                    notification.image_path,
                    NOTIFICATION_IMAGE_SIZE,
                    NOTIFICATION_IMAGE_SIZE,
                    True,
                )

            if getattr(notification, "app_icon", None):
                app_icon = notification.app_icon
                # Try as file path first
                if path.exists(app_icon):
                    return GdkPixbuf.Pixbuf.new_from_file_at_scale(
                        app_icon,
                        NOTIFICATION_IMAGE_SIZE,
                        NOTIFICATION_IMAGE_SIZE,
                        True,
                    )
                # Otherwise, try from icon theme
                theme = Gtk.IconTheme.get_default()
                info = theme.lookup_icon(app_icon, NOTIFICATION_IMAGE_SIZE, 0)
                if info:
                    return info.load_icon()
        except Exception as e:
            print(f"Failed to load notification icon: {e}")

        return None

if __name__ == "__main__":
    app = Application(
        "notifications",
        WaylandWindow(
            margin="8px 8px 8px 8px",
            anchor="top right",
            child=Box(
                size=2,  # so it's not ignored by the compositor
                spacing=4,
                orientation="v",
            ).build(
                lambda viewport, _: Notifications(
                    on_notification_added=lambda notifs_service, nid: viewport.add(
                        NotificationWidget(
                            cast(
                                Notification,
                                notifs_service.get_notification_from_id(nid),
                            )
                        )
                    )
                )
            ),
            visible=True,
            all_visible=True,
        ),
    )

    app.set_stylesheet_from_file(get_relative_path("./style.css"))

    app.run()
