from loguru import logger
from fabric.widgets.box import Box
from fabric.widgets.image import Image
from fabric.widgets.button import Button
from fabric.system_tray.service import SystemTray as SystemTrayService
from fabric.system_tray.service import SystemTrayItem as SystemTrayItemService
from fabric.utils import bulk_connect
from gi.repository import Gdk


class SystemTrayItem(Button):
    def __init__(self, item: SystemTrayItemService, icon_size: int, **kwargs):
        super().__init__(**kwargs)
        self.item = item
        self.image = Image()
        self.icon_size = icon_size
        self.add_events(Gdk.EventMask.SCROLL_MASK | Gdk.EventMask.SMOOTH_SCROLL_MASK)
        self.item.connect("changed", self.do_update_properties)
        bulk_connect(
            self,
            {
                "button-press-event": self.on_clicked,
                "scroll-event": self.on_scroll,
            },
        )
        self.do_update_properties()

    def do_update_properties(self, *arg):
        pixbuf = self.item.get_preferred_icon_pixbuf(
            size=self.icon_size, resize_method="bilinear"
        )
        if pixbuf is not None:
            self.image.set_from_pixbuf(pixbuf)
            self.set_image(self.image)
        tooltip = self.item.get_tooltip()
        title = self.item.get_title()
        self.set_tooltip_markup(
            tooltip.description or tooltip.title
        ) if tooltip is not None else self.set_tooltip_markup(
            title.title()
        ) if title is not None else None
        return

    def on_clicked(self, _, event: Gdk.EventButton):
        match event.button:
            case 1:
                try:
                    self.item.activate_for_event(event)
                except Exception as e:
                    logger.warning(
                        f"[SystemTrayItem] can't activate item with name {self.item.get_title() or self.item.identifier} ({e})"
                    )
            case 3:
                self.item.invoke_menu_for_event(event)
        return

    def on_scroll(self, _, event: Gdk.EventScroll):
        try:
            self.item.scroll_for_event(event)
        except Exception as e:
            logger.warning(
                f"[SystemTrayItem] can't scroll an item with name {self.item.get_title() or self.item.identifier} ({e})"
            )
        return


class SystemTray(Box):
    def __init__(self, icon_size: int = 24, **kwargs):
        super().__init__(**kwargs)
        self.icon_size = icon_size
        self._widget_items: dict[str, SystemTrayItem] = {}
        self.watcher = SystemTrayService()
        bulk_connect(
            self.watcher,
            {
                "item-added": self.on_item_added,
                "item-removed": self.on_item_removed,
            },
        )

    def on_item_added(self, _, item_identifier: str):
        item = self.watcher.get_items().get(item_identifier)
        if not item:
            return
        item_widget = SystemTrayItem(item, self.icon_size)
        self.add(item_widget)
        self._widget_items[item.identifier] = item_widget
        return

    def on_item_removed(self, _, item_identifier):
        item_widget = self._widget_items.get(item_identifier)
        if not item_widget:
            return
        self.remove(item_widget)
        self._widget_items.pop(item_identifier)
