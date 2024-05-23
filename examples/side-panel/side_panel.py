"""side panel example, contains info about the system"""
import fabric
import os
import time
import psutil
from loguru import logger
from fabric.widgets import Box, Label, Window, Overlay, DateTime, CircularProgressBar
from fabric.utils import (
    set_stylesheet_from_file,
    monitor_file,
    invoke_repeater,
    get_relative_path,
)

PYWAL = False


def get_profile_picture_path() -> str | None:
    path = os.path.expanduser("~/Pictures/Other/profile.jpg")
    if not os.path.exists(path):
        path = os.path.expanduser("~/Pictures/Other/profile.jpg")
    if not os.path.exists(path):
        logger.warning("can't fetch a user profile picture")
        path = None
    return path


class SidePanel(Window):
    def __init__(self):
        super().__init__(
            layer="overlay",
            title="fabric-overlay",
            exclusive=True,
            anchor="top right",
            margin="10px 10px 10px 0px",
            visible=False,
            all_visible=False,
        )
        self.uptime_label = Label(
            label=f"{self.get_current_uptime()}",
            style="font-size: 18px;",
        )
        self.cpu_circular_progress_bar = CircularProgressBar(
            size=(64, 64),
            name="circular-progress-bar",
        )
        self.memory_circular_progress_bar = CircularProgressBar(
            size=(64, 64),
            name="circular-progress-bar",
        )
        self.battery_circular_progress_bar = CircularProgressBar(
            size=(64, 64),
            percentage=42,
            name="circular-progress-bar",
        )
        self.update_status()
        invoke_repeater(
            60 * 15 * 1000,
            lambda: [self.uptime_label.set_label(self.get_current_uptime()), True][1],
            1000,
            self.update_status,
        )
        self.add(
            Box(
                spacing=24,
                name="main-window",
                orientation="v",
                children=[
                    Box(
                        spacing=14,
                        name="header",
                        orientation="h",
                        children=[
                            Box(
                                name="profile-pic",
                                style=f"background-image: url('file://{get_profile_picture_path() if get_profile_picture_path() is not None else ''}')",
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
                                    ),
                                ],
                            ),
                            Box(name="circular-progress-bars-sep"),
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
                            Box(name="circular-progress-bars-sep"),
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
                                ],
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
            else 42
        )
        return True

    def get_current_uptime(self):
        uptime = time.time() - psutil.boot_time()
        uptime_days, remainder = divmod(uptime, 86400)
        uptime_hours, remainder = divmod(remainder, 3600)
        # uptime_minutes, _ = divmod(remainder, 60)
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
