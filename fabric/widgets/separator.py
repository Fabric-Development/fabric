from collections.abc import Iterable
from typing import Literal

import gi
from fabric.widgets.widget import Widget
from gi.repository import Gtk

gi.require_version("Gtk", "3.0")


class GtkSeparator(Gtk.Separator, Widget):
    """A separator widget."""

    def __init__(
        self,
        name: str | None = None,
        h_align: Literal["fill", "start", "end", "center", "baseline"]
        | Gtk.Align
        | None = None,
        v_align: Literal["fill", "start", "end", "center", "baseline"]
        | Gtk.Align
        | None = None,
        h_expand: bool = False,
        v_expand: bool = False,
        tooltip_text: str | None = None,
        tooltip_markup: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_classes: Iterable[str] | str | None = None,
        **kwargs,
    ):
        Gtk.Separator.__init__(self)  # type: ignore
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
            **kwargs,
        )
