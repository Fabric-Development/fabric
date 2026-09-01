import gi
import time
from loguru import logger
from typing import Literal
from collections.abc import Iterable
from fabric.widgets.button import Button
from fabric.core.service import Property
from fabric.utils.helpers import invoke_repeater

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gdk


class DateTime(Button):
    """Dead simple implementation of a date-time widget

    The way this widget works is by having a button that listens
    for click events and upon that it switchs to the next date-time format
    from the given list of `formatters`.

    For more about formatters visit https://docs.python.org/3/library/time.html#time.strftime
    """

    @Property(tuple[str, ...], "read-write")
    def formatters(self) -> tuple[str, ...]:
        """The list of datetime format strings used for each cycle

        :rtype: tuple[str, ...]
        """
        return self._formatters

    @formatters.setter
    def formatters(self, value: str | Iterable[str]):
        if isinstance(value, (tuple, list)):
            self._formatters = tuple(value)
        elif isinstance(value, str):
            self._formatters = (value,)
        if len(self._formatters) < 1:
            logger.warning(
                "[DateTime] passed in invalid list of formatters, using default formatters list"
            )
            self._formatters = ("%I:%M %p", "%A", "%m-%d-%Y")
        return

    @Property(int, "read-write")
    def interval(self) -> int:
        """Updating interval time in ms

        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, value: int):
        self._interval = value
        if self._repeater_id:
            GLib.source_remove(self._repeater_id)
        self._repeater_id = invoke_repeater(self._interval, self.do_update_label)
        self.do_update_label()
        return

    def __init__(
        self,
        formatters: str | Iterable[str] = ("%I:%M %p", "%A", "%m-%d-%Y"),
        interval: int = 1000,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_classes: Iterable[str] | str | None = None,
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
        size: Iterable[int] | int | None = None,
        **kwargs,
    ):
        """
        :param formatters: the date-time formatter (or a list of formatters) for each cycle, defaults to ("%I:%M %p", "%A", "%m-%d-%Y")
        :type formatters: str | Iterable[str], optional
        :param interval: the interval for updating this widget's content (rerender date-time) in milliseconds, defaults to 1000
        :type interval: int, optional
        :param name: the name identifer for this widget (useful for styling), defaults to None
        :type name: str | None, optional
        :param visible: whether should this widget be visible or not once initialized, defaults to True
        :type visible: bool, optional
        :param all_visible: whether should this widget and all of its children be visible or not once initialized, defaults to False
        :type all_visible: bool, optional
        :param style: inline stylesheet to be applied on this widget, defaults to None
        :type style: str | None, optional
        :param style_classes: a list of style classes to be added into this widget once initialized, defaults to None
        :type style_classes: Iterable[str] | str | None, optional
        :param tooltip_text: the text that should be rendered inside the tooltip, defaults to None
        :type tooltip_text: str | None, optional
        :param tooltip_markup: same as `tooltip_text` but it accepts simple markup expressions, defaults to None
        :type tooltip_markup: str | None, optional
        :param h_align: horizontal alignment of this widget (compared to its parent), defaults to None
        :type h_align: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None, optional
        :param v_align: vertical alignment of this widget (compared to its parent), defaults to None
        :type v_align: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None, optional
        :param h_expand: whether should this widget fill in all the available horizontal space or not, defaults to False
        :type h_expand: bool, optional
        :param v_expand: whether should this widget fill in all the available vertical space or not, defaults to False
        :type v_expand: bool, optional
        :param size: a fixed size for this widget (not guranteed to get applied), defaults to None
        :type size: Iterable[int] | int | None, optional
        """
        super().__init__(
            None,
            None,
            None,
            name,
            visible,
            all_visible,
            style,
            style_classes,
            tooltip_text,
            tooltip_markup,
            h_align,
            v_align,
            h_expand,
            v_expand,
            size,
            **kwargs,
        )
        self.add_events(Gdk.EventMask.SCROLL_MASK)
        self._formatters: tuple[str, ...] = tuple()
        self._current_index: int = 0
        self._interval: int = interval
        self._repeater_id: int | None = None

        self.formatters = formatters
        self.interval = interval

        self.connect(
            "button-press-event",
            lambda *args: self.do_handle_press(*args),  # to allow overriding
        )
        self.connect("scroll-event", lambda *args: self.do_handle_scroll(*args))

    def do_format(self) -> str:
        return time.strftime(self._formatters[self._current_index])

    def do_update_label(self):
        self.set_label(self.do_format())
        return True

    def do_check_invalid_index(self, index: int) -> bool:
        return (index < 0) or (index > (len(self.formatters) - 1))

    def do_cycle_next(self):
        self._current_index = self._current_index + 1
        if self.do_check_invalid_index(self._current_index):
            self._current_index = 0  # reset tags

        return self.do_update_label()

    def do_cycle_prev(self):
        self._current_index = self._current_index - 1
        if self.do_check_invalid_index(self._current_index):
            self._current_index = len(self.formatters) - 1

        return self.do_update_label()

    def do_handle_press(self, _, event, *args):
        match event.button:
            case 1:  # left click
                self.do_cycle_next()
            case 3:  # right click
                self.do_cycle_prev()
        return

    def do_handle_scroll(self, _, event, *args):
        match event.direction:
            case Gdk.ScrollDirection.UP:  # scrolling up
                self.do_cycle_next()
            case Gdk.ScrollDirection.DOWN:  # scrolling down
                self.do_cycle_prev()
        return
