import gi
from typing import Literal
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango


class Label(Gtk.Label, Widget):
    def __init__(
        self,
        label: str | None = None,
        justfication: Literal[
            "left",
            "right",
            "center",
            "fill",
        ]
        | Gtk.Justification
        | None = None,
        ellipsization: Literal[
            "none",
            "start",
            "middle",
            "end",
        ]
        | Pango.EllipsizeMode
        | None = None,
        character_max_width: int | None = None,
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
        Gtk.Label.__init__(self, **kwargs)
        self.set_label(label) if label is not None else None
        self.set_justify(
            {
                "left": Gtk.Justification.LEFT,
                "right": Gtk.Justification.RIGHT,
                "center": Gtk.Justification.CENTER,
                "fill": Gtk.Justification.FILL,
            }.get(justfication.lower(), Gtk.Justification.LEFT)
        ) if justfication is not None else None
        self.set_ellipsize(
            {
                "none": Pango.EllipsizeMode.NONE,
                "start": Pango.EllipsizeMode.START,
                "middle": Pango.EllipsizeMode.MIDDLE,
                "end": Pango.EllipsizeMode.END,
            }.get(ellipsization.lower(), Pango.EllipsizeMode.NONE)
        ) if ellipsization is not None else None
        self.set_max_width_chars(
            character_max_width
        ) if character_max_width is not None else None
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
