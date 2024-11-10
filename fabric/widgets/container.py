import gi
from typing import Literal
from collections.abc import Iterable
from fabric.core.service import Property
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Container(Gtk.Container, Widget):
    @Property(list[Gtk.Widget], "read-write", install=False)
    def children(self) -> list[Gtk.Widget]:
        return self.get_children()

    @children.setter
    def children(self, value: Gtk.Widget | Iterable[Gtk.Widget]):
        for old_child in self.get_children():
            self.remove(old_child)
        if isinstance(value, (tuple, list)):
            for widget in value:
                self.add(widget)
            return
        self.add(value)
        return

    def __init__(
        self,
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
        Gtk.Container.__init__(self)  # type: ignore
        Widget.__init__(
            self,
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
        if children:
            self.children = children
