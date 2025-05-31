import gi
from collections.abc import Iterable
from typing import Literal, NamedTuple
from fabric.widgets.widget import Widget
from fabric.core.service import Property
from fabric.utils.helpers import get_enum_member

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


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
    def value(self) -> float:
        return self.get_value()

    @value.setter
    def value(self, value: float):
        return self.set_value(value)

    @Property(float, "read-write", default_value=0.0)
    def min_value(self) -> float:
        return self._min_value

    @min_value.setter
    def min_value(self, value: float):
        self._min_value = value
        return self.set_range(self._min_value, self._max_value)

    @Property(float, "read-write", default_value=1.0)
    def max_value(self) -> float:
        return self._max_value

    @max_value.setter
    def max_value(self, value: float):
        self._max_value = value
        return self.set_range(self._min_value, self._max_value)

    def __init__(
        self,
        value: float = 0.0,
        min_value: float = 0.0,
        max_value: float = 1.0,
        draw_value: bool = False,
        value_position: Literal["left", "right", "top", "bottom"]
        | Gtk.PositionType = Gtk.PositionType.TOP,
        orientation: Literal[
            "horizontal",
            "vertical",
            "h",
            "v",
        ]
        | Gtk.Orientation = Gtk.Orientation.HORIZONTAL,
        increments: tuple[float, float] | None = None,
        marks: Iterable[ScaleMark] | None = None,
        digits: int = 1,
        inverted: bool = False,
        has_origin: bool = True,
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
        Gtk.Scale.__init__(self)  # type: ignore
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

        self._min_value: float = 0
        self._max_value: float = 1.0

        self.max_value = max_value
        self.min_value = min_value
        self.value = value

        self.set_orientation(
            get_enum_member(
                Gtk.Orientation,
                orientation,
                {"v": "vertical", "h": "horizontal"},
                default=Gtk.Orientation.HORIZONTAL,
            )
        )
        self.set_draw_value(draw_value)
        self.set_value_pos(
            get_enum_member(
                Gtk.PositionType, value_position, default=Gtk.PositionType.TOP
            )
        )
        if increments is not None:
            self.set_increments(increments[0], increments[1])
        for mark in marks or ():
            self.add_mark(
                mark[0],
                get_enum_member(
                    Gtk.PositionType, mark[2], default=Gtk.PositionType.TOP
                ),
                mark[1],
            )
        self.set_digits(digits)
        self.set_inverted(inverted)
        self.set_has_origin(has_origin)
