import gi
import cairo
from loguru import logger
from collections.abc import Iterable
from typing import Literal, overload
from fabric.widgets.widget import Widget
from fabric.utils import compile_css

gi.require_version("Rsvg", "2.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Rsvg, Gtk


class Svg(Gtk.DrawingArea, Widget):
    @overload
    def __init__(
        self,
        svg_file: str | None = None,
        svg_string: None = None,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
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
    ): ...

    @overload
    def __init__(
        self,
        svg_file: None = None,
        svg_string: str | None = None,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
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
    ): ...

    def __init__(
        self,
        svg_file: str | None = None,
        svg_string: str | None = None,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
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
        Gtk.DrawingArea.__init__(self)  # type: ignore
        Widget.__init__(
            self,
            name,
            visible,
            all_visible,
            style,
            tooltip_text,
            tooltip_markup,
            h_align,
            v_align,
            h_expand,
            v_expand,
            None,
            **kwargs,
        )
        if svg_string and svg_file:
            raise ValueError("both svg_string and svg_file can be set at the same time")
        if not svg_string and not svg_file:
            raise ValueError("please provide a resource to load the svg from")

        self._handle = (
            Rsvg.Handle().new_from_data(svg_string.encode())  # type: ignore
            if svg_string is not None
            else Rsvg.Handle().new_from_file(svg_file)
        )

        if size is not None:
            self.set_size_request(
                *self.do_resize_with_aspect(
                    *(size if isinstance(size, (tuple, list)) else (size, size)),
                    (self._handle.props.width / self._handle.props.height),  # type: ignore
                )
            )
        else:
            self.set_size_request(self._handle.props.width, self._handle.props.height)

        self._style_compiled: str | None = None

        self.set_style(style) if style is not None else None

        self.connect("draw", self.on_draw)

    # override
    def set_style(
        self,
        style: str,
        compiled: bool = True,
        append: bool = False,  # TODO: implement
        add_brackets: bool = True,
    ) -> None:
        self._style_compiled = (
            compile_css(
                f"* {{ {style} }}"
                if "{" not in style or "}" not in style and add_brackets is True
                else style
            )
            if compiled is True
            else style
        )
        self.queue_draw()
        return

    def on_draw(self, widget: Gtk.DrawingArea, ctx: cairo.Context):
        ctx.save()
        if self._style_compiled is not None:
            x = self._handle.set_stylesheet(self._style_compiled.encode())  # type: ignore
            print(x, self._style_compiled)
            if x is not True:
                logger.error(
                    "[Svg] failed to apply style, probably invalid style property"
                )
            del x
        self.do_render_svg_for_ctx(ctx, self._handle)
        ctx.restore()

    def do_scale_to_fit_for_ctx(
        self, ctx: cairo.Context, handle: Rsvg.Handle
    ) -> cairo.Context:
        allocation = self.get_allocation()
        try:
            scale_x = allocation.width / handle.props.width  # type: ignore
            scale_y = allocation.height / handle.props.height  # type: ignore
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

    def do_resize_with_aspect(
        self, width: int, height: int, aspect_ratio: float
    ) -> tuple[int, int]:
        cur_aspect = width / height
        new_width, new_height = width, height
        if cur_aspect > aspect_ratio:
            new_width = height * aspect_ratio
        else:
            new_height = width / aspect_ratio
        return int(new_width), int(new_height)
