import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, GdkPixbuf


class Application:
    def __init__(self, app: Gio.DesktopAppInfo):
        self._app: Gio.DesktopAppInfo = app
        self.name: str = app.get_name()
        self.generic_name: str | None = app.get_generic_name()
        self.display_name: str | None = app.get_display_name()
        self.description: str | None = app.get_description()
        self.window_class: str | None = app.get_startup_wm_class()
        self.executable: str | None = app.get_executable()
        self.command_line: str | None = app.get_commandline()
        self.icon: Gio.Icon | Gio.ThemedIcon | Gio.FileIcon | Gio.LoadableIcon | Gio.EmblemedIcon | None = app.get_icon()
        self.icon_name: str | None = (
            self.icon.to_string() if self.icon is not None else None
        )
        self.hidden: bool = app.get_is_hidden()
        self._pixbuf: GdkPixbuf.Pixbuf | None = None

    def get_icon_pixbuf(
        self,
        size: int = 48,
        default_icon: str = "unknown",
        flags: Gtk.IconLookupFlags = (
            Gtk.IconLookupFlags.FORCE_SIZE | Gtk.IconLookupFlags.FORCE_REGULAR
        ),
    ) -> GdkPixbuf.Pixbuf | None:
        """
        get a pixbuf from the icon (if any)

        :param size: the size of the icon, defaults to 48
        :type size: int, optional
        :param default_icon: the name of the default icon, defaults to "unknown"
        :type default_icon: str, optional
        :param flags: the Gtk.IconLookupFlags to use when fetching the icon
        :type flags: Gtk.IconLookupFlags, defaults to (Gtk.IconLookupFlags.FORCE_SIZE | Gtk.IconLookupFlags.FORCE_REGULAR), optional
        :return: the pixbuf
        :rtype: GdkPixbuf.Pixbuf | None
        """
        if self._pixbuf is not None:
            return self._pixbuf  # already loaded
        icon_theme = Gtk.IconTheme.get_default()
        try:
            self._pixbuf = (
                icon_theme.load_icon(
                    self.icon_name,
                    size,
                    flags,
                )
                if self.icon_name is not None
                else None
            )
        except:
            pass
        if self._pixbuf is None:
            try:
                self._pixbuf = (
                    icon_theme.load_icon(default_icon, size, flags)
                    if default_icon is not None
                    else None
                )
            except:
                pass
        return self._pixbuf


def get_desktop_applications(include_hidden: bool = False) -> list[Application]:
    """
    get a list of all desktop applications
    this might be useful for writing application launchers

    :param include_hidden: whether to include applications unintended to be visible to normal users, defaults to false
    :type include_hidden: bool, optional
    :return: a list of all desktop applications
    :rtype: list[Application]
    """
    return [
        Application(app)
        for app in Gio.DesktopAppInfo.get_all()
        if include_hidden or app.should_show()
    ]
