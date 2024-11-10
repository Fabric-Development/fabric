import gi
from typing import Literal
from collections.abc import Iterable
from fabric.core.service import Property
from fabric.widgets.container import Container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Overlay(Gtk.Overlay, Container):
    @Property(list[Gtk.Widget], "read-write")
    def overlays(self) -> list[Gtk.Widget]:
        return self._overlays

    @overlays.setter
    def overlays(self, value: Gtk.Widget | Iterable[Gtk.Widget]):
        for old_overlay in self._overlays:
            self.remove(old_overlay)
        if isinstance(value, (tuple, list)):
            for widget in value:
                self.add_overlay(widget)
            return
        self.add_overlay(value)  # type: ignore
        return

    def __init__(
        self,
        child: Gtk.Widget | None = None,
        overlays: Gtk.Widget | list[Gtk.Widget] | None = None,
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
        Gtk.Overlay.__init__(self)  # type: ignore
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
            size,
            **kwargs,
        )
        self._overlays = []
        if overlays is not None:
            self.overlays = overlays

    # overrides
    def remove_overlay(self, overlay: Gtk.Widget):
        if overlay not in self._overlays:
            raise ValueError(f"widget {overlay} does not exist in {self} as a overlay")
        self.remove(overlay)
        self._overlays.remove(overlay)
        return

    def add_overlay(self, overlay: Gtk.Widget):
        super().add_overlay(overlay)
        self._overlays.append(overlay)
        return
