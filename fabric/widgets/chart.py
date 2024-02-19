# FIXME: broky
import gi
import cairo
from typing import Literal
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk, Gdk


class Chart(Gtk.DrawingArea, Widget):
    """
    A Chart widget drawn with cairo
    NOTE: uncomplete
    """

    def __init__(
        self,
        update_interval: int,
        data_function,
        margin: int = 1,
        data_count: int = 15,
        frame: bool = False,
        line_width: int = 1,
        line_color: tuple = (1, 1, 1, 1),
        fill_color: tuple = (0, 0, 1, 0.2),
        background_color: tuple = (0, 0, 0, 0),
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
        size: tuple[int, int] | None = (24, 24),
        **kwargs,
    ):
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
        self.margin = margin
        self.data_count = data_count
        self.frame = frame
        self.line_width = line_width
        self.line_color = line_color
        self.fill_color = fill_color
        self.background_color = background_color
        self.update_interval = update_interval
        self.data_function = data_function
        self.data = []
        self.timer = GLib.timeout_add(update_interval, self.update_chart)
        self.do_connect_signals_for_kwargs(kwargs)

    def get_update_interval(self) -> int:
        return self.update_interval

    def set_update_interval(self, update_interval: int) -> int:
        x = GLib.source_remove(self.timer) if self.timer is not None else None
        self.timer = GLib.timeout_add(update_interval, self.update_chart)
        return x

    def do_draw(self, cr: cairo.Context):
        style_context = self.get_style_context()
        allocation = self.get_allocation()
        width = allocation.width
        height = allocation.height

        chart_width = width - 2 * self.margin
        chart_height = height - 2 * self.margin
        chart_x = self.margin
        chart_y = self.margin

        Gdk.cairo_set_source_rgba(
            cr,
            style_context.get_background_color(Gtk.StateFlags.NORMAL),
        )
        cr.paint()

        cr.set_line_width(
            style_context.get_border(Gtk.StateFlags.NORMAL).top,
        )

        if len(self.data) > 1:
            # fill color
            Gdk.cairo_set_source_rgba(
                cr,
                style_context.get_color(Gtk.StateFlags.NORMAL),
            )
            cr.move_to(
                chart_x, chart_y + chart_height - (self.data[0] * chart_height / 100)
            )
            for i, value in enumerate(self.data):
                x = chart_x + chart_width * i / (len(self.data) - 1)
                y = chart_y + chart_height - (value * chart_height / 100)
                cr.line_to(x, y)
            cr.line_to(chart_x + chart_width, chart_y + chart_height)
            cr.line_to(chart_x, chart_y + chart_height)
            cr.close_path()
            cr.fill()

            # line color
            Gdk.cairo_set_source_rgba(
                cr,
                style_context.get_border_color(
                    Gtk.StateFlags.NORMAL,
                ),
            )
            cr.move_to(
                chart_x, chart_y + chart_height - (self.data[0] * chart_height / 100)
            )
            for i, value in enumerate(self.data):
                x = chart_x + chart_width * i / (len(self.data) - 1)
                y = chart_y + chart_height - (value * chart_height / 100)
                cr.line_to(x, y)
            cr.stroke()

        if self.frame:
            cr.set_source_rgba(*self.line_color)
            cr.rectangle(chart_x, chart_y, chart_width, chart_height)
            cr.stroke()

    def update_chart(self):
        new_data_point = self.data_function()
        self.data.append(new_data_point)
        if len(self.data) > self.data_count:
            self.data = self.data[-self.data_count :]
        self.queue_draw()
        return True
