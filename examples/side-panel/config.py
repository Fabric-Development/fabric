"""side panel example, contains info about the system"""

import os
import time
import psutil
from loguru import logger
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.overlay import Overlay
from fabric.widgets.datetime import DateTime
from fabric.widgets.circularprogressbar import CircularProgressBar
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.utils import invoke_repeater, get_relative_path


def get_profile_picture_path() -> str | None:
    path = os.path.expanduser("~/Pictures/Other/face.jpg")
    if not os.path.exists(path):
        path = os.path.expanduser("~/.face")
    if not os.path.exists(path):
        logger.warning(
            "can't fetch a user profile picture, add a profile picture image at ~/.face or at ~/Pictures/Other/profile.jpg"
        )
        path = None
    return path


class SidePanel(Window):
    @staticmethod
    def bake_progress_bar(name: str = "progress-bar", size: int = 64, **kwargs):
        return CircularProgressBar(
            name=name, min_value=0, max_value=100, size=size, **kwargs
        )

    @staticmethod
    def bake_progress_icon(**kwargs):
        return Label(**kwargs).build().add_style_class("progress-icon").unwrap()

    def __init__(self, **kwargs):
        super().__init__(
            layer="overlay",
            title="fabric-overlay",
            anchor="top right",
            margin="10px 10px 10px 0px",
            exclusivity="none",
            visible=False,
            all_visible=False,
            **kwargs,
        )

        self.profile_pic = Box(
            name="profile-pic",
            style=f"background-image: url(\"file://{get_profile_picture_path() or ''}\")",
        )
        self.uptime_label = Label(label=f"{self.get_current_uptime()}")

        self.header = Box(
            spacing=14,
            name="header",
            orientation="h",
            children=[
                self.profile_pic,
                Box(
                    orientation="v",
                    children=[
                        DateTime(
                            name="date-time",
                            style="margin-top: 4px; min-width: 180px;",
                        ),
                        self.uptime_label,
                    ],
                ),
            ],
        )

        self.greeter_label = Label(
            label=f"Good {'Morning' if time.localtime().tm_hour < 12 else 'Afternoon'}, {os.getlogin().title()}!",
            style="font-size: 20px;",
        )

        self.cpu_progress = self.bake_progress_bar()
        self.ram_progress = self.bake_progress_bar()
        self.bat_circular = self.bake_progress_bar().build().set_value(42).unwrap()

        self.progress_container = Box(
            name="progress-bar-container",
            spacing=12,
            children=[
                Box(
                    children=[
                        Overlay(
                            child=self.cpu_progress,
                            overlays=[
                                self.bake_progress_icon(
                                    label="",
                                    style="margin-right: 8px; text-shadow: 0 0 10px #fff, 0 0 10px #fff, 0 0 10px #fff;",
                                )
                            ],
                        ),
                    ],
                ),
                Box(name="progress-bar-sep"),
                Box(
                    children=[
                        Overlay(
                            child=self.ram_progress,
                            overlays=[
                                self.bake_progress_icon(
                                    label="󰘚",
                                    style="margin-right: 4px; text-shadow: 0 0 10px #fff;",
                                )
                            ],
                        )
                    ]
                ),
                Box(name="progress-bar-sep"),
                Box(
                    children=[
                        Overlay(
                            child=self.bat_circular,
                            overlays=[
                                self.bake_progress_icon(
                                    label="󱊣",
                                    style="margin-right: 0px; text-shadow: 0 0 10px #fff, 0 0 18px #fff;",
                                )
                            ],
                        ),
                    ],
                ),
            ],
        )

        self.update_status()
        invoke_repeater(
            15 * 60 * 1000,  # every 15min
            lambda: (self.uptime_label.set_label(self.get_current_uptime()), True)[1],
        )
        invoke_repeater(1000, self.update_status)

        self.add(
            Box(
                name="window-inner",
                orientation="v",
                spacing=24,
                children=[self.header, self.greeter_label, self.progress_container],
            ),
        )
        self.show_all()

    def update_status(self):
        self.cpu_progress.value = psutil.cpu_percent()
        self.ram_progress.value = psutil.virtual_memory().percent
        if not (bat_sen := psutil.sensors_battery()):
            self.bat_circular.value = 42
        else:
            self.bat_circular.value = bat_sen.percent

        return True

    def get_current_uptime(self):
        uptime = time.time() - psutil.boot_time()
        uptime_days, remainder = divmod(uptime, 86400)
        uptime_hours, remainder = divmod(remainder, 3600)
        # uptime_minutes, _ = divmod(remainder, 60)
        return f"{int(uptime_days)} {'days' if uptime_days > 1 else 'day'}, {int(uptime_hours)} {'hours' if uptime_hours > 1 else 'hour'}"


if __name__ == "__main__":
    side_panel = SidePanel()
    app = Application("side-panel", side_panel)
    app.set_stylesheet_from_file(get_relative_path("./style.css"))

    app.run()
