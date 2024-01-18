# TODO: connector
import gi
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Button(Gtk.Button, Widget):
    def __init__(
        self,
        label: str | None = None,
        icon_image: Gtk.Widget | Widget | None = None,
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
        Gtk.Button.__init__(self, **kwargs)
        super().set_label(label) if label is not None else None
        super().set_image(icon_image) if icon_image is not None else None
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
