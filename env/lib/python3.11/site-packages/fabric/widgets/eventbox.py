import gi
from typing import Literal, Iterable
from fabric.widgets.container import Container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class EventBox(Gtk.EventBox, Container):
    def __init__(
        self,
        events: Literal[
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
        | Gdk.EventMask
        | Iterable[
            Literal[
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
        ]  # FIXME: idk what to do so i can get a proper typevar
        | Iterable[Gdk.EventMask]
        | None = None,
        children: Gtk.Widget | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_compiled: bool = True,
        style_append: bool = False,
        style_add_brackets: bool = True,
        name: str | None = None,
        size: tuple[int] | None = None,
        **kwargs,
    ):
        Gtk.EventBox.__init__(
            self,
            **kwargs,
        )
        self.add_events(events) if events is not None else None
        super().add(children) if children is not None else None
        Container.__init__(
            self,
            None,
            visible,
            all_visible,
            style,
            style_compiled,
            style_append,
            style_add_brackets,
            name,
            size,
        )

    def add_events(
        self,
        events: Literal[
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
        | Gdk.EventMask
        | Iterable[
            Literal[
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
        ]
        | Iterable[Gdk.EventMask],
    ):
        events = [events] if not isinstance(events, (list, tuple)) else events
        for event in events:
            if isinstance(event, str):
                event = {
                    "exposure": Gdk.EventMask.EXPOSURE_MASK,
                    "pointer-motion": Gdk.EventMask.POINTER_MOTION_MASK,
                    "pointer-motion-hint": Gdk.EventMask.POINTER_MOTION_HINT_MASK,
                    "button-motion": Gdk.EventMask.BUTTON_MOTION_MASK,
                    "button-1-motion": Gdk.EventMask.BUTTON1_MOTION_MASK,
                    "button-2-motion": Gdk.EventMask.BUTTON2_MOTION_MASK,
                    "button-3-motion": Gdk.EventMask.BUTTON3_MOTION_MASK,
                    "button-press": Gdk.EventMask.BUTTON_PRESS_MASK,
                    "button-release": Gdk.EventMask.BUTTON_RELEASE_MASK,
                    "key-press": Gdk.EventMask.KEY_PRESS_MASK,
                    "key-release": Gdk.EventMask.KEY_RELEASE_MASK,
                    "enter-notify": Gdk.EventMask.ENTER_NOTIFY_MASK,
                    "leave-notify": Gdk.EventMask.LEAVE_NOTIFY_MASK,
                    "focus-change": Gdk.EventMask.FOCUS_CHANGE_MASK,
                    "structure": Gdk.EventMask.STRUCTURE_MASK,
                    "property-change": Gdk.EventMask.PROPERTY_CHANGE_MASK,
                    "visibility-notify": Gdk.EventMask.VISIBILITY_NOTIFY_MASK,
                    "proximity-in": Gdk.EventMask.PROXIMITY_IN_MASK,
                    "proximity-out": Gdk.EventMask.PROXIMITY_OUT_MASK,
                    "substructure": Gdk.EventMask.SUBSTRUCTURE_MASK,
                    "scroll": Gdk.EventMask.SCROLL_MASK,
                    "touch": Gdk.EventMask.TOUCH_MASK,
                    "smooth-scroll": Gdk.EventMask.SMOOTH_SCROLL_MASK,
                    "touchpad-gesture": Gdk.EventMask.TOUCHPAD_GESTURE_MASK,
                    "tablet-pad": Gdk.EventMask.TABLET_PAD_MASK,
                    "all": Gdk.EventMask.ALL_EVENTS_MASK,
                }.get(event, None)  # FIXME: use getattr instead.
                super().add_events(event) if event is not None else None
            elif isinstance(event, int):
                super().add_events(event)
            elif isinstance(event, Gdk.EventMask):
                super().add_events(event)
        return
