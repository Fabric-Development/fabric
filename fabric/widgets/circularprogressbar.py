import math
from typing import Iterable, Literal

import cairo
import gi
from gi.repository import Gdk, Gtk

from fabric.core.service import Property
from fabric.utils.helpers import clamp, get_enum_member
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")


class CircularProgressBar(Gtk.Bin, Widget):
    @Property(float, "read-write", default_value=0.0)
    def start_at(self) -> float:
        return self._start_at

    @start_at.setter
    def start_at(self, value: float):
        self._start_at = clamp(value, 0.0, 1.0)
        return self.queue_draw()

    @Property(float, "read-write", default_value=0.0)
    def end_at(self) -> float:
        return self._end_at

    @end_at.setter
    def end_at(self, value: float):
        self._end_at = clamp(value, 0.0, 1.0)
        return self.queue_draw()

    @Property(float, "read-write", default_value=0.0)
    def min_value(self) -> float:
        return self._min_value

    @min_value.setter
    def min_value(self, value: float):
        self._min_value = clamp(value, self.min_value, self.max_value)
        return self.queue_draw()

    @Property(float, "read-write", default_value=1.0)
    def max_value(self) -> float:
        return self._max_value

    @max_value.setter
    def max_value(self, value: float):
        if value == 0:
            raise ValueError("max_value cannot be zero")
        self._max_value = value
        return self.queue_draw()

    @Property(float, "read-write", default_value=0.0)
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = clamp(value, self.min_value, self.max_value)
        return self.queue_draw()

    @Property(bool, "read-write", default_value=False)
    def pie(self) -> bool:
        return self._pie

    @pie.setter
    def pie(self, value: bool):
        self._pie = value
        return self.queue_draw()

    @Property(int, "read-write", default_value=4)
    def line_width(self) -> int:
        return self._line_width

    @line_width.setter
    def line_width(self, value: int):
        self._line_width = value
        return self.queue_draw()

    @Property(object, "read-write")
    def line_style(self) -> cairo.LineCap:
        return self._line_style  # type: ignore

    @line_style.setter
    def line_style(
        self,
        line_style: (
            Literal[
                "none",
                "butt",
                "round",
                "square",
            ]
            | cairo.LineCap
        ),
    ):
        self._line_style = get_enum_member(cairo.LineCap, line_style)  # type: ignore
        return self.queue_draw()

    @Property(object, "read-write")
    def size(self) -> Iterable[int] | int | None:
        return self._size

    @size.setter
    def size(self, value: Iterable[int] | int | None):
        self._size = value
        return self.queue_draw()

    def __init__(
        self,
        child: Gtk.Widget | None = None,
        value: float = 0.0,
        start_at: float = 0.0,
        end_at: float = 1.0,
        min_value: float = 0.0,
        max_value: float = 1.0,
        pie: bool = False,
        line_width: int = 4,
        line_style: (
            Literal[
                "none",
                "butt",
                "round",
                "square",
            ]
            | cairo.LineCap
        ) = cairo.LineCap.ROUND,
        inverted: bool = False,
        size: Iterable[int] | int | None = None,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_classes: Iterable[str] | str | None = None,
        tooltip_text: str | None = None,
        tooltip_markup: str | None = None,
        h_align: (
            Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None
        ) = None,
        v_align: (
            Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None
        ) = None,
        h_expand: bool = False,
        v_expand: bool = False,
        **kwargs,
    ):
        Gtk.Bin.__init__(self)  # type: ignore
        Widget.__init__(
            self,
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
        self._start_at: float = 0.0
        self._end_at: float = 1.0
        self._min_value: float = 0.0
        self._max_value: float = 1.0
        self._value: float = 0.0
        self._pie: bool = False
        self._line_style: cairo.LineCap = cairo.LineCap.ROUND
        self._inverted: bool = False
        self._size: Iterable[int] | int | None = None

        self.start_at = start_at
        self.end_at = end_at
        self.min_value = min_value
        self.max_value = max_value
        self.value = value
        self.line_width = line_width
        self.pie = pie
        self.line_style = line_style
        self.inverted = inverted
        self.size = size

        if child:
            self.add(child)

        self.connect("draw", self.on_draw)

    def do_get_preferred_width(self):
        if self.size:
            if isinstance(self.size, int):
                return self.size, self.size
            else:
                return self.size[0], self.size[0]
        min_width = self.get_style_context().get_property(
            "min-width", Gtk.StateFlags.NORMAL
        )
        if min_width <= 0:
            min_width = 40
        return min_width, min_width

    def do_get_preferred_height(self):
        if self.size:
            if isinstance(self.size, int):
                return self.size, self.size
            else:
                return self.size[1], self.size[1]
        min_height = self.get_style_context().get_property(
            "min-height", Gtk.StateFlags.NORMAL
        )
        if min_height <= 0:
            min_height = 40
        return min_height, min_height

    def do_convert_to_radian(self, percentage: float) -> float:
        percentage = math.floor(percentage * 100)
        return (percentage / 100) * (2 * math.pi)

    def do_check_full_circle(
        self, start: float, end: float, epsilon: float = 1e-10
    ) -> bool:
        start = (start % 1 + 1) % 1
        end = (end % 1 + 1) % 1
        return abs(start - end) <= epsilon

    def do_scale_arc_value(self, start: float, end: float, value: float) -> float:
        start = (start % 1 + 1) % 1
        end = (end % 1 + 1) % 1

        if abs(end - start) < 1e-10:  # Handles the full circle case
            return value

        arc_length = end - start
        if arc_length < 0:
            arc_length += 1

        scaled = arc_length * value
        scaled = (scaled % 1 + 1) % 1
        return start + scaled

    def do_normalize_value(self) -> float:
        return (self.value - self.min_value) / (self.max_value - self.min_value)

    def do_draw_arc(
        self,
        cr: cairo.Context,
        center_x: float,
        center_y: float,
        radius: float,
        line_width: float,
        start_at: float,
        end_at: float,
        color,
        pie: bool = False,
    ):
        start_radian = self.do_convert_to_radian(start_at)
        end_radian = self.do_convert_to_radian(end_at)

        # Set color
        Gdk.cairo_set_source_rgba(cr, color)  # type: ignore

        # Draw the arc
        cr.set_line_cap(self._line_style)
        cr.move_to(center_x, center_y) if pie else None
        cr.arc(center_x, center_y, radius, start_radian, end_radian)
        cr.set_line_width(line_width)
        cr.fill() if pie else cr.stroke()

    def on_draw(self, _, cr: cairo.Context):
        # CSS properties lookup table
        #  -------------------------------
        # | border: ... ... SIZE          |
        # | will result in SIZE begin     |
        # | used as the line_width value  |
        #  ------------------------------
        # | background fill     | background-color
        # |---------------------|--------
        # | radius fill         | color
        # |---------------------|--------
        # | progress fill       | border-color
        # |---------------------|--------
        # | progress line width | border-color
        #  ------------------------------
        allocation = self.get_allocation()
        style_context = self.get_style_context()

        # Retrieve colors
        background_color = style_context.get_background_color(Gtk.StateFlags.NORMAL)
        radius_color = style_context.get_color(Gtk.StateFlags.NORMAL)
        progress_color = style_context.get_border_color(Gtk.StateFlags.NORMAL)
        border = style_context.get_border(Gtk.StateFlags.BACKDROP)

        # Normalize value
        value = self.do_normalize_value()
        width, height = allocation.width, allocation.height

        # Compute dimensions
        line_width = max(
            self.line_width,
            border.top,  # type: ignore
            border.bottom,  # type: ignore
            border.left,  # type: ignore
            border.right,  # type: ignore
            style_context.get_property("min-width", Gtk.StateFlags.NORMAL),  # type: ignore
            style_context.get_property("min-height", Gtk.StateFlags.NORMAL),  # type: ignore
        )
        radius = min(width, height) / 2.0 - line_width / 2.0
        center_x, center_y = width / 2, height / 2

        # Background arc
        self.do_draw_arc(
            cr,
            center_x,
            center_y,
            radius,
            line_width,
            self.start_at,
            self.end_at,
            background_color,
            self.pie,
        )

        # Progress arc calculation
        if self.inverted:
            start_progress = self.do_scale_arc_value(
                self.start_at, self.end_at, 1 - value
            )
            end_progress = self.end_at
        else:
            start_progress = self.start_at
            end_progress = self.do_scale_arc_value(self.start_at, self.end_at, value)

        self.do_draw_arc(
            cr,
            center_x,
            center_y,
            radius,
            line_width,
            start_progress,
            end_progress,
            progress_color,
            self.pie,
        )

        # Draw radius (optional full-circle outline)
        if not self.pie:
            Gdk.cairo_set_source_rgba(cr, radius_color)  # type: ignore
            cr.arc(center_x, center_y, radius, 0, 2 * math.pi)
            cr.stroke()

        # Handle child widget (if any)
        if self.get_child():
            self.get_child().size_allocate(allocation)
            self.propagate_draw(self.get_child(), cr)
