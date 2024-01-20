import gi
from typing import Literal
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Entry(Gtk.Entry, Widget):
    def __init__(
        self,
        text: str | None = None,
        placeholder_text: str | None = None,
        editable: bool = True,
        characters_visible: bool = True,
        max_length: int | None = None,
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
        Gtk.Entry.__init__(self, **kwargs)
        self.set_text(text) if text is not None else None
        self.set_placeholder_text(
            placeholder_text
        ) if placeholder_text is not None else None
        self.set_max_length(max_length) if max_length is not None else None
        self.set_editable(editable)
        self.set_visibility(characters_visible)
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
