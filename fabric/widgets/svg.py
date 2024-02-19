import gi
import cairo
from typing import Literal
from loguru import logger
from fabric.utils import compile_css
from fabric.widgets.widget import Widget

gi.require_version("Rsvg", "2.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Rsvg, Gtk


class Svg(Gtk.DrawingArea, Widget):
    def __init__(
        self,
        svg_file: str = None,
        svg_string: str = None,
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
        Gtk.DrawingArea.__init__(
            self,
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        Widget.__init__(
            self,
            visible,
            all_visible,
            style,
            None,
            None,
            None,
            tooltip_text,
            tooltip_markup,
            h_align,
            v_align,
            h_expand,
            v_expand,
            name,
            None,
        )
        if all([x is not None for x in [svg_file, svg_string]]):
            raise ValueError("Only one of svg_file and svg_string can be set")
        self.handle = (
            Rsvg.Handle().new_from_data(svg_string.encode())
            if svg_string is not None
            else Rsvg.Handle().new_from_file(svg_file)
            if svg_file is not None
            else None
        )
        if self.handle is None:
            raise ValueError("Failed to load svg, probably invalid arguments")
        self.size = (
            size
            if size is not None
            else (self.handle.props.width, self.handle.props.height)
        )
        self.set_size_request(
            *self.do_calculate_new_size(
                self.handle.props.width,
                self.handle.props.height,
                *(
                    self.size
                    if isinstance(self.size, (tuple, list))
                    else (self.size, self.size)
                ),
            )
        ) if self.size is not None else None
        self._style_result: str = None
        self.set_style(
            style, style_compiled, style_append, style_add_brackets
        ) if style is not None else None
        self.do_connect_signals_for_kwargs(kwargs)
        self.connect("draw", self.draw)

    def set_style(
        self,
        style: str,
        compiled: bool = True,
        append: bool = False,  # TODO: implement
        add_brackets: bool = True,
    ) -> None:
        self._style_result = (
            compile_css(
                f"* {{ {style} }}"
                if not "{" in style or not "}" in style and add_brackets is True
                else style
            )
            if compiled is True
            else style
        )
        self.queue_draw()
        return

    def draw(self, widget: Gtk.DrawingArea, ctx: cairo.Context):
        ctx.save()
        if self._style_result is not None:
            x = self.handle.set_stylesheet(self._style_result.encode())
            if x is not True:
                logger.error(
                    "[Svg] failed to apply style, probably invalid style property"
                )
            del x
        self.do_render_svg_for_ctx(ctx, self.handle)
        ctx.restore()

    def do_calculate_new_size(
        self, base_width, base_height, desired_width, desired_height
    ):
        try:
            aspect_ratio = base_width / base_height
            new_width = aspect_ratio * desired_height
            if new_width > desired_width:
                new_width = desired_width
                new_height = desired_width / aspect_ratio
            else:
                new_height = desired_height
        except ZeroDivisionError:
            new_width = desired_width
            new_height = desired_height
        return new_width, new_height

    def do_scale_to_fit_for_ctx(
        self, ctx: cairo.Context, handle: Rsvg.Handle
    ) -> cairo.Context:
        allocation = self.get_allocation()
        try:
            scale_x = allocation.width / handle.props.width
            scale_y = allocation.height / handle.props.height
        except ZeroDivisionError:
            scale_x = 1
            scale_y = 1

        ctx.scale(scale_x, scale_y)
        return ctx

    def do_render_svg_for_ctx(self, ctx: cairo.Context, handle: Rsvg.Handle):
        handle.set_dpi((self.get_scale_factor() * 160))
        ctx.set_antialias(cairo.Antialias.BEST)
        self.do_scale_to_fit_for_ctx(ctx, handle)
        handle.render_cairo(ctx)
        return ctx
