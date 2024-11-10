from fabric import Application
from collections.abc import Iterator
from fabric.widgets.box import Box
from fabric.widgets.entry import Entry
from fabric.widgets.image import Image
from fabric.widgets.button import Button
from fabric.widgets.window import Window
from fabric.widgets.flowbox import FlowBox
from fabric.widgets.scrolledwindow import ScrolledWindow
from fabric.utils import idle_add, remove_handler

from gi.repository import Gtk


class IconBrowser(Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer="top",
            anchor="center",
            exclusivity="none",
            keyboard_mode="on-demand",
            visible=False,
            all_visible=False,
            on_destroy=lambda *_: app.quit(),
            **kwargs,
        )
        self._arranger_handler: int = 0
        self._icon_theme = Gtk.IconTheme.get_default()
        self._all_icons: list[str] = self._icon_theme.list_icons()

        self.viewport = FlowBox(orientation="v")
        self.search_entry = Entry(
            placeholder="Search Icons...",
            h_expand=True,
            notify_text=lambda entry, *_: self.arrange_viewport(entry.get_text()),
        )
        self.scrolled_window = ScrolledWindow(
            min_content_size=(280, 320), child=self.viewport
        )

        self.add(
            Box(
                spacing=2,
                orientation="v",
                style="margin: 2px",
                children=[
                    # the header with the search entry
                    Box(
                        spacing=2,
                        orientation="h",
                        children=[
                            self.search_entry,
                            Button(
                                image=Image(icon_name="window-close"),
                                tooltip_text="Exit",
                                on_clicked=lambda *_: self.application.quit(),
                            ),
                        ],
                    ),
                    # the actual slots holder
                    self.scrolled_window,
                ],
            )
        )
        self.show_all()

    def arrange_viewport(self, query: str = ""):
        if self._arranger_handler:
            remove_handler(self._arranger_handler)

        self.viewport.children = []
        self._arranger_handler = idle_add(
            self.add_next_icon,
            iter(
                sorted(
                    icon_name
                    for icon_name in self._all_icons
                    if query.casefold() in icon_name.casefold()
                )
            ),
            pin=True,
        )

        return False

    def add_next_icon(self, icons_iter: Iterator[str]):
        if not (icon_name := next(icons_iter, None)):
            return False

        self.viewport.add(
            Button(
                child=Image(
                    icon_name=icon_name, icon_size=32, h_align="center", size=32
                ),
                tooltip_text=icon_name,
            )
        )
        return True


if __name__ == "__main__":
    icon_browser = IconBrowser()
    app = Application("icon-browser", icon_browser)

    app.run()
