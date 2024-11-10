import gi
from typing import Literal, Self, Any
from collections.abc import Callable, Iterable
from fabric.core.service import Property
from fabric.core.application import Application
from fabric.utils.helpers import get_enum_member, bulk_replace
from fabric.widgets.container import Container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class Window(Gtk.Window, Container):
    @Property(Application, install=False)
    def application(self) -> Application:
        return self.get_application()  # type: ignore

    def __init__(
        self,
        title: str = "fabric",
        type: Literal["top-level", "popup"] | Gtk.WindowType = Gtk.WindowType.TOPLEVEL,
        child: Gtk.Widget | None = None,
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

    def do_handle_key_press_event(self, _, event):
        if not (
            keybind_entry := self._keybinding_handlers.get(
                " ".join(
                    bulk_replace(
                        Gtk.accelerator_name(event.keyval, event.state).strip(),
                        ["<Mod2>", "<Shift>", "<Primary>", "<Mod4><Super>", "<Alt>"],
                        [" ", "Shift ", "Ctrl ", "Super ", "Alt "],
                    ).split()
                )
            )
        ):
            return
        for kbh in keybind_entry:
            kbh[0](self, event)
        return

    def do_post_kebinding_removal(self):
        for kbn, kbd in self._keybinding_handlers.copy().items():
            if not kbd:
                self._keybinding_handlers.pop(kbn)
        if not self._keybinding_handlers:
            self.disconnect_by_func(self.do_handle_key_press_event)
            self._key_press_handler = 0
        return

    def add_keybinding(self, keybind: str, callback: Callable[[Self, Any], Any]) -> int:
        handler = GLib.random_int()

        keybind_entry = self._keybinding_handlers.setdefault(keybind, [])
        keybind_entry.append((callback, handler))
        if not self._key_press_handler:
            self._key_press_handler = self.connect(
                "key-press-event", self.do_handle_key_press_event
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
