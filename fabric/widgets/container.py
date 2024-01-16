import gi
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Container(Gtk.Container, Widget):
    def __init__(
        self,
        children: Gtk.Widget | list[Gtk.Widget] | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_compiled: bool = True,
        style_append: bool = False,
        style_add_brackets: bool = True,
        name: str | None = None,
        size: tuple[int] | None = None,
        **kwargs,
    ):
        Gtk.Container.__init__(self, **kwargs)
        self.set_children(children) if children is not None else None
        Widget.__init__(
            self,
            visible,
            all_visible,
            style,
            style_compiled,
            style_append,
            style_add_brackets,
            name,
            size,
        )

    def add_children(self, children: Gtk.Widget | list[Gtk.Widget]):
        if isinstance(children, Gtk.Widget):
            children = [children]
        if isinstance(children, list) and all(
            isinstance(widget, Gtk.Widget) for widget in children
        ):
            for widget in children:
                Gtk.Container.add(self, widget)
            return

    def set_children(self, children: Gtk.Widget | list[Gtk.Widget]):
        self.reset_children()
        return self.add_children(children)

    def reset_children(self):
        for child in super().get_children():
            child: Gtk.Widget
            super().remove(child)
            child.destroy()
        return
