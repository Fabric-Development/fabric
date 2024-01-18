import gi
from typing import Literal
from fabric.widgets.container import Container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Stack(Gtk.Stack, Container):
    def __init__(
        self,
        transition_type: Literal[
            "none",
            "crossfade",
            "slide-right",
            "slide-left",
            "slide-up",
            "slide-down",
            "slide-left-right",
            "slide-up-down",
            "over-up",
            "over-down",
            "over-left",
            "over-right",
            "under-up",
            "under-down",
            "under-left",
            "under-right",
            "over-up-down",
            "over-down-up",
            "over-left-right",
            "over-right-left",
        ]
        | Gtk.StackTransitionType
        | None = None,
        transition_duration: int | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_compiled: bool = True,
        style_append: bool = False,
        style_add_brackets: bool = True,
        name: str | None = None,
        size: tuple[int] | None = None,
        **kwargs,
    ) -> None:
        Gtk.Stack.__init__(self, **kwargs)
        self.set_transition_type(
            transition_type
        ) if transition_type is not None else None
        self.set_transition_duration(
            transition_duration
        ) if transition_duration is not None else None
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

    def set_transition_type(
        self,
        transition: Literal[
            "none",
            "crossfade",
            "slide-right",
            "slide-left",
            "slide-up",
            "slide-down",
            "slide-left-right",
            "slide-up-down",
            "over-up",
            "over-down",
            "over-left",
            "over-right",
            "under-up",
            "under-down",
            "under-left",
            "under-right",
            "over-up-down",
            "over-down-up",
            "over-left-right",
            "over-right-left",
        ]
        | Gtk.StackTransitionType,
    ) -> None:
        return super().set_transition_type(
            transition
            if isinstance(transition, Gtk.StackTransitionType)
            else {
                "none": Gtk.StackTransitionType.NONE,
                "crossfade": Gtk.StackTransitionType.CROSSFADE,
                "slide-right": Gtk.StackTransitionType.SLIDE_RIGHT,
                "slide-left": Gtk.StackTransitionType.SLIDE_LEFT,
                "slide-up": Gtk.StackTransitionType.SLIDE_UP,
                "slide-down": Gtk.StackTransitionType.SLIDE_DOWN,
                "slide-left-right": Gtk.StackTransitionType.SLIDE_LEFT_RIGHT,
                "slide-up-down": Gtk.StackTransitionType.SLIDE_UP_DOWN,
                "over-up": Gtk.StackTransitionType.OVER_UP,
                "over-down": Gtk.StackTransitionType.OVER_DOWN,
                "over-left": Gtk.StackTransitionType.OVER_LEFT,
                "over-right": Gtk.StackTransitionType.OVER_RIGHT,
                "under-up": Gtk.StackTransitionType.UNDER_UP,
                "under-down": Gtk.StackTransitionType.UNDER_DOWN,
                "under-left": Gtk.StackTransitionType.UNDER_LEFT,
                "under-right": Gtk.StackTransitionType.UNDER_RIGHT,
                "over-up-down": Gtk.StackTransitionType.OVER_UP_DOWN,
                "over-down-up": Gtk.StackTransitionType.OVER_DOWN_UP,
                "over-left-right": Gtk.StackTransitionType.OVER_LEFT_RIGHT,
                "over-right-left": Gtk.StackTransitionType.OVER_RIGHT_LEFT,
                # NOTE: GTK 4.0 only
                # "rotate-left": Gtk.StackTransitionType.ROTATE_LEFT,
                # "rotate-right": Gtk.StackTransitionType.ROTATE_RIGHT,
                # "rotate-left-right": Gtk.StackTransitionType.ROTATE_LEFT_RIGHT,
            }.get(transition, Gtk.StackTransitionType.NONE)
        )
