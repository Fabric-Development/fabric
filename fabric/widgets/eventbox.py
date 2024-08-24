import gi
from typing import Literal
from collections.abc import Iterable
from fabric.widgets.container import Container
from fabric.utils.helpers import get_enum_member

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

EVENT_TYPE = Literal[
    "exposure",
    "pointer-motion",
    "pointer-motion-hint",
    "button-motion",
    "button-1-motion",
    "button-2-motion",
    "button-3-motion",
    "button-press",
    "button-release",
    "key-press",
    "key-release",
    "enter-notify",
    "leave-notify",
    "focus-change",
    "structure",
    "property-change",
    "visibility-notify",
    "proximity-in",
    "proximity-out",
    "substructure",
    "scroll",
    "touch",
    "smooth-scroll",
    "touchpad-gesture",
    "tablet-pad",
    "all",
]


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

    def add_events(
        self, events: EVENT_TYPE | Gdk.EventMask | Iterable[EVENT_TYPE | Gdk.EventMask]
    ):
        _events: int = 0
        events_map: dict[str, str] = {
            x: (x if x != "all" else "all-events") + "-mask"
            for x in EVENT_TYPE.__args__
        }
        for event in (events,) if not isinstance(events, (tuple, list)) else events:
            _events |= get_enum_member(Gdk.EventMask, event, events_map, 0)  # type: ignore
        return super().add_events(_events)
