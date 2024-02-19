import gi
from typing import Literal
from fabric.widgets.window import Window
from fabric.utils import extract_css_values, extract_anchor_values

gi.require_version("Gtk", "3.0")
gi.require_version("GtkLayerShell", "0.1")
from gi.repository import Gtk, Gdk, GtkLayerShell


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
        exclusive: bool = True,
        monitor: int | Gdk.Monitor | None = None,
        children: Gtk.Widget | None = None,
        title: str | None = "fabric",
        type: Literal["top-level", "popup"] | Gtk.WindowType = "top-level",
        visible: bool = True,
        all_visible: bool = True,
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
        **kwargs,
    ):
        """
        :param layer: the window layer, defaults to "background"
        :type layer: Literal["background", "bottom", "top", "overlay"] | GtkLayerShell.Layer
        :param anchor: the window anchor it can be one of "top", "bottom", "left", "right" or two or more values separated by space like "top right", defaults to ""
        :type anchor: str, optional
        :param margin: the window margin in the format of "top right bottom left" AKA css values, defaults to "0px 0px 0px 0px"
        :type margin: str, optional
        :param title: the window title which will be displayed in the window title bar, defaults to "fabric"
        :type title: str | None, optional
        :param exclusive: whether this window should reserve space or not, defaults to True
        :type exclusive: bool, optional
        :param monitor: the monitor this window should open at, None means to let the compositor decides which monitor to open at, defaults to None
        :type monitor: int | Gdk.Monitor | None, optional
        :param children: the child widget (single widget), defaults to None
        :type children: Gtk.Widget | None, optional
        :param type: the type of this window, "top-level" means a normal window, defaults to "top-level"
        :type type: Literal["top-level", "popup"] | Gtk.WindowType, optional
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
        :type size: tuple[int] | None, optional
        :param default_size: the default size of the window, defaults to None
        :type default_size: tuple[int, int] | None, optional
        :param ignore_empty_check: whether to disable the checks on this window if it was empty or not before showing it (because this freaks up some compositors) or not, defaults to False
        :type ignore_empty_check: bool, optional
        """
        super().__init__(
            title,
            children,
            type,
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
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        self.ignore_empty_check = ignore_empty_check
        GtkLayerShell.init_for_window(self)
        self.set_monitor(monitor) if monitor is not None else None
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
        self.do_connect_signals_for_kwargs(kwargs)

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

    def set_monitor(self, monitor: int | Gdk.Monitor) -> None | bool:
        if isinstance(monitor, int):
            display = Gdk.Display().get_default()
            monitor = display.get_monitor(monitor) if display is not None else None
        elif isinstance(monitor, Gdk.Monitor):
            monitor = monitor
        return (
            GtkLayerShell.set_monitor(self, monitor) if monitor is not None else False
        )
