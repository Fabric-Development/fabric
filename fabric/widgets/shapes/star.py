import gi
import math
import cairo
from typing import Literal
from collections.abc import Iterable
from fabric.core.service import Property
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class Star(Gtk.DrawingArea, Widget):
    @staticmethod
    def render_shape(
        cr: cairo.Context,
        width: float,
        height: float,
        points: int = 5,
        ratio: float = 0.5,
    ):
        a = 2 * math.pi / points
        s = min(width, height) / 2
        rs = s * ratio

        cr.save()

        cr.translate(width / 2, height / 2)
        cr.rotate(-math.pi / 2)

        for i in range(points):
            cr.line_to(s * math.cos(i * a), s * math.sin(i * a))
            cr.line_to(rs * math.cos((i + 0.5) * a), rs * math.sin((i + 0.5) * a))

        cr.close_path()
        cr.restore()
        return

    @Property(int, "read-write")
    def points(self) -> int:
        return self._points

    @points.setter
    def points(self, value: int):
        self._points = value
        return self.queue_draw()

    @Property(float, "read-write")
    def ratio(self) -> float:
        return self._ratio

    @ratio.setter
    def ratio(self, value: float):
        self._ratio = value
        return self.queue_draw()

    def __init__(
        self,
        points: int = 5,
        ratio: float = 0.5,
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
        self._points = points
        self._ratio = ratio

        self.connect("draw", self.on_draw)

    def on_draw(self, _, cr: cairo.Context):
        aloc: cairo.Rectangle = self.get_allocation()  # type: ignore
        width, height = aloc.width, aloc.height

        state = self.get_state_flags()
        context: Gtk.StyleContext = self.get_style_context()
        border_color: Gdk.RGBA = context.get_border_color(state)  # type: ignore
        border_width = (
            max(
                (border := context.get_border(state)).top,  # type: ignore
                border.bottom,  # type: ignore
                border.left,  # type: ignore
                border.right,  # type: ignore
            )
            * 2
        )

        cr.save()

        # render the background
        self.render_shape(cr, width, height, self._points, self._ratio)
        cr.clip()
        Gtk.render_background(context, cr, 0, 0, width, height)

        if border_width:
            # put the border
            Gdk.cairo_set_source_rgba(cr, border_color)  # type: ignore
            cr.set_line_width(border_width)
            self.render_shape(cr, width, height, self._points, self._ratio)
            cr.stroke()

        cr.restore()
        return
