"""desktop status bar example"""
import fabric
import os
import psutil
from loguru import logger
from fabric.widgets import (
    Box,
    Label,
    Overlay,
    EventBox,
    DateTime,
    CenterBox,
    SystemTray,
    CircularProgressBar,
    WaylandWindow as Window,
    HyprlandWorkspaceButton as WorkspaceButton,
    HyprlandWorkspaces as Workspaces,
    HyprlandActiveWindow as ActiveWindow,
    HyprlandLanguage as Language,
)

from fabric.utils import (
    FormattedString,
    set_stylesheet_from_file,
    bulk_replace,
    monitor_file,
    invoke_repeater,
    get_relative_path,
)

PYWAL = False
AUDIO_WIDGET = True

if AUDIO_WIDGET is True:
    try:
        from fabric.audio.service import Audio
    except Exception as e:
        logger.error(e)
        AUDIO_WIDGET = False


class VolumeWidget(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.audio = Audio()

        self.circular_progress_bar = CircularProgressBar(
            name="volume-circular-progress-bar",
            background_color=False,  # false = disabled
            radius_color=False,
            pie=True,
        )

        self.event_box = EventBox(
            events="scroll",
            children=Overlay(
                children=self.circular_progress_bar,
                overlays=Label(
                    label="",
                    style="margin: 0px 6px 0px 0px; font-size: 12px",  # because glyph icon is not centered
                ),
            ),
        )

        self.event_box.connect("scroll-event", self.on_scroll)
        self.audio.connect("speaker-changed", self.update)
        self.add(self.event_box)

    def on_scroll(self, widget, event):
        if event.direction == 0:
            self.audio.speaker.volume += 8
        elif event.direction == 1:
            self.audio.speaker.volume -= 8

    def update(self, *args):
        if self.audio.speaker is None:
            return
        self.circular_progress_bar.percentage = self.audio.speaker.volume
        return


class StatusBar(Window):
    def __init__(
        self,
    ):
        super().__init__(
            layer="top",
            anchor="left top right",
            margin="10px 10px -2px 10px",
            exclusive=True,
            visible=False,
            all_visible=False,
        )
        self.center_box = CenterBox(name="main-window")
        self.workspaces = Workspaces(
            spacing=2,
            name="workspaces",
            buttons_list=[
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
            ],
        )
        self.active_window = ActiveWindow(
            formatter=FormattedString(
                "{test_title(win_class)}",
                test_title=lambda x, max_length=20: "Desktop"
                if len(x) == 0
                else x
                if len(x) <= max_length
                else x[: max_length - 3] + "...",
            ),
            name="hyprland-window",
        )
        self.language = Language(
            formatter=FormattedString(
                "{replace_lang(language)}",
                replace_lang=lambda x: bulk_replace(
                    x,
                    [r".*Eng.*", r".*Ar.*"],
                    ["ENG", "ARA"],
                    regex=True,
                ),
            ),
            name="hyprland-window",
        )
        self.date_time = DateTime(name="date-time")
        self.system_tray = SystemTray(name="system-tray")
        self.ram_circular_progress_bar = CircularProgressBar(
            name="ram-circular-progress-bar",
            background_color=False,  # false = disabled
            radius_color=False,
            pie=True,
        )
        self.cpu_circular_progress_bar = CircularProgressBar(
            name="cpu-circular-progress-bar",
            background_color=False,
            radius_color=False,
            pie=True,
        )
        self.circular_progress_bars_overlay = Overlay(
            children=self.ram_circular_progress_bar,
            overlays=[
                self.cpu_circular_progress_bar,
                Label("", style="margin: 0px 6px 0px 0px; font-size: 12px"),
            ],
        )
        self.volume = VolumeWidget() if AUDIO_WIDGET is True else None
        self.widgets_container = Box(
            spacing=2,
            orientation="h",
            name="widgets-container",
            children=[
                self.circular_progress_bars_overlay,
            ],
        )
        self.widgets_container.add(self.volume) if self.volume is not None else None

        self.center_box.add_start(self.workspaces)
        self.center_box.add_center(self.active_window)
        self.center_box.add_end(self.widgets_container)
        self.center_box.add_end(self.system_tray)
        self.center_box.add_end(self.date_time)
        self.center_box.add_end(self.language)
        self.add(self.center_box)

        invoke_repeater(1000, self.update_progress_bars)
        self.update_progress_bars()  # initial call

        self.show_all()

    def update_progress_bars(self):
        self.ram_circular_progress_bar.percentage = psutil.virtual_memory().percent
        self.cpu_circular_progress_bar.percentage = psutil.cpu_percent()
        return True


def apply_style(*args):
    logger.info("[Bar] CSS applied")
    return set_stylesheet_from_file(get_relative_path("bar.css"))


if __name__ == "__main__":
    bar = StatusBar()

    if PYWAL is True:
        monitor = monitor_file(
            f"/home/{os.getlogin()}/.cache/wal/colors-widgets.css", "none"
        )
        monitor.connect("changed", apply_style)

    # initialize style
    apply_style()

    fabric.start()
