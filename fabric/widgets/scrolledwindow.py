import gi
from typing import Literal
from collections.abc import Iterable
from fabric.widgets.container import Container
from fabric.core.service import Property
from fabric.utils.helpers import get_enum_member

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ScrolledWindow(Gtk.ScrolledWindow, Container):
    @Property(tuple[int, int], "read-write")
    def min_content_size(self):
        return self.get_min_content_width(), self.get_min_content_height()

    @min_content_size.setter
    def min_content_size(self, value: Iterable[int]):
        if isinstance(value, (tuple, list)) and len(value) == 2:
            self.set_min_content_width(value[0])
            self.set_min_content_height(value[1])
            return
        raise ValueError(
            "the size must be tuple or a list with two values, (width, height)"
        )

    @Property(tuple[int, int], "read-write")
    def max_content_size(self):
        return self.get_max_content_width(), self.get_max_content_height()

    @max_content_size.setter
    def max_content_size(self, value: Iterable[int]):
        if isinstance(value, (tuple, list)) and len(value) == 2:
            self.set_max_content_width(value[0])
            self.set_max_content_height(value[1])
            return
        raise ValueError(
            "the size must be tuple or a list with two values, (width, height)"
        )

    def __init__(
        self,
        min_content_size: Iterable[int] = (-1, -1),
        max_content_size: Iterable[int] = (-1, -1),
        propagate_width: bool = True,
        propagate_height: bool = True,
        kinetic_scroll: bool = False,
        overlay_scroll: bool = False,
        h_scrollbar_policy: Literal[
            "always",
            "automatic",
            "never",
            "external",
        ]
        | Gtk.PolicyType = Gtk.PolicyType.AUTOMATIC,
        v_scrollbar_policy: Literal[
            "always",
            "automatic",
            "never",
            "external",
        ]
        | Gtk.PolicyType = Gtk.PolicyType.AUTOMATIC,
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
        Gtk.ScrolledWindow.__init__(self)  # type: ignore
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

        self.min_content_size = min_content_size
        self.max_content_size = max_content_size
        self.set_propagate_natural_width(propagate_width)
        self.set_propagate_natural_height(propagate_height)
        self.set_kinetic_scrolling(kinetic_scroll)
        self.set_overlay_scrolling(overlay_scroll)
        self.set_policy(
            get_enum_member(
                Gtk.PolicyType, h_scrollbar_policy, default=Gtk.PolicyType.AUTOMATIC
            ),
            get_enum_member(
                Gtk.PolicyType, v_scrollbar_policy, default=Gtk.PolicyType.AUTOMATIC
            ),
        )
