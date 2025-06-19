import gi
from typing import Literal
from collections.abc import Iterable
from fabric.widgets.container import Container
from fabric.core.service import Property
from fabric.utils.helpers import get_enum_member

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Stack(Gtk.Stack, Container):
    @Property(
        Gtk.StackTransitionType,
        "read-write",
        default_value=Gtk.StackTransitionType.NONE,
        install=False,
    )
    def transition_type(self) -> Gtk.StackTransitionType:
        return self.get_transition_type()

    @transition_type.setter
    def transition_type(
        self,
        value: Literal[
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
    ):
        return self.set_transition_type(get_enum_member(Gtk.StackTransitionType, value))

    @Property(int, "read-write", install=False)
    def transition_duration(self):
        return self.get_transition_duration()

    @transition_duration.setter
    def transition_duration(self, value: int):
        return self.set_transition_duration(value)

    @Property(bool, "read-write", default_value=False, install=False)
    def interpolate_size(self):
        return self.get_interpolate_size()

    @interpolate_size.setter
    def interpolate_size(self, value: bool):
        return self.set_interpolate_size(value)

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
        | Gtk.StackTransitionType = Gtk.StackTransitionType.NONE,
        transition_duration: int = 400,
        interpolate_size: bool = False,
        children: Gtk.Widget | Iterable[Gtk.Widget] | None = None,
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
        Gtk.Stack.__init__(self)  # type: ignore
        Container.__init__(
            self,
            children,
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

        self.transition_type = transition_type
        self.transition_duration = transition_duration
        self.interpolate_size = interpolate_size
