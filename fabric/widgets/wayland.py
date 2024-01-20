import gi
from typing import Literal
from fabric.utils.helpers import extract_css_values, extract_anchor_values
from fabric.widgets.window import Window

gi.require_version("Gtk", "3.0")
gi.require_version("GtkLayerShell", "0.1")
from gi.repository import Gtk, GtkLayerShell


class Window(Window):
    """
    Wayland layer window.

    NOTE: Please do NOT show up a empty layer window, some compositors freak out if you do.
    """

    def __init__(
        self,
        layer: Literal["background", "bottom", "top", "overlay"] | GtkLayerShell.Layer,
        anchor: str = "",
        margin: str = "0px 0px 0px 0px",
        title: str | None = "fabric",
        visible: bool = True,
        all_visible: bool = True,
        exclusive: bool = True,
        children: Gtk.Widget | None = None,
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
        default_size: tuple[int, int] | None = None,
        ignore_empty_check: bool = False,
        **kwarg,
    ):
        """
        :param layer: The window layer. Can be one of `"background"`, `"bottom"`, `"top"`, `"overlay"`.
        :param anchor: The anchor of the window. it can be a string of the anchor values, for example `"left top right bottom"`.
        :param margin: The margin of the window. it can be a string of the margin values using the css format (`"top[px] right[px] bottom[px] left[px]"`).
        :param visible: Whether the window is initially visible.
        :param all_visible: Whether all child widgets are initially visible.
        :param exclusive: Whether the window is exclusive.
        :param children: The child widget of the window. (NOTE: windows cannot have more than one child widget)
        :param title: The title of the layer window.
        :param name: The name of the widget. translates to the css class.
        :param style: The css style of the this widget.
        :param ignore_empty_check: Whether to ignore if this window is empty or not before showing it.
        :param default_size: The default window size.
        :param kwarg: Additional keyword arguments passed to the `Gtk.Window` super class.

        :returns: None
        """
        super().__init__(
            title,
            children,
            None,
            None,
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
            default_size,
            **kwarg,
        )
        self.ignore_empty_check = ignore_empty_check
        GtkLayerShell.init_for_window(self)
        GtkLayerShell.set_namespace(self, title)
        GtkLayerShell.auto_exclusive_zone_enable(self) if exclusive else None
        layer = (
            layer
            if isinstance(layer, GtkLayerShell.Layer)
            else {
                "background": GtkLayerShell.Layer.BACKGROUND,
                "bottom": GtkLayerShell.Layer.BOTTOM,
                "top": GtkLayerShell.Layer.TOP,
                "overlay": GtkLayerShell.Layer.OVERLAY,
                "entry-number": GtkLayerShell.Layer.ENTRY_NUMBER,
            }.get(layer, GtkLayerShell.Layer.TOP)
        )
        GtkLayerShell.set_layer(self, layer)
        self.set_anchor(anchor)
        self.set_margin(margin)
        self.show_all() if all_visible else self.show() if visible else None

    def show(self):
        # this is a top level window
        # showing it empty will freak some compositors.
        return (
            super().show()
            if (len(self.get_children()) >= 1) and not self.ignore_empty_check
            else False
        )

    def show_all(self):
        return (
            super().show_all()
            if (len(self.get_children()) >= 1) and not self.ignore_empty_check
            else False
        )

    def set_margin(self, margin: str | tuple):
        if isinstance(margin, str):
            margin = extract_css_values(margin)
        for i, m in enumerate(
            [
                GtkLayerShell.Edge.TOP,
                GtkLayerShell.Edge.RIGHT,
                GtkLayerShell.Edge.BOTTOM,
                GtkLayerShell.Edge.LEFT,
            ]
        ):
            GtkLayerShell.set_margin(self, m, margin[i])
        return

    def set_anchor(self, edges: str | list[GtkLayerShell.Edge]):
        edge_map = {
            "top": GtkLayerShell.Edge.TOP,
            "right": GtkLayerShell.Edge.RIGHT,
            "bottom": GtkLayerShell.Edge.BOTTOM,
            "left": GtkLayerShell.Edge.LEFT,
            "entry-number": GtkLayerShell.Edge.ENTRY_NUMBER,
        }
        if isinstance(edges, str):
            edge_names = extract_anchor_values(edges)
            edges = []
            for edge in edge_names:
                edge = edge_map.get(edge)
                edges.append(edge) if edge is not None else None
        for edge in edges:
            GtkLayerShell.set_anchor(self, edge, True)
        return
