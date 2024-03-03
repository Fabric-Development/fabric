import gi
from typing import Literal
from fabric.widgets.container import Container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Overlay(Gtk.Overlay, Container):
    def __init__(
        self,
        children: Gtk.Widget | None = None,
        overlays: Gtk.Widget | list[Gtk.Widget] | None = None,
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
        :param children: the main children which will be displayed on the lower layer of the widget, defaults to None
        :type children: Gtk.Widget | None, optional
        :param overlays: the children which will be displayed on the upper layer of the widget, defaults to None
        :type overlays: Gtk.Widget | list[Gtk.Widget] | None, optional
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
        Gtk.Overlay.__init__(
            self,
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        Container.__init__(
            self,
            None,
            visible,
            all_visible,
            style,
            style_compiled,
            style_append,
            style_add_brackets,
            tooltip_text,
            tooltip_markup,
            h_align,
            v_align,
            h_expand,
            v_expand,
            name,
            size,
        )
        self._overlays = []
        self._child = children if children is not None else None
        self.add(self._child) if self._child is not None else None
        self.add_overlays(overlays) if overlays is not None else None
        self.do_connect_signals_for_kwargs(kwargs)

    @property
    def children(self) -> Gtk.Widget:
        return self._child

    @children.setter
    def children(self, children: Gtk.Widget):
        self.remove(self._child)
        self._child = children
        return self.add(self._child)

    @property
    def overlays(self) -> list[Gtk.Widget]:
        return self._overlays

    def set_overlays(self, overlays: Gtk.Widget | list[Gtk.Widget]):
        self.reset_overlays()
        return self.add_overlays(overlays)

    def add_overlays(self, overlays: Gtk.Widget | list[Gtk.Widget]) -> bool:
        if isinstance(overlays, Gtk.Widget):
            overlays = [overlays]
        if isinstance(overlays, list) and all(
            isinstance(widget, Gtk.Widget) for widget in overlays
        ):
            for widget in overlays:
                self.add_overlay(widget)
                self._overlays.append(widget)
            return True
        return False

    def reset_overlays(self):
        for widget in self._overlays:
            self.remove_overlay(widget)
        return
