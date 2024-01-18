from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import Atk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Pango

_lock = ...  # FIXME Constant
_namespace: str = "Handy"
_version: str = "1"

def ease_out_cubic(t: float) -> float: ...
def enum_value_row_name(value: EnumValueObject, user_data: None) -> str: ...
def get_enable_animations(widget: Gtk.Widget) -> bool: ...
def init() -> None: ...

class ActionRow(PreferencesRow, Atk.ImplementorIface, Gtk.Actionable, Gtk.Buildable):
    """
    :Constructors:

    ::

        ActionRow(**properties)
        new() -> Gtk.Widget

    Object HdyActionRow

    Signals from HdyActionRow:
      activated ()

    Properties from HdyActionRow:
      icon-name -> gchararray: Icon name
        Icon name
      activatable-widget -> GtkWidget: Activatable widget
        The widget to be activated when the row is activated
      subtitle -> gchararray: Subtitle
        Subtitle
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key
      title-lines -> gint: Number of title lines
        The desired number of title lines
      subtitle-lines -> gint: Number of subtitle lines
        The desired number of subtitle lines

    Properties from HdyPreferencesRow:
      title -> gchararray: Title
        The title of the preference
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: Activatable
        Whether this row can be activated
      selectable -> gboolean: Selectable
        Whether this row can be selected

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        activatable_widget: Optional[Gtk.Widget]
        icon_name: str
        subtitle: Optional[str]
        subtitle_lines: int
        title_lines: int
        use_underline: bool
        title: Optional[str]
        activatable: bool
        selectable: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        action_name: Optional[str]
        action_target: GLib.Variant
        child: Gtk.Widget
    props: Props = ...
    parent_instance: PreferencesRow = ...
    def __init__(
        self,
        activatable_widget: Optional[Gtk.Widget] = ...,
        icon_name: str = ...,
        subtitle: Optional[str] = ...,
        subtitle_lines: int = ...,
        title_lines: int = ...,
        use_underline: bool = ...,
        title: Optional[str] = ...,
        activatable: bool = ...,
        selectable: bool = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        action_name: Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def activate(self) -> None: ...
    def add_prefix(self, widget: Gtk.Widget) -> None: ...
    def get_activatable_widget(self) -> Optional[Gtk.Widget]: ...
    def get_icon_name(self) -> str: ...
    def get_subtitle(self) -> Optional[str]: ...
    def get_subtitle_lines(self) -> int: ...
    def get_title_lines(self) -> int: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> ActionRow: ...
    def set_activatable_widget(self, widget: Optional[Gtk.Widget] = None) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_subtitle(self, subtitle: Optional[str] = None) -> None: ...
    def set_subtitle_lines(self, subtitle_lines: int) -> None: ...
    def set_title_lines(self, title_lines: int) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class ActionRowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionRowClass()
    """

    parent_class: Gtk.ListBoxRowClass = ...
    activate: Callable[[ActionRow], None] = ...
    padding: list[None] = ...

class ApplicationWindow(
    Gtk.ApplicationWindow,
    Atk.ImplementorIface,
    Gio.ActionGroup,
    Gio.ActionMap,
    Gtk.Buildable,
):
    """
    :Constructors:

    ::

        ApplicationWindow(**properties)
        new() -> Gtk.Widget

    Object HdyApplicationWindow

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Properties from GtkApplicationWindow:
      show-menubar -> gboolean: Show a menubar
        TRUE if the window should show a menubar at the top of the window

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        show_menubar: bool
        accept_focus: bool
        application: Optional[Gtk.Application]
        attached_to: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: Optional[GdkPixbuf.Pixbuf]
        icon_name: Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: Optional[str]
        transient_for: Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        startup_id: str
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.ApplicationWindow = ...
    def __init__(
        self,
        show_menubar: bool = ...,
        accept_focus: bool = ...,
        application: Optional[Gtk.Application] = ...,
        attached_to: Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        focus_on_map: bool = ...,
        focus_visible: bool = ...,
        gravity: Gdk.Gravity = ...,
        has_resize_grip: bool = ...,
        hide_titlebar_when_maximized: bool = ...,
        icon: Optional[GdkPixbuf.Pixbuf] = ...,
        icon_name: Optional[str] = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        role: str = ...,
        screen: Gdk.Screen = ...,
        skip_pager_hint: bool = ...,
        skip_taskbar_hint: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: Optional[Gtk.Window] = ...,
        type: Gtk.WindowType = ...,
        type_hint: Gdk.WindowTypeHint = ...,
        urgency_hint: bool = ...,
        window_position: Gtk.WindowPosition = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    @classmethod
    def new(cls) -> ApplicationWindow: ...

class ApplicationWindowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ApplicationWindowClass()
    """

    parent_class: Gtk.ApplicationWindowClass = ...
    padding: list[None] = ...

class Avatar(Gtk.DrawingArea, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        Avatar(**properties)
        new(size:int, text:str=None, show_initials:bool) -> Gtk.Widget

    Object HdyAvatar

    Properties from HdyAvatar:
      icon-name -> gchararray: Icon name
        The name of the icon from the icon theme
      text -> gchararray: Text
        The text used to generate the color and the initials
      show-initials -> gboolean: Show initials
        Whether to show the initials
      size -> gint: Size
        The size of the avatar
      loadable-icon -> GLoadableIcon: Loadable Icon
        The loadable icon used to load the avatar

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        icon_name: Optional[str]
        loadable_icon: Optional[Gio.LoadableIcon]
        show_initials: bool
        size: int
        text: Optional[str]
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
    props: Props = ...
    def __init__(
        self,
        icon_name: Optional[str] = ...,
        loadable_icon: Optional[Gio.LoadableIcon] = ...,
        show_initials: bool = ...,
        size: int = ...,
        text: Optional[str] = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def draw_to_pixbuf(self, size: int, scale_factor: int) -> GdkPixbuf.Pixbuf: ...
    def draw_to_pixbuf_async(
        self,
        size: int,
        scale_factor: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def draw_to_pixbuf_finish(
        self, async_result: Gio.AsyncResult
    ) -> GdkPixbuf.Pixbuf: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_loadable_icon(self) -> Optional[Gio.LoadableIcon]: ...
    def get_show_initials(self) -> bool: ...
    def get_size(self) -> int: ...
    def get_text(self) -> Optional[str]: ...
    @classmethod
    def new(cls, size: int, text: Optional[str], show_initials: bool) -> Avatar: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_image_load_func(
        self,
        load_image: Optional[Callable[..., Optional[GdkPixbuf.Pixbuf]]] = None,
        *user_data: Any,
    ) -> None: ...
    def set_loadable_icon(self, icon: Optional[Gio.LoadableIcon] = None) -> None: ...
    def set_show_initials(self, show_initials: bool) -> None: ...
    def set_size(self, size: int) -> None: ...
    def set_text(self, text: Optional[str] = None) -> None: ...

class AvatarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AvatarClass()
    """

    parent_class: Gtk.DrawingAreaClass = ...

class Carousel(
    Gtk.EventBox, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable, Swipeable
):
    """
    :Constructors:

    ::

        Carousel(**properties)
        new() -> Gtk.Widget

    Object HdyCarousel

    Signals from HdyCarousel:
      page-changed (guint)

    Properties from HdyCarousel:
      n-pages -> guint: Number of pages
        Number of pages
      position -> gdouble: Position
        Current scrolling position
      interactive -> gboolean: Interactive
        Whether the widget can be swiped
      spacing -> guint: Spacing
        Spacing between pages
      animation-duration -> guint: Animation duration
        Default animation duration
      allow-mouse-drag -> gboolean: Allow mouse drag
        Whether to allow dragging with mouse pointer
      allow-scroll-wheel -> gboolean: Allow scroll wheel
        Whether the widget will respond to scroll wheel events
      allow-long-swipes -> gboolean: Allow long swipes
        Whether to allow swiping for more than one page at a time
      reveal-duration -> guint: Reveal duration
        Page reveal duration

    Signals from HdySwipeable:
      child-switched (guint, gint64)

    Properties from GtkEventBox:
      visible-window -> gboolean: Visible Window
        Whether the event box is visible, as opposed to invisible and only used to trap events.
      above-child -> gboolean: Above child
        Whether the event-trapping window of the eventbox is above the window of the child widget as opposed to below it.

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        allow_long_swipes: bool
        allow_mouse_drag: bool
        allow_scroll_wheel: bool
        animation_duration: int
        interactive: bool
        n_pages: int
        position: float
        reveal_duration: int
        spacing: int
        above_child: bool
        visible_window: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        allow_long_swipes: bool = ...,
        allow_mouse_drag: bool = ...,
        allow_scroll_wheel: bool = ...,
        animation_duration: int = ...,
        interactive: bool = ...,
        reveal_duration: int = ...,
        spacing: int = ...,
        above_child: bool = ...,
        visible_window: bool = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_allow_long_swipes(self) -> bool: ...
    def get_allow_mouse_drag(self) -> bool: ...
    def get_allow_scroll_wheel(self) -> bool: ...
    def get_animation_duration(self) -> int: ...
    def get_interactive(self) -> bool: ...
    def get_n_pages(self) -> int: ...
    def get_position(self) -> float: ...
    def get_reveal_duration(self) -> int: ...
    def get_spacing(self) -> int: ...
    def insert(self, child: Gtk.Widget, position: int) -> None: ...
    @classmethod
    def new(cls) -> Carousel: ...
    def prepend(self, child: Gtk.Widget) -> None: ...
    def reorder(self, child: Gtk.Widget, position: int) -> None: ...
    def scroll_to(self, widget: Gtk.Widget) -> None: ...
    def scroll_to_full(self, widget: Gtk.Widget, duration: int) -> None: ...
    def set_allow_long_swipes(self, allow_long_swipes: bool) -> None: ...
    def set_allow_mouse_drag(self, allow_mouse_drag: bool) -> None: ...
    def set_allow_scroll_wheel(self, allow_scroll_wheel: bool) -> None: ...
    def set_animation_duration(self, duration: int) -> None: ...
    def set_interactive(self, interactive: bool) -> None: ...
    def set_reveal_duration(self, reveal_duration: int) -> None: ...
    def set_spacing(self, spacing: int) -> None: ...

class CarouselClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CarouselClass()
    """

    parent_class: Gtk.EventBoxClass = ...

class CarouselIndicatorDots(
    Gtk.DrawingArea, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable
):
    """
    :Constructors:

    ::

        CarouselIndicatorDots(**properties)
        new() -> Gtk.Widget

    Object HdyCarouselIndicatorDots

    Properties from HdyCarouselIndicatorDots:
      carousel -> HdyCarousel: Carousel
        Carousel

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        carousel: Optional[Carousel]
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(
        self,
        carousel: Optional[Carousel] = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_carousel(self) -> Optional[Carousel]: ...
    @classmethod
    def new(cls) -> CarouselIndicatorDots: ...
    def set_carousel(self, carousel: Optional[Carousel] = None) -> None: ...

class CarouselIndicatorDotsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CarouselIndicatorDotsClass()
    """

    parent_class: Gtk.DrawingAreaClass = ...

class CarouselIndicatorLines(
    Gtk.DrawingArea, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable
):
    """
    :Constructors:

    ::

        CarouselIndicatorLines(**properties)
        new() -> Gtk.Widget

    Object HdyCarouselIndicatorLines

    Properties from HdyCarouselIndicatorLines:
      carousel -> HdyCarousel: Carousel
        Carousel

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        carousel: Optional[Carousel]
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(
        self,
        carousel: Optional[Carousel] = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_carousel(self) -> Optional[Carousel]: ...
    @classmethod
    def new(cls) -> CarouselIndicatorLines: ...
    def set_carousel(self, carousel: Optional[Carousel] = None) -> None: ...

class CarouselIndicatorLinesClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CarouselIndicatorLinesClass()
    """

    parent_class: Gtk.DrawingAreaClass = ...

class Clamp(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        Clamp(**properties)
        new() -> Gtk.Widget

    Object HdyClamp

    Properties from HdyClamp:
      maximum-size -> gint: Maximum size
        The maximum size allocated to the child
      tightening-threshold -> gint: Tightening threshold
        The size from which the clamp will tighten its grip on the child

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        maximum_size: int
        tightening_threshold: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        maximum_size: int = ...,
        tightening_threshold: int = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_maximum_size(self) -> int: ...
    def get_tightening_threshold(self) -> int: ...
    @classmethod
    def new(cls) -> Clamp: ...
    def set_maximum_size(self, maximum_size: int) -> None: ...
    def set_tightening_threshold(self, tightening_threshold: int) -> None: ...

class ClampClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClampClass()
    """

    parent_class: Gtk.BinClass = ...

class ComboRow(ActionRow, Atk.ImplementorIface, Gtk.Actionable, Gtk.Buildable):
    """
    :Constructors:

    ::

        ComboRow(**properties)
        new() -> Gtk.Widget

    Object HdyComboRow

    Properties from HdyComboRow:
      selected-index -> gint: Selected index
        The index of the selected item
      use-subtitle -> gboolean: Use subtitle
        Set the current value as the subtitle

    Signals from HdyActionRow:
      activated ()

    Properties from HdyActionRow:
      icon-name -> gchararray: Icon name
        Icon name
      activatable-widget -> GtkWidget: Activatable widget
        The widget to be activated when the row is activated
      subtitle -> gchararray: Subtitle
        Subtitle
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key
      title-lines -> gint: Number of title lines
        The desired number of title lines
      subtitle-lines -> gint: Number of subtitle lines
        The desired number of subtitle lines

    Properties from HdyPreferencesRow:
      title -> gchararray: Title
        The title of the preference
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: Activatable
        Whether this row can be activated
      selectable -> gboolean: Selectable
        Whether this row can be selected

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        selected_index: int
        use_subtitle: bool
        activatable_widget: Optional[Gtk.Widget]
        icon_name: str
        subtitle: Optional[str]
        subtitle_lines: int
        title_lines: int
        use_underline: bool
        title: Optional[str]
        activatable: bool
        selectable: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        action_name: Optional[str]
        action_target: GLib.Variant
        child: Gtk.Widget
    props: Props = ...
    parent_instance: ActionRow = ...
    def __init__(
        self,
        selected_index: int = ...,
        use_subtitle: bool = ...,
        activatable_widget: Optional[Gtk.Widget] = ...,
        icon_name: str = ...,
        subtitle: Optional[str] = ...,
        subtitle_lines: int = ...,
        title_lines: int = ...,
        use_underline: bool = ...,
        title: Optional[str] = ...,
        activatable: bool = ...,
        selectable: bool = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        action_name: Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def bind_model(
        self,
        model: Optional[Gio.ListModel] = None,
        create_list_widget_func: Optional[Callable[..., Gtk.Widget]] = None,
        create_current_widget_func: Optional[Callable[..., Gtk.Widget]] = None,
        *user_data: Any,
    ) -> None: ...
    def bind_name_model(
        self,
        model: Optional[Gio.ListModel] = None,
        get_name_func: Optional[Callable[..., str]] = None,
        *user_data: Any,
    ) -> None: ...
    def get_model(self) -> Optional[Gio.ListModel]: ...
    def get_selected_index(self) -> int: ...
    def get_use_subtitle(self) -> bool: ...
    @classmethod
    def new(cls) -> ComboRow: ...
    def set_for_enum(
        self,
        enum_type: Type,
        get_name_func: Optional[Callable[..., str]] = None,
        *user_data: Any,
    ) -> None: ...
    def set_get_name_func(
        self, get_name_func: Optional[Callable[..., str]] = None, *user_data: Any
    ) -> None: ...
    def set_selected_index(self, selected_index: int) -> None: ...
    def set_use_subtitle(self, use_subtitle: bool) -> None: ...

class ComboRowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ComboRowClass()
    """

    parent_class: ActionRowClass = ...
    padding: list[None] = ...

class Deck(
    Gtk.Container, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable, Swipeable
):
    """
    :Constructors:

    ::

        Deck(**properties)
        new() -> Gtk.Widget

    Object HdyDeck

    Properties from HdyDeck:
      hhomogeneous -> gboolean: Horizontally homogeneous
        Horizontally homogeneous sizing
      vhomogeneous -> gboolean: Vertically homogeneous
        Vertically homogeneous sizing
      visible-child -> GtkWidget: Visible child
        The widget currently visible
      visible-child-name -> gchararray: Name of visible child
        The name of the widget currently visible
      transition-type -> HdyDeckTransitionType: Transition type
        The type of animation used to transition between children
      transition-duration -> guint: Transition duration
        The transition animation duration, in milliseconds
      transition-running -> gboolean: Transition running
        Whether or not the transition is currently running
      interpolate-size -> gboolean: Interpolate size
        Whether or not the size should smoothly change when changing between differently sized children
      can-swipe-back -> gboolean: Can swipe back
        Whether or not swipe gesture can be used to switch to the previous child
      can-swipe-forward -> gboolean: Can swipe forward
        Whether or not swipe gesture can be used to switch to the next child

    Signals from HdySwipeable:
      child-switched (guint, gint64)

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        can_swipe_back: bool
        can_swipe_forward: bool
        hhomogeneous: bool
        interpolate_size: bool
        transition_duration: int
        transition_running: bool
        transition_type: DeckTransitionType
        vhomogeneous: bool
        visible_child: Gtk.Widget
        visible_child_name: str
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Container = ...
    def __init__(
        self,
        can_swipe_back: bool = ...,
        can_swipe_forward: bool = ...,
        hhomogeneous: bool = ...,
        interpolate_size: bool = ...,
        transition_duration: int = ...,
        transition_type: DeckTransitionType = ...,
        vhomogeneous: bool = ...,
        visible_child: Gtk.Widget = ...,
        visible_child_name: str = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_adjacent_child(
        self, direction: NavigationDirection
    ) -> Optional[Gtk.Widget]: ...
    def get_can_swipe_back(self) -> bool: ...
    def get_can_swipe_forward(self) -> bool: ...
    def get_child_by_name(self, name: str) -> Optional[Gtk.Widget]: ...
    def get_homogeneous(self, orientation: Gtk.Orientation) -> bool: ...
    def get_interpolate_size(self) -> bool: ...
    def get_transition_duration(self) -> int: ...
    def get_transition_running(self) -> bool: ...
    def get_transition_type(self) -> DeckTransitionType: ...
    def get_visible_child(self) -> Gtk.Widget: ...
    def get_visible_child_name(self) -> str: ...
    def insert_child_after(
        self, child: Gtk.Widget, sibling: Optional[Gtk.Widget] = None
    ) -> None: ...
    def navigate(self, direction: NavigationDirection) -> bool: ...
    @classmethod
    def new(cls) -> Deck: ...
    def prepend(self, child: Gtk.Widget) -> None: ...
    def reorder_child_after(
        self, child: Gtk.Widget, sibling: Optional[Gtk.Widget] = None
    ) -> None: ...
    def set_can_swipe_back(self, can_swipe_back: bool) -> None: ...
    def set_can_swipe_forward(self, can_swipe_forward: bool) -> None: ...
    def set_homogeneous(
        self, orientation: Gtk.Orientation, homogeneous: bool
    ) -> None: ...
    def set_interpolate_size(self, interpolate_size: bool) -> None: ...
    def set_transition_duration(self, duration: int) -> None: ...
    def set_transition_type(self, transition: DeckTransitionType) -> None: ...
    def set_visible_child(self, visible_child: Gtk.Widget) -> None: ...
    def set_visible_child_name(self, name: str) -> None: ...

class DeckClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeckClass()
    """

    parent_class: Gtk.ContainerClass = ...
    padding: list[None] = ...

class EnumValueObject(GObject.Object):
    """
    :Constructors:

    ::

        EnumValueObject(**properties)
        new(enum_value:GObject.EnumValue) -> Handy.EnumValueObject

    Object HdyEnumValueObject

    Signals from GObject:
      notify (GParam)
    """

    def get_name(self) -> str: ...
    def get_nick(self) -> str: ...
    def get_value(self) -> int: ...
    @classmethod
    def new(cls, enum_value: GObject.EnumValue) -> EnumValueObject: ...

class EnumValueObjectClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EnumValueObjectClass()
    """

    parent_class: GObject.ObjectClass = ...

class ExpanderRow(PreferencesRow, Atk.ImplementorIface, Gtk.Actionable, Gtk.Buildable):
    """
    :Constructors:

    ::

        ExpanderRow(**properties)
        new() -> Gtk.Widget

    Object HdyExpanderRow

    Properties from HdyExpanderRow:
      subtitle -> gchararray: Subtitle
        The subtitle for this row
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key
      icon-name -> gchararray: Icon name
        Icon name
      expanded -> gboolean: Expanded
        Whether the row is expanded
      enable-expansion -> gboolean: Enable expansion
        Whether the expansion is enabled
      show-enable-switch -> gboolean: Show enable switch
        Whether the switch enabling the expansion is visible

    Properties from HdyPreferencesRow:
      title -> gchararray: Title
        The title of the preference
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: Activatable
        Whether this row can be activated
      selectable -> gboolean: Selectable
        Whether this row can be selected

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        enable_expansion: bool
        expanded: bool
        icon_name: str
        show_enable_switch: bool
        subtitle: Optional[str]
        use_underline: bool
        title: Optional[str]
        activatable: bool
        selectable: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        action_name: Optional[str]
        action_target: GLib.Variant
        child: Gtk.Widget
    props: Props = ...
    parent_instance: PreferencesRow = ...
    def __init__(
        self,
        enable_expansion: bool = ...,
        expanded: bool = ...,
        icon_name: str = ...,
        show_enable_switch: bool = ...,
        subtitle: Optional[str] = ...,
        use_underline: bool = ...,
        title: Optional[str] = ...,
        activatable: bool = ...,
        selectable: bool = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        action_name: Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def add_action(self, widget: Gtk.Widget) -> None: ...
    def add_prefix(self, widget: Gtk.Widget) -> None: ...
    def get_enable_expansion(self) -> bool: ...
    def get_expanded(self) -> bool: ...
    def get_icon_name(self) -> str: ...
    def get_show_enable_switch(self) -> bool: ...
    def get_subtitle(self) -> Optional[str]: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> ExpanderRow: ...
    def set_enable_expansion(self, enable_expansion: bool) -> None: ...
    def set_expanded(self, expanded: bool) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_show_enable_switch(self, show_enable_switch: bool) -> None: ...
    def set_subtitle(self, subtitle: Optional[str] = None) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class ExpanderRowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ExpanderRowClass()
    """

    parent_class: PreferencesRowClass = ...
    padding: list[None] = ...

class Flap(
    Gtk.Container, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable, Swipeable
):
    """
    :Constructors:

    ::

        Flap(**properties)
        new() -> Gtk.Widget

    Object HdyFlap

    Properties from HdyFlap:
      content -> GtkWidget: Content
        The content Widget
      flap -> GtkWidget: Flap
        The flap widget
      separator -> GtkWidget: Separator
        The separator widget
      flap-position -> GtkPackType: Flap Position
        The flap position
      reveal-flap -> gboolean: Reveal Flap
        Whether the flap is revealed
      reveal-duration -> guint: Reveal Duration
        The reveal transition animation duration, in milliseconds
      reveal-progress -> gdouble: Reveal Progress
        The current reveal transition progress
      fold-policy -> HdyFlapFoldPolicy: Fold Policy
        The current fold policy
      fold-duration -> guint: Fold Duration
        The fold transition animation duration, in milliseconds
      folded -> gboolean: Folded
        Whether the flap is currently folded
      locked -> gboolean: Locked
        Whether the flap is locked
      transition-type -> HdyFlapTransitionType: Transition Type
        The type of animation used for reveal and fold transitions
      modal -> gboolean: Modal
        Whether the flap is modal
      swipe-to-open -> gboolean: Swipe to Open
        Whether the flap can be opened with a swipe gesture
      swipe-to-close -> gboolean: Swipe to Close
        Whether the flap can be closed with a swipe gesture

    Signals from HdySwipeable:
      child-switched (guint, gint64)

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        content: Optional[Gtk.Widget]
        flap: Optional[Gtk.Widget]
        flap_position: Gtk.PackType
        fold_duration: int
        fold_policy: FlapFoldPolicy
        folded: bool
        locked: bool
        modal: bool
        reveal_duration: int
        reveal_flap: bool
        reveal_progress: float
        separator: Optional[Gtk.Widget]
        swipe_to_close: bool
        swipe_to_open: bool
        transition_type: FlapTransitionType
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        content: Optional[Gtk.Widget] = ...,
        flap: Optional[Gtk.Widget] = ...,
        flap_position: Gtk.PackType = ...,
        fold_duration: int = ...,
        fold_policy: FlapFoldPolicy = ...,
        locked: bool = ...,
        modal: bool = ...,
        reveal_duration: int = ...,
        reveal_flap: bool = ...,
        separator: Optional[Gtk.Widget] = ...,
        swipe_to_close: bool = ...,
        swipe_to_open: bool = ...,
        transition_type: FlapTransitionType = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_content(self) -> Optional[Gtk.Widget]: ...
    def get_flap(self) -> Optional[Gtk.Widget]: ...
    def get_flap_position(self) -> Gtk.PackType: ...
    def get_fold_duration(self) -> int: ...
    def get_fold_policy(self) -> FlapFoldPolicy: ...
    def get_folded(self) -> bool: ...
    def get_locked(self) -> bool: ...
    def get_modal(self) -> bool: ...
    def get_reveal_duration(self) -> int: ...
    def get_reveal_flap(self) -> bool: ...
    def get_reveal_progress(self) -> float: ...
    def get_separator(self) -> Optional[Gtk.Widget]: ...
    def get_swipe_to_close(self) -> bool: ...
    def get_swipe_to_open(self) -> bool: ...
    def get_transition_type(self) -> FlapTransitionType: ...
    @classmethod
    def new(cls) -> Flap: ...
    def set_content(self, content: Optional[Gtk.Widget] = None) -> None: ...
    def set_flap(self, flap: Optional[Gtk.Widget] = None) -> None: ...
    def set_flap_position(self, position: Gtk.PackType) -> None: ...
    def set_fold_duration(self, duration: int) -> None: ...
    def set_fold_policy(self, policy: FlapFoldPolicy) -> None: ...
    def set_locked(self, locked: bool) -> None: ...
    def set_modal(self, modal: bool) -> None: ...
    def set_reveal_duration(self, duration: int) -> None: ...
    def set_reveal_flap(self, reveal_flap: bool) -> None: ...
    def set_separator(self, separator: Optional[Gtk.Widget] = None) -> None: ...
    def set_swipe_to_close(self, swipe_to_close: bool) -> None: ...
    def set_swipe_to_open(self, swipe_to_open: bool) -> None: ...
    def set_transition_type(self, transition_type: FlapTransitionType) -> None: ...

class FlapClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FlapClass()
    """

    parent_class: Gtk.ContainerClass = ...

class HeaderBar(Gtk.Container, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        HeaderBar(**properties)
        new() -> Gtk.Widget

    Object HdyHeaderBar

    Properties from HdyHeaderBar:
      title -> gchararray: Title
        The title to display
      subtitle -> gchararray: Subtitle
        The subtitle to display
      has-subtitle -> gboolean: Has Subtitle
        Whether to reserve space for a subtitle
      custom-title -> GtkWidget: Custom Title
        Custom title widget to display
      spacing -> gint: Spacing
        The amount of space between children
      show-close-button -> gboolean: Show decorations
        Whether to show window decorations
      decoration-layout -> gchararray: Decoration Layout
        The layout for window decorations
      decoration-layout-set -> gboolean: Decoration Layout Set
        Whether the decoration-layout property has been set
      centering-policy -> HdyCenteringPolicy: Centering policy
        The policy to horizontally align the center widget
      transition-duration -> guint: Transition duration
        The animation duration, in milliseconds
      transition-running -> gboolean: Transition running
        Whether or not the transition is currently running
      interpolate-size -> gboolean: Interpolate size
        Whether or not the size should smoothly change when changing between differently sized children

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        centering_policy: CenteringPolicy
        custom_title: Optional[Gtk.Widget]
        decoration_layout: str
        decoration_layout_set: bool
        has_subtitle: bool
        interpolate_size: bool
        show_close_button: bool
        spacing: int
        subtitle: Optional[str]
        title: Optional[str]
        transition_duration: int
        transition_running: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Container = ...
    def __init__(
        self,
        centering_policy: CenteringPolicy = ...,
        custom_title: Optional[Gtk.Widget] = ...,
        decoration_layout: Optional[str] = ...,
        decoration_layout_set: bool = ...,
        has_subtitle: bool = ...,
        interpolate_size: bool = ...,
        show_close_button: bool = ...,
        spacing: int = ...,
        subtitle: Optional[str] = ...,
        title: Optional[str] = ...,
        transition_duration: int = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def get_centering_policy(self) -> CenteringPolicy: ...
    def get_custom_title(self) -> Optional[Gtk.Widget]: ...
    def get_decoration_layout(self) -> str: ...
    def get_has_subtitle(self) -> bool: ...
    def get_interpolate_size(self) -> bool: ...
    def get_show_close_button(self) -> bool: ...
    def get_subtitle(self) -> Optional[str]: ...
    def get_title(self) -> Optional[str]: ...
    def get_transition_duration(self) -> int: ...
    def get_transition_running(self) -> bool: ...
    @classmethod
    def new(cls) -> HeaderBar: ...
    def pack_end(self, child: Gtk.Widget) -> None: ...
    def pack_start(self, child: Gtk.Widget) -> None: ...
    def set_centering_policy(self, centering_policy: CenteringPolicy) -> None: ...
    def set_custom_title(self, title_widget: Optional[Gtk.Widget] = None) -> None: ...
    def set_decoration_layout(self, layout: Optional[str] = None) -> None: ...
    def set_has_subtitle(self, setting: bool) -> None: ...
    def set_interpolate_size(self, interpolate_size: bool) -> None: ...
    def set_show_close_button(self, setting: bool) -> None: ...
    def set_subtitle(self, subtitle: Optional[str] = None) -> None: ...
    def set_title(self, title: Optional[str] = None) -> None: ...
    def set_transition_duration(self, duration: int) -> None: ...

class HeaderBarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HeaderBarClass()
    """

    parent_class: Gtk.ContainerClass = ...
    padding: list[None] = ...

class HeaderGroup(GObject.Object, Gtk.Buildable):
    """
    :Constructors:

    ::

        HeaderGroup(**properties)
        new() -> Handy.HeaderGroup

    Object HdyHeaderGroup

    Signals from HdyHeaderGroup:
      update-decoration-layouts ()

    Properties from HdyHeaderGroup:
      decorate-all -> gboolean: Decorate all
        Whether the elements of the group should all receive the full decoration

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        decorate_all: bool
    props: Props = ...
    def __init__(self, decorate_all: bool = ...): ...
    def add_gtk_header_bar(self, header_bar: Gtk.HeaderBar) -> None: ...
    def add_header_bar(self, header_bar: HeaderBar) -> None: ...
    def add_header_group(self, header_group: HeaderGroup) -> None: ...
    def get_children(self) -> list[HeaderGroupChild]: ...
    def get_decorate_all(self) -> bool: ...
    @classmethod
    def new(cls) -> HeaderGroup: ...
    def remove_child(self, child: HeaderGroupChild) -> None: ...
    def remove_gtk_header_bar(self, header_bar: Gtk.HeaderBar) -> None: ...
    def remove_header_bar(self, header_bar: HeaderBar) -> None: ...
    def remove_header_group(self, header_group: HeaderGroup) -> None: ...
    def set_decorate_all(self, decorate_all: bool) -> None: ...

class HeaderGroupChild(GObject.Object):
    """
    :Constructors:

    ::

        HeaderGroupChild(**properties)

    Object HdyHeaderGroupChild

    Signals from GObject:
      notify (GParam)
    """

    def get_child_type(self) -> HeaderGroupChildType: ...
    def get_gtk_header_bar(self) -> Gtk.HeaderBar: ...
    def get_header_bar(self) -> HeaderBar: ...
    def get_header_group(self) -> HeaderGroup: ...

class HeaderGroupChildClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HeaderGroupChildClass()
    """

    parent_class: GObject.ObjectClass = ...

class HeaderGroupClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HeaderGroupClass()
    """

    parent_class: GObject.ObjectClass = ...

class Keypad(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        Keypad(**properties)
        new(symbols_visible:bool, letters_visible:bool) -> Gtk.Widget

    Object HdyKeypad

    Properties from HdyKeypad:
      row-spacing -> guint: Row spacing
        The amount of space between two consecutive rows
      column-spacing -> guint: Column spacing
        The amount of space between two consecutive columns
      letters-visible -> gboolean: Letters visible
        Whether the letters below the digits should be visible
      symbols-visible -> gboolean: Symbols visible
        Whether the hash, plus, and asterisk symbols should be visible
      entry -> GtkEntry: Entry
        The entry widget connected to the keypad
      end-action -> GtkWidget: End action
        The end action widget
      start-action -> GtkWidget: Start action
        The start action widget

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        column_spacing: int
        end_action: Optional[Gtk.Widget]
        entry: Gtk.Entry
        letters_visible: bool
        row_spacing: int
        start_action: Optional[Gtk.Widget]
        symbols_visible: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Bin = ...
    def __init__(
        self,
        column_spacing: int = ...,
        end_action: Optional[Gtk.Widget] = ...,
        entry: Optional[Gtk.Entry] = ...,
        letters_visible: bool = ...,
        row_spacing: int = ...,
        start_action: Optional[Gtk.Widget] = ...,
        symbols_visible: bool = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def get_column_spacing(self) -> int: ...
    def get_end_action(self) -> Optional[Gtk.Widget]: ...
    def get_entry(self) -> Gtk.Entry: ...
    def get_letters_visible(self) -> bool: ...
    def get_row_spacing(self) -> int: ...
    def get_start_action(self) -> Optional[Gtk.Widget]: ...
    def get_symbols_visible(self) -> bool: ...
    @classmethod
    def new(cls, symbols_visible: bool, letters_visible: bool) -> Keypad: ...
    def set_column_spacing(self, spacing: int) -> None: ...
    def set_end_action(self, end_action: Optional[Gtk.Widget] = None) -> None: ...
    def set_entry(self, entry: Optional[Gtk.Entry] = None) -> None: ...
    def set_letters_visible(self, letters_visible: bool) -> None: ...
    def set_row_spacing(self, spacing: int) -> None: ...
    def set_start_action(self, start_action: Optional[Gtk.Widget] = None) -> None: ...
    def set_symbols_visible(self, symbols_visible: bool) -> None: ...

class KeypadClass(GObject.GPointer):
    """
    :Constructors:

    ::

        KeypadClass()
    """

    parent_class: Gtk.BinClass = ...
    padding: list[None] = ...

class Leaflet(
    Gtk.Container, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable, Swipeable
):
    """
    :Constructors:

    ::

        Leaflet(**properties)
        new() -> Gtk.Widget

    Object HdyLeaflet

    Properties from HdyLeaflet:
      folded -> gboolean: Folded
        Whether the widget is folded
      hhomogeneous-folded -> gboolean: Horizontally homogeneous folded
        Horizontally homogeneous sizing when the leaflet is folded
      vhomogeneous-folded -> gboolean: Vertically homogeneous folded
        Vertically homogeneous sizing when the leaflet is folded
      hhomogeneous-unfolded -> gboolean: Box horizontally homogeneous
        Horizontally homogeneous sizing when the leaflet is unfolded
      vhomogeneous-unfolded -> gboolean: Box vertically homogeneous
        Vertically homogeneous sizing when the leaflet is unfolded
      visible-child -> GtkWidget: Visible child
        The widget currently visible when the leaflet is folded
      visible-child-name -> gchararray: Name of visible child
        The name of the widget currently visible when the children are stacked
      transition-type -> HdyLeafletTransitionType: Transition type
        The type of animation used to transition between modes and children
      mode-transition-duration -> guint: Mode transition duration
        The mode transition animation duration, in milliseconds
      child-transition-duration -> guint: Child transition duration
        The child transition animation duration, in milliseconds
      child-transition-running -> gboolean: Child transition running
        Whether or not the child transition is currently running
      interpolate-size -> gboolean: Interpolate size
        Whether or not the size should smoothly change when changing between differently sized children
      can-swipe-back -> gboolean: Can swipe back
        Whether or not swipe gesture can be used to switch to the previous child
      can-swipe-forward -> gboolean: Can swipe forward
        Whether or not swipe gesture can be used to switch to the next child

    Signals from HdySwipeable:
      child-switched (guint, gint64)

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        can_swipe_back: bool
        can_swipe_forward: bool
        child_transition_duration: int
        child_transition_running: bool
        folded: bool
        hhomogeneous_folded: bool
        hhomogeneous_unfolded: bool
        interpolate_size: bool
        mode_transition_duration: int
        transition_type: LeafletTransitionType
        vhomogeneous_folded: bool
        vhomogeneous_unfolded: bool
        visible_child: Gtk.Widget
        visible_child_name: str
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Container = ...
    def __init__(
        self,
        can_swipe_back: bool = ...,
        can_swipe_forward: bool = ...,
        child_transition_duration: int = ...,
        hhomogeneous_folded: bool = ...,
        hhomogeneous_unfolded: bool = ...,
        interpolate_size: bool = ...,
        mode_transition_duration: int = ...,
        transition_type: LeafletTransitionType = ...,
        vhomogeneous_folded: bool = ...,
        vhomogeneous_unfolded: bool = ...,
        visible_child: Gtk.Widget = ...,
        visible_child_name: str = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_adjacent_child(
        self, direction: NavigationDirection
    ) -> Optional[Gtk.Widget]: ...
    def get_can_swipe_back(self) -> bool: ...
    def get_can_swipe_forward(self) -> bool: ...
    def get_child_by_name(self, name: str) -> Optional[Gtk.Widget]: ...
    def get_child_transition_duration(self) -> int: ...
    def get_child_transition_running(self) -> bool: ...
    def get_folded(self) -> bool: ...
    def get_homogeneous(self, folded: bool, orientation: Gtk.Orientation) -> bool: ...
    def get_interpolate_size(self) -> bool: ...
    def get_mode_transition_duration(self) -> int: ...
    def get_transition_type(self) -> LeafletTransitionType: ...
    def get_visible_child(self) -> Gtk.Widget: ...
    def get_visible_child_name(self) -> str: ...
    def insert_child_after(
        self, child: Gtk.Widget, sibling: Optional[Gtk.Widget] = None
    ) -> None: ...
    def navigate(self, direction: NavigationDirection) -> bool: ...
    @classmethod
    def new(cls) -> Leaflet: ...
    def prepend(self, child: Gtk.Widget) -> None: ...
    def reorder_child_after(
        self, child: Gtk.Widget, sibling: Optional[Gtk.Widget] = None
    ) -> None: ...
    def set_can_swipe_back(self, can_swipe_back: bool) -> None: ...
    def set_can_swipe_forward(self, can_swipe_forward: bool) -> None: ...
    def set_child_transition_duration(self, duration: int) -> None: ...
    def set_homogeneous(
        self, folded: bool, orientation: Gtk.Orientation, homogeneous: bool
    ) -> None: ...
    def set_interpolate_size(self, interpolate_size: bool) -> None: ...
    def set_mode_transition_duration(self, duration: int) -> None: ...
    def set_transition_type(self, transition: LeafletTransitionType) -> None: ...
    def set_visible_child(self, visible_child: Gtk.Widget) -> None: ...
    def set_visible_child_name(self, name: str) -> None: ...

class LeafletClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LeafletClass()
    """

    parent_class: Gtk.ContainerClass = ...
    padding: list[None] = ...

class PreferencesGroup(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        PreferencesGroup(**properties)
        new() -> Gtk.Widget

    Object HdyPreferencesGroup

    Properties from HdyPreferencesGroup:
      description -> gchararray: Description
        Description
      title -> gchararray: Title
        Title
      use-markup -> gboolean: Use markup
        Whether to use markup for the title and description

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        description: str
        title: str
        use_markup: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Bin = ...
    def __init__(
        self,
        description: str = ...,
        title: str = ...,
        use_markup: bool = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def get_description(self) -> str: ...
    def get_title(self) -> str: ...
    def get_use_markup(self) -> bool: ...
    @classmethod
    def new(cls) -> PreferencesGroup: ...
    def set_description(self, description: str) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_use_markup(self, use_markup: bool) -> None: ...

class PreferencesGroupClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PreferencesGroupClass()
    """

    parent_class: Gtk.BinClass = ...
    padding: list[None] = ...

class PreferencesPage(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        PreferencesPage(**properties)
        new() -> Gtk.Widget

    Object HdyPreferencesPage

    Properties from HdyPreferencesPage:
      icon-name -> gchararray: Icon name
        Icon name
      title -> gchararray: Title
        Title

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        icon_name: Optional[str]
        title: Optional[str]
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Bin = ...
    def __init__(
        self,
        icon_name: Optional[str] = ...,
        title: Optional[str] = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_title(self) -> Optional[str]: ...
    @classmethod
    def new(cls) -> PreferencesPage: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_title(self, title: Optional[str] = None) -> None: ...

class PreferencesPageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PreferencesPageClass()
    """

    parent_class: Gtk.BinClass = ...
    padding: list[None] = ...

class PreferencesRow(
    Gtk.ListBoxRow, Atk.ImplementorIface, Gtk.Actionable, Gtk.Buildable
):
    """
    :Constructors:

    ::

        PreferencesRow(**properties)
        new() -> Gtk.Widget

    Object HdyPreferencesRow

    Properties from HdyPreferencesRow:
      title -> gchararray: Title
        The title of the preference
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: Activatable
        Whether this row can be activated
      selectable -> gboolean: Selectable
        Whether this row can be selected

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        title: Optional[str]
        use_underline: bool
        activatable: bool
        selectable: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        action_name: Optional[str]
        action_target: GLib.Variant
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.ListBoxRow = ...
    def __init__(
        self,
        title: Optional[str] = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        selectable: bool = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        action_name: Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def get_title(self) -> Optional[str]: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> PreferencesRow: ...
    def set_title(self, title: Optional[str] = None) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class PreferencesRowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PreferencesRowClass()
    """

    parent_class: Gtk.ListBoxRowClass = ...
    padding: list[None] = ...

class PreferencesWindow(Window, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        PreferencesWindow(**properties)
        new() -> Gtk.Widget

    Object HdyPreferencesWindow

    Properties from HdyPreferencesWindow:
      search-enabled -> gboolean: Search enabled
        Whether search is enabled
      can-swipe-back -> gboolean: Can swipe back
        Whether or not swipe gesture can be used to switch from a subpage to the preferences

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        can_swipe_back: bool
        search_enabled: bool
        accept_focus: bool
        application: Optional[Gtk.Application]
        attached_to: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: Optional[GdkPixbuf.Pixbuf]
        icon_name: Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: Optional[str]
        transient_for: Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        startup_id: str
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Window = ...
    def __init__(
        self,
        can_swipe_back: bool = ...,
        search_enabled: bool = ...,
        accept_focus: bool = ...,
        application: Optional[Gtk.Application] = ...,
        attached_to: Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        focus_on_map: bool = ...,
        focus_visible: bool = ...,
        gravity: Gdk.Gravity = ...,
        has_resize_grip: bool = ...,
        hide_titlebar_when_maximized: bool = ...,
        icon: Optional[GdkPixbuf.Pixbuf] = ...,
        icon_name: Optional[str] = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        role: str = ...,
        screen: Gdk.Screen = ...,
        skip_pager_hint: bool = ...,
        skip_taskbar_hint: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: Optional[Gtk.Window] = ...,
        type: Gtk.WindowType = ...,
        type_hint: Gdk.WindowTypeHint = ...,
        urgency_hint: bool = ...,
        window_position: Gtk.WindowPosition = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def close_subpage(self) -> None: ...
    def get_can_swipe_back(self) -> bool: ...
    def get_search_enabled(self) -> bool: ...
    @classmethod
    def new(cls) -> PreferencesWindow: ...
    def present_subpage(self, subpage: Gtk.Widget) -> None: ...
    def set_can_swipe_back(self, can_swipe_back: bool) -> None: ...
    def set_search_enabled(self, search_enabled: bool) -> None: ...

class PreferencesWindowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PreferencesWindowClass()
    """

    parent_class: WindowClass = ...
    padding: list[None] = ...

class SearchBar(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        SearchBar(**properties)
        new() -> Gtk.Widget

    Object HdySearchBar

    Properties from HdySearchBar:
      search-mode-enabled -> gboolean: Search Mode Enabled
        Whether the search mode is on and the search bar shown
      show-close-button -> gboolean: Show Close Button
        Whether to show the close button in the toolbar

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        search_mode_enabled: bool
        show_close_button: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Bin = ...
    def __init__(
        self,
        search_mode_enabled: bool = ...,
        show_close_button: bool = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def connect_entry(self, entry: Gtk.Entry) -> None: ...
    def get_search_mode(self) -> bool: ...
    def get_show_close_button(self) -> bool: ...
    def handle_event(self, event: Gdk.Event) -> bool: ...
    @classmethod
    def new(cls) -> SearchBar: ...
    def set_search_mode(self, search_mode: bool) -> None: ...
    def set_show_close_button(self, visible: bool) -> None: ...

class SearchBarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SearchBarClass()
    """

    parent_class: Gtk.BinClass = ...
    padding: list[None] = ...

class Squeezer(Gtk.Container, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        Squeezer(**properties)
        new() -> Gtk.Widget

    Object HdySqueezer

    Properties from HdySqueezer:
      homogeneous -> gboolean: Homogeneous
        Homogeneous sizing
      visible-child -> GtkWidget: Visible child
        The widget currently visible in the squeezer
      transition-duration -> guint: Transition duration
        The animation duration, in milliseconds
      transition-type -> HdySqueezerTransitionType: Transition type
        The type of animation used to transition
      transition-running -> gboolean: Transition running
        Whether or not the transition is currently running
      interpolate-size -> gboolean: Interpolate size
        Whether or not the size should smoothly change when changing between differently sized children
      xalign -> gfloat: X align
        The horizontal alignment, from 0 (start) to 1 (end)
      yalign -> gfloat: Y align
        The vertical alignment, from 0 (top) to 1 (bottom)

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        homogeneous: bool
        interpolate_size: bool
        transition_duration: int
        transition_running: bool
        transition_type: SqueezerTransitionType
        visible_child: Optional[Gtk.Widget]
        xalign: float
        yalign: float
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        homogeneous: bool = ...,
        interpolate_size: bool = ...,
        transition_duration: int = ...,
        transition_type: SqueezerTransitionType = ...,
        xalign: float = ...,
        yalign: float = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_child_enabled(self, child: Gtk.Widget) -> bool: ...
    def get_homogeneous(self) -> bool: ...
    def get_interpolate_size(self) -> bool: ...
    def get_transition_duration(self) -> int: ...
    def get_transition_running(self) -> bool: ...
    def get_transition_type(self) -> SqueezerTransitionType: ...
    def get_visible_child(self) -> Optional[Gtk.Widget]: ...
    def get_xalign(self) -> float: ...
    def get_yalign(self) -> float: ...
    @classmethod
    def new(cls) -> Squeezer: ...
    def set_child_enabled(self, child: Gtk.Widget, enabled: bool) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...
    def set_interpolate_size(self, interpolate_size: bool) -> None: ...
    def set_transition_duration(self, duration: int) -> None: ...
    def set_transition_type(self, transition: SqueezerTransitionType) -> None: ...
    def set_xalign(self, xalign: float) -> None: ...
    def set_yalign(self, yalign: float) -> None: ...

class SqueezerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SqueezerClass()
    """

    parent_class: Gtk.ContainerClass = ...

class StatusPage(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        StatusPage(**properties)
        new() -> Gtk.Widget

    Object HdyStatusPage

    Properties from HdyStatusPage:
      icon-name -> gchararray: Icon name
        The name of the icon to be used
      title -> gchararray: Title
        The title to be displayed below the icon
      description -> gchararray: Description
        The description to be displayed below the title

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        description: Optional[str]
        icon_name: Optional[str]
        title: Optional[str]
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        description: Optional[str] = ...,
        icon_name: Optional[str] = ...,
        title: Optional[str] = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def get_description(self) -> Optional[str]: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_title(self) -> Optional[str]: ...
    @classmethod
    def new(cls) -> StatusPage: ...
    def set_description(self, description: Optional[str] = None) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_title(self, title: Optional[str] = None) -> None: ...

class StatusPageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StatusPageClass()
    """

    parent_class: Gtk.BinClass = ...

class StyleManager(GObject.Object):
    """
    :Constructors:

    ::

        StyleManager(**properties)

    Object HdyStyleManager

    Properties from HdyStyleManager:
      display -> GdkDisplay: Display
        Display
      color-scheme -> HdyColorScheme: Color Scheme
        The current color scheme
      system-supports-color-schemes -> gboolean: System supports color schemes
        Whether the system supports color schemes
      dark -> gboolean: Dark
        Whether the application is using dark appearance
      high-contrast -> gboolean: High Contrast
        Whether the application is using high contrast appearance

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        color_scheme: ColorScheme
        dark: bool
        display: Gdk.Display
        high_contrast: bool
        system_supports_color_schemes: bool
    props: Props = ...
    def __init__(self, color_scheme: ColorScheme = ..., display: Gdk.Display = ...): ...
    def get_color_scheme(self) -> ColorScheme: ...
    def get_dark(self) -> bool: ...
    @staticmethod
    def get_default() -> StyleManager: ...
    def get_display(self) -> Gdk.Display: ...
    @staticmethod
    def get_for_display(display: Gdk.Display) -> StyleManager: ...
    def get_high_contrast(self) -> bool: ...
    def get_system_supports_color_schemes(self) -> bool: ...
    def set_color_scheme(self, color_scheme: ColorScheme) -> None: ...

class StyleManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class SwipeGroup(GObject.Object, Gtk.Buildable):
    """
    :Constructors:

    ::

        SwipeGroup(**properties)
        new() -> Handy.SwipeGroup

    Object HdySwipeGroup

    Signals from GObject:
      notify (GParam)
    """

    def add_swipeable(self, swipeable: Swipeable) -> None: ...
    def get_swipeables(self) -> list[Swipeable]: ...
    @classmethod
    def new(cls) -> SwipeGroup: ...
    def remove_swipeable(self, swipeable: Swipeable) -> None: ...

class SwipeGroupClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SwipeGroupClass()
    """

    parent_class: GObject.ObjectClass = ...

class SwipeTracker(GObject.Object, Gtk.Orientable):
    """
    :Constructors:

    ::

        SwipeTracker(**properties)
        new(swipeable:Handy.Swipeable) -> Handy.SwipeTracker

    Object HdySwipeTracker

    Signals from HdySwipeTracker:
      begin-swipe (HdyNavigationDirection, gboolean)
      update-swipe (gdouble)
      end-swipe (gint64, gdouble)

    Properties from HdySwipeTracker:
      swipeable -> HdySwipeable: Swipeable
        The swipeable the swipe tracker is attached to
      enabled -> gboolean: Enabled
        Whether the swipe tracker processes events
      reversed -> gboolean: Reversed
        Whether swipe direction is reversed
      allow-mouse-drag -> gboolean: Allow mouse drag
        Whether to allow dragging with mouse pointer
      allow-long-swipes -> gboolean: Allow long swipes
        Whether to allow swiping for more than one snap point at a time

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        allow_long_swipes: bool
        allow_mouse_drag: bool
        enabled: bool
        reversed: bool
        swipeable: Swipeable
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(
        self,
        allow_long_swipes: bool = ...,
        allow_mouse_drag: bool = ...,
        enabled: bool = ...,
        reversed: bool = ...,
        swipeable: Swipeable = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_allow_long_swipes(self) -> bool: ...
    def get_allow_mouse_drag(self) -> bool: ...
    def get_enabled(self) -> bool: ...
    def get_reversed(self) -> bool: ...
    def get_swipeable(self) -> Swipeable: ...
    @classmethod
    def new(cls, swipeable: Swipeable) -> SwipeTracker: ...
    def set_allow_long_swipes(self, allow_long_swipes: bool) -> None: ...
    def set_allow_mouse_drag(self, allow_mouse_drag: bool) -> None: ...
    def set_enabled(self, enabled: bool) -> None: ...
    def set_reversed(self, reversed: bool) -> None: ...
    def shift_position(self, delta: float) -> None: ...

class SwipeTrackerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SwipeTrackerClass()
    """

    parent_class: GObject.ObjectClass = ...

class Swipeable(GObject.GInterface):
    """
    Interface HdySwipeable

    Signals from GObject:
      notify (GParam)
    """

    def emit_child_switched(self, index: int, duration: int) -> None: ...
    def get_cancel_progress(self) -> float: ...
    def get_distance(self) -> float: ...
    def get_progress(self) -> float: ...
    def get_snap_points(self) -> list[float]: ...
    def get_swipe_area(
        self, navigation_direction: NavigationDirection, is_drag: bool
    ) -> Gdk.Rectangle: ...
    def get_swipe_tracker(self) -> SwipeTracker: ...
    def switch_child(self, index: int, duration: int) -> None: ...

class SwipeableInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        SwipeableInterface()
    """

    parent: GObject.TypeInterface = ...
    switch_child: Callable[[Swipeable, int, int], None] = ...
    get_swipe_tracker: Callable[[Swipeable], SwipeTracker] = ...
    get_distance: Callable[[Swipeable], float] = ...
    get_snap_points: Callable[[Swipeable], list[float]] = ...
    get_progress: Callable[[Swipeable], float] = ...
    get_cancel_progress: Callable[[Swipeable], float] = ...
    get_swipe_area: Callable[
        [Swipeable, NavigationDirection, bool], Gdk.Rectangle
    ] = ...
    padding: list[None] = ...

class TabBar(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        TabBar(**properties)
        new() -> Handy.TabBar

    Object HdyTabBar

    Signals from HdyTabBar:
      extra-drag-data-received (HdyTabPage, GdkDragContext, GtkSelectionData, guint, guint)

    Properties from HdyTabBar:
      view -> HdyTabView: View
        The view the tab bar controls.
      start-action-widget -> GtkWidget: Start action widget
        The widget shown before the tabs
      end-action-widget -> GtkWidget: End action widget
        The widget shown after the tabs
      autohide -> gboolean: Autohide
        Whether the tabs automatically hide
      tabs-revealed -> gboolean: Tabs revealed
        Whether the tabs are currently revealed
      expand-tabs -> gboolean: Expand tabs
        Whether tabs expand to full width
      inverted -> gboolean: Inverted
        Whether tabs use inverted layout
      extra-drag-dest-targets -> GtkTargetList: Extra drag destination targets
        Extra drag destination targets
      is-overflowing -> gboolean: Is overflowing
        Whether the tab bar is overflowing

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        autohide: bool
        end_action_widget: Optional[Gtk.Widget]
        expand_tabs: bool
        extra_drag_dest_targets: Optional[Gtk.TargetList]
        inverted: bool
        is_overflowing: bool
        start_action_widget: Optional[Gtk.Widget]
        tabs_revealed: bool
        view: Optional[TabView]
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        autohide: bool = ...,
        end_action_widget: Optional[Gtk.Widget] = ...,
        expand_tabs: bool = ...,
        extra_drag_dest_targets: Optional[Gtk.TargetList] = ...,
        inverted: bool = ...,
        start_action_widget: Optional[Gtk.Widget] = ...,
        view: Optional[TabView] = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def get_autohide(self) -> bool: ...
    def get_end_action_widget(self) -> Optional[Gtk.Widget]: ...
    def get_expand_tabs(self) -> bool: ...
    def get_extra_drag_dest_targets(self) -> Optional[Gtk.TargetList]: ...
    def get_inverted(self) -> bool: ...
    def get_is_overflowing(self) -> bool: ...
    def get_start_action_widget(self) -> Optional[Gtk.Widget]: ...
    def get_tabs_revealed(self) -> bool: ...
    def get_view(self) -> Optional[TabView]: ...
    @classmethod
    def new(cls) -> TabBar: ...
    def set_autohide(self, autohide: bool) -> None: ...
    def set_end_action_widget(self, widget: Optional[Gtk.Widget] = None) -> None: ...
    def set_expand_tabs(self, expand_tabs: bool) -> None: ...
    def set_extra_drag_dest_targets(
        self, extra_drag_dest_targets: Optional[Gtk.TargetList] = None
    ) -> None: ...
    def set_inverted(self, inverted: bool) -> None: ...
    def set_start_action_widget(self, widget: Optional[Gtk.Widget] = None) -> None: ...
    def set_view(self, view: Optional[TabView] = None) -> None: ...

class TabBarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TabBarClass()
    """

    parent_class: Gtk.BinClass = ...

class TabPage(GObject.Object):
    """
    :Constructors:

    ::

        TabPage(**properties)

    Object HdyTabPage

    Properties from HdyTabPage:
      child -> GtkWidget: Child
        The child of the page
      parent -> HdyTabPage: Parent
        The parent page of the page
      selected -> gboolean: Selected
        Whether the page is selected
      pinned -> gboolean: Pinned
        Whether the page is pinned
      title -> gchararray: Title
        The title of the page
      tooltip -> gchararray: Tooltip
        The tooltip of the page
      icon -> GIcon: Icon
        The icon of the page
      loading -> gboolean: Loading
        Whether the page is loading
      indicator-icon -> GIcon: Indicator icon
        An indicator icon for the page
      indicator-activatable -> gboolean: Indicator activatable
        Whether the indicator icon is activatable
      needs-attention -> gboolean: Needs attention
        Whether the page needs attention

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        child: Gtk.Widget
        icon: Optional[Gio.Icon]
        indicator_activatable: bool
        indicator_icon: Optional[Gio.Icon]
        loading: bool
        needs_attention: bool
        parent: Optional[TabPage]
        pinned: bool
        selected: bool
        title: Optional[str]
        tooltip: Optional[str]
    props: Props = ...
    def __init__(
        self,
        child: Gtk.Widget = ...,
        icon: Optional[Gio.Icon] = ...,
        indicator_activatable: bool = ...,
        indicator_icon: Optional[Gio.Icon] = ...,
        loading: bool = ...,
        needs_attention: bool = ...,
        parent: TabPage = ...,
        title: Optional[str] = ...,
        tooltip: Optional[str] = ...,
    ): ...
    def get_child(self) -> Gtk.Widget: ...
    def get_icon(self) -> Optional[Gio.Icon]: ...
    def get_indicator_activatable(self) -> bool: ...
    def get_indicator_icon(self) -> Optional[Gio.Icon]: ...
    def get_loading(self) -> bool: ...
    def get_needs_attention(self) -> bool: ...
    def get_parent(self) -> Optional[TabPage]: ...
    def get_pinned(self) -> bool: ...
    def get_selected(self) -> bool: ...
    def get_title(self) -> Optional[str]: ...
    def get_tooltip(self) -> Optional[str]: ...
    def set_icon(self, icon: Optional[Gio.Icon] = None) -> None: ...
    def set_indicator_activatable(self, activatable: bool) -> None: ...
    def set_indicator_icon(self, indicator_icon: Optional[Gio.Icon] = None) -> None: ...
    def set_loading(self, loading: bool) -> None: ...
    def set_needs_attention(self, needs_attention: bool) -> None: ...
    def set_title(self, title: Optional[str] = None) -> None: ...
    def set_tooltip(self, tooltip: Optional[str] = None) -> None: ...

class TabPageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TabPageClass()
    """

    parent_class: GObject.ObjectClass = ...

class TabView(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        TabView(**properties)
        new() -> Handy.TabView

    Object HdyTabView

    Signals from HdyTabView:
      page-reordered (HdyTabPage, gint)
      create-window () -> HdyTabView
      page-attached (HdyTabPage, gint)
      page-detached (HdyTabPage, gint)
      close-page (HdyTabPage) -> gboolean
      setup-menu (HdyTabPage)
      indicator-activated (HdyTabPage)

    Properties from HdyTabView:
      n-pages -> gint: Number of pages
        The number of pages in the tab view
      n-pinned-pages -> gint: Number of pinned pages
        The number of pinned pages in the tab view
      is-transferring-page -> gboolean: Is transferring page
        Whether a page is being transferred
      selected-page -> HdyTabPage: Selected page
        The currently selected page
      default-icon -> GIcon: Default icon
        Default page icon
      menu-model -> GMenuModel: Menu model
        Tab context menu model
      shortcut-widget -> GtkWidget: Shortcut widget
        Tab shortcut widget

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        default_icon: Gio.Icon
        is_transferring_page: bool
        menu_model: Optional[Gio.MenuModel]
        n_pages: int
        n_pinned_pages: int
        selected_page: Optional[TabPage]
        shortcut_widget: Optional[Gtk.Widget]
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        default_icon: Gio.Icon = ...,
        menu_model: Optional[Gio.MenuModel] = ...,
        selected_page: TabPage = ...,
        shortcut_widget: Optional[Gtk.Widget] = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def add_page(
        self, child: Gtk.Widget, parent: Optional[TabPage] = None
    ) -> TabPage: ...
    def append(self, child: Gtk.Widget) -> TabPage: ...
    def append_pinned(self, child: Gtk.Widget) -> TabPage: ...
    def close_other_pages(self, page: TabPage) -> None: ...
    def close_page(self, page: TabPage) -> None: ...
    def close_page_finish(self, page: TabPage, confirm: bool) -> None: ...
    def close_pages_after(self, page: TabPage) -> None: ...
    def close_pages_before(self, page: TabPage) -> None: ...
    def get_default_icon(self) -> Gio.Icon: ...
    def get_is_transferring_page(self) -> bool: ...
    def get_menu_model(self) -> Optional[Gio.MenuModel]: ...
    def get_n_pages(self) -> int: ...
    def get_n_pinned_pages(self) -> int: ...
    def get_nth_page(self, position: int) -> TabPage: ...
    def get_page(self, child: Gtk.Widget) -> TabPage: ...
    def get_page_position(self, page: TabPage) -> int: ...
    def get_pages(self) -> Gio.ListModel: ...
    def get_selected_page(self) -> Optional[TabPage]: ...
    def get_shortcut_widget(self) -> Optional[Gtk.Widget]: ...
    def insert(self, child: Gtk.Widget, position: int) -> TabPage: ...
    def insert_pinned(self, child: Gtk.Widget, position: int) -> TabPage: ...
    @classmethod
    def new(cls) -> TabView: ...
    def prepend(self, child: Gtk.Widget) -> TabPage: ...
    def prepend_pinned(self, child: Gtk.Widget) -> TabPage: ...
    def reorder_backward(self, page: TabPage) -> bool: ...
    def reorder_first(self, page: TabPage) -> bool: ...
    def reorder_forward(self, page: TabPage) -> bool: ...
    def reorder_last(self, page: TabPage) -> bool: ...
    def reorder_page(self, page: TabPage, position: int) -> bool: ...
    def select_next_page(self) -> bool: ...
    def select_previous_page(self) -> bool: ...
    def set_default_icon(self, default_icon: Gio.Icon) -> None: ...
    def set_menu_model(self, menu_model: Optional[Gio.MenuModel] = None) -> None: ...
    def set_page_pinned(self, page: TabPage, pinned: bool) -> None: ...
    def set_selected_page(self, selected_page: TabPage) -> None: ...
    def set_shortcut_widget(self, widget: Optional[Gtk.Widget] = None) -> None: ...
    def transfer_page(
        self, page: TabPage, other_view: TabView, position: int
    ) -> None: ...

class TabViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TabViewClass()
    """

    parent_class: Gtk.BinClass = ...

class TitleBar(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        TitleBar(**properties)
        new() -> Gtk.Widget

    Object HdyTitleBar

    Properties from HdyTitleBar:
      selection-mode -> gboolean: Selection mode
        Whether or not the title bar is in selection mode

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        selection_mode: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        selection_mode: bool = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def get_selection_mode(self) -> bool: ...
    @classmethod
    def new(cls) -> TitleBar: ...
    def set_selection_mode(self, selection_mode: bool) -> None: ...

class TitleBarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TitleBarClass()
    """

    parent_class: Gtk.BinClass = ...

class ValueObject(GObject.Object):
    """
    :Constructors:

    ::

        ValueObject(**properties)
        new(value:GObject.Value) -> Handy.ValueObject

    Object HdyValueObject

    Properties from HdyValueObject:
      value -> GValue: Value
        The contained value

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        value: Any
    props: Props = ...
    def __init__(self, value: Any = ...): ...
    def copy_value(self, dest: Any) -> None: ...
    def dup_string(self) -> str: ...
    def get_string(self) -> str: ...
    def get_value(self) -> Any: ...
    @classmethod
    def new(cls, value: Any) -> ValueObject: ...

class ValueObjectClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ValueObjectClass()
    """

    parent_class: GObject.ObjectClass = ...

class ViewSwitcher(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        ViewSwitcher(**properties)
        new() -> Gtk.Widget

    Object HdyViewSwitcher

    Properties from HdyViewSwitcher:
      policy -> HdyViewSwitcherPolicy: Policy
        The policy to determine the mode to use
      narrow-ellipsize -> PangoEllipsizeMode: Narrow ellipsize
        The preferred place to ellipsize the string, if the narrow mode label does not have enough room to display the entire string
      stack -> GtkStack: Stack
        Stack

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        narrow_ellipsize: Pango.EllipsizeMode
        policy: ViewSwitcherPolicy
        stack: Optional[Gtk.Stack]
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        narrow_ellipsize: Pango.EllipsizeMode = ...,
        policy: ViewSwitcherPolicy = ...,
        stack: Optional[Gtk.Stack] = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def get_narrow_ellipsize(self) -> Pango.EllipsizeMode: ...
    def get_policy(self) -> ViewSwitcherPolicy: ...
    def get_stack(self) -> Optional[Gtk.Stack]: ...
    @classmethod
    def new(cls) -> ViewSwitcher: ...
    def set_narrow_ellipsize(self, mode: Pango.EllipsizeMode) -> None: ...
    def set_policy(self, policy: ViewSwitcherPolicy) -> None: ...
    def set_stack(self, stack: Optional[Gtk.Stack] = None) -> None: ...

class ViewSwitcherBar(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        ViewSwitcherBar(**properties)
        new() -> Gtk.Widget

    Object HdyViewSwitcherBar

    Properties from HdyViewSwitcherBar:
      policy -> HdyViewSwitcherPolicy: Policy
        The policy to determine the mode to use
      stack -> GtkStack: Stack
        Stack
      reveal -> gboolean: Reveal
        Whether the view switcher is revealed

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        policy: ViewSwitcherPolicy
        reveal: bool
        stack: Optional[Gtk.Stack]
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        policy: ViewSwitcherPolicy = ...,
        reveal: bool = ...,
        stack: Optional[Gtk.Stack] = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def get_policy(self) -> ViewSwitcherPolicy: ...
    def get_reveal(self) -> bool: ...
    def get_stack(self) -> Optional[Gtk.Stack]: ...
    @classmethod
    def new(cls) -> ViewSwitcherBar: ...
    def set_policy(self, policy: ViewSwitcherPolicy) -> None: ...
    def set_reveal(self, reveal: bool) -> None: ...
    def set_stack(self, stack: Optional[Gtk.Stack] = None) -> None: ...

class ViewSwitcherBarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ViewSwitcherBarClass()
    """

    parent_class: Gtk.BinClass = ...

class ViewSwitcherClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ViewSwitcherClass()
    """

    parent_class: Gtk.BinClass = ...

class ViewSwitcherTitle(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        ViewSwitcherTitle(**properties)
        new() -> Handy.ViewSwitcherTitle

    Object HdyViewSwitcherTitle

    Properties from HdyViewSwitcherTitle:
      policy -> HdyViewSwitcherPolicy: Policy
        The policy to determine the mode to use
      stack -> GtkStack: Stack
        Stack
      title -> gchararray: Title
        The title to display
      subtitle -> gchararray: Subtitle
        The subtitle to display
      view-switcher-enabled -> gboolean: View switcher enabled
        Whether the view switcher is enabled
      title-visible -> gboolean: Title visible
        Whether the title label is visible

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        policy: ViewSwitcherPolicy
        stack: Optional[Gtk.Stack]
        subtitle: Optional[str]
        title: Optional[str]
        title_visible: bool
        view_switcher_enabled: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        policy: ViewSwitcherPolicy = ...,
        stack: Optional[Gtk.Stack] = ...,
        subtitle: Optional[str] = ...,
        title: Optional[str] = ...,
        view_switcher_enabled: bool = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def get_policy(self) -> ViewSwitcherPolicy: ...
    def get_stack(self) -> Optional[Gtk.Stack]: ...
    def get_subtitle(self) -> Optional[str]: ...
    def get_title(self) -> Optional[str]: ...
    def get_title_visible(self) -> bool: ...
    def get_view_switcher_enabled(self) -> bool: ...
    @classmethod
    def new(cls) -> ViewSwitcherTitle: ...
    def set_policy(self, policy: ViewSwitcherPolicy) -> None: ...
    def set_stack(self, stack: Optional[Gtk.Stack] = None) -> None: ...
    def set_subtitle(self, subtitle: Optional[str] = None) -> None: ...
    def set_title(self, title: Optional[str] = None) -> None: ...
    def set_view_switcher_enabled(self, enabled: bool) -> None: ...

class ViewSwitcherTitleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ViewSwitcherTitleClass()
    """

    parent_class: Gtk.BinClass = ...

class Window(Gtk.Window, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        Window(**properties)
        new() -> Gtk.Widget

    Object HdyWindow

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accept_focus: bool
        application: Optional[Gtk.Application]
        attached_to: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: Optional[GdkPixbuf.Pixbuf]
        icon_name: Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: Optional[str]
        transient_for: Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        startup_id: str
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Window = ...
    def __init__(
        self,
        accept_focus: bool = ...,
        application: Optional[Gtk.Application] = ...,
        attached_to: Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        focus_on_map: bool = ...,
        focus_visible: bool = ...,
        gravity: Gdk.Gravity = ...,
        has_resize_grip: bool = ...,
        hide_titlebar_when_maximized: bool = ...,
        icon: Optional[GdkPixbuf.Pixbuf] = ...,
        icon_name: Optional[str] = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        role: str = ...,
        screen: Gdk.Screen = ...,
        skip_pager_hint: bool = ...,
        skip_taskbar_hint: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: Optional[Gtk.Window] = ...,
        type: Gtk.WindowType = ...,
        type_hint: Gdk.WindowTypeHint = ...,
        urgency_hint: bool = ...,
        window_position: Gtk.WindowPosition = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    @classmethod
    def new(cls) -> Window: ...

class WindowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WindowClass()
    """

    parent_class: Gtk.WindowClass = ...
    padding: list[None] = ...

class WindowHandle(Gtk.EventBox, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        WindowHandle(**properties)
        new() -> Gtk.Widget

    Object HdyWindowHandle

    Properties from GtkEventBox:
      visible-window -> gboolean: Visible Window
        Whether the event box is visible, as opposed to invisible and only used to trap events.
      above-child -> gboolean: Above child
        Whether the event-trapping window of the eventbox is above the window of the child widget as opposed to below it.

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        above_child: bool
        visible_window: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        above_child: bool = ...,
        visible_window: bool = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    @classmethod
    def new(cls) -> WindowHandle: ...

class WindowHandleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WindowHandleClass()
    """

    parent_class: Gtk.EventBoxClass = ...

class CenteringPolicy(GObject.GEnum):
    LOOSE = 0
    STRICT = 1

class ColorScheme(GObject.GEnum):
    DEFAULT = 0
    FORCE_DARK = 4
    FORCE_LIGHT = 1
    PREFER_DARK = 3
    PREFER_LIGHT = 2

class DeckTransitionType(GObject.GEnum):
    OVER = 0
    SLIDE = 2
    UNDER = 1

class FlapFoldPolicy(GObject.GEnum):
    ALWAYS = 1
    AUTO = 2
    NEVER = 0

class FlapTransitionType(GObject.GEnum):
    OVER = 0
    SLIDE = 2
    UNDER = 1

class HeaderGroupChildType(GObject.GEnum):
    GTK_HEADER_BAR = 1
    HEADER_BAR = 0
    HEADER_GROUP = 2

class LeafletTransitionType(GObject.GEnum):
    OVER = 0
    SLIDE = 2
    UNDER = 1

class NavigationDirection(GObject.GEnum):
    BACK = 0
    FORWARD = 1

class SqueezerTransitionType(GObject.GEnum):
    CROSSFADE = 1
    NONE = 0

class ViewSwitcherPolicy(GObject.GEnum):
    AUTO = 0
    NARROW = 1
    WIDE = 2
