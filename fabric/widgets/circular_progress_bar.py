import gi
import math
import cairo
from typing import Literal, Iterable
from fabric.widgets.widget import Widget
from fabric.utils.helpers import get_gdk_rgba

gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, Gtk


class CircularProgressBar(Gtk.DrawingArea, Widget):
    """a circular progress bar widget drawn with cairo"""
    def __init__(
        self,
        percentage: int = 0,
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
        :type percentage: int, optional
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
        :type size: tuple[int] | None, optional
        """
        Gtk.DrawingArea.__init__(self, **kwargs)
        if percentage < 0 or percentage > 100 or not isinstance(percentage, int):
            raise ValueError(
                f"percentage must be an integer with a value between 0 and 100",
                f"but got {percentage}",
            )
        self._line_width = line_width
        self._percentage = percentage
        self.background_color = background_color
        self.radius_color = radius_color
        self.progress_color = progress_color
        self.pie = pie
        self.angle = angle
        self.line_style = (
            line_style
            if isinstance(line_style, cairo.LineCap)
            else {
                "none": None,
                "butt": cairo.LineCap.BUTT,
                "round": cairo.LineCap.ROUND,
                "square": cairo.LineCap.SQUARE,
            }.get(line_style, cairo.LineCap.ROUND)
        )
        self.size = size
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

    @property
    def percentage(self) -> int:
        return self._percentage

    @percentage.setter
    def percentage(self, value: int):
        self._percentage = value
        return self.queue_draw()

    @property
    def line_width(self) -> int | None:
        return self._line_width

    @line_width.setter
    def line_width(self, value: int | None):
        self._line_width = value
        return self.queue_draw()

    def set_line_width(self, value: int | None):
        self.line_width = value
        return

    def set_percentage(self, value: int):
        self.percentage = value
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
        if d > self.size[0]:
            natural = d
        else:
            natural = self.size[0]
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

        cr.set_line_cap(self.line_style) if self.line_style is not None else None
        cr.set_line_width(self._line_width)

        # background fill
        if self.background_color is not False:
            cr.arc(center_x, center_y, delta + (self._line_width / 2), 0, 2 * math.pi)
            Gdk.cairo_set_source_rgba(
                cr,
                style_context.get_background_color(Gtk.StateFlags.NORMAL)
                if self.background_color is None
                or not isinstance(self.radius_color, bool)
                else get_gdk_rgba(self.background_color),
            )
            cr.fill()

        # radius
        if self.radius_color is not False:
            cr.move_to(center_x, center_y) if self.pie is True else None
            cr.arc(
                center_x,
                center_y,
                delta + (self._line_width / 2) if self.pie is True else delta,
                0,
                (2 * math.pi),
            )
            Gdk.cairo_set_source_rgba(
                cr,
                style_context.get_color(Gtk.StateFlags.NORMAL)
                if self.radius_color is None or not isinstance(self.radius_color, bool)
                else get_gdk_rgba(self.radius_color),
            )
            cr.fill() if self.pie is True else cr.stroke()

        # progress
        if (self._percentage / 100) > -1 and self.progress_color is not False:
            cr.move_to(center_x, center_y) if self.pie is True else None
            cr.arc(
                center_x,
                center_y,
                delta + (self._line_width / 2) if self.pie is True else delta,
                self.angle + (1.5 * math.pi),
                self.angle + (1.5 + (self._percentage / 100) * 2) * math.pi,
            )
            Gdk.cairo_set_source_rgba(
                cr,
                style_context.get_border_color(
                    Gtk.StateFlags.NORMAL,
                )
                if self.progress_color is None
                or not isinstance(self.radius_color, bool)
                else get_gdk_rgba(self.progress_color),
            )
            cr.fill() if self.pie is True else cr.stroke()
        cr.restore()
