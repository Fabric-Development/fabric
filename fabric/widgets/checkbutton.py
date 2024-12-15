import gi
from typing import Literal
from collections.abc import Iterable

# from fabric.widgets.container import Container
from fabric.widgets.button import Button

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class CheckButton(Gtk.CheckButton, Button):
    def __init__(
        self,
        label: str | None = None,
        child: Gtk.Widget | None = None,
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
        Gtk.CheckButton.__init__(self)  # type: ignore
        Button.__init__(
            self,
            None,
            name,
            None,
            None,
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
        self.add(child) if child is not None else None
