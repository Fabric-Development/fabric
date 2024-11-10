import gi
from typing import Literal
from collections.abc import Iterable
from fabric.core.service import Property
from fabric.widgets.container import Container
from fabric.utils.helpers import get_enum_member

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Revealer(Gtk.Revealer, Container):
    @Property(bool, "read-write", default_value=False, install=False)
    def child_revealed(self):
        return self.get_reveal_child()

    @child_revealed.setter
    def child_revealed(self, value: bool):
        return self.set_reveal_child(value)

    @Property(bool, "readable", default_value=False)
    def fully_revealed(self):
        return self.get_child_revealed()

    @Property(
        Gtk.RevealerTransitionType,
        "read-write",
        default_value=Gtk.RevealerTransitionType.NONE,
        install=False,
    )
    def transition_type(self) -> Gtk.RevealerTransitionType:
        return self.get_transition_type()

    @transition_type.setter
    def transition_type(
        self,
        value: Literal[
            "none", "crossfade", "slide-right", "slide-left", "slide-up", "slide-down"
        ]
        | Gtk.RevealerTransitionType,
    ):
        return self.set_transition_type(
            get_enum_member(Gtk.RevealerTransitionType, value)
        )

    @Property(int, "read-write", install=False)
    def transition_duration(self):
        return self.get_transition_duration()

    @transition_duration.setter
    def transition_duration(self, value: int):
        return self.set_transition_duration(value)

    def __init__(
        self,
        child: Gtk.Widget | None = None,
        child_revealed: bool = False,
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
        | Gtk.RevealerTransitionType = Gtk.RevealerTransitionType.NONE,
        transition_duration: int = 400,
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
        Gtk.Revealer.__init__(self)  # type: ignore
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
        self.child_revealed = child_revealed
        self.transition_type = transition_type
        self.transition_duration = transition_duration

    def reveal(self):
        self.child_visible = True
        self.child_revealed = True
        return

    def unreveal(self):
        self.child_revealed = False
        return
