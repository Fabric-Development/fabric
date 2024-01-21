import gi
from loguru import logger
from typing import Literal
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Window(Gtk.Window, Widget):
    """a normal top-level window"""

    def __init__(
        self,
        title: str | None = "fabric",
        children: Gtk.Widget | None = None,
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
        default_size: tuple[int, int] | None = None,
        **kwargs,
    ):
        """
        :param title: the window title which will be displayed in the window title bar, defaults to "fabric"
        :type title: str | None, optional
        :param children: the child widget (single widget), defaults to None
        :type children: Gtk.Widget | None, optional
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
        :type size: tuple[int] | None, optional
        :param default_size: the default size of the window, defaults to None
        :type default_size: tuple[int, int] | None, optional
        """
        Gtk.Window.__init__(
            self,
            **kwargs,
        )
        self.set_title(title) if title is not None else None
        (
            self.add(children)
            if children is not None and not isinstance(children, list)
            else (
                logger.warning(
                    "Window widget accepts a single child widget only. using the first widget in the passed list."
                ),
                self.add(children[0]),
            )
            if children is not None and isinstance(children, list)
            else None,
        )
        self.set_default_size(*default_size) if default_size is not None else None
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
            default_size,
        )
        self.connect("destroy", Gtk.main_quit)


if __name__ == "__main__":
    from fabric.widgets.label import Label
    from fabric import start

    Window(
        children=Label(label="Fabric Window Test. Hello, World!"),
        all_visible=True,
    )
    start()
