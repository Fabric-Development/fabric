import gi
from typing import Literal
from fabric.widgets.widget import Widget

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Scale(Gtk.Scale, Widget):
    def __init__(
        self,
        min: int  = 0,
        max: int  = 1,
        step: float = 0.01,
        marks: int | None = None,
        mark_text: str = "",
        digits: int | None = None,
        draw_value: bool = False,
        value_pos: Literal[
            "bottom",
            "left",
            "right",
            "top",
        ]
        | Gtk.PositionType = None,
        mark_pos: Literal [
            "bottom",
            "left",
            "right",
            "top",            
        ] 
        | Gtk.PositionType = None,
        has_origin: bool = True,
        orientation: Literal[
            "horizontal",
            "vertical",
            "h",
            "v",
        ]
        | Gtk.Orientation = None,
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
        size: tuple[int] | None = None,
        **kwargs,
    ):
        """
        :param min: the minimum value of the scale, defaults to 0
        :type min: int, optional
        :param max: the maximum value of the scale, defaults to 1
        :type max: int, optional
        :param step: the step increment (tick size) used with keyboard shortcuts, defaults to 0.01
        :type step: float, optional
        :param marks: value at which marks will be placed, must be between min and max, defaults to None
        :type marks: int | None, optional
        :param mark_text: the text to be shown at the mark defaults to empty string
        :type mark_text: str, optional
        :param digits: the number of decimal places to display, defaults to None
        :type digits: int | None, optional
        :param draw_value: whether to draw the current value, defaults to False
        :type draw_value: bool, optional
        :param value_pos: sets the position for where the value should be displayed, defaults to None
        :type value_pos: Literal["bottom", "left", "right", "top"] | Gtk.PositionType | None, optional
        :param mark_pos: sets the position of where to draw the marks, defaults to None
        :type mark_pos: Literal["bottom", "left", "right", "top"] | Gtk.PositionType | None, optional
        :param has_origin: whether the scale should have an origin, defaults to True
        :type has_origin: bool, optional
        :param orientation: the orientation of the scale, defaults to None
        :type orientation: Literal["horizontal", "vertical", "h", "v"] | Gtk.Orientation, optional
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
        _orientation = (
            orientation
            if isinstance(orientation, Gtk.Orientation)
            else {
                "horizontal": Gtk.Orientation.HORIZONTAL,
                "vertical": Gtk.Orientation.VERTICAL,
                "h": Gtk.Orientation.HORIZONTAL,
                "v": Gtk.Orientation.VERTICAL,
            }.get(orientation, Gtk.Orientation.HORIZONTAL)
        )
        _value_pos = (
            value_pos
            if isinstance(orientation, Gtk.PositionType)
            else {
                "bottom": Gtk.PositionType.BOTTOM,
                "left": Gtk.PositionType.LEFT,
                "right": Gtk.PositionType.RIGHT,
                "top": Gtk.PositionType.TOP,
            }.get(value_pos, Gtk.PositionType.BOTTOM)
        )
        _mark_pos = (
            mark_pos
            if isinstance(orientation, Gtk.PositionType)
            else {
                "bottom": Gtk.PositionType.BOTTOM,
                "left": Gtk.PositionType.LEFT,
                "right": Gtk.PositionType.RIGHT,
                "top": Gtk.PositionType.TOP,
            }.get(mark_pos, Gtk.PositionType.BOTTOM)
        )
        Gtk.Scale.__init__(
            self,
            value_pos=_value_pos,
            orientation=_orientation,
            **kwargs,
        )
        super().set_digits(digits) if digits is not None else None
        super().set_draw_value(draw_value) if draw_value is not None else None
        super().set_has_origin(has_origin) if has_origin is not None else None
        super().set_range(min, max) if min is not None and max is not None else None
        super().set_increments(step,step) if step is not None else None
        super().add_mark(marks,_mark_pos,mark_text) if marks is not None else None
        

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