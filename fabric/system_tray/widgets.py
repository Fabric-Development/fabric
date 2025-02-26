from loguru import logger
from fabric.widgets.box import Box
from fabric.widgets.image import Image
from fabric.widgets.button import Button
from fabric.system_tray.service import (
    SystemTray as SystemTrayService,
    SystemTrayItem as SystemTrayItemService,
)


class SystemTrayItem(Button):
    def __init__(self, item: SystemTrayItemService, icon_size: int, **kwargs):
        super().__init__(**kwargs)
        self._item = item
        self._icon_size = icon_size
        self._image = Image()
        self.set_image(self._image)

        self._item.changed.connect(self.do_update_properties)
        self.connect("button-press-event", self.on_clicked)

        self.do_update_properties()

    def do_update_properties(self, *_):
        pixbuf = self._item.get_preferred_icon_pixbuf(self._icon_size)
        if pixbuf is not None:
            self._image.set_from_pixbuf(pixbuf)
        else:
            self._image.set_from_icon_name("image-missing", self._icon_size)

        tooltip = self._item.tooltip
        self.set_tooltip_markup(
            tooltip.description or tooltip.title or self._item.title.title() if self._item.title else "Unknown"
        )
        return

    def on_clicked(self, _, event):
        match event.button:
            case 1:
                try:
                    self._item.activate_for_event(event)
                except Exception as e:
                    logger.warning(
                        f"[SystemTrayItem] can't activate item with name {self._item.title or self._item.identifier} ({e})"
                    )
            case 3:
                self._item.invoke_menu_for_event(event)
        return


class SystemTray(Box):
    def __init__(self, icon_size: int = 24, **kwargs):
        super().__init__(**kwargs)
        self._icon_size = icon_size
        self._items: dict[str, SystemTrayItem] = {}
        self._watcher = SystemTrayService(
            on_item_added=self.on_item_added, on_item_removed=self.on_item_removed
        )

    def on_item_added(self, _, item_identifier: str):
        item = self._watcher.items.get(item_identifier)
        if not item:
            return

        item_button = SystemTrayItem(item, self._icon_size)
        self.add(item_button)
        self._items[item.identifier] = item_button
        return

    def on_item_removed(self, _, item_identifier):
        item_button = self._items.get(item_identifier)
        if not item_button:
            return

        self.remove(item_button)
        self._items.pop(item_identifier)
        return


__all__ = ["SystemTray", "SystemTrayItem"]
