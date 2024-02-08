"""side panel example, contains info about the system"""
import fabric
import os
import time
import psutil
from loguru import logger
from gi.repository import GLib
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.wayland import Window
from fabric.widgets.overlay import Overlay
from fabric.widgets.date_time import DateTime
from fabric.utils import (
    set_stylesheet_from_file,
    monitor_file,
    get_relative_path,
)
from fabric.widgets.circular_progress_bar import CircularProgressBar

PYWAL = False
PROFILE_PICTURE = os.path.expanduser("~/Pictures/Other/profile.jpg")


class SidePanel(Window):
    def __init__(self):
        super().__init__(
            layer="overlay",
            exclusive=True,
            anchor="top right",
            margin="10px 10px 10px 0px",
            all_visible=True,
            visible=True,
        )
        self.uptime_label = Label(
            label=f"{self.get_current_uptime()}",
            style="font-size: 18px;",
        )
        self.cpu_circular_progress_bar = CircularProgressBar(
            size=(64, 64),
            percentage=0,
            name="circular-progress-bar",
        )
        self.memory_circular_progress_bar = CircularProgressBar(
            size=(64, 64),
            percentage=0,
            name="circular-progress-bar",
        )
        self.battery_circular_progress_bar = CircularProgressBar(
            size=(64, 64),
            percentage=68,
            name="circular-progress-bar",
        )
        self.update_status()
        GLib.timeout_add_seconds(1, self.update_status)
        GLib.timeout_add_seconds(
            60 * 15,
            lambda: [self.uptime_label.set_label(self.get_current_uptime()), True][1],
        )
        self.add(
            Box(
                spacing=24,
                name="main-window",
                style="border-radius: 12px; padding: 10px;",
                orientation="v",
                children=[
                    Box(
                        spacing=15,
                        name="header",
                        orientation="h",
                        children=[
                            Box(
                                style=f"""
                                * {{
                                    background-image: url("file://{PROFILE_PICTURE}");
                                    background-position: center;
                                    background-repeat: no-repeat;
                                    background-size: cover;
                                    padding: 30px;
                                    margin: 4px;
                                    border-radius: 6px;
                                }}
                                """,
                            ),
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
                    ),
                    Label(
                        label=f"Good {'Morning' if time.localtime().tm_hour < 12 else 'Afternoon'}, {os.getlogin()}",
                        style="font-size: 20px;",
                    ),
                    Box(
                        name="circular-progress-bar-container",
                        spacing=12,
                        children=[
                            Box(
                                children=[
                                    Overlay(
                                        children=self.cpu_circular_progress_bar,
                                        overlays=[
                                            Label(
                                                label="",
                                                style="font-size: 18px; margin-right: 8px; text-shadow: 0 0 10px #fff, 0 0 10px #fff, 0 0 10px #fff;",
                                            ),
                                        ],
                                    )
                                ],
                            ),
                            Box(
                                name="circular-progress-bars-sep",
                            ),
                            Box(
                                children=[
                                    Overlay(
                                        children=self.memory_circular_progress_bar,
                                        overlays=[
                                            Label(
                                                label="󰘚",
                                                style="font-size: 18px; margin-right: 4px; text-shadow: 0 0 10px #fff;",
                                            ),
                                        ],
                                    )
                                ]
                            ),
                            Box(
                                name="circular-progress-bars-sep",
                            ),
                            Box(
                                children=[
                                    Overlay(
                                        children=self.battery_circular_progress_bar,
                                        overlays=[
                                            Label(
                                                label="󱊣",
                                                style="font-size: 18px; margin-right: 0px; text-shadow: 0 0 10px #fff, 0 0 18px #fff;",
                                            ),
                                        ],
                                    ),
                                ]
                            ),
                        ],
                    ),
                ],
            ),
        )
        self.show_all()

    def update_status(self):
        self.cpu_circular_progress_bar.percentage = psutil.cpu_percent()
        self.memory_circular_progress_bar.percentage = psutil.virtual_memory().percent
        self.battery_circular_progress_bar.percentage = (
            psutil.sensors_battery().percent
            if psutil.sensors_battery() is not None
            else 82
        )
        return True

    def get_current_uptime(self):
        uptime = time.time() - psutil.boot_time()
        uptime_days, remainder = divmod(uptime, 86400)
        uptime_hours, remainder = divmod(remainder, 3600)
        uptime_minutes, _ = divmod(remainder, 60)
        return f"{int(uptime_days)} {'days' if uptime_days > 1 else 'day'}, {int(uptime_hours)} {'hours' if uptime_hours > 1 else 'hour'}"


def apply_style(*args):
    logger.info("[Side Panel] CSS applied")
    return set_stylesheet_from_file(get_relative_path("side_panel.css"))


if __name__ == "__main__":
    side_panel = SidePanel()

    if PYWAL is True:
        monitor = monitor_file(
            f"/home/{os.getlogin()}/.cache/wal/colors-widgets.css", "none"
        )
        monitor.connect("changed", apply_style)

    # initialize style
    apply_style()

    fabric.start()
