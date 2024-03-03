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
        size: tuple[int] | int | None = None,
        **kwargs,
    ):
        """
        :param events: the events to add, defaults to None
        :param children: the children of the widget (a single widget), defaults to None
        :type children: Gtk.Widget | None, optional
        :param visible: whether the widget is initially visible, defaults to True
        :type visible: bool, optional
        :param all_visible: whether all child widgets are initially visible, defaults to False
        :type all_visible: bool, optional
        :param style: inline css style string, defaults to None
        :type style: str | None, optional
        :param style_compiled: whether the passed css should get compiled before applying, defaults to True
        :type style_compiled: bool, optional
        :param style_append: whether the passed css should be appended to the existing css, defaults to False
        :type style_append: bool, optional
        :param style_add_brackets: whether the passed css should be wrapped in brackets if they were missing, defaults to True
        :type style_add_brackets: bool, optional
        :param tooltip_text: the text added to the tooltip, defaults to None
        :type tooltip_text: str | None, optional
        :param tooltip_markup: the markup added to the tooltip, defaults to None
        :type tooltip_markup: str | None, optional
        :param h_align: the horizontal alignment, defaults to None
        :type h_align: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None, optional
        :param v_align: the vertical alignment, defaults to None
        :type v_align: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None, optional
        :param h_expand: the horizontal expansion, defaults to False
        :type h_expand: bool, optional
        :param v_expand: the vertical expansion, defaults to False
        :type v_expand: bool, optional
        :param name: the name of the widget it can be used to style the widget, defaults to None
        :type name: str | None, optional
        :param size: the size of the widget, defaults to None
        :type size: tuple[int] | int | None, optional
        """
        Gtk.EventBox.__init__(
            self,
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        Container.__init__(
            self,
            None,
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
        super().add(children) if children is not None else None
        self.add_events(events) if events is not None else None
        self.do_connect_signals_for_kwargs(kwargs)

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
