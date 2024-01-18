import gi
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
        name: str | None = None,
        size: tuple[int] | None = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        super().show_all() if all_visible is True else super().show() if visible is True else None
        self.style_provider: Gtk.CssProvider = None
        size = (size, size) if isinstance(size, int) is True else size
        super().set_name(name) if name is not None else None
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
