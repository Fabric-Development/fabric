import gi
from collections.abc import Iterable
from typing import Literal, NamedTuple
from fabric.widgets.widget import Widget
from fabric.core.service import Property

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ScaleIncrements(NamedTuple):
    step: float
    "space between increments"
    page: float | None = None
    "space between increments (for the page keys in the keyboard), if set to None then use `step`'s value"


class ScaleMark(NamedTuple):
    value: float
    markup: str | None = None
    position: (
        Literal[
            "bottom",
            "left",
            "right",
            "top",
        ]
        | Gtk.PositionType
    ) = Gtk.PositionType.RIGHT


class Scale(Gtk.Scale, Widget):
    @Property(float, "read-write", install=False)
    def value(self):
        return self.get_value()

    @value.setter
    def value(self, value: float):
        return self.set_value(value)

    def __init__(
        self,
        value: float = 0.0,
        min_value: float = 0.0,
        max_value: float = 1.0,
        value_position: Literal["left", "right", "top", "bottom"]
        | Gtk.PositionType = Gtk.PositionType.TOP,
        increments: ScaleIncrements | tuple[float, float | None] | None = None,
        draw_value: bool = True,
        digits: int = 1,
        marks: Iterable[ScaleMark] | None = None,
        has_origin: bool = True,
        inverted: bool = False,
        orientation: Literal[
            "horizontal",
            "vertical",
            "h",
            "v",
        ]
        | Gtk.Orientation = Gtk.Orientation.HORIZONTAL,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
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
        Gtk.Scale.__init__(self)  # type: ignore
        Widget.__init__(
            self,
            name,
            visible,
            all_visible,
            style,
            tooltip_text,
            tooltip_markup,
            h_align,
            v_align,
            h_expand,
            v_expand,
            size,
            **kwargs,
        )


Scale(increments=(0.1, 0.1))

# class Scale(Gtk.Scale, Widget):
#     def __init__(
#         self,
#         value: float = 0.0,
#         min_value: float = 0.0,
#         max_value: float = 1.0,
#         value_position: Literal["left", "right", "top", "bottom"]
#         | Gtk.PositionType = Gtk.PositionType.TOP,
#         increments: ScaleIncrements | None = None,
#         draw_value: bool = True,
#         digits: int = 1,
#         marks: Iterable[ScaleMark] | None = None,
#         has_origin: bool = True,
#         inverted: bool = False,
#         orientation: Literal[
#             "horizontal",
#             "vertical",
#             "h",
#             "v",
#         ]
#         | Gtk.Orientation = Gtk.Orientation.HORIZONTAL,
#         visible: bool = True,
#         all_visible: bool = False,
#         style: str | None = None,
#         style_compiled: bool = True,
#         style_append: bool = False,
#         style_add_brackets: bool = True,
#         tooltip_text: str | None = None,
#         tooltip_markup: str | None = None,
#         h_align: Literal["fill", "start", "end", "center", "baseline"]
#         | Gtk.Align
#         | None = None,
#         v_align: Literal["fill", "start", "end", "center", "baseline"]
#         | Gtk.Align
#         | None = None,
#         h_expand: bool = False,
#         v_expand: bool = False,
#         name: str | None = None,
#         size: tuple[int] | int | None = None,
#         **kwargs,
#     ):
#         _orientation = (
#             orientation
#             if isinstance(orientation, Gtk.Orientation)
#             else {
#                 "horizontal": Gtk.Orientation.HORIZONTAL,
#                 "vertical": Gtk.Orientation.VERTICAL,
#                 "h": Gtk.Orientation.HORIZONTAL,
#                 "v": Gtk.Orientation.VERTICAL,
#             }.get(orientation, Gtk.Orientation.HORIZONTAL)
#         )
#         _value_position = (
#             value_position
#             if isinstance(orientation, Gtk.PositionType)
#             else {
#                 "bottom": Gtk.PositionType.BOTTOM,
#                 "left": Gtk.PositionType.LEFT,
#                 "right": Gtk.PositionType.RIGHT,
#                 "top": Gtk.PositionType.TOP,
#             }.get(value_position, Gtk.PositionType.BOTTOM)
#         )
#         _mark_position = (
#             mark_position
#             if isinstance(orientation, Gtk.PositionType)
#             else {
#                 "bottom": Gtk.PositionType.BOTTOM,
#                 "left": Gtk.PositionType.LEFT,
#                 "right": Gtk.PositionType.RIGHT,
#                 "top": Gtk.PositionType.TOP,
#             }.get(mark_position, Gtk.PositionType.BOTTOM)
#         )
#         Gtk.Scale.__init__(
#             self,
#             value_pos=_value_position,
#             orientation=_orientation,
#             inverted=inverted,
#             **(self.do_get_filtered_kwargs(kwargs)),
#         )
#         Widget.__init__(
#             self,
#             visible,
#             all_visible,
#             style,
#             style_compiled,
#             style_append,
#             style_add_brackets,
#             tooltip_text,
#             tooltip_markup,
#             h_align,
#             v_align,
#             h_expand,
#             v_expand,
#             name,
#             size,
#         )
#         super().set_digits(digits) if digits is not None else None
#         super().set_draw_value(draw_value) if draw_value is not None else None
#         super().set_has_origin(has_origin) if has_origin is not None else None
#         super().set_range(
#             min_value if min_value is not None else 0,
#             max_value if max_value is not None else 100,
#         )
#         super().set_increments(
#             *(
#                 increments
#                 if isinstance(increments, (tuple, list)) and len(increments) == 2
#                 else (increments, increments)
#                 if isinstance(increments, float)
#                 else (0.01, 0.01)
#             )
#         ) if increments is not None else None
#         if marks is not None:
#             if isinstance(marks, (tuple, list)) and all(
#                 isinstance(mark, (tuple, list)) and len(mark) == 2 for mark in marks
#             ):
#                 for mark in marks:
#                     super().add_mark(
#                         mark[0], _mark_position, mark[1]
#                     )  # all good (i guess)
#             elif (
#                 isinstance(marks, (tuple, list))
#                 and all(isinstance(mark, (int, float)) for mark in marks)
#                 and isinstance(marks_text, (tuple, list)) is True
#                 and len(marks) == len(marks_text)
#             ):
#                 for mark, mark_text in zip(marks, marks_text):
#                     super().add_mark(mark, _mark_position, mark_text)
#             elif isinstance(marks, (tuple, list)) and all(
#                 isinstance(mark, (int, float)) for mark in marks
#             ):
#                 for mark in marks:
#                     super().add_mark(mark, _mark_position, marks_text)
#             elif isinstance(marks, (int, float)):
#                 super().add_mark(marks, _mark_position, marks)

#         super().set_value(value) if value is not None else None
#         super().do_connect_signals_for_kwargs(kwargs)
