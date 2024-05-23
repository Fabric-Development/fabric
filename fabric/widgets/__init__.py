from .box import Box
from .button import Button
from .centerbox import CenterBox
from .chart import Chart
from .circular_progress_bar import CircularProgressBar
from .container import Container
from .date_time import DateTime
from .entry import Entry
from .eventbox import EventBox
from .flowbox import FlowBox
from .image import Image
from .label import Label
from .overlay import Overlay
from .revealer import Revealer
from .scale import Scale, ScaleIncrements, ScaleMark
from .scrolled_window import ScrolledWindow
from .stack import Stack
from .svg import Svg
from .widget import Widget
from .window import Window
from .webview import WebView

# widgets depending on a fabric service
# system tray
from fabric.system_tray.widgets import SystemTray

# hyprland widgets
from fabric.hyprland.widgets import Workspaces as HyprlandWorkspaces
from fabric.hyprland.widgets import WorkspaceButton as HyprlandWorkspaceButton
from fabric.hyprland.widgets import ActiveWindow as HyprlandActiveWindow
from fabric.hyprland.widgets import Language as HyprlandLanguage

# display protocol specific widgets
from .wayland import Window as WaylandWindow
from .x11 import Window as X11Window
