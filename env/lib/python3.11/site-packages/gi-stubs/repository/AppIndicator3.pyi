from typing import Any
from typing import Callable
from typing import Optional

from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import Gtk

INDICATOR_SIGNAL_CONNECTION_CHANGED: str = "connection-changed"
INDICATOR_SIGNAL_NEW_ATTENTION_ICON: str = "new-attention-icon"
INDICATOR_SIGNAL_NEW_ICON: str = "new-icon"
INDICATOR_SIGNAL_NEW_ICON_THEME_PATH: str = "new-icon-theme-path"
INDICATOR_SIGNAL_NEW_LABEL: str = "new-label"
INDICATOR_SIGNAL_NEW_STATUS: str = "new-status"
INDICATOR_SIGNAL_SCROLL_EVENT: str = "scroll-event"
_lock = ...  # FIXME Constant
_namespace: str = "AppIndicator3"
_version: str = "0.1"

class Indicator(GObject.Object):
    """
    :Constructors:

    ::

        Indicator(**properties)
        new(id:str, icon_name:str, category:AppIndicator3.IndicatorCategory) -> AppIndicator3.Indicator
        new_with_path(id:str, icon_name:str, category:AppIndicator3.IndicatorCategory, icon_theme_path:str) -> AppIndicator3.Indicator

    Object AppIndicator

    Signals from AppIndicator:
      scroll-event (gint, GdkScrollDirection)
      new-icon ()
      new-attention-icon ()
      new-status (gchararray)
      new-label (gchararray, gchararray)
      connection-changed (gboolean)
      new-icon-theme-path (gchararray)

    Properties from AppIndicator:
      id -> gchararray: The ID for this indicator
        An ID that should be unique, but used consistently by this program and its indicator.
      category -> gchararray: Indicator Category
        The type of indicator that this represents.  Please don't use 'other'. Defaults to 'ApplicationStatus'.
      status -> gchararray: Indicator Status
        Whether the indicator is shown or requests attention. Defaults to 'Passive'.
      icon-name -> gchararray: An icon for the indicator
        The default icon that is shown for the indicator.
      icon-desc -> gchararray: A description of the icon for the indicator
        A description of the default icon that is shown for the indicator.
      attention-icon-name -> gchararray: An icon to show when the indicator request attention.
        If the indicator sets it's status to 'attention' then this icon is shown.
      attention-icon-desc -> gchararray: A description of the icon to show when the indicator request attention.
        When the indicator is an attention mode this should describe the icon shown
      icon-theme-path -> gchararray: An additional path for custom icons.
        An additional place to look for icon names that may be installed by the application.
      connected -> gboolean: Whether we're conneced to a watcher
        Pretty simple, true if we have a reasonable expectation of being displayed through this object.  You should hide your TrayIcon if so.
      label -> gchararray: A label next to the icon
        A label to provide dynamic information.
      label-guide -> gchararray: A string to size the space available for the label.
        To ensure that the label does not cause the panel to 'jiggle' this string should provide information on how much space it could take.
      ordering-index -> guint: The location that this app indicator should be in the list.
        A way to override the default ordering of the applications by providing a very specific idea of where this entry should be placed.
      dbus-menu-server -> DbusmenuServer: The internal DBusmenu Server
        DBusmenu server which is available for testing the application indicators.
      title -> gchararray: Title of the application indicator
        A human readable way to refer to this application indicator in the UI.

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        attention_icon_desc: str
        attention_icon_name: str
        category: str
        connected: bool
        icon_desc: str
        icon_name: str
        icon_theme_path: str
        id: str
        label: str
        label_guide: str
        ordering_index: int
        status: str
        title: str
    props: Props = ...
    parent: GObject.Object = ...
    priv: IndicatorPrivate = ...

    def __init__(
        self,
        attention_icon_desc: str = ...,
        attention_icon_name: str = ...,
        category: str = ...,
        icon_desc: str = ...,
        icon_name: str = ...,
        icon_theme_path: str = ...,
        id: str = ...,
        label: str = ...,
        label_guide: str = ...,
        ordering_index: int = ...,
        status: str = ...,
        title: str = ...,
    ): ...
    def build_menu_from_desktop(
        self, desktop_file: str, desktop_profile: str
    ) -> None: ...
    def do_connection_changed(self, connected: bool, *user_data: Any) -> None: ...
    def do_new_attention_icon(self, *user_data: Any) -> None: ...
    def do_new_icon(self, *user_data: Any) -> None: ...
    def do_new_icon_theme_path(self, icon_theme_path: str, *user_data: Any) -> None: ...
    def do_new_label(self, label: str, guide: str, *user_data: Any) -> None: ...
    def do_new_status(self, status: str, *user_data: Any) -> None: ...
    def do_scroll_event(
        self, delta: int, direction: Gdk.ScrollDirection, *user_data: Any
    ) -> None: ...
    def do_unfallback(self, status_icon: Gtk.StatusIcon) -> None: ...
    def get_attention_icon(self) -> str: ...
    def get_attention_icon_desc(self) -> str: ...
    def get_category(self) -> IndicatorCategory: ...
    def get_icon(self) -> str: ...
    def get_icon_desc(self) -> str: ...
    def get_icon_theme_path(self) -> str: ...
    def get_id(self) -> str: ...
    def get_label(self) -> str: ...
    def get_label_guide(self) -> str: ...
    def get_menu(self) -> Gtk.Menu: ...
    def get_ordering_index(self) -> int: ...
    def get_secondary_activate_target(self) -> Gtk.Widget: ...
    def get_status(self) -> IndicatorStatus: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(cls, id: str, icon_name: str, category: IndicatorCategory) -> Indicator: ...
    @classmethod
    def new_with_path(
        cls, id: str, icon_name: str, category: IndicatorCategory, icon_theme_path: str
    ) -> Indicator: ...
    def set_attention_icon(self, icon_name: str) -> None: ...
    def set_attention_icon_full(self, icon_name: str, icon_desc: str) -> None: ...
    def set_icon(self, icon_name: str) -> None: ...
    def set_icon_full(self, icon_name: str, icon_desc: str) -> None: ...
    def set_icon_theme_path(self, icon_theme_path: str) -> None: ...
    def set_label(self, label: str, guide: str) -> None: ...
    def set_menu(self, menu: Optional[Gtk.Menu] = None) -> None: ...
    def set_ordering_index(self, ordering_index: int) -> None: ...
    def set_secondary_activate_target(
        self, menuitem: Optional[Gtk.Widget] = None
    ) -> None: ...
    def set_status(self, status: IndicatorStatus) -> None: ...
    def set_title(self, title: Optional[str] = None) -> None: ...

class IndicatorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        IndicatorClass()
    """

    parent_class: GObject.ObjectClass = ...
    new_icon: Callable[..., None] = ...
    new_attention_icon: Callable[..., None] = ...
    new_status: Callable[..., None] = ...
    new_icon_theme_path: Callable[..., None] = ...
    new_label: Callable[..., None] = ...
    connection_changed: Callable[..., None] = ...
    scroll_event: Callable[..., None] = ...
    app_indicator_reserved_ats: Callable[[], None] = ...
    fallback: None = ...
    unfallback: Callable[[Indicator, Gtk.StatusIcon], None] = ...
    app_indicator_reserved_1: Callable[[], None] = ...
    app_indicator_reserved_2: Callable[[], None] = ...
    app_indicator_reserved_3: Callable[[], None] = ...
    app_indicator_reserved_4: Callable[[], None] = ...
    app_indicator_reserved_5: Callable[[], None] = ...
    app_indicator_reserved_6: Callable[[], None] = ...

class IndicatorPrivate(GObject.GPointer): ...

class IndicatorCategory(GObject.GEnum):
    APPLICATION_STATUS = 0
    COMMUNICATIONS = 1
    HARDWARE = 3
    OTHER = 4
    SYSTEM_SERVICES = 2

class IndicatorStatus(GObject.GEnum):
    ACTIVE = 1
    ATTENTION = 2
    PASSIVE = 0
