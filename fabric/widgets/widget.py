import gi
from typing import Literal
from fabric.utils.helpers import compile_css

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Widget(Gtk.Widget):
    def __init__(
        self,
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
        size: tuple[int] | None = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        super().show_all() if all_visible is True else super().show() if visible is True else None
        self.style_provider: Gtk.CssProvider = None
        size = (size, size) if isinstance(size, int) is True else size
        super().set_name(name) if name is not None else None
        super().set_tooltip_text(tooltip_text) if tooltip_text is not None else None
        super().set_tooltip_markup(
            tooltip_markup
        ) if tooltip_markup is not None else None
        super().set_halign(
            {
                "fill": Gtk.Align.FILL,
                "start": Gtk.Align.START,
                "end": Gtk.Align.END,
                "center": Gtk.Align.CENTER,
                "baseline": Gtk.Align.BASELINE,
            }.get(h_align.lower(), Gtk.Align.START)
        ) if h_align is not None else None
        super().set_valign(
            {
                "fill": Gtk.Align.FILL,
                "start": Gtk.Align.START,
                "end": Gtk.Align.END,
                "center": Gtk.Align.CENTER,
                "baseline": Gtk.Align.BASELINE,
            }.get(v_align.lower(), Gtk.Align.START)
        ) if v_align is not None else None
        super().set_hexpand(
            True if h_expand is True else False
        ) if h_expand is not None else None
        super().set_vexpand(
            True if v_expand is True else False
        ) if v_expand is not None else None
        super().set_size_request(*size) if size is not None else None
        self.set_style(
            style, style_compiled, style_append, style_add_brackets
        ) if style is not None else None

    def set_style(
        self,
        style: str,
        compiled: bool = True,
        append: bool = False,
        add_brackets: bool = True,
    ) -> None:
        """
        set the styles for this widget from a string

        :param style: the css style
        :type style: str
        :param compile: to compile the style, defaults to True
        :type compile: bool, optional
        :param append: appends this style to other loaded styles (if any), if this is set to False it will clear all other styles before applying, defaults to False
        :type append: bool, optional
        :param add_brackets: add brackets to the style if they are missing (e.g. `padding: 10; some-thing-useful: unset;` was passed; will be converted to `* { padding: 10; some-thing-useful: unset; }`), defaults to True
        """
        style = (
            f"* {{ {style} }}"
            if not "{" in style or not "}" in style and add_brackets is True
            else style
        )
        style = compile_css(style) if compiled is True else style

        self.get_style_context().remove_provider(
            self.style_provider
        ) if self.style_provider is not None and append is False else None

        self.style_provider = Gtk.CssProvider()
        self.style_provider.load_from_data(style.encode())
        self.get_style_context().add_provider(
            self.style_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER
        )
        return

    def get_style_classes(self) -> list[str]:
        return self.get_style_context().list_classes() or []

    def set_style_classes(self, classes: list[str]) -> None:
        for cls in self.get_style_classes():
            self.get_style_context().remove_class(cls)
        for cls in classes:
            self.get_style_context().add_class(cls)
        return
