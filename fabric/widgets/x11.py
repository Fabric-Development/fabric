import gi
from enum import Enum
from loguru import logger
from collections.abc import Iterable
from typing import no_type_check, Literal
from fabric.core.service import Property
from fabric.widgets.window import Window
from fabric.utils import get_enum_member, extract_css_values, idle_add

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

try:
    from Xlib import X as XServer
    from Xlib.display import Display as XDisplay
    from Xlib.xobject.drawable import Window as XWindow
except Exception:
    logger.warning(
        "using Fabric under X11 might require extra dependencies for extra features, consider installing the python package Xlib"
    )


class X11WindowLayer(Enum):
    TOP = 1
    BOTTOM = 2


class X11WindowGeometry(Enum):
    CENTER = 1
    CENTER_AUTO = 2
    TOP = 3
    TOP_LEFT = 4
    TOP_RIGHT = 5
    BOTTOM = 6
    BOTTOM_LEFT = 7
    BOTTOM_RIGHT = 8
    LEFT = 9
    RIGHT = 10


class X11Window(Window):
    # it's nothing fancy, but we have to work with what we have (so far)
    """
    a dockable window for X11/Xorg

    ### NOTE
    none of the properties this window takes is guaranteed to work
    since EMWH is not a standard protocol across all window managers
    """

    @Property(X11WindowLayer, "read-write")
    def layer(self) -> X11WindowLayer:
        return self._layer

    @layer.setter
    def layer(self, value: Literal["top", "bottom"] | X11WindowLayer):
        self._layer = get_enum_member(X11WindowLayer, value, default=X11WindowLayer.TOP)
        self.do_dispatch_layer()
        return

    @Property(tuple, "read-write")
    def margin(self) -> tuple[int, int, int, int]:
        return self._margin

    @margin.setter
    def margin(self, value: str | Iterable[int]):
        # (top, right, bottom, left)
        self._margin = (
            extract_css_values(value)
            if isinstance(value, str)
            else value
            if isinstance(value, (tuple, list)) and len(value) == 4
            else (0, 0, 0, 0)
        )  # type: ignore
        self.do_dispatch_geometry()
        return

    @Property(X11WindowGeometry, "read-write")
    def geometry(self) -> X11WindowGeometry:
        return self._geometry

    @geometry.setter
    def geometry(
        self,
        value: Literal[
            "center",
            "center-auto",
            "top-left",
            "top",
            "top-right",
            "left",
            "right",
            "bottom-left",
            "bottom",
            "bottom-right",
        ]
        | X11WindowGeometry,
    ):
        self._geometry = get_enum_member(
            X11WindowGeometry, value, default=X11WindowGeometry.TOP
        )
        if self._geometry in (X11WindowGeometry.CENTER, X11WindowGeometry.CENTER_AUTO):
            # don't use our way to handle window centering, gdk can do that for us
            self.handler_disconnect(
                self._size_allocate_hook
            ) if self._size_allocate_hook is not None else None
            self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        else:
            self.do_dispatch_geometry()
            if not self._size_allocate_hook:
                self._size_allocate_hook = self.connect(
                    "size-allocate", lambda _, __: self.do_dispatch_geometry()
                )  # type: ignore
        return

    def __init__(
        self,
        type_hint: Literal[
            "normal",
            "dialog",
            "menu",
            "toolbar",
            "splashscreen",
            "utility",
            "dock",
            "desktop",
            "dropdown-menu",
            "popup-menu",
            "tooltip",
            "notification",
            "combo",
            "dnd",
        ]
        | Gdk.WindowTypeHint = Gdk.WindowTypeHint.DOCK,
        geometry: Literal[
            "center",
            "center-auto",
            "top-left",
            "top",
            "top-right",
            "left",
            "right",
            "bottom-left",
            "bottom",
            "bottom-right",
        ]
        | X11WindowGeometry = X11WindowGeometry.TOP,
        margin: str | Iterable[int] = "0px 0px 0px 0px",
        layer: Literal["top", "bottom"] | X11WindowLayer = X11WindowLayer.TOP,
        sticky: bool = True,
        focusable: bool = True,
        resizable: bool = False,
        decorated: bool = False,
        taskbar_hint: bool = False,
        pager_hint: bool = False,
        title: str = "fabric",
        type: Literal["top-level", "popup"] | Gtk.WindowType = Gtk.WindowType.TOPLEVEL,
        child: Gtk.Widget | None = None,
        pass_through: bool = False,
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

        self._margin: tuple[int, int, int, int] = (0, 0, 0, 0)
        self._layer = X11WindowLayer.TOP
        self._geometry = X11WindowGeometry.TOP
        self._size_allocate_hook: int | None = None

        self._display: Gdk.Display
        self._rectangle: Gdk.Rectangle
        self._scale_factor: int

        # for extra functionality
        self._xdisplay: "XDisplay | None" = None
        self._xwindow: "XWindow | None" = None
        self._xid: int = 0

        self.set_type_hint(
            get_enum_member(
                Gdk.WindowTypeHint, type_hint, default=Gdk.WindowTypeHint.DOCK
            )
        )
        self.set_accept_focus(focusable)
        self.set_skip_taskbar_hint(not taskbar_hint)
        self.set_skip_pager_hint(not pager_hint)
        self.set_decorated(decorated)
        self.set_resizable(resizable)
        self.stick() if sticky else self.unstick()
        # all aboard...
        self.do_initialize()
        self.do_initialize_x_backend()

        self.layer = layer
        self.margin = margin
        self.geometry = geometry

        self.show_all() if all_visible is True else self.show() if visible is True else None

    def do_initialize(self):
        self._display, self._rectangle, self._scale_factor = self.do_get_display_props()
        visual = self._display.get_default_screen().get_rgba_visual()
        self.set_visual(visual)  # to get alpha w/o a X11 compositor
        self.set_app_paintable(True)
        return

    def do_initialize_x_backend(self):
        try:
            self._xdisplay = XDisplay()
        except Exception:

            def requires_xlib(*_):
                raise RuntimeError(
                    "this method requires the python package `Xlib` to be installed"
                )

            self.steal_input_soft = requires_xlib  # type: ignore
            return

        def on_draw(*_):
            # as of my test's results, the draw signal is
            # the only signal emitted when the window is fully realized
            # and that's needed so we don't face a unexpected behavior later
            self._xid = self.get_window().get_xid()  # type: ignore
            self._xwindow = self._xdisplay.create_resource_object("window", self._xid)  # type: ignore
            # thank you, goodbye!
            self.disconnect_by_func(on_draw)

        self.connect("draw", on_draw)

    def steal_input(self) -> bool:
        if not (win := self.get_window()):
            return False
        idle_add(lambda *_: Gdk.keyboard_grab(win, False, Gdk.CURRENT_TIME))
        return True

    def unsteal_input(self):
        return idle_add(lambda *_: Gdk.keyboard_ungrab(Gdk.CURRENT_TIME))

    def steal_input_soft(self, can_release: bool = False) -> bool:
        if (
            not (self.get_realized() and self.is_visible())
            or not self._xdisplay
            or not self._xwindow
        ):
            return False
        self._xdisplay.set_input_focus(
            self._xwindow,  # type: ignore
            XServer.RevertToPointerRoot if can_release else XServer.RevertToNone,
            XServer.CurrentTime,
        )
        self._xdisplay.sync()
        self._xdisplay.flush()

        return True

    def do_get_display_props(self) -> tuple[Gdk.Display, Gdk.Rectangle, int]:
        display = Gdk.Display.get_default()
        rectangle = display.get_primary_monitor().get_geometry()
        scale_factor = display.get_primary_monitor().get_scale_factor()
        return display, rectangle, scale_factor  # type: ignore

    def do_dispatch_layer(self):
        self.set_keep_above(self._layer == X11WindowLayer.TOP)
        self.set_keep_below(self._layer == X11WindowLayer.BOTTOM)
        return

    @no_type_check
    def do_dispatch_geometry(self):
        # move the window to match the asked geometry
        # this requires us knowing the geometry and the margin
        if self._rectangle is None:
            self._display, self._rectangle, self._scale_factor = (
                self.do_get_display_props()
            )
        aloc_size, natural_size = self.get_allocated_size()
        aloc_width, aloc_height = aloc_size.width, aloc_size.height

        x = y = 0
        match self._geometry:
            # case X11WindowGeometry.CENTER_AUTO:
            #     x = self._rectangle.width // 2 - aloc_width // 2
            #     y = self._rectangle.height // 2 - aloc_height // 2
            case X11WindowGeometry.TOP:
                y = 0
                x = self._rectangle.width // 2 - aloc_width // 2
            case X11WindowGeometry.TOP_LEFT:
                x, y = 0, 0
            case X11WindowGeometry.TOP_RIGHT:
                y = 0
                x = self._rectangle.width - aloc_width
            case X11WindowGeometry.BOTTOM:
                x = self._rectangle.width // 2 - aloc_width // 2
                y = self._rectangle.height - aloc_height
            case X11WindowGeometry.BOTTOM_LEFT:
                x = 0
                y = self._rectangle.height - aloc_height
            case X11WindowGeometry.BOTTOM_RIGHT:
                x = self._rectangle.width - aloc_width
                y = self._rectangle.height - aloc_height
            case X11WindowGeometry.LEFT:
                x = 0
                y = self._rectangle.height // 2 - aloc_height // 2
            case X11WindowGeometry.RIGHT:
                x = self._rectangle.width - aloc_width
                y = self._rectangle.height // 2 - aloc_height // 2
            case _:
                return False

        x_margin = self._margin[1] - self._margin[3]
        y_margin = self._margin[0] - self._margin[2]
        x += self._rectangle.x
        y += self._rectangle.y
        x = x + x_margin
        y = y + y_margin

        return self.move(x, y)
