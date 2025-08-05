import psutil
from fabric import Application, Fabricator
from fabric.widgets.box import Box
from fabric.widgets.image import Image
from fabric.widgets.eventbox import EventBox
from fabric.widgets.datetime import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.system_tray.widgets import SystemTray
from fabric.widgets.circularprogressbar import CircularProgressBar
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.hyprland.widgets import (
    HyprlandLanguage,
    HyprlandActiveWindow,
    HyprlandWorkspaces,
    WorkspaceButton,
)
from fabric.utils import FormattedString, get_relative_path, bulk_replace

AUDIO_WIDGET = True

if AUDIO_WIDGET is True:
    try:
        from fabric.audio.service import Audio
    except Exception as e:
        AUDIO_WIDGET = False
        print(e)


class VolumeWidget(Box):
    def __init__(self, **kwargs):
        self.progress_bar = CircularProgressBar(
            name="volume-progress-bar",
            pie=True,
            child=Image(icon_name="audio-speakers-symbolic", icon_size=12),
            size=24,
        )

        self.audio = Audio(notify_speaker=self.on_speaker_changed)

        super().__init__(
            children=EventBox(
                events="scroll", child=self.progress_bar, on_scroll_event=self.on_scroll
            ),
            **kwargs,
        )

    def on_scroll(self, _, event):
        match event.direction:
            case 0:
                self.audio.speaker.volume += 8
            case 1:
                self.audio.speaker.volume -= 8
        return

    def on_speaker_changed(self):
        if not self.audio.speaker:
            return

        self.progress_bar.value = self.audio.speaker.volume / 100
        return self.audio.speaker.bind(
            "volume", "value", self.progress_bar, lambda _, v: v / 100
        )


class StatusBar(Window):
    def __init__(
        self,
    ):
        super().__init__(
            name="bar",
            layer="top",
            anchor="left top right",
            margin="10px 10px -2px 10px",
            exclusivity="auto",
            visible=False,
        )

        self.system_status = Box(
            name="system-status",
            spacing=4,
            orientation="h",
            children=[
                # a progress bar (ram) has a child of a progress bar (cpu) that which has a child (the icon)
                CircularProgressBar(
                    name="ram-progress-bar",
                    pie=True,
                    child=CircularProgressBar(
                        name="cpu-progress-bar",
                        pie=True,
                        child=Image(icon_name="cpu-symbolic", icon_size=12),
                        size=24,
                    ).build(
                        lambda progres: Fabricator(
                            interval=1000,
                            poll_from=lambda f: psutil.cpu_percent() / 100,
                            on_changed=lambda _, value: progres.set_value(value),
                        )
                    ),
                    size=24,
                ).build(
                    lambda progres: Fabricator(
                        interval=1000,
                        poll_from=lambda f: psutil.virtual_memory().percent / 100,
                        on_changed=lambda _, value: progres.set_value(value),
                    )
                )
            ]
            # create a volume widget if enabled
            + ([VolumeWidget()] if AUDIO_WIDGET else []),
        )

        self.children = CenterBox(
            name="bar-inner",
            start_children=Box(
                name="start-container",
                children=HyprlandWorkspaces(
                    name="workspaces",
                    spacing=4,
                    buttons_factory=lambda ws_id: WorkspaceButton(id=ws_id, label=None),
                ),
            ),
            center_children=Box(
                name="center-container",
                children=HyprlandActiveWindow(name="hyprland-window"),
            ),
            end_children=Box(
                name="end-container",
                spacing=4,
                orientation="h",
                children=[
                    self.system_status,
                    SystemTray(name="system-tray", spacing=4),
                    DateTime(name="date-time"),
                    HyprlandLanguage(
                        name="hyprland-window",
                        formatter=FormattedString(
                            "{replace_lang(language)}",
                            replace_lang=lambda lang: bulk_replace(
                                lang,
                                (r".*Eng.*", r".*Ar.*"),
                                ("ENG", "ARA"),
                                regex=True,
                            ),
                        ),
                    ),
                ],
            ),
        )

        return self.show_all()


if __name__ == "__main__":
    bar = StatusBar()
    app = Application("bar", bar)
    app.set_stylesheet_from_file(get_relative_path("./style.css"))

    app.run()
