import gi
from typing import Literal, overload
from collections.abc import Iterable
from fabric.widgets.widget import Widget
from fabric.utils.helpers import get_enum_member

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango


class Label(Gtk.Label, Widget):
    @overload
    def __init__(
        self,
        label: str | None = None,
        markup: None = None,
        justification: Literal[
            "left",
            "right",
            "center",
            "fill",
        ]
        | Gtk.Justification = Gtk.Justification.LEFT,
        ellipsization: Literal[
            "none",
            "start",
            "middle",
            "end",
        ]
        | Pango.EllipsizeMode = Pango.EllipsizeMode.NONE,
        chars_width: int = -1,
        max_chars_width: int = -1,
        line_wrap: Literal["word", "char", "word-char"] | Pango.WrapMode | None = None,
        angle: float = 0.0,
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
    ): ...

    @overload
    def __init__(
        self,
        label: None = None,
        markup: str | None = None,
        justification: Literal[
            "left",
            "right",
            "center",
            "fill",
        ]
        | Gtk.Justification = Gtk.Justification.LEFT,
        ellipsization: Literal[
            "none",
            "start",
            "middle",
            "end",
        ]
        | Pango.EllipsizeMode = Pango.EllipsizeMode.NONE,
        chars_width: int = -1,
        max_chars_width: int = -1,
        line_wrap: Literal["word", "char", "word-char"] | Pango.WrapMode | None = None,
        angle: float = 0.0,
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
    ): ...

    def __init__(
        self,
        label: str | None = None,
        markup: str | None = None,
        justification: Literal[
            "left",
            "right",
            "center",
            "fill",
        ]
        | Gtk.Justification = Gtk.Justification.LEFT,
        ellipsization: Literal[
            "none",
            "start",
            "middle",
            "end",
        ]
        | Pango.EllipsizeMode = Pango.EllipsizeMode.NONE,
        chars_width: int = -1,
        max_chars_width: int = -1,
        line_wrap: Literal["word", "char", "word-char"] | Pango.WrapMode | None = None,
        angle: float = 0.0,
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
        Gtk.Label.__init__(self)  # type: ignore
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
        self.set_label(label) if label is not None else None
        self.set_markup(markup) if markup is not None else None

        self.set_justify(
            get_enum_member(
                Gtk.Justification, justification, default=Gtk.Justification.LEFT
            )
        )
        self.set_ellipsize(
            get_enum_member(
                Pango.EllipsizeMode, ellipsization, default=Pango.EllipsizeMode.NONE
            )
        )

        self.set_width_chars(chars_width)
        self.set_max_width_chars(max_chars_width)
        if line_wrap is not None:
            self.set_line_wrap(True)
            self.set_line_wrap_mode(
                get_enum_member(Pango.WrapMode, line_wrap, default=Pango.WrapMode.WORD)
            )
        self.set_angle(angle)
