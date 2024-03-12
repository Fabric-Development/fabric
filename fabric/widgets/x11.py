import gi
from typing import Literal
from fabric.widgets.window import Window
from fabric.utils import extract_css_values

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib


class Window(Window):
    """
    a surface window made specifically for X11/Xorg

    this will NOT work under any other display server/environment.
    """

    def __init__(
        self,
        layer: Literal[
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
        | Gdk.WindowTypeHint = "dock",
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
        | Gdk.Gravity = "center",
        margin: str | tuple | list | None = "0px 0px 0px 0px",
        above: bool = True,
        below: bool = False,
        taskbar_hint: bool = False,
        pager_hint: bool = False,
        can_resize: bool = False,
        can_focus: bool = False,
        decorated: bool = False,
        children: Gtk.Widget | None = None,
        type: Literal["top-level", "popup"] | Gtk.WindowType = "top-level",
        main_window: bool = True,
        open_inspector: bool = False,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_compiled: bool = True,
        style_append: bool = False,
        style_add_brackets: bool = True,
        title: str | None = "fabric",
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
        default_size: tuple[int] | int | None = None,
        ignore_empty_check: bool = False,
        **kwargs,
    ):
        """

        :param layer: the layer of the window, defaults to "dock"
        :type layer: Literal["normal", "dialog", "menu", "toolbar", "splashscreen", "utility", "dock", "desktop", "dropdown"], optional
        :param geometry: the geometry of the window AKA position, defaults to "center"
        :type geometry: Literal["north-west", "north", "north-east", "west", "center", "east", "south-west", "south", "south-east"], optional
        :param margin: the margin of the window, defaults to "0px 0px 0px 0px"
        :type margin: str | tuple | list | None, optional
        :param above: whether the window should be above other windows, defaults to True
        :type above: bool, optional
        :param below: whether the window should be below other windows, defaults to False
        :type below: bool, optional
        :param taskbar_hint: whether the window should be on the taskbar, defaults to False
        :type taskbar_hint: bool, optional
        :param pager_hint: whether the window should be on the pager, defaults to False
        :type pager_hint: bool, optional
        :param decorated: whether the window should be decorated (have a title bar and borders or any other server side decorations), defaults to False
        :type decorated: bool, optional
        :param can_resize: whether the window can be resized (somehow), defaults to False
        :type can_resize: bool, optional
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
        :param default_size: the default size of the window, defaults to None
        :type default_size: tuple[int] | int | None, optional
        """
        # TODO: reflect the changes on the docstring
        # FIXME: improve me
        super().__init__(
            title,
            children,
            type,
            main_window,
            open_inspector,
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
            default_size,
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        self.ignore_empty_check = ignore_empty_check
        self.margin = margin
        self.above = above
        self.below = below
        layer = (
            layer
            if isinstance(layer, Gdk.WindowTypeHint)
            else {
                "normal": Gdk.WindowTypeHint.NORMAL,
                "dialog": Gdk.WindowTypeHint.DIALOG,
                "menu": Gdk.WindowTypeHint.MENU,
                "toolbar": Gdk.WindowTypeHint.TOOLBAR,
                "splashscreen": Gdk.WindowTypeHint.SPLASHSCREEN,
                "utility": Gdk.WindowTypeHint.UTILITY,
                "dock": Gdk.WindowTypeHint.DOCK,
                "desktop": Gdk.WindowTypeHint.DESKTOP,
                "dropdown-menu": Gdk.WindowTypeHint.DROPDOWN_MENU,
                "popup-menu": Gdk.WindowTypeHint.POPUP_MENU,
                "tooltip": Gdk.WindowTypeHint.TOOLTIP,
                "notification": Gdk.WindowTypeHint.NOTIFICATION,
                "combo": Gdk.WindowTypeHint.COMBO,
                "dnd": Gdk.WindowTypeHint.DND,
            }.get(layer.lower(), Gdk.WindowTypeHint.DOCK)
            if layer is not None
            else None
        )
        geometry = (
            geometry
            if isinstance(geometry, Gdk.Gravity)
            else {
                "center-auto": "center-auto",
                "center": Gdk.Gravity.CENTER,
                "top-left": Gdk.Gravity.NORTH_WEST,
                "top": Gdk.Gravity.NORTH,
                "top-right": Gdk.Gravity.NORTH_EAST,
                "left": Gdk.Gravity.WEST,
                "right": Gdk.Gravity.EAST,
                "bottom-left": Gdk.Gravity.SOUTH_WEST,
                "bottom": Gdk.Gravity.SOUTH,
                "bottom-right": Gdk.Gravity.SOUTH_EAST,
            }.get(geometry.lower(), Gdk.Gravity.CENTER)
            if isinstance(geometry, str)
            else None
        )

        self.display: Gdk.Display = None
        self.rectangle: Gdk.Rectangle = None
        self.scale_factor: int = None

        self.set_type_hint(layer) if layer is not None else None
        self.set_default_size(*default_size) if default_size is not None else None
        self.set_accept_focus(can_focus) if can_focus is not None else None

        # setting some window props with EXTREME type checking
        self.set_skip_taskbar_hint(not taskbar_hint) if taskbar_hint == True else None
        self.set_skip_pager_hint(not pager_hint) if pager_hint == True else None
        self.set_decorated(decorated)
        self.set_resizable(can_resize) if can_resize is not None else None
        self.init_window()

        if isinstance(geometry, Gdk.Gravity) and geometry == Gdk.Gravity.CENTER:
            # not using our way to handle window centering beacuse gdk already had one
            self.set_position(Gtk.WindowPosition.CENTER)
        elif geometry is not None:
            # auto remap window to it's proper position (when window size changes)
            self.set_geometry(geometry, margin)
            self.connect(
                "size-allocate",
                lambda _, __: self.set_geometry(geometry),
            )
        self.do_connect_signals_for_kwargs(kwargs)

    def init_window(
        self,
    ):
        if self.display is None:
            self.display, self.rectangle, self.scale_factor = self.get_display_props()
        self.set_app_paintable(True)
        self.set_visual(self.display.get_default_screen().get_rgba_visual())
        return

    def set_z_axis(self):
        self.set_keep_above(self.above) if self.above is not None else None
        self.set_keep_below(self.above) if self.below is not None else None
        return

    def get_display_props(self) -> tuple[Gdk.Display, Gdk.Rectangle, int]:
        display = Gdk.Display.get_default()
        rectangle = display.get_primary_monitor().get_geometry()
        scale_factor = display.get_primary_monitor().get_scale_factor()
        return display, rectangle, scale_factor

    def set_geometry(
        self, geometry: Gdk.Gravity, margin: str | tuple[int] | list[int] | None = None
    ):
        if self.rectangle is None:
            self.display, self.rectangle, self.scale_factor = self.get_display_props()
        aloc_size, natural_size = self.get_allocated_size()
        aloc_width, aloc_height = aloc_size.width, aloc_size.height
        margin = (
            margin
            if margin is not None
            else self.margin
            if self.margin is not None
            else (0, 0, 0, 0)
        )
        margin = (
            extract_css_values(margin)
            if isinstance(margin, str)
            else margin
            if isinstance(margin, (tuple, list)) and len(margin) == 4
            else [0, 0, 0, 0]
            # top right bottom left
        )
        x = y = 0
        x_margin = y_margin = 0
        match geometry:
            case "center-auto":
                x = self.rectangle.width // 2 - aloc_width // 2
                y = self.rectangle.height // 2 - aloc_height // 2
            case Gdk.Gravity.NORTH_WEST:
                x, y = 0, 0
            case Gdk.Gravity.NORTH:
                y = 0
                x = self.rectangle.width // 2 - aloc_width // 2
            case Gdk.Gravity.NORTH_EAST:
                y = 0
                x = self.rectangle.width - aloc_width
            case Gdk.Gravity.WEST:
                x = 0
                y = self.rectangle.height // 2 - aloc_height // 2
            case Gdk.Gravity.EAST:
                x = self.rectangle.width - aloc_width
                y = self.rectangle.height // 2 - aloc_height // 2
            case Gdk.Gravity.SOUTH_WEST:
                x = 0
                y = self.rectangle.height - aloc_height
            case Gdk.Gravity.SOUTH:
                x = self.rectangle.width // 2 - aloc_width // 2
                y = self.rectangle.height - aloc_height
            case Gdk.Gravity.SOUTH_EAST:
                x = self.rectangle.width - aloc_width
                y = self.rectangle.height - aloc_height
            case _:  # Gravity.STATIC or default
                return False

        x_margin = margin[1] - margin[3]
        y_margin = margin[0] - margin[2]
        x += self.rectangle.x
        y += self.rectangle.y
        x = x + x_margin
        y = y + y_margin

        return self.move(x, y)

    def show(self):
        # showing an empty window will result a glitched window
        if self.ignore_empty_check is False and len(self.get_children()) >= 1:
            super().show()
            self.set_z_axis()
            return
        return False

    def show_all(self):
        if self.ignore_empty_check is False and len(self.get_children()) >= 1:
            self.style_provider
            super().show_all()
            self.set_z_axis()
        return False


if __name__ == "__main__":
    from fabric.widgets.revealer import Revealer
    from fabric.widgets.button import Button
    from fabric.widgets.box import Box
    from fabric import start

    reveal = Revealer(
        transition_type="slide-right",
        transition_duration=1500,
        children=Button(label="|------------>", visible=True),
    )

    is_rev = False

    def toggle_reveal():
        global is_rev
        reveal.set_reveal_child(not is_rev)
        is_rev = not is_rev
        return True

    GLib.timeout_add(1000, toggle_reveal)

    window = Window(
        children=Box(
            children=[
                Button(
                    label="X11 Window Test",
                ),
                reveal,
            ],
        ),
        all_visible=True,
    )
    start()
