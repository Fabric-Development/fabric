import gi
import time
from loguru import logger
from typing import Literal
from fabric.widgets.button import Button

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class DateTime(Button):
    """
    a custom widget to display the current date/time in different formats.
    it allows to cycle through a passed list of date/time formats by clicking on the widget.
    """

    def __init__(
        self,
        format_list: list[str] = ["%I:%M %p", "%A", "%m-%d-%Y"],
        interval: int = 1000,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_compiled: bool = True,
        style_append: bool = False,
        style_add_brackets: bool = True,
        tooltip_text: str | None = None,
        tooltip_markup: str | None = None,
        h_align: Literal["fill", "start", "end", "center", "baseline"]
        | Gtk.Align
        | None = None,
        v_align: Literal["fill", "start", "end", "center", "baseline"]
        | Gtk.Align
        | None = None,
        h_expand: bool = False,
        v_expand: bool = False,
        name: str | None = None,
        size: tuple[int] | int | None = None,
        **kwargs,
    ):
        super().__init__(
            visible=visible,
            all_visible=all_visible,
            style=style,
            style_compiled=style_compiled,
            style_append=style_append,
            style_add_brackets=style_add_brackets,
            tooltip_text=tooltip_text,
            tooltip_markup=tooltip_markup,
            h_align=h_align,
            v_align=v_align,
            h_expand=h_expand,
            v_expand=v_expand,
            name=name,
            size=size,
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        self.format_list = format_list
        self.interval = interval
        if not type(format_list) == list or len(format_list) == 0:
            logger.warning(
                "[DateTime] Please use non-empty list for format_list. falling back to default value."
            )
            self.format_list = ["%I:%M %p", "%A", "%m-%d-%Y"]
        self.index: int = 0
        self.do_bake_label()
        GLib.timeout_add(self.interval, self.do_bake_label)
        self.connect("button-press-event", self.on_button_press)
        self.do_connect_signals_for_kwargs(kwargs)

    def on_button_press(self, scale, event):
        """
        Handles the button press event and cycles through the format list to update the displayed date and time.
        """
        for i, s in enumerate(self.format_list):
            if self.index == i:
                try:
                    self.format_list[self.index + 1]
                    self.index += 1
                except IndexError:
                    self.index = 0
                self.do_bake_label()
                break
            else:
                continue

    def set_format_list(self, format_list: list[str]):
        """
        Sets a new list of date and time formats for the widget.
        """
        if not type(format_list) == list or len(format_list) == 0:
            logger.warning(
                "[DateTime] Please use non-empty list object for format_list."
            )
            self.format_list = (
                ["%I:%M %p", "%A", "%m-%d-%Y"]
                if not self.format_list
                else self.format_list
            )
            self.do_bake_label()
            return
        self.format_list = format_list
        self.do_bake_label()

    def set_interval(self, interval: int):
        """
        Sets a new interval for updating the displayed date and time.
        """
        if not type(interval) == int or interval < 1:
            logger.warning("[DateTime] Please pass a valid interval value.")
            self.interval = 1000
            return
        self.interval = interval
        return

    def do_bake_label(self):
        """
        Updates the label of the widget with the current date and time format.
        """
        self.set_label(time.strftime(self.format_list[self.index]))
        return True
