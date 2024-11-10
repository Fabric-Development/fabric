import gi
from typing import Literal
from collections.abc import Iterable
from fabric.widgets.widget import EVENT_TYPE
from fabric.widgets.container import Container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class EventBox(Gtk.EventBox, Container):
    def __init__(
        self,
        events: EVENT_TYPE
        | Gdk.EventMask
        | Iterable[EVENT_TYPE | Gdk.EventMask]
        | None = None,
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
        Gtk.EventBox.__init__(self)  # type: ignore
        Container.__init__(
            self,
            child,
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
        self.add_events(events) if events is not None else None
