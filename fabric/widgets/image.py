import gi
from typing import Literal
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf


class Image(Gtk.Image, Widget):
    def __init__(
        self,
        image_file: str | None = None,
        icon_name: str | None = None,
        pixbuf: GdkPixbuf.Pixbuf | None = None,
        pixel_size: int | None = None,
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
        Gtk.Image.__init__(self, **kwargs)
        self.set_from_file(image_file) if image_file is not None else None
        self.set_from_icon_name(icon_name) if icon_name is not None else None
        self.set_from_pixbuf(pixbuf) if pixbuf is not None else None
        self.set_pixel_size(pixel_size) if pixel_size is not None else None
        Widget.__init__(
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
