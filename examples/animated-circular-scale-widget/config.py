import gi
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.scale import Scale
from fabric.widgets.label import Label
from fabric.widgets.x11 import X11Window as Window
from fabric.widgets.circularscale import CircularScale
from fabric.utils import get_relative_path, monitor_file

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk # type: ignore

class AnimatedCircularScale(CircularScale):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animator = (
            Animator(
                # edit the following parameters to customize the animation
                bezier_curve=(0.15, 0.88, 0.68, 0.95),
                duration=0.8,
                min_value=self.min_value,
                max_value=self.value,
                tick_widget=self,
                notify_value=lambda p, *_: self.set_value(p.value),
            )
            .build()
            .play()
            .unwrap()
        )

    def animate_value(self, value: float):
        self.animator.pause()
        self.animator.min_value = self.value
        self.animator.max_value = value
        self.animator.play()
        return


if __name__ == "__main__":
    DEFAULT = 50

    scale = AnimatedCircularScale(
        name="demo-circular-scale",
        min_value=0,
        max_value=100,
        start_angle=-90,
        end_angle=270,
        h_expand=True,
        v_expand=True,
        child=Label(),
    )

    h_scale = Scale(
        name="demo-scale",
        orientation="h",
        min_value=0,
        max_value=100,
        increments=(1, 1),
    )
    h_scale.connect("value-changed", lambda s: scale.animate_value(s.get_value()))
    
    # init
    h_scale.set_value(DEFAULT)

    def on_value_change(widget, value):
        if child := widget.get_child():
            child.set_text(f"{int(widget.value)}%")

    scale.connect("notify::value", on_value_change)

    desktop_widget = Window(
        type_hint="normal",
        geometry="center",
        child=Box(
            name="container-box",
            orientation="v",
            size=250,
            spacing=10,
            children=[scale, h_scale],
        ),
        all_visible=True,
    )

    app = Application("desktop-widget", desktop_widget)

    def set_css(*args):
        app.set_stylesheet_from_file(get_relative_path("style.css"))

    app.style_monitor = monitor_file(get_relative_path("./style.css"))
    app.style_monitor.connect("changed", set_css)
    set_css()

    app.run()
