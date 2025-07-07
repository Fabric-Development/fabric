import gi
import re
import json
from loguru import logger
from typing import Literal
from collections.abc import Iterable, Callable
from fabric.core.service import Signal, Property
from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.eventbox import EventBox
from fabric.hyprland.service import Hyprland, HyprlandEvent
from fabric.utils.helpers import FormattedString, bulk_connect, truncate

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


connection: Hyprland | None = None


def get_hyprland_connection() -> Hyprland:
    global connection
    if not connection:
        connection = Hyprland()

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

    @Signal
    def workspace_activated(self, workspace_id: int):
        if workspace_id == self._active_workspace:
            return

        if self._active_workspace is not None and (
            old_btn := self._buttons.get(self._active_workspace)
        ):
            old_btn.active = False

        self._active_workspace = workspace_id
        if not (btn := self.lookup_or_bake_button(workspace_id)):
            return

        btn.urgent = False
        btn.active = True

        if btn in self._container.children:
            return
        return self.insert_button(btn)

    @Signal
    def workspace_created(self, workspace_id: int):
        if not (btn := self.lookup_or_bake_button(workspace_id)):
            return

        btn.empty = False
        if btn in self._buttons_preset:
            return
        return self.insert_button(btn)

    @Signal
    def workspace_destroyed(self, workspace_id: int):
        if not (btn := self._buttons.get(workspace_id)):
            return  # doesn't exist, skip

        btn.active = False
        btn.urgent = False
        btn.empty = True

        if btn in self._buttons_preset:
            return
        return self.remove_button(btn)

    @Signal
    def urgent(self, workspace_id: int):
        if not (btn := self._buttons.get(workspace_id)):
            return  # doesn't exist, skip

        btn.urgent = True
        return logger.info(f"[Workspaces] workspace {workspace_id} is now urgent")

    # user interaction (e.g. scrolling)
    @Signal
    def action_next(self): ...

    @Signal
    def action_previous(self): ...

    @Signal
    def button_clicked(self, button: WorkspaceButton): ...

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
        self.connection = get_hyprland_connection()
        self._container = Box(**kwargs)
        self.children = self._container

        self._active_workspace: int | None = None
        self._buttons: dict[int, WorkspaceButton] = {}
        self._buttons_preset: list[WorkspaceButton] = [
            button for button in buttons or ()
        ]
        self._buttons_factory = buttons_factory
        self._invert_scroll = invert_scroll
        self._empty_scroll = empty_scroll

        for btn in self._buttons_preset:
            self.insert_button(btn)

        bulk_connect(
            self.connection,
            {
                "event::workspacev2": self.on_workspace,
                "event::focusedmon": self.on_monitor,
                "event::createworkspacev2": self.on_createworkspace,
                "event::destroyworkspacev2": self.on_destroyworkspace,
                "event::urgent": self.on_urgent,
            },
        )

        # all aboard...
        if self.connection.ready:
            self.on_ready(None)
        else:
            self.connection.connect("event::ready", self.on_ready)
        self.connect("scroll-event", self.do_handle_scroll)

    def on_ready(self, _):
        open_workspaces: tuple[int, ...] = tuple(
            workspace["id"]
            for workspace in json.loads(
                self.connection.send_command("j/workspaces").reply.decode()
            )
        )
        active_workspace = json.loads(
            self.connection.send_command("j/activeworkspace").reply.decode()
        )["id"]

        for id in open_workspaces:
            self.workspace_created(id)
            if id == active_workspace:
                self.workspace_activated(id)
        return

    def on_monitor(self, _, event: HyprlandEvent):
        if len(event.data) != 2:
            return
        return self.workspace_activated(int(event.data[1]))

    def on_workspace(self, _, event: HyprlandEvent):
        if len(event.data) != 2:
            return
        return self.workspace_activated(int(event.data[0]))

    def on_createworkspace(self, _, event: HyprlandEvent):
        if len(event.data) != 2:
            return
        return self.workspace_created(int(event.data[0]))

    def on_destroyworkspace(self, _, event: HyprlandEvent):
        if len(event.data) != 2:
            return
        return self.workspace_destroyed(int(event.data[0]))

    def on_urgent(self, _, event: HyprlandEvent):
        if len(event.data) != 1:
            return

        clients = json.loads(self.connection.send_command("j/clients").reply.decode())
        clients_map = {client["address"]: client for client in clients}
        urgent_client: dict = clients_map.get("0x" + event.data[0], {})
        if not (raw_workspace := urgent_client.get("workspace")):
            return logger.warning(
                f"[Workspaces] received urgent signal, but data received ({event.data[0]}) is incorrect, skipping..."
            )
        return self.workspace_destroyed(int(raw_workspace["id"]))

    def do_handle_scroll(self, _, event: Gdk.EventScroll):  # TODO: abstract
        match event.direction:  # type: ignore
            case Gdk.ScrollDirection.UP:
                self.action_next() if not self._invert_scroll else self.action_previous()
                logger.info("[Workspaces] Moving to the next workspace")
            case Gdk.ScrollDirection.DOWN:
                self.action_previous() if not self._invert_scroll else self.action_next()
                logger.info("[Workspaces] Moving to the previous workspace")
            case _:
                return logger.warning(
                    f"[Workspaces] Unknown scroll direction ({event.direction})"  # type: ignore
                )
        return

    def insert_button(self, button: WorkspaceButton) -> None:
        self._buttons[button.id] = button
        self._container.add(button)
        button.connect("clicked", self.do_handle_button_press)
        return self.reorder_buttons()

    def reorder_buttons(self):
        for _, child in sorted(self._buttons.items(), key=lambda i: i[0]):
            self._container.reorder_child(child, (child.id - 1))
        return

    def remove_button(self, button: WorkspaceButton) -> None:
        if self._buttons.pop(button.id, None) is not None:
            self._container.remove(button)
        return button.destroy()

    def lookup_or_bake_button(self, workspace_id: int) -> WorkspaceButton | None:
        if not (btn := self._buttons.get(workspace_id)) and self._buttons_factory:
            btn = self._buttons_factory(workspace_id)
        return btn

    def do_handle_button_press(self, button: WorkspaceButton):  # TODO: abstract
        self.button_clicked(button)
        return logger.info(f"[Workspaces] Moved to workspace {button.id}")

    # TODO: be a part of the hyprland widget implementation
    def do_action_next(self):
        return self.connection.send_command("batch/dispatch workspace e+1")

    def do_action_previous(self):
        return self.connection.send_command("batch/dispatch workspace e-1")

    def do_button_clicked(self, button: WorkspaceButton):
        return self.connection.send_command(f"batch/dispatch workspace {button.id}")


class ActiveWindow(Button):
    @Signal
    def window_activated(self, window_class: str, window_title: str):
        return self.set_label(
            self.formatter.format(win_class=window_class, win_title=window_title)
        )

    def __init__(
        self,
        formatter: FormattedString = FormattedString(
            "{'Desktop' if not win_title else truncate(win_title, 42)}",
            truncate=truncate,
        ),
        # TODO: hint super's kwargs
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.formatter = formatter

        # window manager specific
        self.connection = get_hyprland_connection()
        bulk_connect(
            self.connection,
            {
                "event::activewindow": self.on_activewindow,
                "event::closewindow": self.on_closewindow,
            },
        )

        # all aboard...
        if self.connection.ready:
            self.on_ready(None)
        else:
            self.connection.connect("event::ready", self.on_ready)

    def on_ready(self, _):
        return self.do_initialize(), logger.info(
            "[ActiveWindow] Connected to the hyprland socket"
        )

    def on_closewindow(self, _, event: HyprlandEvent):
        if len(event.data) < 1:
            return
        return self.do_initialize(), logger.info(
            f"[ActiveWindow] Closed window 0x{event.data[0]}"
        )

    def on_activewindow(self, _, event: HyprlandEvent):
        if len(event.data) < 2:
            return
        return self.window_activated(event.data[0], event.data[1]), logger.info(
            f"[ActiveWindow] Activated window {event.data[0]}, {event.data[1]}"
        )

    def do_initialize(self):
        win_data: dict = json.loads(
            self.connection.send_command("j/activewindow").reply.decode()
        )
        win_class = win_data.get("class", "unknown")
        win_title = win_data.get("title", win_class)

        return self.window_activated(win_class, win_title)


class Language(Button):
    @Signal
    def layout_changed(self, language: str, keyboard: str) -> bool:
        matched: bool = False

        if re.match(self.keyboard, keyboard) and (matched := True):
            self.set_label(self.formatter.format(language=language))

        logger.debug(
            f"[Language] Keyboard: {keyboard}, Language: {language}, Match: {matched}"
        )
        return matched

    def __init__(
        self,
        keyboard: str = ".*",
        formatter: FormattedString = FormattedString("{language}"),
        # TODO: hint super's kwargs
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.keyboard = keyboard
        self.formatter = formatter

        # window manager specific
        self.connection = get_hyprland_connection()
        self.connection.connect("event::activelayout", self.on_activelayout)

        # all aboard...
        if self.connection.ready:
            self.on_ready(None)
        else:
            self.connection.connect("event::ready", self.on_ready)

    def on_ready(self, _):
        return self.do_initialize(), logger.info(
            "[Language] Connected to the hyprland socket"
        )

    def on_activelayout(self, _, event: HyprlandEvent):
        if len(event.data) < 2:
            return logger.warning(
                f"[Language] got invalid event data from hyprland, raw data is\n{event.raw_data}"
            )
        keyboard, language = event.data
        matched: bool = False

        if re.match(self.keyboard, keyboard) and (matched := True):
            self.set_label(self.formatter.format(language=language))

        return logger.debug(
            f"[Language] Keyboard: {keyboard}, Language: {language}, Match: {matched}"
        )

    def do_initialize(self):
        devices: dict[str, list[dict[str, str]]] = json.loads(
            self.connection.send_command("j/devices").reply.decode()
        )
        if not devices or not (keyboards := devices.get("keyboards")):
            return logger.warning(
                f"[Language] coulnd't get devices from hyprctl, gotten data\n{devices}"
            )

        language: str | None = None
        for kb in keyboards:
            if (
                not (kb_name := kb.get("name"))
                or not (language := kb.get("active_keymap"))
                or not self.layout_changed(language, kb_name)
            ):
                continue

            logger.debug(
                f"[Language] found language: {language} for keyboard {kb_name}"
            )
            break

        return (
            logger.info(
                f"[Language] Could not find language for keyboard: {self.keyboard}, gotten keyboards: {keyboards}"
            )
            if not language
            else logger.info(
                f"[Language] Set language: {language} for keyboard: {self.keyboard}"
            )
        )
