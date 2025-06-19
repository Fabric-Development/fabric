import gi
import math
import cairo
from typing import Literal, Iterable
from fabric.core.service import Property
from fabric.widgets.container import Container
from fabric.utils.helpers import get_enum_member, clamp

gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, Gtk


class CircularProgressBar(Gtk.Bin, Container):
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

    @Property(float, "read-write", default_value=1.0)
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value
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
        line_style: Literal[
            "none",
            "butt",
            "round",
            "square",
        ]
        | cairo.LineCap,
    ):
        self._line_style = get_enum_member(cairo.LineCap, line_style)  # type: ignore
        return self.queue_draw()

    @Property(float, "read-write", default_value=0.0)
    def start_angle(self) -> float:
        return self._start_angle

    @start_angle.setter
    def start_angle(self, value: float):
        self._start_angle = value
        return self.queue_draw()

    @Property(float, "read-write", default_value=360.0)
    def end_angle(self) -> float:
        return self._end_angle

    @end_angle.setter
    def end_angle(self, value: float):
        self._end_angle = value
        return self.queue_draw()

    @Property(bool, "read-write", default_value=False)
    def invert(self) -> bool:
        return self._invert

    @invert.setter
    def invert(self, value: bool):
        self._invert = value
        return self.queue_draw()

    def __init__(
        self,
        value: float = 1.0,
        min_value: float = 0.0,
        max_value: float = 1.0,
        start_angle: float | None = None,
        end_angle: float | None = None,
        line_width: int = 4,
        line_style: Literal["none", "butt", "round", "square"]
        | cairo.LineCap = cairo.LineCap.ROUND,
        pie: bool = False,
        invert: bool = False,  # TODO: implement...
        child: Gtk.Widget | None = None,
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
        Gtk.DrawingArea.__init__(self)  # type: ignore
        Container.__init__(
            self,
            child,
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
        self._value: float = 1.0
        self._min_value: float = 0.0
        self._max_value: float = 1.0
        self._line_width: int = 4
        self._line_style: cairo.LineCap = cairo.LineCap.ROUND
        self._pie: bool = False
        self._invert: bool = False
        self._start_angle: float = 0.0
        self._end_angle: float = 360.0

        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.line_width = line_width
        self.line_style = line_style
        self.pie = pie
        self.invert = invert
        self.start_angle = start_angle if start_angle is not None else 0.0
        self.end_angle = end_angle if end_angle is not None else 360.0

    def do_calculate_radius(self) -> int:
        alloc = self.get_allocation()
        return min(alloc.width, alloc.height) // 2

    def do_get_preferred_width(self):
        return (2 * self.do_calculate_radius(),) * 2

    def do_get_preferred_height(self):
        return self.do_get_preferred_width()

    def do_draw(self, cr: cairo.Context):
        state = self.get_state_flags()
        style_context = self.get_style_context()

        border = style_context.get_border(state)  # type: ignore
        radius_color = style_context.get_color(state)  # type: ignore
        progress_color = style_context.get_border_color(state)  # type: ignore
        background_color = style_context.get_background_color(state)  # type: ignore

        line_width = max(
            self._line_width,
            border.top,  # type: ignore
            border.bottom,  # type: ignore
            border.left,  # type: ignore
            border.right,  # type: ignore
            style_context.get_property("min-width", state),  # type: ignore
            style_context.get_property("min-height", state),  # type: ignore
        )

        delta = 0
        center_x = self.get_allocated_width() / 2
        center_y = self.get_allocated_height() / 2
        radius = self.do_calculate_radius()

        if (radius - line_width) < 0:
            line_width = radius
        else:
            delta = radius - line_width / 2

        cr.save()

        cr.set_line_cap(self._line_style)
        cr.set_line_width(line_width)

        # background fill
        Gdk.cairo_set_source_rgba(cr, background_color)  # type: ignore
        cr.arc(center_x, center_y, delta + (line_width / 2), 0, 2 * math.pi)
        cr.fill()

        # radius
        Gdk.cairo_set_source_rgba(cr, radius_color)  # type: ignore
        cr.move_to(center_x, center_y) if self._pie is True else None
        cr.arc(
            center_x,
            center_y,
            delta + (self._line_width / 2) if self._pie is True else delta,
            math.radians(self._start_angle),
            math.radians(self._end_angle),
        )
        cr.fill() if self._pie is True else cr.stroke()

        # progress
        normalized_value = clamp(  # normalized & clamped value
            (self._value - self._min_value) / (self._max_value - self._min_value),
            0.0,
            1.0,
        )

        Gdk.cairo_set_source_rgba(cr, progress_color)  # type: ignore
        cr.move_to(center_x, center_y) if self._pie is True else None
        cr.arc(
            center_x,
            center_y,
            delta + (self._line_width / 2) if self._pie is True else delta,
            math.radians(self._start_angle),
            math.radians(
                self._start_angle
                + normalized_value * (self._end_angle - self._start_angle)
            ),
        )
        cr.fill() if self._pie is True else cr.stroke()

        # all aboard, draw child (if any)
        if child := self.get_child():
            self.propagate_draw(child, cr)

        return cr.restore()
