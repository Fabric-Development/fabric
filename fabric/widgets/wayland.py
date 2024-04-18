import gi
import cairo
from loguru import logger
from typing import Literal
from fabric.service import Property
from fabric.widgets.window import Window
from fabric.utils import extract_margin_from_string, extract_edges_from_string

gi.require_version("Gtk", "3.0")
gi.require_version("GtkLayerShell", "0.1")
from gi.repository import Gtk, Gdk, GtkLayerShell


class Window(Window):
    """
    a layer window for wayland

    NOTE: Please do NOT show up am empty layer window.
    some compositors might freak out if you do so.
    read the [FAQ](https://fabric-development.github.io/fabric-wiki/faq.html) for more info.
    """

    def __init__(
        self,
        layer: Literal["background", "bottom", "top", "overlay"] | GtkLayerShell.Layer,
        keyboard_mode: Literal["none", "exclusive", "on-demand"]
        | GtkLayerShell.KeyboardMode = "none",
        anchor: str = "",
        margin: str | list[GtkLayerShell.Edge] = "0px 0px 0px 0px",
        exclusive: bool = True,
        exclusivity: Literal["auto", "normal"] = "auto",
        pass_through: bool = False,
        monitor: int | Gdk.Monitor | None = None,
        children: Gtk.Widget | None = None,
        title: str | None = "fabric",
        type: Literal["top-level", "popup"] | Gtk.WindowType = "top-level",
        main_window: bool = True,
        open_inspector: bool = False,
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
        :param exclusivity: the window exclusivity mode, defaults to "auto"
        :type exclusivity: Literal["auto", "normal"], optional
        :param pass_through: whether this window should pass-through mouse events to other windows or not, defaults to False
        :type pass_through: bool, optional
        :param monitor: the monitor this window should open at, None means to let the compositor decides which monitor to open at, defaults to None
        :type monitor: int | Gdk.Monitor | None, optional
        :param children: the child widget (single widget), defaults to None
        :type children: Gtk.Widget | None, optional
        :param type: the type of this window, "top-level" means a normal window, defaults to "top-level"
        :type type: Literal["top-level", "popup"] | Gtk.WindowType, optional
        :param main_window: whether this window is the main window (exit on close), defaults to True
        :type main_window: bool, optional
        :param open_inspector: whether to open the inspector for this window, useful for debugging, defaults to False
        :type open_inspector: bool, optional
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
        :param default_size: the default size of the window, defaults to None
        :type default_size: tuple[int, int] | None, optional
        """
        super().__init__(
            None,
            children,
            type,
            main_window,
            open_inspector,
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
        self.__initialized = False  # secrets
        self._layer = layer
        self._keyboard_mode = keyboard_mode
        self._anchor = anchor
        self._margin = margin
        self._exclusive = exclusive
        self._exclusivity = exclusivity
        self._pass_through = pass_through
        self._monitor = monitor

        self.do_initialize_layer()
        self.set_monitor(monitor) if monitor is not None else None
        self.set_exclusive(exclusive, exclusivity)
        self.set_layer(layer)
        self.set_keyboard_mode(keyboard_mode)
        self.set_anchor(anchor)
        self.set_margin(margin)
        self.set_pass_through(pass_through)
        self.set_title(title) if title is not None else None
        # all aboard, window is ready to be shown
        self.show_all() if all_visible is True else self.show() if visible is True else None
        self.do_connect_signals_for_kwargs(kwargs)

    @Property(value_type=object, flags="read-write")
    def layer(self) -> str | GtkLayerShell.Layer:
        return self._layer

    @layer.setter
    def layer(self, value: str | GtkLayerShell.Layer) -> None:
        self._layer = value
        self.set_layer(value)
        return

    @Property(value_type=object, flags="read-write")
    def keyboard_mode(self) -> str | GtkLayerShell.KeyboardMode:
        return self._keyboard_mode

    @keyboard_mode.setter
    def keyboard_mode(self, value: str | GtkLayerShell.KeyboardMode):
        self._keyboard_mode = value
        self.set_keyboard_mode(value)

    @Property(value_type=object, flags="read-write")
    def anchor(self) -> str | list[GtkLayerShell.Edge]:
        return self._anchor

    @anchor.setter
    def anchor(self, value: str | list[GtkLayerShell.Edge]) -> None:
        self._anchor = value
        self.set_anchor(self, value)
        return

    @Property(value_type=object, flags="read-write")
    def margin(self) -> str | tuple[int]:
        return self._margin

    @margin.setter
    def margin(self, value: str | tuple[int]) -> None:
        self._margin = value
        self.set_margin(self, value)
        return

    @Property(value_type=object, flags="read-write")
    def pass_through(self) -> bool:
        return self._pass_through

    @pass_through.setter
    def pass_through(self, value: bool) -> None:
        self._pass_through = value
        self.set_pass_through(self, value)
        return

    @Property(value_type=object, flags="read-write")
    def exclusive(self) -> bool:
        return self._exclusive

    @exclusive.setter
    def exclusive(self, value: bool) -> None:
        self._exclusive = value
        self.set_exclusive(self, value)
        return

    @Property(value_type=object, flags="read-write")
    def exclusivity(self) -> Literal["auto", "normal"]:
        return self._exclusivity

    @exclusivity.setter
    def exclusivity(self, value: Literal["auto", "normal"]) -> None:
        self._exclusivity = value
        self.set_exclusive(self, value)
        return

    def do_initialize_layer(self) -> None:
        GtkLayerShell.init_for_window(self)
        self.__initialized = True
        return

    def set_layer(self, layer: str | GtkLayerShell.Layer) -> None:
        if not isinstance(layer, (str, GtkLayerShell.Layer)):
            raise TypeError(
                f"layer must be str or GtkLayerShell.Layer, but got {type(layer)}"
            )
        if isinstance(layer, str):
            layer = {
                "background": GtkLayerShell.Layer.BACKGROUND,
                "bottom": GtkLayerShell.Layer.BOTTOM,
                "top": GtkLayerShell.Layer.TOP,
                "overlay": GtkLayerShell.Layer.OVERLAY,
                "entry-number": GtkLayerShell.Layer.ENTRY_NUMBER,
            }.get(layer, GtkLayerShell.Layer.TOP)
        GtkLayerShell.set_layer(self, layer)
        return

    def set_keyboard_mode(
        self, keyboard_mode: str | GtkLayerShell.KeyboardMode
    ) -> None:
        if not isinstance(keyboard_mode, (str, GtkLayerShell.Layer)):
            raise TypeError(
                f"keyboard_mode must be str or GtkLayerShell.KeyboardMode, but got {type(keyboard_mode)}"
            )
        if isinstance(keyboard_mode, str):
            keyboard_mode = {
                "none": GtkLayerShell.KeyboardMode.NONE,
                "exclusive": GtkLayerShell.KeyboardMode.EXCLUSIVE,
                "on-demand": GtkLayerShell.KeyboardMode.ON_DEMAND,
                "entry-number": GtkLayerShell.KeyboardMode.ENTRY_NUMBER,
            }.get(keyboard_mode, GtkLayerShell.KeyboardMode.NONE)
        return GtkLayerShell.set_keyboard_mode(self, keyboard_mode)

    def set_margin(self, margins: str | tuple[int]) -> None:
        if isinstance(margins, str):
            for edge, value in extract_margin_from_string(margins).items():
                GtkLayerShell.set_margin(self, edge, value)
        elif isinstance(margins, tuple) and len(margins) == 4:
            for edge, value in zip(
                [
                    GtkLayerShell.Edge.TOP,
                    GtkLayerShell.Edge.RIGHT,
                    GtkLayerShell.Edge.BOTTOM,
                    GtkLayerShell.Edge.LEFT,
                ],
                margins,
            ):
                GtkLayerShell.set_margin(self, edge, value)
        return

    def set_anchor(self, edges: str | list[GtkLayerShell.Edge]) -> None:
        if isinstance(edges, list) and all(
            isinstance(edge, GtkLayerShell.Edge) for edge in edges
        ):
            for edge in [
                GtkLayerShell.Edge.TOP,
                GtkLayerShell.Edge.RIGHT,
                GtkLayerShell.Edge.BOTTOM,
                GtkLayerShell.Edge.LEFT,
            ]:
                if edge not in edges:
                    GtkLayerShell.set_anchor(self, edge, False)
                GtkLayerShell.set_anchor(self, edge, True)
            return
        elif isinstance(edges, str):
            for edge, value in extract_edges_from_string(edges).items():
                GtkLayerShell.set_anchor(self, edge, value)
        return

    def set_monitor(self, monitor: int | Gdk.Monitor | None) -> None | bool:
        if not isinstance(monitor, (int, Gdk.Monitor, type(None))):
            raise TypeError(
                f"monitor must be int or Gdk.Monitor, but got {type(monitor)}"
            )
        if isinstance(monitor, int):
            display = Gdk.Display().get_default()
            monitor = display.get_monitor(monitor) if display is not None else None
        return (
            GtkLayerShell.set_monitor(self, monitor) if monitor is not None else False
        )

    def set_pass_through(self, pass_through: bool = False) -> None:
        region = cairo.Region() if pass_through is True else None
        self.input_shape_combine_region(region)
        del region
        return

    def set_exclusive(
        self, exclusive: bool = True, mode: Literal["auto", "normal"] = "auto"
    ) -> None:
        if mode == "normal":
            return GtkLayerShell.set_exclusive_zone(self, exclusive)
        return GtkLayerShell.auto_exclusive_zone_enable(self) if exclusive else None

    def get_exclusivity(self) -> tuple[bool, Literal["auto", "normal"]]:
        return self._exclusive, self._exclusivity

    # custom overrides
    def show(self):
        self.do_warn_if_no_children()
        return super().show()

    def show_all(self):
        self.do_warn_if_no_children()
        return super().show_all()

    def do_warn_if_no_children(self) -> None:
        if self.get_children() == []:
            logger.warning(
                "[Window] showing an empty window is not recommended, some compositors might freak out."
            )
        return

    def set_title(self, title: str) -> None:
        GtkLayerShell.set_namespace(self, title) if self.__initialized else None
        # if not initialized, we just return safely
        # manually initializing the layer ain't a good idea
        return super().set_title(title)
