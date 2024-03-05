import gi
import cairo
from typing import Literal
from fabric.widgets.widget import Widget
from fabric.utils import ValueEnum

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class CornerOrientation(ValueEnum):
    TOP_LEFT = 1
    TOP_RIGHT = 2
    BOTTOM_LEFT = 3
    BOTTOM_RIGHT = 4


class Corner(Gtk.DrawingArea, Widget):
    """
    a corner that can be placed on the edges of the screen.
    use the css property `background-color` to set the color of this corner
    also use the `size` argument, otherwise parent's widget size will be used
    """

    def __init__(
        self,
        orientation: Literal["top-left", "top-right", "bottom-left", "bottom-right"]
        | CornerOrientation = "top-right",
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
        """
        :param orientation: the orientation of this corner, defaults to "top-right"
        :type orientation: Literal["top-left", "top-right", "bottom-left", "bottom-right"] | CornerOrientation, optional
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
        super().__init__(
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
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        if (
            orientation is None
            or isinstance(orientation, (CornerOrientation, str)) is not True
        ):
            raise ValueError(
                "orientation must the name of the orientation or a CornerOrientation",
                f"but got {orientation}",
            )
        self.orientation = (
            orientation
            if isinstance(orientation, CornerOrientation)
            else {
                "bottom-left": CornerOrientation.BOTTOM_LEFT,
                "bottom-right": CornerOrientation.BOTTOM_RIGHT,
                "top-left": CornerOrientation.TOP_LEFT,
                "top-right": CornerOrientation.TOP_RIGHT,
            }.get(orientation.lower(), CornerOrientation.TOP_RIGHT)
        )
        self.do_connect_signals_for_kwargs(kwargs)
        self.connect("draw", self.on_draw)

    def on_draw(self, widget: "Corner", cr: cairo.Context):
        aloc: cairo.Rectangle = self.get_allocation()
        # ^ hear me out, Gtk.Allocation == Gdk.Rectangle == cairo.Rectangle
        width, height = aloc.width, aloc.height

        context: Gtk.StyleContext = self.get_style_context()
        background_color: Gdk.RGBA = context.get_background_color(Gtk.StateFlags.NORMAL)

        cr.save()

        Gdk.cairo_set_source_rgba(cr, background_color)

        # _this is fine_
        match self.orientation:
            case CornerOrientation.TOP_LEFT:
                cr.move_to(width, 0)
                cr.curve_to(0, 0, 0, height, 0, height)
                cr.line_to(0, 0)
            case CornerOrientation.TOP_RIGHT:
                cr.move_to(0, 0)
                cr.curve_to(width, 0, width, height, width, height)
                cr.line_to(width, 0)
            case CornerOrientation.BOTTOM_LEFT:
                cr.move_to(width, height)
                cr.curve_to(0, height, 0, 0, 0, 0)
                cr.line_to(0, height)
            case CornerOrientation.BOTTOM_RIGHT:
                cr.move_to(0, height)
                cr.curve_to(width, height, width, 0, width, 0)
                cr.line_to(width, height)

        cr.close_path()
        cr.fill()

        cr.restore()
        return
