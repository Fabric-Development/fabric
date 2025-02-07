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
            None,
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

    def do_draw(self, cr: cairo.Context):
        if not self._handle:
            return

        alloc = self.get_allocation()
        width: int = alloc.width  # type: ignore
        height: int = alloc.height  # type: ignore

        rect = Rsvg.Rectangle()
        rect.x = rect.y = 0  # type: ignore
        rect.width = width  # type: ignore
        rect.height = height  # type: ignore

        if self._style_compiled is not None and self._handle.set_stylesheet(
            self._style_compiled.encode()  # type: ignore
        ):
            logger.error("[Svg] failed to apply style, probably invalid style property")
        self._handle.set_dpi((self.get_scale_factor() * 160))

        cr.save()
        cr.set_antialias(cairo.Antialias.BEST)
        self._handle.render_document(cr, rect)  # type: ignore
        cr.restore()

        return

    def do_finalize_handle(self):
        if not self._handle:
            return
        self._handle.free()
        del self._handle

        self._handle = None
        return

    def get_svg_size(self) -> tuple[int, int] | None:
        """Get the dimensions of the loaded svg buffer (if any)

        :return: a tuple holding (width, height) values, None if couldn't find a loaded svg
        :rtype: tuple[int, int]
        """
        if not self._handle:
            return None
        return self._handle.props.width, self._handle.props.height  # type: ignore

    def set_from_file(self, file: str):
        self.do_finalize_handle()
        self._handle = Rsvg.Handle.new_from_file(file)
        return self.queue_draw()

    def set_from_string(self, string: str):
        self.do_finalize_handle()
        self._handle = Rsvg.Handle.new_from_data(string.encode())  # type: ignore
        return self.queue_draw()

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
