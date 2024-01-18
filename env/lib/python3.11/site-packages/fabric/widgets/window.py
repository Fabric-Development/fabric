import gi
from loguru import logger
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Window(Gtk.Window, Widget):
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
        name: str | None = None,
        default_size: tuple[int, int] | None = None,
        **kwargs,
    ):
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
