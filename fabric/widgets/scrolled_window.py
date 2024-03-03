import gi
from typing import Literal
from fabric.widgets.container import Container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ScrolledWindow(Gtk.ScrolledWindow, Container):
    """
    a scrollable container, it can be used to make your big content scrollable

    NOTE: this widget have nothing to do with top level windows
    it's just a normal container that can be added to other containers
    """

    def __init__(
        self,
        min_content_height: int | None = None,
        min_content_width: int | None = None,
        max_content_height: int | None = None,
        max_content_width: int | None = None,
        propagate_natural_height: bool | None = None,
        propagate_natural_width: bool | None = None,
        kinetic_scrolling: bool | None = None,
        overlay_scrolling: bool | None = None,
        h_scrollbar_policy: Literal[
            "always",
            "automatic",
            "never",
            "external",
        ]
        | Gtk.PolicyType
        | None = "automatic",
        v_scrollbar_policy: Literal[
            "always",
            "automatic",
            "never",
            "external",
        ]
        | Gtk.PolicyType
        | None = "automatic",
        children: Gtk.Widget | None = None,
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
        :param min_content_height: the minimum height of the content, defaults to None
        :type min_content_height: int | None, optional
        :param min_content_width: the minimum width of the content, defaults to None
        :type min_content_width: int | None, optional
        :param max_content_height: the maximum height of the content, defaults to None
        :type max_content_height: int | None, optional
        :param max_content_width: the maximum width of the content, defaults to None
        :type max_content_width: int | None, optional
        :param propagate_natural_height: the natural height of the content, defaults to None
        :type propagate_natural_height: bool | None, optional
        :param propagate_natural_width: the natural width of the content, defaults to None
        :type propagate_natural_width: bool | None, optional
        :param kinetic_scrolling: whether kinetic scrolling is enabled or not, defaults to None
        :type kinetic_scrolling: bool | None, optional
        :param overlay_scrolling: whether overlay scrolling is enabled or not (makes the scrollbars look like a widget in the sides of the content if disabled), defaults to None
        :type overlay_scrolling: bool | None, optional
        :param h_scrollbar_policy: determines when the scrollbar should appear for the horizontal scroll, defaults to "automatic"
        :type h_scrollbar_policy: Literal[always, automatic, never, external] | Gtk.PolicyType | None, optional
        :param v_scrollbar_policy: determines when the scrollbar should appear for the vertical scroll, defaults to "automatic"
        :type v_scrollbar_policy: Literal[always, automatic, never, external] | Gtk.PolicyType | None, optional
        :param children: the child to add (single child), defaults to None
        :type children: Gtk.Widget | None, optional
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
        Gtk.ScrolledWindow.__init__(
            self,
            **(self.do_get_filtered_kwargs(kwargs)),
        )
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

        _policy_map = {
            "always": Gtk.PolicyType.AUTOMATIC,
            "automatic": Gtk.PolicyType.AUTOMATIC,
            "never": Gtk.PolicyType.NEVER,
            "external": Gtk.PolicyType.EXTERNAL,
        }
        h_scrollbar_policy = (
            _policy_map.get(h_scrollbar_policy.lower(), Gtk.PolicyType.AUTOMATIC)
            if isinstance(h_scrollbar_policy, str)
            else h_scrollbar_policy
            if isinstance(h_scrollbar_policy, Gtk.PolicyType)
            else Gtk.PolicyType.AUTOMATIC
        )
        v_scrollbar_policy = (
            _policy_map.get(v_scrollbar_policy.lower(), Gtk.PolicyType.AUTOMATIC)
            if isinstance(v_scrollbar_policy, str)
            else v_scrollbar_policy
            if isinstance(v_scrollbar_policy, Gtk.PolicyType)
            else Gtk.PolicyType.AUTOMATIC
        )
        self.add(children) if children is not None else None
        self.set_min_content_height(
            min_content_height
        ) if min_content_height is not None else None
        self.set_min_content_width(
            min_content_width
        ) if min_content_width is not None else None
        self.set_max_content_height(
            max_content_height
        ) if max_content_height is not None else None
        self.set_max_content_width(
            max_content_width
        ) if max_content_width is not None else None
        self.set_propagate_natural_height(
            propagate_natural_height
        ) if propagate_natural_height is not None else None
        self.set_propagate_natural_width(
            propagate_natural_width
        ) if propagate_natural_width is not None else None
        self.set_kinetic_scrolling(
            kinetic_scrolling
        ) if kinetic_scrolling is not None else None
        self.set_overlay_scrolling(
            overlay_scrolling
        ) if overlay_scrolling is not None else None
        self.set_policy(h_scrollbar_policy, v_scrollbar_policy)
        self.do_connect_signals_for_kwargs(kwargs)
