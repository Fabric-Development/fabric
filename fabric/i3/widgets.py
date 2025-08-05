from typing import cast
from loguru import logger
from collections.abc import Iterable, Callable

from fabric.i3.service import I3, I3Event, I3MessageType
from fabric.core.widgets import WorkspaceButton, Workspaces, ActiveWindow, Language
from fabric.utils.helpers import FormattedString, bulk_connect, truncate


connection: I3 | None = None


def get_i3_connection() -> I3:
    global connection
    if not connection:
        connection = I3()

    return connection


class I3Workspaces(Workspaces):
    def __init__(
        self,
        buttons: Iterable[WorkspaceButton] | None = None,
        buttons_factory: Callable[[int], WorkspaceButton | None]
        | None = Workspaces.default_buttons_factory,
        invert_scroll: bool = False,
        **kwargs,
    ):
        super().__init__(buttons, buttons_factory, invert_scroll, **kwargs)
        self.connection = get_i3_connection()

        bulk_connect(
            self.connection,
            {
                "event::workspace::focus": self.on_workspace_event,
                "event::workspace::init": self.on_workspace_event,
                "event::workspace::empty": self.on_workspace_event,
                "event::workspace::urgent": self.on_workspace_event,
            },
        )

        if self.connection.ready:
            self.on_ready()
        else:
            self.connection.connect("notify::ready", self.on_ready)
        self.connect("scroll-event", self.do_handle_scroll)

    def on_ready(self):
        workspaces_reply = self.connection.send_command(
            "", I3MessageType.GET_WORKSPACES
        )
        if not (workspaces_reply.is_ok and isinstance(workspaces_reply.reply, list)):
            return logger.error(
                f"[I3Workspaces] Failed to get workspaces from i3: {workspaces_reply}"
            )

        for ws in cast(list[dict[str, int]], workspaces_reply.reply):
            if (ws_id := ws.get("num")) is None:
                continue

            self.workspace_created(ws_id)

            if ws.get("focused", False):
                self.workspace_activated(ws_id)

            if ws.get("urgent", False):
                self.urgent(ws_id)

    def on_workspace_event(self, _, event: I3Event):
        change = event.data.get("change")

        workspace_data = event.data.get("current", {})
        ws_id = workspace_data.get("num")

        if ws_id is None:
            return

        match change:
            case "focus":
                self.workspace_activated(ws_id)
            case "init":
                self.workspace_created(ws_id)
            case "empty":
                self.workspace_destroyed(ws_id)
            case "urgent":
                self.urgent(ws_id)

        return logger.debug(f"[I3Workspaces] Event: {change}, Workspace ID: {ws_id}")

    # override signals from super class
    def do_action_next(self):
        return self.connection.send_command("workspace next_on_output")

    def do_action_previous(self):
        return self.connection.send_command("workspace prev_on_output")

    def do_button_clicked(self, button: WorkspaceButton):
        return self.connection.send_command(f"workspace number {button.id}")


class I3ActiveWindow(ActiveWindow):
    def __init__(
        self,
        formatter: FormattedString = FormattedString(
            "{'Desktop' if not win_title else truncate(win_title, 42)}",
            truncate=truncate,
        ),
        **kwargs,
    ):
        super().__init__(formatter, **kwargs)
        self.connection = get_i3_connection()

        bulk_connect(
            self.connection,
            {
                "event::window::focus": self.on_window_event,
                "event::window::title": self.on_window_event,
                "event::window::close": self.on_window_event,
            },
        )

        if self.connection.ready:
            self.on_ready()
        else:
            self.connection.connect("notify::ready", self.on_ready)

    def on_ready(self):
        return self.do_initialize(), logger.info(
            "[I3ActiveWindow] Connected to the i3 socket and initialized."
        )

    def do_find_focused_window(self, node: dict):
        if node.get("focused"):
            return node
        for sub_node in node.get("nodes", []) + node.get("floating_nodes", []):
            if found := self.do_find_focused_window(sub_node):
                return found
        return None

    def do_initialize(self):
        tree_reply = self.connection.send_command("", I3MessageType.GET_TREE)
        if not (tree_reply.is_ok and isinstance(tree_reply.reply, dict)):
            return self.window_activated("", "Desktop")

        focused_node = self.do_find_focused_window(tree_reply.reply)
        if not focused_node:
            self.window_activated("", "")
            return
        win_class = focused_node.get("window_properties", {}).get("class", "unknown")
        win_title = focused_node.get("name", win_class)
        return self.window_activated(win_class, win_title)

    def on_window_event(self, _, event: I3Event):
        change = event.data.get("change")
        container = event.data.get("container", {})

        if change in ("focus", "title"):
            win_class = container.get("window_properties", {}).get("class", "unknown")
            win_title = container.get("name", win_class)
            self.window_activated(win_class, win_title)
        elif change == "close":
            self.do_initialize()

        return logger.debug(
            f"[I3ActiveWindow] Event: {change}, Container: {container.get('name')}"
        )


class I3Language(Language):
    def __init__(
        self,
        keyboard: str = ".*",
        formatter: FormattedString = FormattedString("{language}"),
        **kwargs,
    ):
        super().__init__(keyboard, formatter, **kwargs)
        self.connection = get_i3_connection()
        self.connection.connect("event::input::xkb_layout", self.on_active_layout)

        if self.connection.ready:
            self.on_ready()
        else:
            self.connection.connect("notify::ready", self.on_ready)

    def on_ready(self):
        return self.do_initialize(), logger.info(
            "[I3Language] Connected to the sway socket"
        )

    def on_active_layout(self, _, event: I3Event):
        input_device = event.data.get("input", {})
        if not input_device:
            return logger.warning(
                f"[I3Language] Invalid event data from sway: {event.raw_data}"
            )

        keyboard_name = input_device.get("identifier")
        language = input_device.get("xkb_active_layout_name")

        if not keyboard_name or not language:
            return logger.warning(
                f"[I3Language] Could not extract keyboard or language from event: {event.raw_data}"
            )

        return self.layout_changed(language, keyboard_name)

    def do_initialize(self):
        devices_reply = self.connection.send_command("", I3MessageType.GET_INPUTS)

        if not (devices_reply.is_ok and isinstance(devices_reply.reply, list)):
            return logger.warning(
                f"[I3Language] Couldn't get devices from sway, got: {devices_reply.reply}"
            )

        keyboards = [d for d in devices_reply.reply if d.get("type") == "keyboard"]
        if not keyboards:
            return logger.warning("[I3Language] No keyboards found.")

        active_language: str | None = None
        for kb in keyboards:
            kb_name = kb.get("identifier")
            language = kb.get("xkb_active_layout_name")

            if not kb_name or not language:
                continue

            if self.layout_changed(language, kb_name):
                active_language = language
                logger.debug(
                    f"[Language] Found language: {language} for keyboard {kb_name}"
                )
                break

        return (
            logger.warning(
                f"[I3Language] No matching keyboard found for pattern: {self.keyboard}"
            )
            if not active_language
            else None
        )


__all__ = [
    "I3Language",
    "I3Workspaces",
    "I3ActiveWindow",
    "WorkspaceButton",
    "get_i3_connection",
]
