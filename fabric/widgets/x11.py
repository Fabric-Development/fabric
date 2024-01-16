import gi
from typing import Literal
from fabric.widgets.window import Window

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
            "north-west",
            "north",
            "north-east",
            "west",
            "center",
            "east",
            "south-west",
            "south",
            "south-east",
        ]
        | Gdk.Gravity = "center",
        taskbar_hint: bool = False,
        pager_hint: bool = False,
        decorated: bool = False,
        can_resize: bool = False,
        children: list[Gtk.Widget] | Gtk.Widget | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_compiled: bool = True,
        style_append: bool = False,
        style_add_brackets: bool = True,
        title: str | None = "fabric",
        name: str | None = None,
        default_size: tuple[int] | None = None,
        **kwargs,
    ):
        # FIXME: improve me
        super().__init__(
            children,
            visible,
            all_visible,
            style,
            style_compiled,
            style_append,
            style_add_brackets,
            title,
            name,
            **kwargs,
        )
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
        )
        geometry = (
            geometry
            if isinstance(geometry, Gdk.Gravity)
            else {
                "north-west": Gdk.Gravity.NORTH_WEST,
                "north": Gdk.Gravity.NORTH,
                "north-east": Gdk.Gravity.NORTH_EAST,
                "west": Gdk.Gravity.WEST,
                "center": Gdk.Gravity.CENTER,
                "east": Gdk.Gravity.EAST,
                "south-west": Gdk.Gravity.SOUTH_WEST,
                "south": Gdk.Gravity.SOUTH,
                "south-east": Gdk.Gravity.SOUTH_EAST,
            }.get(geometry.lower(), Gdk.Gravity.CENTER)
        )

        self.display = self.rectangle = None
        self.get_primary_monitor_geometry()

        self.set_type_hint(layer)
        self.set_container_size(default_size) if default_size != None else None

        # setting some window props with EXTREME type checking
        self.set_skip_taskbar_hint(not taskbar_hint) if taskbar_hint == True else None
        self.set_skip_pager_hint(not pager_hint) if pager_hint == True else None
        self.set_decorated(decorated)
        self.set_resizable(can_resize) if can_resize != None or type(
            can_resize
        ) == bool else None
        self.init_window()

        if (isinstance(geometry, str) and geometry.lower() == "center") or (
            isinstance(geometry, Gdk.Gravity) and geometry == Gdk.Gravity.CENTER
        ):
            # not using our way to handle window centering beacuse gdk already had one
            self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        else:
            # auto remap window to it's proper position (when window size changes)
            self.set_window_geometry(geometry)
            self.connect(
                "size-allocate",
                lambda _, __: self.set_window_geometry(geometry),
            )

    def init_window(
        self,
    ):
        if self.display is None:
            self.get_primary_monitor_geometry()
        self.set_app_paintable(True)
        self.set_keep_above(True)
        self.set_accept_focus(False)
        self.set_visual(self.display.get_default_screen().get_rgba_visual())
        return

    def get_primary_monitor_geometry(self):
        self.display = Gdk.Display.get_default()
        self.rectangle = self.display.get_primary_monitor().get_geometry()
        return self.display, self.rectangle

    def set_window_geometry(self, geometry: Gdk.Gravity):
        if self.rectangle is None:
            self.get_primary_monitor_geometry()
        min_size, natural_size = self.get_preferred_size()
        min_width, min_height = min_size.width, min_size.height
        # natural_width, natural_height = natural_size.width, natural_size.height
        x, y = 0, 0
        match geometry:
            case Gdk.Gravity.NORTH_WEST:
                x, y = 0, 0
            case Gdk.Gravity.NORTH:
                y = 0
                x = self.rectangle.width // 2 - min_width // 2
            case Gdk.Gravity.NORTH_EAST:
                y = 0
                x = self.rectangle.width - min_width
            case Gdk.Gravity.WEST:
                x = 0
                y = self.rectangle.height // 2 - min_height // 2
            case Gdk.Gravity.CENTER:
                x = self.rectangle.width // 2 - min_width // 2
                y = self.rectangle.height // 2 - min_height // 2
            case Gdk.Gravity.EAST:
                x = self.rectangle.width - min_width
                y = self.rectangle.height // 2 - min_height // 2
            case Gdk.Gravity.SOUTH_WEST:
                x = 0
                y = self.rectangle.height - min_height
            case Gdk.Gravity.SOUTH:
                x = self.rectangle.width // 2 - min_width // 2
                y = self.rectangle.height - min_height
            case Gdk.Gravity.SOUTH_EAST:
                x = self.rectangle.width - min_width
                y = self.rectangle.height - min_height
            case _:  # Gravity.STATIC or default
                return
        x += self.rectangle.x
        y += self.rectangle.y
        # placeholder for logging
        self.move(x, y)
        return self


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
