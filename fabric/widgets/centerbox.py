import gi
from typing import Literal
from fabric.widgets.box import Box

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class CenterBox(Box):
    """
    A box that can hold widgets in the center, left, and right, useful for creating bars

    # Note
    This should be the ONLY widget placed in the parent contianer/window.
    """

    def __init__(
        self,
        left_widgets: list[Gtk.Widget] | Gtk.Widget | None = None,
        center_widgets: list[Gtk.Widget] | Gtk.Widget | None = None,
        right_widgets: list[Gtk.Widget] | Gtk.Widget | None = None,
        spacing: int | None = None,
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
    ):
        super().__init__(
            spacing,
            "v",
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
            **kwargs,
        )
        self.widgets_container = Box(
            orientation="h",
        )

        self.left_widgets = Box()
        self.center_widgets = Box()
        self.right_widgets = Box()

        self.add(self.widgets_container)
        self.widgets_container.pack_start(self.left_widgets, False, False, 0)
        self.widgets_container.set_center_widget(self.center_widgets)
        self.widgets_container.pack_end(self.right_widgets, False, False, 0)
        self.initialize_children(left_widgets, center_widgets, right_widgets)

    def initialize_children(self, left, center, right):
        if left:
            if isinstance(left, (list, tuple)):
                [self.left_widgets.add(widget) for widget in left]
            else:
                self.left_widgets.add(left)
        if center:
            if isinstance(center, (list, tuple)):
                [self.center_widgets.add(widget) for widget in center]
            else:
                self.center_widgets.add(center)
        if right:
            if isinstance(right, (list, tuple)):
                [self.right_widgets.add(widget) for widget in right]
            else:
                self.right_widgets.add(right)
        return

    def add_left(self, widget: Gtk.Widget):
        self.left_widgets.add(widget)

    def add_center(self, widget: Gtk.Widget):
        self.center_widgets.pack_start(widget, False, False, 0)

    def add_right(self, widget: Gtk.Widget):
        self.right_widgets.add(widget)

    def remove_left(self, widget: Gtk.Widget):
        self.left_widgets.remove(widget)

    def remove_center(self, widget: Gtk.Widget):
        self.center_widgets.remove(widget)

    def remove_right(self, widget: Gtk.Widget):
        self.right_widgets.remove(widget)
