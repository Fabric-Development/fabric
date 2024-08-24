import gi
from typing import Literal
from collections.abc import Iterable
from fabric.core.service import Property
from fabric.core.application import Application
from fabric.utils.helpers import get_enum_member
from fabric.widgets.container import Container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


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
