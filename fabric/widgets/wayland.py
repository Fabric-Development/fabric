import gi
import re
from enum import Enum
from typing import cast, Literal
from collections.abc import Iterable
from fabric.core.service import Property
from fabric.widgets.window import Window
from fabric.utils.helpers import extract_css_values, get_enum_member

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

try:
    gi.require_version("GtkLayerShell", "0.1")
    from gi.repository import GtkLayerShell
except:
    raise ImportError(
        "looks like we don't have gtk-layer-shell installed, make sure to install it first (as well as using wayland)"
    )


class WaylandWindowExclusivity(Enum):
    NONE = 1
    NORMAL = 2
    AUTO = 3


class WaylandWindow(Window):
    @Property(
        GtkLayerShell.Layer,
        flags="read-write",
        default_value=GtkLayerShell.Layer.TOP,
    )
    def layer(self) -> GtkLayerShell.Layer:  # type: ignore
        return self._layer  # type: ignore

    @layer.setter
    def layer(
        self,
        value: Literal["background", "bottom", "top", "overlay"] | GtkLayerShell.Layer,
    ) -> None:
        self._layer = get_enum_member(
            GtkLayerShell.Layer, value, default=GtkLayerShell.Layer.TOP
        )
        return GtkLayerShell.set_layer(self, self._layer)

    @Property(int, "read-write")
    def monitor(self) -> int:
        if not (monitor := cast(Gdk.Monitor, GtkLayerShell.get_monitor(self))):
            return -1
        display = monitor.get_display() or Gdk.Display.get_default()
        for i in range(0, display.get_n_monitors()):
            if display.get_monitor(i) is monitor:
                return i
        return -1

    @monitor.setter
    def monitor(self, monitor: int | Gdk.Monitor) -> bool:
        if isinstance(monitor, int):
            display = Gdk.Display().get_default()
            monitor = display.get_monitor(monitor)
        return (
            (GtkLayerShell.set_monitor(self, monitor), True)[1]
            if monitor is not None
            else False
        )

    @Property(WaylandWindowExclusivity, "read-write")
    def exclusivity(self) -> WaylandWindowExclusivity:
        return self._exclusivity

    @exclusivity.setter
    def exclusivity(
        self, value: Literal["none", "normal", "auto"] | WaylandWindowExclusivity
    ) -> None:
        value = get_enum_member(
            WaylandWindowExclusivity, value, default=WaylandWindowExclusivity.NONE
        )
        self._exclusivity = value
        match value:
            case WaylandWindowExclusivity.NORMAL:
                return GtkLayerShell.set_exclusive_zone(self, True)
            case WaylandWindowExclusivity.AUTO:
                return GtkLayerShell.auto_exclusive_zone_enable(self)
            case _:
                return GtkLayerShell.set_exclusive_zone(self, False)

    @Property(
        GtkLayerShell.KeyboardMode,
        "read-write",
        default_value=GtkLayerShell.KeyboardMode.NONE,
    )
    def keyboard_mode(self) -> GtkLayerShell.KeyboardMode:
        return self._keyboard_mode

    @keyboard_mode.setter
    def keyboard_mode(
        self,
        value: Literal[
            "none",
            "exclusive",
            "on-demand",
            "entry-number",
        ]
        | GtkLayerShell.KeyboardMode,
    ):
        self._keyboard_mode = get_enum_member(
            GtkLayerShell.KeyboardMode, value, default=GtkLayerShell.KeyboardMode.NONE
        )
        return GtkLayerShell.set_keyboard_mode(self, self._keyboard_mode)

    @Property(tuple[GtkLayerShell.Edge, ...], "read-write")
    def anchor(self):
        return tuple(
            x
            for x in [
                GtkLayerShell.Edge.TOP,
                GtkLayerShell.Edge.RIGHT,
                GtkLayerShell.Edge.BOTTOM,
                GtkLayerShell.Edge.LEFT,
            ]
            if GtkLayerShell.get_anchor(self, x)
        )

    @anchor.setter
    def anchor(self, value: str | Iterable[GtkLayerShell.Edge]) -> None:
        self._anchor = value
        if isinstance(value, (list, tuple)) and all(
            isinstance(edge, GtkLayerShell.Edge) for edge in value
        ):
            for edge in [
                GtkLayerShell.Edge.TOP,
                GtkLayerShell.Edge.RIGHT,
                GtkLayerShell.Edge.BOTTOM,
                GtkLayerShell.Edge.LEFT,
            ]:
                if edge not in value:
                    GtkLayerShell.set_anchor(self, edge, False)
                GtkLayerShell.set_anchor(self, edge, True)
            return
        elif isinstance(value, str):
            for edge, anchored in WaylandWindow.extract_edges_from_string(
                value
            ).items():
                GtkLayerShell.set_anchor(self, edge, anchored)

        return

    @Property(tuple[int, ...], flags="read-write")
    def margin(self) -> tuple[int, ...]:
        return tuple(
            GtkLayerShell.get_margin(self, x)
            for x in [
                GtkLayerShell.Edge.TOP,
                GtkLayerShell.Edge.RIGHT,
                GtkLayerShell.Edge.BOTTOM,
                GtkLayerShell.Edge.LEFT,
            ]
        )

    @margin.setter
    def margin(self, value: str | Iterable[int]) -> None:
        for edge, mrgv in WaylandWindow.extract_margin(value).items():
            GtkLayerShell.set_margin(self, edge, mrgv)
        return

    @Property(object, "read-write")
    def keyboard_mode(self):
        kb_mode = GtkLayerShell.get_keyboard_mode(self)
        if GtkLayerShell.get_keyboard_interactivity(self):
            kb_mode = GtkLayerShell.KeyboardMode.EXCLUSIVE
        return kb_mode

    @keyboard_mode.setter
    def keyboard_mode(
        self,
        value: Literal["none", "exclusive", "on-demand"] | GtkLayerShell.KeyboardMode,
    ):
        return GtkLayerShell.set_keyboard_mode(
            self,
            get_enum_member(
                GtkLayerShell.KeyboardMode,
                value,
                default=GtkLayerShell.KeyboardMode.NONE,
            ),
        )

    def __init__(
        self,
        layer: Literal["background", "bottom", "top", "overlay"]
        | GtkLayerShell.Layer = GtkLayerShell.Layer.TOP,
        anchor: str = "",
        margin: str | Iterable[int] = "0px 0px 0px 0px",
        exclusivity: Literal["auto", "normal", "none"]
        | WaylandWindowExclusivity = WaylandWindowExclusivity.NONE,
        keyboard_mode: Literal["none", "exclusive", "on-demand"]
        | GtkLayerShell.KeyboardMode = GtkLayerShell.KeyboardMode.NONE,
        pass_through: bool = False,
        monitor: int | Gdk.Monitor | None = None,
        title: str = "fabric",
        type: Literal["top-level", "popup"] | Gtk.WindowType = Gtk.WindowType.TOPLEVEL,
        child: Gtk.Widget | None = None,
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
        Window.__init__(
            self,
            title,
            type,
            child,
            pass_through,
            name,
            False,
            False,
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
        self._layer = GtkLayerShell.Layer.ENTRY_NUMBER
        self._keyboard_mode = GtkLayerShell.KeyboardMode.NONE
        self._anchor = anchor
        self._exclusivity = WaylandWindowExclusivity.NONE

        GtkLayerShell.init_for_window(self)
        GtkLayerShell.set_namespace(self, title)
        self.connect(
            "notify::title",
            lambda *_: GtkLayerShell.set_namespace(self, self.get_title()),
        )
        if monitor is not None:
            self.monitor = monitor
        self.layer = layer
        self.anchor = anchor
        self.margin = margin
        self.keyboard_mode = keyboard_mode
        self.exclusivity = exclusivity
        self.show_all() if all_visible is True else self.show() if visible is True else None

    def steal_input(self) -> None:
        return GtkLayerShell.set_keyboard_interactivity(self, True)

    def return_input(self) -> None:
        return GtkLayerShell.set_keyboard_interactivity(self, False)

    @staticmethod
    def extract_anchor_values(string: str) -> tuple[str, ...]:
        """
        extracts the geometry values from a given geometry string.

        :param string: the string containing the geometry values.
        :type string: str
        :return: a list of unique directions extracted from the geometry string.
        :rtype: list
        """
        direction_map = {"l": "left", "t": "top", "r": "right", "b": "bottom"}
        pattern = re.compile(r"\b(left|right|top|bottom)\b", re.IGNORECASE)
        matches = pattern.findall(string)
        return tuple(set(tuple(direction_map[match.lower()[0]] for match in matches)))

    @staticmethod
    def extract_edges_from_string(string: str) -> dict["GtkLayerShell.Edge", bool]:
        anchor_values = WaylandWindow.extract_anchor_values(string.lower())
        return {
            GtkLayerShell.Edge.TOP: "top" in anchor_values,
            GtkLayerShell.Edge.RIGHT: "right" in anchor_values,
            GtkLayerShell.Edge.BOTTOM: "bottom" in anchor_values,
            GtkLayerShell.Edge.LEFT: "left" in anchor_values,
        }

    @staticmethod
    def extract_margin(input: str | Iterable[int]) -> dict["GtkLayerShell.Edge", int]:
        margins = (
            extract_css_values(input.lower())
            if isinstance(input, str)
            else input
            if isinstance(input, (tuple, list)) and len(input) == 4
            else (0, 0, 0, 0)
        )
        return {
            GtkLayerShell.Edge.TOP: margins[0],
            GtkLayerShell.Edge.RIGHT: margins[1],
            GtkLayerShell.Edge.BOTTOM: margins[2],
            GtkLayerShell.Edge.LEFT: margins[3],
        }
