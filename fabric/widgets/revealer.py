import gi
from typing import Literal
from fabric.widgets.container import Container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Revealer(Gtk.Revealer, Container):
    def __init__(
        self,
        children: Gtk.Widget | None = None,
        child_visible: bool | None = None,
        reveal_child: bool | None = None,
        transition_duration: int | None = None,
        transition_type: Literal[
            "none",
            "crossfade",
            "slide-right",
            "slide-left",
            "slide-up",
            "slide-down",
            # "swing-right",
            # "swing-left",
            # "swing-up",
            # "swing-down",
        ]
        | Gtk.RevealerTransitionType
        | None = None,
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
    ) -> None:
        Gtk.Revealer.__init__(
            self,
            **kwargs,
        )
        self.add(children) if children is not None else None
        self.set_transition_type(
            transition_type
        ) if transition_type is not None else None
        self.set_child_visible(child_visible) if child_visible is not None else None
        self.set_reveal_child(reveal_child) if reveal_child is not None else None
        self.set_transition_duration(
            transition_duration
        ) if transition_duration is not None else None
        Container.__init__(
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

    def set_transition_type(
        self,
        transition: Literal[
            "none",
            "crossfade",
            "slide-right",
            "slide-left",
            "slide-up",
            "slide-down",
            # "swing-right",
            # "swing-left",
            # "swing-up",
            # "swing-down",
        ]
        | Gtk.RevealerTransitionType,
    ) -> None:
        return super().set_transition_type(
            transition
            if isinstance(transition, Gtk.RevealerTransitionType)
            else {
                "none": Gtk.RevealerTransitionType.NONE,
                "crossfade": Gtk.RevealerTransitionType.CROSSFADE,
                "slide-right": Gtk.RevealerTransitionType.SLIDE_RIGHT,
                "slide-left": Gtk.RevealerTransitionType.SLIDE_LEFT,
                "slide-up": Gtk.RevealerTransitionType.SLIDE_UP,
                "slide-down": Gtk.RevealerTransitionType.SLIDE_DOWN,
                # NOTE: GTK 4.0 only
                # "swing-right": Gtk.RevealerTransitionType.SWING_RIGHT,
                # "swing-left": Gtk.RevealerTransitionType.SWING_LEFT,
                # "swing-up": Gtk.RevealerTransitionType.SWING_UP,
                # "swing-down": Gtk.RevealerTransitionType.SWING_DOWN,
            }.get(transition, Gtk.RevealerTransitionType.NONE),
        )
