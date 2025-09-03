import gi
import cairo
from loguru import logger
from typing import Literal, Self, Any
from collections.abc import Callable, Iterable
from fabric.core.service import Property
from fabric.core.application import Application
from fabric.widgets.container import Container
from fabric.utils.helpers import (
    get_enum_member,
    keyboard_event_serialize,
    make_arguments_ignorable,
)

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class Window(Gtk.Window, Container):
    @Property(Application, install=False)
    def application(self) -> Application:
        return self.get_application()  # type: ignore

    @Property(bool, "read-write", default_value=False)
    def pass_through(self) -> bool:
        return self._pass_through

    @pass_through.setter
    def pass_through(self, pass_through: bool = False):
        self._pass_through = pass_through

        self.input_shape_combine_region(
            cairo.Region(cairo.RectangleInt()) if pass_through is True else None
        )

        return

    def __init__(
        self,
        title: str = "fabric",
        type: Literal["top-level", "popup"] | Gtk.WindowType = Gtk.WindowType.TOPLEVEL,
        child: Gtk.Widget | None = None,
        pass_through: bool = False,
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
        self._pass_through = pass_through

        Gtk.Window.__init__(
            self,  # type: ignore
            title=title,
            type=get_enum_member(
                Gtk.WindowType, type, {"top-level": "toplevel"}, Gtk.WindowType.TOPLEVEL
            ),
        )
        Container.__init__(
            self,
            child,
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
            None,
            **kwargs,
        )

        self.set_default_size(
            *((size, size) if isinstance(size, int) else size)
        ) if size is not None else None

        self._key_press_handler: int = 0
        self._keybinding_handlers: dict[
            str, list[tuple[Callable[[Self, Any], Any], int]]
        ] = {}

        self.pass_through = pass_through

    def do_handle_key_press_event(self, _, event):
        if not (
            keybind_entries := self._keybinding_handlers.get(
                keyboard_event_serialize(event)
            )
        ):
            return
        for kbh in keybind_entries:
            kbh[0](self, event)
        return

    def do_post_kebinding_removal(self):
        for kbn, kbd in self._keybinding_handlers.copy().items():
            if not kbd:
                self._keybinding_handlers.pop(kbn)
        if not self._keybinding_handlers:
            self.disconnect(self._keybinding_handlers)
            self._key_press_handler = 0
        return

    def add_keybinding(
        self,
        keybind: str,
        callback: Callable[[Self, Any], Any] | Callable,
        ignore_missing: bool = True,
    ) -> int:
        handler = GLib.random_int()

        keybind_entry = self._keybinding_handlers.setdefault(keybind.casefold(), [])
        keybind_entry.append(
            (
                callback if not ignore_missing else make_arguments_ignorable(callback),
                handler,
            )
        )

        if not self._key_press_handler:
            self._key_press_handler = self.connect(
                "key-press-event", self.do_handle_key_press_event, ignore_missing=False
            )

        return handler

    def remove_keybinding(self, reference: int | Callable | str):
        if isinstance(reference, (int, Callable)):
            for kbn, kbd in self._keybinding_handlers.items():
                for bindref in kbd:
                    if reference in bindref:
                        kbd.remove(bindref)
            return self.do_post_kebinding_removal()
        self._keybinding_handlers.pop(reference, None)
        return self.do_post_kebinding_removal()

    # overrides
    def do_handle_post_show_request(self) -> None:
        if not self.get_children():
            logger.warning(
                "[Window] showing an empty window is not recommended, some compositors might freak out."
            )
        return

    def show(self):
        super().show()
        return self.do_handle_post_show_request()

    def show_all(self):
        super().show_all()
        return self.do_handle_post_show_request()

    def do_size_allocate(self, alloc):
        Gtk.Window.do_size_allocate(self, alloc)  # type: ignore

        return self.set_pass_through(self._pass_through)
  
    def toggle(self):
        return self.hide() if self.get_visible() else self.show()