import gi
import re
import json

from loguru import logger
from collections.abc import Iterable, Callable
from typing import Literal

from fabric.core.service import Property
from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.eventbox import EventBox
from fabric.niri.service import Niri, NiriEvent
from fabric.utils.helpers import FormattedString, bulk_connect, truncate

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

connection: Niri | None = None

def get_niri_connection() -> Niri:
    global connection
    if not connection:
        connection = Niri()

    return connection

class WorkspaceButton(Button):
    @Property(int, "readable")
    def id(self) -> int:
        return self._id

    @Property(bool, "read-write", default_value=False)
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value: bool):
        self._active = value
        if value is True:
            self.urgent = False
        (self.remove_style_class if not value else self.add_style_class)("active")
        return self.do_bake_label()

    @Property(bool, "read-write", default_value=False)
    def urgent(self) -> bool:
        return self._urgent

    @urgent.setter
    def urgent(self, value: bool):
        self._urgent = value
        (self.remove_style_class if not value else self.add_style_class)("urgent")
        return self.do_bake_label()

    @Property(bool, "read-write", default_value=True)
    def empty(self) -> bool:
        return self._empty

    @empty.setter
    def empty(self, value: bool):
        self._empty = value
        (self.remove_style_class if not value else self.add_style_class)("empty")
        return self.do_bake_label()

    def __init__(
        self,
        id: int,
        label: FormattedString | str | None = None,
        image: Gtk.Image | None = None,
        child: Gtk.Widget | None = None,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_classes: Iterable[str] | str | None = None,
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
        size: Iterable[int] | int | None = None,
        **kwargs,
    ):
        super().__init__(
            None,
            image,
            child,
            name,
            visible,
            all_visible,
            style,
            style_classes,
            tooltip_text,
            tooltip_markup,
            h_align,
            v_align,
            h_expand,
            v_expand,
            size,
            **kwargs,
        )
        self._id: int = id
        self._label: FormattedString | None = (
            FormattedString(label) if isinstance(label, str) else label
        )
        self._active: bool = False
        self._urgent: bool = False
        self._empty: bool = True

        self.active = False
        self.urgent = False
        self.empty = True

    def do_bake_label(self):
        if not self._label:
            return
        return self.set_label(self._label.format(button=self))

class Workspaces(EventBox):
    @staticmethod
    def default_buttons_factory(workspace_id: int):
        return WorkspaceButton(id=workspace_id, label=str(workspace_id))

    def __init__(
        self,
        buttons: Iterable[WorkspaceButton] | None = None,
        buttons_factory: Callable[[int], WorkspaceButton | None]
        | None = default_buttons_factory,
        invert_scroll: bool = False,
        empty_scroll: bool = False,
        **kwargs,
    ):
        super().__init__(events="scroll")
        self.connection = get_niri_connection()
        self._container = Box(**kwargs)
        self.children = self._container

        self._active_workspace: int | None = None
        self._buttons: dict[int, WorkspaceButton] = {}
        self._buttons_preset: list[WorkspaceButton] = list(buttons or [])
        self._buttons_factory = buttons_factory
        self._invert_scroll = invert_scroll
        self._empty_scroll = empty_scroll

        bulk_connect(
            self.connection,
            {
                "event::WorkspaceActivated": self.on_workspace,
                "event::WorkspacesChanged": self.on_workspace,
                "event::WorkspaceUrgencyChanged": self.on_workspace_urgent,
            },
        )

        if self.connection.ready:
            self.on_ready(None)
        else:
            self.connection.connect("event::ready", self.on_ready)

        self.connect("scroll-event", self.scroll_handler)

    def on_ready(self, _):
        response = self.connection.send_command("Workspaces").reply
        json_data = self.parse_niri_response(response)
        if not json_data:
            return

        workspaces = json_data.get("Workspaces", [])
        self.sync_workspaces(workspaces)

        active = self.check_active_workspace_niri(json_data)
        if active:
            self._active_workspace = active["id"]
            if (btn := self._buttons.get(self._active_workspace)):
                btn.active = True

    def on_workspace(self, _, event: NiriEvent):
        logger.debug(f"[EVENT] on_workspace: {event.data}")

        response = self.connection.send_command("Workspaces").reply
        json_data = self.parse_niri_response(response)
        if not json_data:
            return

        workspaces = json_data.get("Workspaces", [])
        self.sync_workspaces(workspaces)

        active_ws = self.check_active_workspace_niri(json_data)
        if not active_ws:
            return

        new_active_id = active_ws["id"]
        if new_active_id == self._active_workspace:
            return

        if (old := self._buttons.get(self._active_workspace)):
            old.active = False

        self._active_workspace = new_active_id

        if (new := self._buttons.get(new_active_id)):
            new.active = True
            new.urgent = False

    def on_workspace_urgent(self, _, event: NiriEvent):
        urgent_ws = self.check_urgent_workspace_niri(event.data)
        ws_id = urgent_ws.get("id")
        if not ws_id:
            return

        if (btn := self._buttons.get(ws_id)):
            btn.urgent = True
            logger.info(f"[Workspaces] workspace {ws_id} is now urgent")

    def scroll_handler(self, _, event: Gdk.EventScroll):
        cmd = "" if self._empty_scroll else "e"
        direction = event.direction

        if direction == Gdk.ScrollDirection.UP:
            cmd += "-1" if self._invert_scroll else "+1"
            logger.info("[Workspaces] Moving to the next workspace")
        elif direction == Gdk.ScrollDirection.DOWN:
            cmd += "+1" if self._invert_scroll else "-1"
            logger.info("[Workspaces] Moving to the previous workspace")
        else:
            logger.warning(f"[Workspaces] Unknown scroll direction ({direction})")
            return

        self.connection.send_command(f"batch/dispatch workspace {cmd}")

    def sync_workspaces(self, fresh_data: list[dict]) -> None:
        """
        Sync internal workspace buttons with the latest workspace data.
        Adds new buttons, updates existing ones, and removes stale ones.
        """
        fresh_ids = {ws["id"] for ws in fresh_data if "id" in ws}

        # Add/update buttons
        for ws in fresh_data:
            id_ = ws["id"]
            btn = self._buttons.get(id_)
            if not btn:
                btn = self.lookup_or_bake_button(id_)
                if not btn:
                    continue
                self.insert_button(btn)

            btn.empty = False
            btn.active = ws.get("is_active", False)

        # Remove old buttons
        for id_, btn in list(self._buttons.items()):
            if id_ not in fresh_ids:
                self.remove_button(btn)

    def insert_button(self, button: WorkspaceButton) -> None:
        self._buttons[button.id] = button
        self._container.add(button)
        button.connect("clicked", self.on_workspace_button_clicked)
        self.reorder_buttons()

    def remove_button(self, button: WorkspaceButton) -> None:
        if self._buttons.pop(button.id, None):
            self._container.remove(button)
        button.destroy()

    def reorder_buttons(self):
        for pos, btn in enumerate(sorted(self._buttons.values(), key=lambda b: b.id)):
            self._container.reorder_child(btn, pos)

    def lookup_or_bake_button(self, workspace_id: int) -> WorkspaceButton | None:
        return self._buttons.get(workspace_id) or (
            self._buttons_factory(workspace_id) if self._buttons_factory else None
        )

    def on_workspace_button_clicked(self, button: WorkspaceButton):
        cmd = {
            "Action": {
                "FocusWorkspace": {
                    "reference": {"Id": button.id}
                }
            }
        }
        self.connection.send_command(cmd)
        logger.info(f"[Workspaces] Moved to workspace {button.id}")

    def parse_niri_response(self, json_data: dict) -> dict | None:
        if "Err" in json_data:
            logger.warning(f"[Niri] Error: {json_data['Err']}")
            return

        ok_data = json_data.get("Ok")
        if not isinstance(ok_data, dict) or len(ok_data) != 1:
            logger.warning(f"[Niri] Unexpected response: {json_data}")
            return

        return ok_data

    def check_active_workspace_niri(self, json_data: dict) -> dict | None:
        for key in ("Workspaces", "workspaces"):
            for ws in json_data.get(key, []):
                if ws.get("is_active"):
                    return ws
        return None

    def check_urgent_workspace_niri(self, json_data: dict) -> dict:
        return json_data.get("WorkspaceUrgencyChanged", {})

class ActiveWindow(Button):
    def __init__(
        self,
        formatter: FormattedString = FormattedString(
            "{'Desktop' if not win_title else truncate(win_title, 42)}",
            truncate=truncate,
        ),
        **kwargs
    ):
        super().__init__(**kwargs)
        self.connection = get_niri_connection()
        self.formatter = formatter

        bulk_connect(
            self.connection,
            {
                "event::WindowFocusChanged": self.on_focused_window,
                "event::WindowClosed": self.on_closed_window,
            },
        )

        if self.connection.ready:
            self.on_ready(None)
        else:
            self.connection.connect("event::ready", self.on_ready)

    def on_ready(self, _):
        return self.do_initialize(), logger.info(
            "[ActiveWindow] Connected to the Niri socket"
        )

    def on_closed_window(self, _, event: NiriEvent):
        if event.data.get("WindowClosed", None) is None:
            return self.do_initialize()

        return self.do_initialize(), logger.info(
            f"[ActiveWindow] Closed window {event.data['WindowClosed']['id']}"
        )

    def on_focused_window(self, _, event: NiriEvent):
        focused_window = self.parse_niri_response(self.connection.send_command("FocusedWindow").reply)["FocusedWindow"]

        if focused_window is None:
            return self.do_initialize()

        if focused_window.get("app_id", None) is None:
            return self.do_initialize()

        return self.set_label(
            self.formatter.format(win_class=focused_window["app_id"], win_title=focused_window["title"])), logger.info(
            f"[ActiveWindow] Activated window {focused_window['app_id']}, {focused_window['title']}"
        )

    def do_initialize(self):
        win_data: dict = self.parse_niri_response(self.connection.send_command("FocusedWindow").reply)["FocusedWindow"]

        if win_data is None:
            return self.set_label("")

        win_class = win_data.get("app_id", "unknown")
        win_title = win_data.get("title", win_class)

        return self.set_label(
            self.formatter.format(win_class=win_class, win_title=win_title)
        )

    def parse_niri_response(self, json_data: dict) -> dict | None:
        if "Err" in json_data:
            logger.warning(f"[Niri] Error: {json_data['Err']}")
            return

        ok_data = json_data.get("Ok")
        if not isinstance(ok_data, dict) or len(ok_data) != 1:
            logger.warning(f"[Niri] Unexpected response: {json_data}")
            return

        return ok_data

class Language(Button):
    def __init__(
        self,
        formatter: FormattedString = FormattedString("{language}"),
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.connection = get_niri_connection()
        self.formatter = formatter
        self._keyboard_layouts = []

        bulk_connect(
            self.connection,
            {
                "event::KeyboardLayoutsChanged": self.on_layout_changed,
                "event::KeyboardLayoutSwitched": self.on_layout_switched,
            },
        )

        if self.connection.ready:
            self.on_ready(None)
        else:
            self.connection.connect("event::ready", self.on_ready)

    def on_ready(self, _):
        return self.do_initialize(), logger.info(
            "[Language] Connected to the Niri socket"
        )

    def on_layout_changed(self, _, event: NiriEvent):
        data = event.data["keyboard_layouts"]
        names = data["names"]
        current_idx = data["current_idx"]
        current_layout = names[current_idx]

        logger.debug(current_layout)
        return self.set_label(self.formatter.format(language=current_layout))

    def on_layout_switched(self, _, event: NiriEvent):
        current_idx = event.data.get("idx", None)

        if current_idx is None:
            return self.do_initialize()

        return self.set_label(self.formatter.format(language=self._keyboard_layouts[current_idx]))

    def do_initialize(self):
        keyboard_layouts = self.parse_niri_response(self.connection.send_command("KeyboardLayouts").reply)["KeyboardLayouts"]
        names = keyboard_layouts["names"]
        current_idx = keyboard_layouts["current_idx"]

        self._keyboard_layouts = names

        current_layout = names[current_idx]
        return self.set_label(self.formatter.format(language=current_layout))            

    def parse_niri_response(self, json_data: dict) -> dict | None:
        if "Err" in json_data:
            logger.warning(f"[Niri] Error: {json_data['Err']}")
            return

        ok_data = json_data.get("Ok")
        if not isinstance(ok_data, dict) or len(ok_data) != 1:
            logger.warning(f"[Niri] Unexpected response: {json_data}")
            return

        return ok_data


