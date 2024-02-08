import fabric
import time
import psutil
from fabric.widgets.box import Box
from fabric.widgets.image import Image
from fabric.widgets.label import Label
from fabric.widgets.button import Button
from fabric.widgets.wayland import Window
from fabric.widgets.date_time import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.utils.fabricator import Fabricate
from fabric.utils.string_formatter import FormattedString
from fabric.hyprland.widgets import Language, WorkspaceButton, Workspaces
from fabric.utils import (
    set_stylesheet_from_file,
    bulk_replace,
    bulk_connect,
    exec_shell_command,
    get_relative_path,
)


class PowerMenu(Window):
    def __init__(self):
        super().__init__(
            layer="overlay",
            anchor="left bottom",
            margin="10px 10px 10px 10px",
            exclusive=False,
        )
        self.shut_down_button = Button(
            label="",
            name="shut-down-button",
        )
        self.reboot_button = Button(
            label="",
            name="reboot-button",
        )
        self.logout_button = Button(
            label="",
            name="logout-button",
        )
        self.add(
            Box(
                spacing=8,
                orientation="v",
                name="power-window",
                children=[
                    self.shut_down_button,
                    self.reboot_button,
                    self.logout_button,
                ],
            )
        )
        for btn in [self.shut_down_button, self.reboot_button, self.logout_button]:
            bulk_connect(
                btn,
                {
                    "enter-notify-event": lambda *args: self.change_cursor("pointer"),
                    "leave-notify-event": lambda *args: self.change_cursor("default"),
                    "button-press-event": self.on_button_press,
                },
            )
        self.hide()

    def on_button_press(self, button: Button, event):
        if event.button == 1 and event.type == 5:
            # this block will be executed on double click
            if button.get_name() == "shut-down-button":
                exec_shell_command("notify-send Shutting down")
            elif button.get_name() == "reboot-button":
                exec_shell_command("notify-send Rebooting")
            elif button.get_name() == "logout-button":
                exec_shell_command("notify-send Logging out")
            self.toggle_window()

    def toggle_window(self):
        if not self.is_visible():
            self.show_all()
        else:
            self.hide()
        return self


class VerticalBar(Window):
    def __init__(self):
        super().__init__(
            layer="top",
            anchor="left top bottom",
            margin="10px -2px 10px 10px",
            exclusive=True,
        )
        self.power_menu = PowerMenu()
        self.time_sep = Label(
            label="",
            name="time-separator",
        )
        self.time_sep_var = Fabricate(
            value="",
            poll_from=lambda _: [
                "",
                self.time_sep.set_style_classes(["day"]),
            ][0]
            if time.strftime("%p").lower() == "am"
            else [
                "",
                self.time_sep.set_style_classes(["night"]),
            ][0],
            interval=1000,
        )
        self.time_sep.bind_property(
            "label",
            self.time_sep_var,
            "value-str",
            1,
        )
        self.center_box = CenterBox(name="main-window", orientation="v")
        self.run_button = Button(
            name="run-button",
            tooltip_text="Show Applications Menu",
            child=Image(
                image_file=get_relative_path("assets/applications.svg"),
            ),
        )
        self.power_button = Button(
            name="power-button",
            tooltip_text="Show Power Menu",
            child=Image(image_file=get_relative_path("assets/power.svg")),
        )
        for btn in [self.run_button, self.power_button]:
            bulk_connect(
                btn,
                {
                    "button-press-event": self.on_button_press,  # run_button -> open wofi, power_button -> toggle the power menu
                    "enter-notify-event": self.on_button_hover,  # to change the cursor to a pointer
                    "leave-notify-event": self.on_button_unhover,  # resets the cursor
                },
            )
        self.center_box.add_left(
            Box(
                orientation="v",
                style="min-width: calc(44px - 8px); margin: 8px;",
                children=[
                    self.run_button,
                    Box(
                        name="module-separator",
                    ),
                    Box(
                        spacing=4,
                        orientation="v",
                        children=[
                            Image(
                                image_file=get_relative_path("assets/language.svg"),
                            ),
                            Language(
                                # NOTE: This is an example of how to use the Language widget,
                                # you will have to pass the keyboard name to the widget in order for it to work
                                # you can find the keyboard names in the output of the `hyprctl` command.
                                formatter=FormattedString(
                                    "{filter(language)}",
                                    filter=lambda x: bulk_replace(
                                        x,
                                        [r".*Eng.*", r".*Ar.*"],
                                        ["ENG", "ARA"],
                                        regex=True,
                                    ),
                                ),
                            ),
                        ],
                    ),
                    Box(
                        name="module-separator",
                    ),
                    Workspaces(
                        spacing=6,
                        orientation="v",
                        name="workspaces",
                        buttons_list=[
                            WorkspaceButton(label=FormattedString("I")),
                            WorkspaceButton(label=FormattedString("II")),
                            WorkspaceButton(label=FormattedString("III")),
                            WorkspaceButton(label=FormattedString("IV")),
                            WorkspaceButton(label=FormattedString("V")),
                            WorkspaceButton(label=FormattedString("VI")),
                            WorkspaceButton(label=FormattedString("VII")),
                        ],
                    ),
                ],
            )
        )
        self.cpu_label = Label(label="0")
        self.memory_label = Label(label="0")
        self.battery_label = Label(label="0")
        self.system_info_var = Fabricate(
            value={"ram": 0, "cpu": 0},
            poll_from=lambda _: {
                "ram": str(int(psutil.virtual_memory().percent)),
                "cpu": str(int(psutil.cpu_percent())),
                "battery": str(
                    int(
                        psutil.sensors_battery().percent
                        if psutil.sensors_battery() is not None
                        else 42
                    )
                ),
            },
            interval=1000,
        )
        self.system_info_var.connect(
            "changed",
            lambda _, value: (
                self.cpu_label.set_label(value["cpu"]),
                self.memory_label.set_label(value["ram"]),
                self.battery_label.set_label(value["battery"]),
            ),
        )
        self.center_box.add_right(
            Box(
                orientation="v",
                style="min-width: calc(44px - 8px); margin: 8px;",
                children=[
                    Box(
                        spacing=4,
                        orientation="v",
                        children=[
                            Image(
                                image_file=get_relative_path("assets/battery.svg"),
                            ),
                            self.battery_label,
                        ],
                    ),
                    Box(name="module-separator"),
                    Box(
                        spacing=4,
                        orientation="v",
                        children=[
                            Image(
                                image_file=get_relative_path("assets/ram.svg"),
                            ),
                            self.memory_label,
                        ],
                    ),
                    Box(name="module-separator"),
                    Box(
                        spacing=4,
                        orientation="v",
                        children=[
                            Image(
                                image_file=get_relative_path("assets/cpu.svg"),
                            ),
                            self.cpu_label,
                        ],
                    ),
                    Box(name="module-separator"),
                    Box(
                        orientation="v",
                        name="time-container",
                        children=[
                            DateTime(format_list=["%I"]),
                            self.time_sep,
                            DateTime(format_list=["%M"]),
                        ],
                    ),
                    Box(name="module-separator"),
                    self.power_button,
                ],
            )
        )
        self.add(self.center_box)
        self.show_all()

    def on_button_press(self, button: Button, event):
        if event.button == 1 and event.type == 5:
            if button == self.run_button:
                return exec_shell_command("wofi -S drun --allow-images")
        elif button == self.power_button:
            return self.power_menu.toggle_window()

    def on_button_hover(self, button: Button, event):
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        return self.change_cursor("default")


if __name__ == "__main__":
    bar = VerticalBar()  # entery point

    set_stylesheet_from_file(get_relative_path("vertical_bar.css"))
    fabric.start()
