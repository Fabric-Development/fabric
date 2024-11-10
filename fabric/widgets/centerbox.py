import gi
from typing import Literal
from collections.abc import Iterable
from fabric.core.service import Property
from fabric.widgets.box import Box
from fabric.utils.helpers import get_enum_member

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class CenterBox(Box):
    # using `.fset` directly isn't a good idea but it works for now
    @Property(list[Gtk.Widget], "read-write")
    def start_children(self) -> list[Gtk.Widget]:
        return self.start_container.get_children()

    @start_children.setter
    def start_children(self, value: Gtk.Widget | Iterable[Gtk.Widget]):
        return Box.children.fset(self.start_container, value)  # type: ignore

    @Property(list[Gtk.Widget], "read-write")
    def center_children(self) -> list[Gtk.Widget]:
        return self.center_container.get_children()

    @center_children.setter
    def center_children(self, value: Gtk.Widget | Iterable[Gtk.Widget]):
        return Box.children.fset(self.center_container, value)  # type: ignore

    @Property(list[Gtk.Widget], "read-write")
    def end_children(self) -> list[Gtk.Widget]:
        return self.end_container.get_children()

    @end_children.setter
    def end_children(self, value: Gtk.Widget | Iterable[Gtk.Widget]):
        return Box.children.fset(self.end_container, value)  # type: ignore

    def __init__(
        self,
        start_children: Gtk.Widget | Iterable[Gtk.Widget] | None = None,
        center_children: Gtk.Widget | Iterable[Gtk.Widget] | None = None,
        end_children: Gtk.Widget | Iterable[Gtk.Widget] | None = None,
        spacing: int = 0,
        orientation: Literal[
            "horizontal",
            "vertical",
            "h",
            "v",
        ]
        | Gtk.Orientation = Gtk.Orientation.HORIZONTAL,
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
        orientation = get_enum_member(
            Gtk.Orientation,
            orientation,
            {
                "h": "horizontal",
                "v": "vertical",
            },
            Gtk.Orientation.VERTICAL,
        )
        orientation_flipped = {
            Gtk.Orientation.VERTICAL: Gtk.Orientation.HORIZONTAL,
            Gtk.Orientation.HORIZONTAL: Gtk.Orientation.VERTICAL,
        }.get(orientation, Gtk.Orientation.VERTICAL)
        super().__init__(
            spacing,
            orientation_flipped,
            None,
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

        def box_factory():
            return Box(orientation=orientation).build(
                lambda _, builder: builder.set_vexpand(True)
                if orientation == Gtk.Orientation.HORIZONTAL
                else builder.set_hexpand(True)
            )

        self._inner = box_factory()

        self.start_container = box_factory()
        self.center_container = box_factory()
        self.end_container = box_factory()

        self._inner.pack_start(self.start_container, False, False, 0)
        self._inner.set_center_widget(self.center_container)
        self._inner.pack_end(self.end_container, False, False, 0)

        self.start_container.children = start_children or ()
        self.center_container.children = center_children or ()
        self.end_container.children = end_children or ()

        self.add(self._inner)

    def add_start(self, widget: Gtk.Widget):
        return self.start_container.add(widget)

    def add_center(self, widget: Gtk.Widget):
        return self.center_container.add(widget)

    def add_end(self, widget: Gtk.Widget):
        return self.end_container.add(widget)

    def remove_start(self, widget: Gtk.Widget):
        return self.start_container.remove(widget)

    def remove_center(self, widget: Gtk.Widget):
        return self.center_container.remove(widget)

    def remove_end(self, widget: Gtk.Widget):
        return self.end_container.remove(widget)
