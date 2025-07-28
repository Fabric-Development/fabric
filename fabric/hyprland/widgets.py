import json
from loguru import logger
from typing import TypeVar
from collections.abc import Iterable, Callable

from fabric.hyprland.service import Hyprland, HyprlandEvent
from fabric.core.widgets import WorkspaceButton, Workspaces, ActiveWindow, Language
from fabric.utils.helpers import FormattedString, bulk_connect, truncate


connection: Hyprland | None = None


def get_hyprland_connection() -> Hyprland:
    global connection
    if not connection:
        connection = Hyprland()

    return connection


class HyprlandWorkspaces(Workspaces):
    def __init__(
        self,
        buttons: Iterable[WorkspaceButton] | None = None,
        buttons_factory: Callable[[int], WorkspaceButton | None]
        | None = Workspaces.default_buttons_factory,
        invert_scroll: bool = False,
        empty_scroll: bool = False,
        **kwargs,
    ):
        super().__init__(buttons, buttons_factory, invert_scroll, **kwargs)
        self.connection = get_hyprland_connection()

        self._empty_scroll = empty_scroll
        bulk_connect(
            self.connection,
            {
                "event::workspacev2": self.on_workspace,
                "event::focusedmonv2": self.on_monitor,
                "event::createworkspacev2": self.on_create_workspace,
                "event::destroyworkspacev2": self.on_destroy_workspace,
                "event::urgent": self.on_urgent,
            },
        )

        # all aboard...
        if self.connection.ready:
            self.on_ready()
        else:
            self.connection.connect("event::ready", self.on_ready)
        self.connect("scroll-event", self.do_handle_scroll)

    def on_ready(self):
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

    def on_create_workspace(self, _, event: HyprlandEvent):
        if len(event.data) != 2:
            return
        return self.workspace_created(int(event.data[0]))

    def on_destroy_workspace(self, _, event: HyprlandEvent):
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
        return self.urgent(int(raw_workspace["id"]))

    def do_action_next(self):
        return self.connection.send_command(
            f"batch/dispatch workspace {'e' if not self._empty_scroll else ''}+1"
        )

    def do_action_previous(self):
        return self.connection.send_command(
            f"batch/dispatch workspace {'e' if not self._empty_scroll else ''}-1"
        )

    def do_button_clicked(self, button: WorkspaceButton):
        return self.connection.send_command(f"batch/dispatch workspace {button.id}")


class HyprlandActiveWindow(ActiveWindow):
    def __init__(
        self,
        formatter: FormattedString = FormattedString(
            "{'Desktop' if not win_title else truncate(win_title, 42)}",
            truncate=truncate,
        ),
        # TODO: hint super's kwargs
        **kwargs,
    ):
        super().__init__(formatter, **kwargs)

        self.connection = get_hyprland_connection()
        bulk_connect(
            self.connection,
            {
                "event::activewindow": self.on_active_window,
                "event::closewindow": self.on_close_window,
            },
        )

        # all aboard...
        if self.connection.ready:
            self.on_ready()
        else:
            self.connection.connect("event::ready", self.on_ready)

    def on_ready(self):
        return self.do_initialize(), logger.info(
            "[ActiveWindow] Connected to the hyprland socket"
        )

    def on_close_window(self, _, event: HyprlandEvent):
        if len(event.data) < 1:
            return
        return self.do_initialize(), logger.info(
            f"[ActiveWindow] Closed window 0x{event.data[0]}"
        )

    def on_active_window(self, _, event: HyprlandEvent):
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


class HyprlandLanguage(Language):
    def __init__(
        self,
        keyboard: str = ".*",
        formatter: FormattedString = FormattedString("{language}"),
        # TODO: hint super's kwargs
        **kwargs,
    ):
        super().__init__(keyboard, formatter, **kwargs)

        self.connection = get_hyprland_connection()
        self.connection.connect("event::activelayout", self.on_active_layout)

        # all aboard...
        if self.connection.ready:
            self.on_ready()
        else:
            self.connection.connect("event::ready", self.on_ready)

    def on_ready(self):
        return self.do_initialize(), logger.info(
            "[Language] Connected to the hyprland socket"
        )

    def on_active_layout(self, _, event: HyprlandEvent):
        if len(event.data) < 2:
            return logger.warning(
                f"[Language] got invalid event data from hyprland, raw data is\n{event.raw_data}"
            )
        keyboard, language, *_ = event.data

        return self.layout_changed(language, keyboard)

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


# TODO: remove in v0.0.3
T = TypeVar("T")


def __bake_deprecation_message(obj: T, old_name: str) -> T:
    def wrapper():
        logger.warning(
            f"[{old_name}][DEPRECATION] `{old_name}` has been renamed to `{obj.__name__}`. "
            "Window manager-specific widget classes are now prefixed with their corresponding window manager name. "
            "Please update your imports accordingly."
        )
        return obj

    return wrapper  # type: ignore


Language = __bake_deprecation_message(HyprlandLanguage, "Language")
Workspaces = __bake_deprecation_message(HyprlandWorkspaces, "Workspaces")
ActiveWindow = __bake_deprecation_message(HyprlandActiveWindow, "ActiveWindow")


__all__ = [
    "HyprlandWorkspaces",
    "HyprlandActiveWindow",
    "HyprlandLanguage",
    "WorkspaceButton",
    "get_hyprland_connection",
    "Language",
    "Workspaces",
    "ActiveWindow",
]
