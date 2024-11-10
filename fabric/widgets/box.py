import gi
from typing import Literal
from collections.abc import Iterable
from fabric.widgets.container import Container
from fabric.utils.helpers import get_enum_member

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Box(Gtk.Box, Container):
    """a box able to hold widgets as a container"""

    def __init__(
        self,
        spacing: int = 0,
        orientation: Literal[
            "horizontal",
            "vertical",
            "h",
            "v",
        ]
        | Gtk.Orientation = Gtk.Orientation.HORIZONTAL,
        children: Gtk.Widget | Iterable[Gtk.Widget] | None = None,
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
    ) -> None:
        orientation = get_enum_member(
            Gtk.Orientation,
            orientation,
            {"v": "vertical", "h": "horizontal"},
            default=Gtk.Orientation.HORIZONTAL,
        )

        Gtk.Box.__init__(self, spacing=spacing, orientation=orientation)  # type: ignore
        Container.__init__(
            self,
            children,
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
            size,
            **kwargs,
        )
