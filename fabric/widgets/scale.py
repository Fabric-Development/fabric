import gi
from typing import Literal, NamedTuple
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ScaleMark(NamedTuple):
    value: float | int
    text: str | None = None


class ScaleIncrements(NamedTuple):
    step: float | int = 0.01
    page: float | int = 0.01


class Scale(Gtk.Scale, Widget):
    def __init__(
        self,
        value: float | int = 0,
        min_value: float | int = 0,
        max_value: float | int = 100,
        increments: ScaleIncrements
        | tuple[float | int, float | int]
        | list[float | int, float | int]
        | float
        | int
        | None = None,
        marks: float
        | int
        | list[
            float | int | ScaleMark | list[float, str | None] | tuple[float, str | None]
        ]
        | None = None,
        marks_text: str | list[str | None] | None = None,
        draw_value: bool = False,
        digits: int | None = None,
        value_position: Literal[
            "bottom",
            "left",
            "right",
            "top",
        ]
        | Gtk.PositionType = None,
        mark_position: Literal[
            "bottom",
            "left",
            "right",
            "top",
        ]
        | Gtk.PositionType = None,
        has_origin: bool = True,
        inverted: bool = False,
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
        size: tuple[int] | int | None = None,
        **kwargs,
    ):
        """
        :param value: the current value of the scale, defaults to 0
        :type value: float | int, optional
        :param min_value: the minimum value of the scale, defaults to 0
        :type min_value: float | int, optional
        :param max_value: the maximum value of the scale, defaults to 100
        :type max_value: float | int, optional
        :param increments: the increments of the scale, you can use a tuple or list (step, page) or ScaleIncrements, or a float or int to set both the step and page with the same value, defaults to None
        :type increments: ScaleIncrements | tuple[float | int, float | int] | list[float | int, float | int] | float | int | None, optional
        :param marks: the mark(s) added to the scale, this can be a `list` of `tuple`s / `list`s (value, text) or a `list` of `ScaleMark` if it was a `list` of `tuple`s / `list`s the `marks_text` will be ignored, also this can be a `list` of `float` / `int`, if it was a `list` of `float` / `int` `marks_text` to add will be used to get the text if it was a `list` with the same length as `marks` or if it was a single `str`, if `marks_text` was `None` then no text will be added, defaults to None
        :type marks: float | int | list[float | int | ScaleMark | list[float, str | None] | tuple[float, str | None]] | None, optional
        :param marks_text: the text added to the marks, defaults to None
        :type marks_text: str | list[str | None] | None, optional
        :param draw_value: whether to draw the current value, defaults to False
        :type draw_value: bool, optional
        :param digits: the number of decimal places to display on the drawn value (if `draw_value` is True), defaults to None
        :type digits: int | None, optional
        :param value_position: sets the position for where the value should be displayed, defaults to None
        :type value_position: Literal["bottom", "left", "right", "top"] | Gtk.PositionType | None, optional
        :param mark_position: sets the position of where to draw the marks, defaults to None
        :type mark_position: Literal["bottom", "left", "right", "top"] | Gtk.PositionType | None, optional
        :param has_origin: whether the scale should have an origin, defaults to True
        :type has_origin: bool, optional
        :param inverted: whether the scale should be inverted/flipped, defaults to False
        :type inverted: bool, optional
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
        :type size: tuple[int] | int | None, optional
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
        _value_position = (
            value_position
            if isinstance(orientation, Gtk.PositionType)
            else {
                "bottom": Gtk.PositionType.BOTTOM,
                "left": Gtk.PositionType.LEFT,
                "right": Gtk.PositionType.RIGHT,
                "top": Gtk.PositionType.TOP,
            }.get(value_position, Gtk.PositionType.BOTTOM)
        )
        _mark_position = (
            mark_position
            if isinstance(orientation, Gtk.PositionType)
            else {
                "bottom": Gtk.PositionType.BOTTOM,
                "left": Gtk.PositionType.LEFT,
                "right": Gtk.PositionType.RIGHT,
                "top": Gtk.PositionType.TOP,
            }.get(mark_position, Gtk.PositionType.BOTTOM)
        )
        Gtk.Scale.__init__(
            self,
            value_pos=_value_position,
            orientation=_orientation,
            inverted=inverted,
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
        super().set_digits(digits) if digits is not None else None
        super().set_draw_value(draw_value) if draw_value is not None else None
        super().set_has_origin(has_origin) if has_origin is not None else None
        super().set_range(
            min_value if min_value is not None else 0,
            max_value if max_value is not None else 100,
        )
        super().set_increments(
            *(
                increments
                if isinstance(increments, (tuple, list)) and len(increments) == 2
                else (increments, increments)
                if isinstance(increments, float)
                else (0.01, 0.01)
            )
        ) if increments is not None else None
        if marks is not None:
            if isinstance(marks, (tuple, list)) and all(
                isinstance(mark, (tuple, list)) and len(mark) == 2 for mark in marks
            ):
                for mark in marks:
                    super().add_mark(
                        mark[0], _mark_position, mark[1]
                    )  # all good (i guess)
            elif (
                isinstance(marks, (tuple, list))
                and all(isinstance(mark, (int, float)) for mark in marks)
                and isinstance(marks_text, (tuple, list)) is True
                and len(marks) == len(marks_text)
            ):
                for mark, mark_text in zip(marks, marks_text):
                    super().add_mark(mark, _mark_position, mark_text)
            elif isinstance(marks, (tuple, list)) and all(
                isinstance(mark, (int, float)) for mark in marks
            ):
                for mark in marks:
                    super().add_mark(mark, _mark_position, marks_text)
            elif isinstance(marks, (int, float)):
                super().add_mark(marks, _mark_position, marks)

        super().set_value(value) if value is not None else None
        super().do_connect_signals_for_kwargs(kwargs)
