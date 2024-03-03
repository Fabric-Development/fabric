import gi
import math
import cairo
from typing import Literal, Iterable
from fabric.widgets.widget import Widget
from fabric.utils import get_gdk_rgba

gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, Gtk


class CircularProgressBar(Gtk.DrawingArea, Widget):
    """a circular progress bar widget drawn with cairo"""

    def __init__(
        self,
        percentage: int | float = 0,
        line_width: int | None = None,
        line_style: Literal[
            "none",
            "butt",
            "round",
            "square",
        ]
        | cairo.LineCap = "round",
        background_color: str | Iterable[int] | bool | None = None,
        radius_color: str | Iterable[int] | bool | None = None,
        progress_color: str | Iterable[int] | bool | None = None,
        pie: bool | None = False,
        gap_size: int | None = None,
        angle: int | None = 0,
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
        size: tuple[int, int] | int | None = (24, 24),
        **kwargs,
    ):
        """
        :param percentage: the initial percentage of the progress bar value can be between 0 and 100, defaults to 0
        :type percentage: int | float, optional
        :param line_width: the width of the line, if None falls back to the highest value of `border-[top|bottom|left|right]-width` or `min-[width|height]` gotten from the style, defaults to None
        :type line_width: int | None, optional
        :param line_style: the line style, defaults to "round"
        :type line_style: Literal["none", "butt", "round", "square"] | cairo.LineCap, optional
        :param background_color: the background color, if False passed then the background will not be drawn, if None, fall back to `background(color)` from the style, defaults to None
        :type background_color: str | Iterable[int] | bool | None, optional
        :param radius_color: the radius color, if False passed then the radius will not be drawn, if None, fall back to `color` from the style, defaults to None
        :type radius_color: str | Iterable[int] | bool | None, optional
        :param progress_color: the progress color, if False passed then the progress will not be drawn, if None, fall back to border color from the style, defaults to None
        :type progress_color: str | Iterable[int] | bool | None, optional
        :param pie: whether the progress bar is a pie or not, defaults to False
        :type pie: bool | None, optional
        :param gap_size: the gap size (makes the progress bar look like a meter) setting it to 0 will disable the gap, if None falls back to the highest value of `margin[-top|-bottom|-left|-right]` gotten from the style, defaults to None
        :type gap_size: int | None, optional
        :param angle: the angle of the progress bar AKA the start angle, defaults to 0
        :type angle: int | None, optional
        :param visible: whether the widget is initially visible, defaults to True
        :type visible: bool, optional
        :param all_visible: whether all child widgets are initially visible, defaults to False
        :type all_visible: bool, optional
        :param style: inline css style string, defaults to None
        :type style: str | None, optional
        :param style_compiled: whether the passed css should get compiled before applying, defaults to True
        :type style_compiled: bool, optional
        :param style_append: whether the passed css should be appended to the existing css, defaults to False
        :type style_append: bool, optional
        :param style_add_brackets: whether the passed css should be wrapped in brackets if they were missing, defaults to True
        :type style_add_brackets: bool, optional
        :param tooltip_text: the text added to the tooltip, defaults to None
        :type tooltip_text: str | None, optional
        :param tooltip_markup: the markup added to the tooltip, defaults to None
        :type tooltip_markup: str | None, optional
        :param h_align: the horizontal alignment, defaults to None
        :type h_align: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None, optional
        :param v_align: the vertical alignment, defaults to None
        :type v_align: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None, optional
        :param h_expand: the horizontal expansion, defaults to False
        :type h_expand: bool, optional
        :param v_expand: the vertical expansion, defaults to False
        :type v_expand: bool, optional
        :param name: the name of the widget it can be used to style the widget, defaults to None
        :type name: str | None, optional
        :param size: the size of the widget, defaults to None
        :type size: tuple[int] | int | None, optional
        """
        Gtk.DrawingArea.__init__(
            self,
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        Widget.__init__(
            self,
            visible,
            all_visible,
            style,
            style_compiled,
            style_append,
            style_add_brackets,
            tooltip_text,
            tooltip_markup,
            h_align,
            v_align,
            h_expand,
            v_expand,
            name,
            size,
        )
        if (
            percentage < 0
            or percentage > 100
            or not isinstance(percentage, (int, float))
        ):
            raise ValueError(
                f"percentage must be an integer or a float with a value between 0 and 100",
                f"but got {percentage}",
            )
        self._line_width = line_width
        self._percentage = percentage
        self._background_color = background_color
        self._radius_color = radius_color
        self._progress_color = progress_color
        self._pie = pie
        self._gap_size = gap_size
        self._angle = angle
        self._line_style = (
            line_style
            if isinstance(line_style, cairo.LineCap)
            else {
                "none": None,
                "butt": cairo.LineCap.BUTT,
                "round": cairo.LineCap.ROUND,
                "square": cairo.LineCap.SQUARE,
            }.get(line_style.lower(), cairo.LineCap.ROUND)
        )
        self._size = (
            (size, size)
            if size is not None and isinstance(size, int)
            else size
            if size is not None
            else (self.get_allocation().width, self.get_allocation().height)
        )
        self.do_connect_signals_for_kwargs(kwargs)

    @property
    def percentage(self) -> int:
        return self._percentage

    @percentage.setter
    def percentage(self, value: int):
        self._percentage = value
        self.queue_draw()
        return

    @property
    def line_width(self) -> int | None:
        return self._line_width

    @line_width.setter
    def line_width(self, value: int | None):
        self._line_width = value
        self.queue_draw()
        return

    @property
    def gap_size(self) -> int | None:
        return self._gap_size

    @gap_size.setter
    def gap_size(self, value: int | None):
        self._gap_size = value
        self.queue_draw()
        return

    @property
    def angle(self) -> int | None:
        return self._angle

    @angle.setter
    def angle(self, value: int | None):
        self._angle = value
        self.queue_draw()
        return

    @property
    def line_style(self) -> cairo.LineCap:
        return self._line_style

    @line_style.setter
    def line_style(
        self, value: Literal["none", "butt", "round", "square"] | cairo.LineCap | None
    ):
        self._line_style = (
            value
            if isinstance(value, cairo.LineCap)
            else {
                "none": None,
                "butt": cairo.LineCap.BUTT,
                "round": cairo.LineCap.ROUND,
                "square": cairo.LineCap.SQUARE,
            }.get(value.lower(), cairo.LineCap.ROUND)
        )
        self.queue_draw()
        return

    @property
    def radius_color(self) -> bool | None:
        return self._radius_color

    @radius_color.setter
    def radius_color(self, value: bool | None):
        self._radius_color = value
        self.queue_draw()
        return

    @property
    def progress_color(self) -> bool | None:
        return self._progress_color

    @progress_color.setter
    def progress_color(self, value: bool | None):
        self._progress_color = value
        self.queue_draw()
        return

    @property
    def background_color(self) -> bool | None:
        return self._background_color

    @background_color.setter
    def background_color(self, value: bool | None):
        self._background_color = value
        self.queue_draw()
        return

    @property
    def pie(self) -> bool:
        return self._pie

    @pie.setter
    def pie(self, value: bool):
        self._pie = value
        self.queue_draw()
        return

    def calculate_radius(self):
        width = float(self.get_allocated_width()) / 2
        height = (float(self.get_allocated_height()) / 2) - 1
        return int(min(width, height))

    def calculate_diameter(self):
        return 2 * self.calculate_radius()

    @property
    def perferred_size(self):
        d = self.calculate_diameter()
        if d > self._size[0]:
            natural = d
        else:
            natural = self._size[0]
        return d, natural

    def do_get_preferred_width(self):
        return self.perferred_size

    def do_get_preferred_height(self):
        return self.perferred_size

    def do_draw(self, cr: cairo.Context):
        cr.save()
        cr.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
        style_context = self.get_style_context()
        border = (
            style_context.get_border(Gtk.StateFlags.NORMAL)
            if self._line_width is None
            else None
        )
        self._line_width = (
            max(
                border.top,
                border.bottom,
                border.left,
                border.right,
                style_context.get_property("min-width", Gtk.StateFlags.NORMAL),
                style_context.get_property("min-height", Gtk.StateFlags.NORMAL),
            )
            if border is not None
            else self._line_width
        )
        margin = (
            style_context.get_margin(Gtk.StateFlags.NORMAL)
            if self._gap_size is None
            else None
        )
        self._gap_size = (
            max(
                margin.top,
                margin.bottom,
                margin.left,
                margin.right,
            )
            if margin is not None
            else self._gap_size
        )

        # doing the math
        delta = 0
        center_x = self.get_allocated_width() / 2
        center_y = self.get_allocated_height() / 2
        radius = self.calculate_radius()
        d = radius - self._line_width
        delta = radius - self._line_width / 2
        if d < 0:
            delta = 0
            self._line_width = radius

        cr.set_line_cap(self._line_style) if self._line_style is not None else None
        cr.set_line_width(self._line_width)

        gap_angle = (
            (((2 * math.pi * delta) * (self.gap_size / 100)) / delta)
            if delta > 0
            else 0
        )

        # background fill
        if self._background_color is not False:
            cr.arc(center_x, center_y, delta + (self._line_width / 2), 0, 2 * math.pi)
            Gdk.cairo_set_source_rgba(
                cr,
                style_context.get_background_color(Gtk.StateFlags.NORMAL)
                if self._background_color is None
                or not isinstance(self._radius_color, bool)
                else get_gdk_rgba(self._background_color),
            )
            cr.fill()

        # radius
        if self._radius_color is not False:
            cr.move_to(center_x, center_y) if self._pie is True else None
            start_angle = self._angle + (1.5 * math.pi) + (gap_angle / 2)
            end_angle = self._angle + (1.5 + 1 * 2) * math.pi - (gap_angle / 2)
            cr.arc(
                center_x,
                center_y,
                delta + (self._line_width / 2) if self._pie is True else delta,
                start_angle,
                end_angle,
            )
            Gdk.cairo_set_source_rgba(
                cr,
                style_context.get_color(Gtk.StateFlags.NORMAL)
                if self._radius_color is None
                or not isinstance(self._radius_color, bool)
                else get_gdk_rgba(self._radius_color),
            )
            cr.fill() if self._pie is True else cr.stroke()

        # progress
        if (self._percentage / 100) > -1 and self._progress_color is not False:
            cr.move_to(center_x, center_y) if self._pie is True else None
            start_angle = self.angle + (1.5 * math.pi) + (gap_angle / 2)
            end_angle = (
                self.angle
                + (1.5 + (self._percentage / 100) * 2) * math.pi
                - (gap_angle / 2)
            )
            cr.arc(
                center_x,
                center_y,
                delta + (self._line_width / 2) if self._pie is True else delta,
                start_angle,
                end_angle,
            )
            Gdk.cairo_set_source_rgba(
                cr,
                style_context.get_border_color(
                    Gtk.StateFlags.NORMAL,
                )
                if self._progress_color is None
                or not isinstance(self._radius_color, bool)
                else get_gdk_rgba(self._progress_color),
            )
            cr.fill() if self._pie is True else cr.stroke()
        cr.restore()
