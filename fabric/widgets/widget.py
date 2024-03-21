import gi
from typing import Literal
from fabric.service import *
from fabric.utils import compile_css

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

# shhhh
import logging

logging.captureWarnings(True)
logging.getLogger("gi.overrides").setLevel(logging.ERROR)


class Widget(Gtk.Widget, Service):
    """the base widget, all other widgets should inherit from this class"""

    def __init__(
        self,
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
        super().__init__(
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        self.style_provider: Gtk.CssProvider | None = None
        self._cursor: Gdk.Cursor | Gdk.CursorType | str | None = None
        self.show_all() if all_visible is True else self.show() if visible is True else None
        self.set_name(name) if name is not None else None
        self.set_tooltip_text(tooltip_text) if tooltip_text is not None else None
        self.set_tooltip_markup(tooltip_markup) if tooltip_markup is not None else None
        self.set_halign(
            {
                "fill": Gtk.Align.FILL,
                "start": Gtk.Align.START,
                "end": Gtk.Align.END,
                "center": Gtk.Align.CENTER,
                "baseline": Gtk.Align.BASELINE,
            }.get(h_align.lower(), Gtk.Align.START)
            if isinstance(h_align, str)
            else h_align
            if isinstance(h_align, Gtk.Align)
            else Gtk.Align.START
        ) if h_align is not None else None
        self.set_valign(
            {
                "fill": Gtk.Align.FILL,
                "start": Gtk.Align.START,
                "end": Gtk.Align.END,
                "center": Gtk.Align.CENTER,
                "baseline": Gtk.Align.BASELINE,
            }.get(v_align.lower(), Gtk.Align.START)
            if isinstance(v_align, str)
            else v_align
            if isinstance(v_align, Gtk.Align)
            else Gtk.Align.START
        ) if v_align is not None else None
        self.set_hexpand(
            True if h_expand is True else False
        ) if h_expand is not None else None
        self.set_vexpand(
            True if v_expand is True else False
        ) if v_expand is not None else None
        self.set_size_request(
            *((size, size) if isinstance(size, int) is True else size)
        ) if size is not None else None
        self.set_style(
            style, style_compiled, style_append, style_add_brackets
        ) if style is not None else None

    def set_style(
        self,
        style: str,
        compiled: bool = True,
        append: bool = False,
        add_brackets: bool = True,
    ) -> None:
        """
        set the styles for this widget from a string

        :param style: the css style
        :type style: str
        :param compile: to compile the style, defaults to True
        :type compile: bool, optional
        :param append: appends this style to other loaded styles (if any), if this is set to False it will clear all other styles before applying, defaults to False
        :type append: bool, optional
        :param add_brackets: add brackets to the style if they are missing (e.g. `padding: 10; some-thing-useful: unset;` was passed; will be converted to `* { padding: 10; some-thing-useful: unset; }`), defaults to True
        """
        style = (
            f"* {{ {style} }}"
            if not "{" in style or not "}" in style and add_brackets is True
            else style
        )
        style = compile_css(style) if compiled is True else style

        self.get_style_context().remove_provider(
            self.style_provider
        ) if self.style_provider is not None and append is False else None

        self.style_provider = Gtk.CssProvider()
        self.style_provider.load_from_data(style.encode())  # type: ignore
        self.get_style_context().add_provider(
            self.style_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER
        )
        return

    def get_style_classes(self) -> list[str]:
        return self.get_style_context().list_classes() or []

    def set_style_classes(self, classes: list[str]) -> None:
        for cls in self.get_style_classes():
            self.get_style_context().remove_class(cls)
        for cls in classes:
            self.get_style_context().add_class(cls)
        return

    @Property(value_type=object, flags="read-write")
    def cursor(
        self
    ) -> (
        Literal[
            "default",
            "help",
            "pointer",
            "context-menu",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "no-drop",
            "move",
            "not-allowed",
            "grab",
            "grabbing",
            "all-scroll",
            "col-resize",
            "row-resize",
            "n-resize",
            "e-resize",
            "s-resize",
            "w-resize",
            "ne-resize",
            "nw-resize",
            "sw-resize",
            "se-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "zoom-in",
            "zoom-out",
        ]
        | Gdk.Cursor
        | Gdk.CursorType
        | None
    ):
        return self._cursor

    @cursor.setter
    def cursor(
        self,
        cursor: Literal[
            "default",
            "help",
            "pointer",
            "context-menu",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "no-drop",
            "move",
            "not-allowed",
            "grab",
            "grabbing",
            "all-scroll",
            "col-resize",
            "row-resize",
            "n-resize",
            "e-resize",
            "s-resize",
            "w-resize",
            "ne-resize",
            "nw-resize",
            "sw-resize",
            "se-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "zoom-in",
            "zoom-out",
        ]
        | Gdk.Cursor
        | Gdk.CursorType
        | None,
    ) -> None:
        self.change_cursor(cursor)
        return

    def change_cursor(
        self,
        cursor: Literal[
            "default",
            "help",
            "pointer",
            "context-menu",
            "progress",
            "wait",
            "cell",
            "crosshair",
            "text",
            "vertical-text",
            "alias",
            "copy",
            "no-drop",
            "move",
            "not-allowed",
            "grab",
            "grabbing",
            "all-scroll",
            "col-resize",
            "row-resize",
            "n-resize",
            "e-resize",
            "s-resize",
            "w-resize",
            "ne-resize",
            "nw-resize",
            "sw-resize",
            "se-resize",
            "ew-resize",
            "ns-resize",
            "nesw-resize",
            "nwse-resize",
            "zoom-in",
            "zoom-out",
        ]
        | Gdk.Cursor
        | Gdk.CursorType
        | None = None,
    ) -> bool | None:
        self._cursor = cursor
        display = Gdk.Display.get_default()
        window = self.get_window()
        if display is None or window is None:
            raise RuntimeError(
                f"can't set new cursor, one of display or window is None ({display}, {window})"
            )
        cursor: Gdk.Cursor = (
            Gdk.Cursor.new_from_name(display, cursor)
            if isinstance(cursor, str)
            else cursor
            if isinstance(cursor, Gdk.Cursor)
            else Gdk.Cursor.new_for_display(display, cursor)
            if isinstance(cursor, Gdk.CursorType)
            else Gdk.Cursor.new_from_name(display, "default")
        )
        return (
            window.set_cursor(cursor)
            if self.is_hovered()
            else window.set_cursor(Gdk.Cursor.new_from_name(display, "default"))
        )

    def is_hovered(self, event: Gdk.Event | None = None) -> bool:
        x, y = self.get_pointer()
        allocation = self.get_allocation()
        if event:
            x, y = event.get_coords()
        return 0 < x < allocation.width and 0 < y < allocation.height
