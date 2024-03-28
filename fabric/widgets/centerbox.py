import gi
from typing import Literal
from fabric.widgets.box import Box

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class CenterBox(Box):
    """
    a box that can hold widgets in the center, start, and end, useful for creating bars

    NOTE: this should be the ONLY widget placed in it's parent contianer.
    """

    def __init__(
        self,
        start_children: list[Gtk.Widget] | Gtk.Widget | None = None,
        center_children: list[Gtk.Widget] | Gtk.Widget | None = None,
        end_children: list[Gtk.Widget] | Gtk.Widget | None = None,
        spacing: int | None = None,
        orientation: Literal[
            "horizontal",
            "vertical",
            "h",
            "v",
        ]
        | Gtk.Orientation = None,
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
        orientation = (
            orientation
            if isinstance(orientation, Gtk.Orientation)
            else {
                "horizontal": Gtk.Orientation.HORIZONTAL,
                "vertical": Gtk.Orientation.VERTICAL,
                "h": Gtk.Orientation.HORIZONTAL,
                "v": Gtk.Orientation.VERTICAL,
            }.get(orientation, Gtk.Orientation.HORIZONTAL)
        )
        super().__init__(
            spacing,
            "h" if orientation == Gtk.Orientation.VERTICAL else "v",
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
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        self._container = Box(
            orientation="v" if orientation == Gtk.Orientation.VERTICAL else "h",
        )

        self.start_container = Box(
            orientation="v" if orientation == Gtk.Orientation.VERTICAL else "h"
        )
        self.center_container = Box(
            orientation="v" if orientation == Gtk.Orientation.VERTICAL else "h"
        )
        self.end_container = Box(
            orientation="v" if orientation == Gtk.Orientation.VERTICAL else "h"
        )

        self.add(self._container)
        self._container.pack_start(self.start_container, False, False, 0)
        self._container.set_center_widget(self.center_container)
        self._container.pack_end(self.end_container, False, False, 0)
        self.initialize_children(start_children, center_children, end_children)
        self.do_connect_signals_for_kwargs(kwargs)

    def initialize_children(self, start, center, end):
        if start:
            if isinstance(start, (list, tuple)):
                [self.add_start(widget) for widget in start]
            else:
                self.add_start(start)
        if center:
            if isinstance(center, (list, tuple)):
                [self.add_center(widget) for widget in center]
            else:
                self.add_center(center)
        if end:
            if isinstance(end, (list, tuple)):
                [self.add_end(widget) for widget in end]
            else:
                self.add_end(end)
        return

    def add_start(self, widget: Gtk.Widget):
        self.start_container.add(widget)

    def add_center(self, widget: Gtk.Widget):
        self.center_container.add(widget)

    def add_end(self, widget: Gtk.Widget):
        self.end_container.add(widget)

    def remove_start(self, widget: Gtk.Widget):
        self.start_container.remove(widget)

    def remove_center(self, widget: Gtk.Widget):
        self.center_container.remove(widget)

    def remove_end(self, widget: Gtk.Widget):
        self.end_container.remove(widget)
