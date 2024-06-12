import gi
from typing import Literal
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango


class Label(Gtk.Label, Widget):
    def __init__(
        self,
        label: str | None = None,
        markup: bool = False,
        justification: Literal[
            "left",
            "right",
            "center",
            "fill",
        ]
        | Gtk.Justification
        | None = None,
        ellipsization: Literal[
            "none",
            "start",
            "middle",
            "end",
        ]
        | Pango.EllipsizeMode
        | None = None,
        character_max_width: int | None = None,
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
        :param label: the actual label text, defaults to None
        :type label: str | None, optional
        :param markup: whether to use markup or plain text, defaults to False
        :type markup: bool, optional
        :param justification: justification mode, defaults to None
        :type justification: Literal["left", "right", "center", "fill",] | Gtk.Justification | None, optional
        :param ellipsization: ellipsization mode, defaults to None
        :type ellipsization: Literal["none", "start", "middle", "end",] | Pango.EllipsizeMode | None, optional
        :param character_max_width: the maximum width of the label, defaults to None
        :type character_max_width: int | None, optional
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
        Gtk.Label.__init__(
            self,
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        Widget.__init__(
            self,
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

        if label is not None and markup is True:
            self.set_markup(label)
        elif label is not None:
            self.set_label(label)

        self.set_justify(
            {
                "left": Gtk.Justification.LEFT,
                "right": Gtk.Justification.RIGHT,
                "center": Gtk.Justification.CENTER,
                "fill": Gtk.Justification.FILL,
            }.get(justification.lower(), Gtk.Justification.LEFT)
        ) if justification is not None else None
        self.set_ellipsize(
            {
                "none": Pango.EllipsizeMode.NONE,
                "start": Pango.EllipsizeMode.START,
                "middle": Pango.EllipsizeMode.MIDDLE,
                "end": Pango.EllipsizeMode.END,
            }.get(ellipsization.lower(), Pango.EllipsizeMode.NONE)
        ) if ellipsization is not None else None
        self.set_max_width_chars(
            character_max_width
        ) if character_max_width is not None else None
        self.do_connect_signals_for_kwargs(kwargs)
