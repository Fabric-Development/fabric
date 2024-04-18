import gi
from typing import Literal
from fabric.widgets.container import Container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class FlowBox(Gtk.FlowBox, Container):
    def __init__(
        self,
        row_spacing: int | None = None,
        column_spacing: int | None = None,
        orientation: Literal[
            "horizontal",
            "vertical",
            "h",
            "v",
        ]
        | Gtk.Orientation = None,
        children: Gtk.Widget | list[Gtk.Widget] | None = None,
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
        """
        :param row_spacing: the spacing between rows, defaults to None
        :type row_spacing: int | None, optional
        :param column_spacing: the spacing between columns, defaults to None
        :type column_spacing: int | None, optional
        :param orientation: the orientation of the box, defaults to None
        :type orientation: Literal["horizontal", "vertical", "h", "v"] | Gtk.Orientation, optional
        :param children: the children of the widget, defaults to None
        :type children: Gtk.Widget | list[Gtk.Widget] | None, optional
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
        :param size: the size of the widget, defaults to None
        :type size: tuple[int] | int | None, optional
        """
        orientation = (
            orientation
            if isinstance(orientation, Gtk.Orientation)
            else {
                "horizontal": Gtk.Orientation.HORIZONTAL,
                "vertical": Gtk.Orientation.VERTICAL,
                "h": Gtk.Orientation.HORIZONTAL,
                "v": Gtk.Orientation.VERTICAL,
            }.get(orientation, Gtk.Orientation.HORIZONTAL)
        )
        column_spacing = column_spacing if isinstance(column_spacing, int) else 0
        row_spacing = row_spacing if isinstance(row_spacing, int) else 0
        Gtk.FlowBox.__init__(
            self,
            column_spacing=column_spacing,
            row_spacing=row_spacing,
            orientation=orientation,
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        Container.__init__(
            self,
            children,
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
            size,
        )
        self.do_connect_signals_for_kwargs(kwargs)
