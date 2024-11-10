import gi
from typing import Literal, overload
from collections.abc import Iterable
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf


class Image(Gtk.Image, Widget):
    @overload
    def __init__(
        self,
        image_file: str | None = None,
        icon_name: None = None,
        icon_size: int = 24,
        pixbuf: None = None,
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
    ): ...

    @overload
    def __init__(
        self,
        image_file: None = None,
        icon_name: str | None = None,
        icon_size: int = 24,
        pixbuf: None = None,
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
    ): ...
    @overload
    def __init__(
        self,
        image_file: None = None,
        icon_name: None = None,
        icon_size: int = 24,
        pixbuf: GdkPixbuf.Pixbuf | None = None,
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
    ): ...

    def __init__(
        self,
        image_file: str | None = None,
        icon_name: str | None = None,
        icon_size: int = 24,
        pixbuf: GdkPixbuf.Pixbuf | None = None,
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
        Gtk.Image.__init__(self)  # type: ignore
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

        if image_file is not None:
            alloc = self.get_size_request()
            pixsize: tuple[int, int] = (alloc.width, alloc.height)  # type: ignore
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(image_file, *pixsize)
        elif icon_name is not None:
            self.set_from_icon_name(icon_name, icon_size)

        self.set_from_pixbuf(pixbuf) if pixbuf is not None else None

    # overrides
    def set_from_icon_name(
        self,
        icon_name: str,
        icon_size: int = 24,
    ):
        super().set_from_icon_name(
            icon_name,
            Gtk.IconSize.LARGE_TOOLBAR,  # type: ignore
        )
        return self.set_pixel_size(icon_size)
