import gi
import cairo
from loguru import logger
from typing import Literal, overload
from collections.abc import Iterable
from fabric.widgets.widget import Widget
from fabric.utils import compile_css

gi.require_version("Gtk", "3.0")
gi.require_version("Rsvg", "2.0")
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
    ): ...

    def __init__(
        self,
        svg_file: str | None = None,
        svg_string: str | None = None,
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
        Gtk.DrawingArea.__init__(self)  # type: ignore
        Widget.__init__(
            self,
            name,
            visible,
            all_visible,
            style,
            style_classes,
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
            raise ValueError(
                "both svg_string and svg_file can't be set at the same time"
            )

        if not svg_string and not svg_file:
            raise ValueError("you must provide a source to load the svg from")

        if svg_file:
            self._handle = Rsvg.Handle.new_from_file(svg_file)
        else:
            self._handle = Rsvg.Handle.new_from_data(svg_string.encode())  # type: ignore

        self._style_compiled: str | None = None
        if style:
            self.set_style(style)

        svg_size = self.do_get_svg_size()
        if size is not None:
            self.set_size_request(
                *self.do_calculate_size(
                    *(size if isinstance(size, (tuple, list)) else (size, size)),
                    (svg_size[0] / svg_size[1]),  # type: ignore
                )
            )
        else:
            self.set_size_request(*svg_size)

    def do_get_svg_size(self) -> tuple[int, int]:
        return self._handle.props.width, self._handle.props.height  # type: ignore

    def do_get_viewport_rectangle(self) -> Rsvg.Rectangle:
        alloc = self.get_allocation()
        rect = Rsvg.Rectangle()
        rect.x, rect.y, rect.width, rect.height = 0, 0, alloc.width, alloc.height  # type: ignore
        return rect

    def do_calculate_size(
        self, width: int, height: int, aspect_ratio: float
    ) -> tuple[int, int]:
        cur_aspect = width / height
        new_width, new_height = width, height
        if cur_aspect > aspect_ratio:
            new_width = height * aspect_ratio
        else:
            new_height = width / aspect_ratio
        return round(new_width), round(new_height)

    def do_draw(self, cr: cairo.Context):
        if not self._handle:
            return
        cr.save()

        cr.set_antialias(cairo.Antialias.BEST)

        if self._style_compiled is not None and self._handle.set_stylesheet(
            self._style_compiled.encode()  # type: ignore
        ):
            logger.error("[Svg] failed to apply style, probably invalid style property")

        self._handle.set_dpi((self.get_scale_factor() * 160))
        self._handle.render_document(cr, self.do_get_viewport_rectangle())  # type: ignore

        cr.restore()

    def do_finalize_handle(self):
        if self._handle:
            self._handle.free()

            del self._handle
            self._handle = None
        return

    # override
    def set_style(
        self,
        style: str,
        compiled: bool = True,
        append: bool = False,  # TODO: implement
        add_brackets: bool = True,
    ) -> None:
        if compiled:
            self._style_compiled = compile_css(
                f"* {{ {style} }}"
                if "{" not in style or "}" not in style and add_brackets is True
                else style
            )
        else:
            self._style_compiled = style

        return self.queue_draw()

    def set_from_file(self, file: str):
        self.do_finalize_handle()
        self._handle = Rsvg.Handle.new_from_file(file)
        return self.queue_draw()

    def set_from_string(self, string: str):
        self.do_finalize_handle()
        self._handle = Rsvg.Handle.new_from_data(string.encode())  # type: ignore
        return self.queue_draw()
