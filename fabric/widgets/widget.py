import gi
from typing import overload, Literal
from fabric.utils import compile_css, get_enum_member
from fabric.core.service import Service, Property
from collections.abc import Iterable

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf

# shhhh
import logging

logging.captureWarnings(True)
logging.getLogger("gi.overrides").setLevel(logging.ERROR)


CURSOR_TYPE = Literal[
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

EVENT_TYPE = Literal[
    "exposure",
    "pointer-motion",
    "pointer-motion-hint",
    "button-motion",
    "button-1-motion",
    "button-2-motion",
    "button-3-motion",
    "button-press",
    "button-release",
    "key-press",
    "key-release",
    "enter-notify",
    "leave-notify",
    "focus-change",
    "structure",
    "property-change",
    "visibility-notify",
    "proximity-in",
    "proximity-out",
    "substructure",
    "scroll",
    "touch",
    "smooth-scroll",
    "touchpad-gesture",
    "tablet-pad",
    "all",
]


class Widget(Gtk.Widget, Service):
    """the base widget, all other widgets should inherit from this class"""

    @Property(Gtk.Align, "read-write", default_value=Gtk.Align.BASELINE)
    def v_align(self):
        return self.get_valign()

    @v_align.setter
    def v_align(
        self, value: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align
    ):
        self.set_valign(get_enum_member(Gtk.Align, value, {}, Gtk.Align.BASELINE))

    @Property(Gtk.Align, "read-write", default_value=Gtk.Align.BASELINE)
    def h_align(self):
        return self.get_halign()

    @h_align.setter
    def h_align(
        self, value: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align
    ):
        self.set_halign(get_enum_member(Gtk.Align, value, {}, Gtk.Align.BASELINE))

    @Property(bool, default_value=False)
    def v_expand(self):
        return self.get_vexpand()

    @v_expand.setter
    def v_expand(self, value: bool):
        return self.set_vexpand(value)

    @Property(bool, default_value=False)
    def h_expand(self):
        return self.get_hexpand()

    @h_expand.setter
    def h_expand(self, value: bool):
        return self.set_hexpand(value)

    @Property(list[str], "read-write")
    def style_classes(self) -> list[str]:
        return self.get_style_context().list_classes() or []

    @style_classes.setter
    def style_classes(self, classes: Iterable[str] | str) -> None:
        self.remove_style_class(self.style_classes)
        self.add_style_class(classes)
        return

    def __init__(
        self,
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
        Gtk.Widget.__init__(self)  # type: ignore
        Service.__init__(self, **kwargs)

        self._style_provider: Gtk.CssProvider | None = None
        self._cursor: Gdk.Cursor | None = None

        self.set_name(name) if name is not None else None
        self.set_tooltip_text(tooltip_text) if tooltip_text is not None else None
        self.set_tooltip_markup(tooltip_markup) if tooltip_markup is not None else None

        if v_align:
            self.v_align = v_align
        if h_align:
            self.h_align = h_align

        self.v_expand = v_expand
        self.h_expand = h_expand

        if size is not None:
            self.set_size_request(*((size, size) if isinstance(size, int) else size))

        if style_classes:
            self.add_style_class(style_classes)  # to not override default classes

        if style:
            self.set_style(style)

        self.show_all() if all_visible is True else self.show() if visible is True else None

    def set_alignment(
        self,
        orientation: Literal["v", "vertical", "h", "horizontal"] | Gtk.Orientation,
        alignment: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align,
    ):
        ornt = get_enum_member(
            Gtk.Orientation, orientation, {"v": "vertical", "h": "horizontal"}
        )
        align = get_enum_member(Gtk.Align, alignment)
        return (
            self.set_valign if ornt == Gtk.Orientation.VERTICAL else self.set_halign
        )(align)

    def set_style(
        self,
        style: str,
        compile: bool = True,
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
        :param add_brackets: add brackets to the style if they are missing (e.g. `padding: 10; something-useful: unset;` was passed; will be converted to `* { padding: 10; something-useful: unset; }`), defaults to True
        """
        style = (
            f"* {{ {style} }}"
            if "{" not in style or "}" not in style and add_brackets is True
            else style
        )
        style = compile_css(style) if compile is True else style

        self.get_style_context().remove_provider(
            self._style_provider
        ) if self._style_provider is not None and append is False else None

        self._style_provider = Gtk.CssProvider()
        self._style_provider.load_from_data(style.encode())  # type: ignore
        self.get_style_context().add_provider(
            self._style_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER
        )
        return

    @overload
    def set_cursor(
        self,
        cursor: CURSOR_TYPE | Gdk.CursorType | Gdk.Cursor | None,
        pixbuf: None = None,
        x_offset: int = 0,
        y_offset: int = 0,
    ): ...

    @overload
    def set_cursor(
        self,
        cursor: None,
        pixbuf: GdkPixbuf.Pixbuf | None = None,
        x_offset: int = 0,
        y_offset: int = 0,
    ): ...

    def set_cursor(
        self,
        cursor: CURSOR_TYPE | Gdk.CursorType | Gdk.Cursor | None,
        pixbuf: GdkPixbuf.Pixbuf | None = None,
        x_offset: int = 0,
        y_offset: int = 0,
    ):
        display = Gdk.Display.get_default()
        window = self.get_window()
        if display is None or window is None:
            raise RuntimeError(
                f"can't set new cursor, one of `display` or `window` is None ({display}, {window})"
            )
        elif not self.is_hovered():
            return window.set_cursor(Gdk.Cursor.new_from_name(display, "default"))

        if pixbuf is not None:
            cursor = Gdk.Cursor.new_from_pixbuf(display, pixbuf, x_offset, y_offset)
        elif isinstance(cursor, Gdk.Cursor):
            pass
        elif isinstance(cursor, str):
            cursor = Gdk.Cursor.new_from_name(display, cursor)
        elif isinstance(cursor, Gdk.CursorType):
            cursor = Gdk.Cursor.new_for_display(display, cursor)
        else:
            cursor = Gdk.Cursor.new_from_name(display, "default")

        return window.set_cursor(cursor)

    def is_hovered(self, event: Gdk.EventAny | None = None) -> bool:
        x, y = self.get_pointer()  # type: ignore
        allocation = self.get_allocation()
        if event:
            x, y = event.get_coords()  # type: ignore
        return 0 < x < allocation.width and 0 < y < allocation.height  # type: ignore

    def add_style_class(self, class_name: str | Iterable[str]):
        if isinstance(class_name, str):
            class_name = class_name.strip().lstrip().split()
        for klass in class_name:
            self.get_style_context().add_class(klass)
        return

    def remove_style_class(self, class_name: str | Iterable[str]):
        if isinstance(class_name, str):
            class_name = class_name.strip().lstrip().split()
        for klass in class_name:
            self.get_style_context().remove_class(klass)
        return

    def add_events(
        self, events: EVENT_TYPE | Gdk.EventMask | Iterable[EVENT_TYPE | Gdk.EventMask]
    ):
        _events: int = 0
        events_map: dict[str, str] = {
            x: (x if x != "all" else "all-events") + "-mask"
            for x in EVENT_TYPE.__args__
        }
        for event in (events,) if not isinstance(events, (tuple, list)) else events:
            _events |= get_enum_member(Gdk.EventMask, event, events_map, 0)  # type: ignore
        return super().add_events(_events)
