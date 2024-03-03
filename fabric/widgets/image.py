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
        icon_size: int | None = 24,
        pixbuf: GdkPixbuf.Pixbuf | None = None,
        pixel_size: int | tuple[int] | None = None,
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
        """
        :param image_file: the path to the image if any, defaults to None
        :type image_file: str | None, optional
        :param icon_name: the name of the icon if any, defaults to None
        :type icon_name: str | None, optional
        :param icon_size: the size of the icon if any, defaults to None
        :type icon_size: int | None, optional
        :param pixbuf: the pixbuf if any, defaults to None
        :type pixbuf: GdkPixbuf.Pixbuf | None, optional
        :param pixel_size: the image pixel size, defaults to None
        :type pixel_size: int | None, optional
        :param visible: whether the widget is initially visible, defaults to True
        :type visible: bool, optional
        :param all_visible: whether all child widgets are initially visible, defaults to False
        :type all_visible: bool, optional
        :param style: inline css style string, defaults to None
        :type style: str | None, optional
        :param style_compiled: whether the passed css should get compiled before applying, defaults to True
        :type style_compiled: bool, optional
        :param style_append: whether the passed css should be appended to the existing css, defaults to False
        :type style_append: bool, optional
        :param style_add_brackets: whether the passed css should be wrapped in brackets if they were missing, defaults to True
        :type style_add_brackets: bool, optional
        :param tooltip_text: the text added to the tooltip, defaults to None
        :type tooltip_text: str | None, optional
        :param tooltip_markup: the markup added to the tooltip, defaults to None
        :type tooltip_markup: str | None, optional
        :param h_align: the horizontal alignment, defaults to None
        :type h_align: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None, optional
        :param v_align: the vertical alignment, defaults to None
        :type v_align: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None, optional
        :param h_expand: the horizontal expansion, defaults to False
        :type h_expand: bool, optional
        :param v_expand: the vertical expansion, defaults to False
        :type v_expand: bool, optional
        :param name: the name of the widget it can be used to style the widget, defaults to None
        :type name: str | None, optional
        :param size: the size of the widget, defaults to None
        :type size: tuple[int] | int | None, optional
        """
        Gtk.Image.__init__(
            self,
            **(self.do_get_filtered_kwargs(kwargs)),
        )
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
        if pixel_size is not None and image_file is not None:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
                image_file,
                *(
                    (pixel_size, pixel_size)
                    if isinstance(pixel_size, int)
                    else pixel_size
                ),
            )
            self.set_from_pixbuf(pixbuf)
        else:
            self.set_from_file(image_file) if image_file is not None else None
            self.set_from_icon_name(
                icon_name, icon_size
            ) if icon_name is not None and icon_size is not None else None
            self.set_from_pixbuf(pixbuf) if pixbuf is not None else None
            self.set_pixel_size(pixel_size) if pixel_size is not None else None
        self.do_connect_signals_for_kwargs(kwargs)
