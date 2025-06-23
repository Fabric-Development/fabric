import gi
from collections.abc import Iterable
from typing import Literal

from fabric.widgets.widget import Widget
from gi.repository import Gtk


class Grid(Gtk.Grid, Widget):

    def __init__(
        self,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        row_spacing: int = 0,
        column_spacing: int = 0,
        column_homogeneous: bool = False,
        row_homogeneous: bool = False,
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
        Gtk.Grid.__init__(self)
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
            size,
            **kwargs,
        )
        self.set_row_spacing(row_spacing)
        self.set_column_spacing(column_spacing)
        self.set_column_homogeneous(column_homogeneous)
        self.set_row_homogeneous(row_homogeneous)

    def attach_flow(
        self, children: Iterable[Widget], columns, start_row=0, start_col=0
    ):
        """
        Adds widgets to a Gtk.Grid in a flow layout.

        Args:
            children (list): List of Gtk.Widget to add.
            columns (int): Number of columns in the grid.
            start_row (int): Optional starting row.
            start_col (int): Optional starting column.
        """
        for index, child in enumerate(children):
            row = start_row + index // columns
            col = start_col + index % columns
            self.attach(child, col, row, 1, 1)
