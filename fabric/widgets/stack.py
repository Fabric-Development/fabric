import gi
from typing import Literal
from fabric.widgets.container import Container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Stack(Gtk.Stack, Container):
    def __init__(
        self,
        transition_type: Literal[
            "none",
            "crossfade",
            "slide-right",
            "slide-left",
            "slide-up",
            "slide-down",
            "slide-left-right",
            "slide-up-down",
            "over-up",
            "over-down",
            "over-left",
            "over-right",
            "under-up",
            "under-down",
            "under-left",
            "under-right",
            "over-up-down",
            "over-down-up",
            "over-left-right",
            "over-right-left",
        ]
        | Gtk.StackTransitionType
        | None = None,
        transition_duration: int | None = None,
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
    ) -> None:
        """
        :param transition_type: the transition type to use, defaults to None
        :param transition_duration: the duration of the transition, defaults to None
        :type transition_duration: int | None, optional
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
        Gtk.Stack.__init__(
            self,
            **(self.do_get_filtered_kwargs(kwargs)),
        )
        self.set_transition_type(
            transition_type
        ) if transition_type is not None else None
        self.set_transition_duration(
            transition_duration
        ) if transition_duration is not None else None
        Container.__init__(
            self,
            None,
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

    def set_transition_type(
        self,
        transition: Literal[
            "none",
            "crossfade",
            "slide-right",
            "slide-left",
            "slide-up",
            "slide-down",
            "slide-left-right",
            "slide-up-down",
            "over-up",
            "over-down",
            "over-left",
            "over-right",
            "under-up",
            "under-down",
            "under-left",
            "under-right",
            "over-up-down",
            "over-down-up",
            "over-left-right",
            "over-right-left",
        ]
        | Gtk.StackTransitionType,
    ) -> None:
        return super().set_transition_type(
            transition
            if isinstance(transition, Gtk.StackTransitionType)
            else {
                "none": Gtk.StackTransitionType.NONE,
                "crossfade": Gtk.StackTransitionType.CROSSFADE,
                "slide-right": Gtk.StackTransitionType.SLIDE_RIGHT,
                "slide-left": Gtk.StackTransitionType.SLIDE_LEFT,
                "slide-up": Gtk.StackTransitionType.SLIDE_UP,
                "slide-down": Gtk.StackTransitionType.SLIDE_DOWN,
                "slide-left-right": Gtk.StackTransitionType.SLIDE_LEFT_RIGHT,
                "slide-up-down": Gtk.StackTransitionType.SLIDE_UP_DOWN,
                "over-up": Gtk.StackTransitionType.OVER_UP,
                "over-down": Gtk.StackTransitionType.OVER_DOWN,
                "over-left": Gtk.StackTransitionType.OVER_LEFT,
                "over-right": Gtk.StackTransitionType.OVER_RIGHT,
                "under-up": Gtk.StackTransitionType.UNDER_UP,
                "under-down": Gtk.StackTransitionType.UNDER_DOWN,
                "under-left": Gtk.StackTransitionType.UNDER_LEFT,
                "under-right": Gtk.StackTransitionType.UNDER_RIGHT,
                "over-up-down": Gtk.StackTransitionType.OVER_UP_DOWN,
                "over-down-up": Gtk.StackTransitionType.OVER_DOWN_UP,
                "over-left-right": Gtk.StackTransitionType.OVER_LEFT_RIGHT,
                "over-right-left": Gtk.StackTransitionType.OVER_RIGHT_LEFT,
                # NOTE: GTK 4.0 only
                # "rotate-left": Gtk.StackTransitionType.ROTATE_LEFT,
                # "rotate-right": Gtk.StackTransitionType.ROTATE_RIGHT,
                # "rotate-left-right": Gtk.StackTransitionType.ROTATE_LEFT_RIGHT,
            }.get(transition, Gtk.StackTransitionType.NONE)
        )
