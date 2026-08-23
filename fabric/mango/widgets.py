from loguru import logger
from collections.abc import Iterable, Callable

from fabric.mango.service import Mango, MangoEvent
from fabric.core.widgets import WorkspaceButton, Workspaces, ActiveWindow, Language
from fabric.utils.helpers import FormattedString, bulk_connect, truncate


connection: Mango | None = None


def get_mango_connection() -> Mango:
    global connection
    if not connection:
        connection = Mango()
    return connection


class MangoWorkspaces(Workspaces):
    def __init__(
        self,
        monitor: str | None = None,
        tag_count: int = 9,
        tag_start: int = 1,
        buttons: Iterable[WorkspaceButton] | None = None,
        buttons_factory: Callable[[int], WorkspaceButton | None]
        | None = Workspaces.default_buttons_factory,
        invert_scroll: bool = False,
        **kwargs,
    ):
        self._tag_buttons: dict[int, WorkspaceButton] = {}
        _factory = buttons_factory or Workspaces.default_buttons_factory

        def capturing_factory(ws_id: int) -> WorkspaceButton | None:
            btn = _factory(ws_id)
            if btn:
                self._tag_buttons[ws_id] = btn
            return btn

        super().__init__(buttons, capturing_factory, invert_scroll, **kwargs)
        self.connection = get_mango_connection()
        self._monitor = monitor
        self._tag_count = tag_count
        self._tag_start = tag_start
        self._active_tag: int = tag_start

        for i in range(tag_start, tag_start + tag_count):
            self.workspace_created(i)
        self.workspace_activated(self._active_tag)

        bulk_connect(
            self.connection,
            {
                "event::all-tags": self.on_tags_changed,
                "event::all-clients": self.on_clients_changed,
            },
        )

        if self.connection.ready:
            self.on_ready()
        else:
            self.connection.connect("notify::ready", self.on_ready)
        self.connect("scroll-event", self.do_handle_scroll)

    def _resolve_monitor(self) -> str:
        if self._monitor:
            return self._monitor
        cursor = self.connection.send_command("get cursorpos").parsed_reply
        if isinstance(cursor, dict) and (mon := cursor.get("monitor")):
            return mon
        monitors = self.connection.send_command("get all-monitors").parsed_reply
        if isinstance(monitors, list) and monitors:
            return monitors[0].get("name", monitors[0].get("output", "eDP-1"))
        return "eDP-1"

    def _extract_tag_list(self, data) -> list[dict]:
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            if "all_tags" in data:
                for entry in data["all_tags"]:
                    if isinstance(entry, dict):
                        mon = entry.get("monitor", "")
                        if not self._monitor or mon == self._monitor:
                            tags = entry.get("tags", [])
                            if isinstance(tags, list):
                                return tags
                if data["all_tags"]:
                    return data["all_tags"][0].get("tags", [])
            if "tags" in data and isinstance(data["tags"], list):
                return data["tags"]
        return []

    def _find_active_tag(self, data) -> int | None:
        tags = self._extract_tag_list(data)
        for tag in tags:
            if isinstance(tag, dict) and tag.get("is_active"):
                return tag.get("index")
        return None

    def _update_occupied(self, tags: list[dict]):
        for tag in tags:
            if not isinstance(tag, dict):
                continue
            idx = tag.get("index", 0)
            btn = self._tag_buttons.get(idx)
            if not btn:
                continue
            ctx = btn.get_style_context()
            if tag.get("client_count", 0) > 0:
                ctx.remove_class("empty")
            else:
                ctx.add_class("empty")

    def on_ready(self):
        self._monitor = self._resolve_monitor()
        raw = self.connection.send_command(f"get tags {self._monitor}")
        tags = self._extract_tag_list(raw.parsed_reply)
        active = self._find_active_tag(raw.parsed_reply)

        if active is not None:
            self._active_tag = active
            self.workspace_activated(active)

        self._update_occupied(tags)
        return

    def on_tags_changed(self, _, event: MangoEvent):
        active = self._find_active_tag(event.data)
        if active is not None:
            self._active_tag = active
            self.workspace_activated(active)

        tags = self._extract_tag_list(event.data)
        self._update_occupied(tags)

    def on_clients_changed(self, _, event: MangoEvent):
        if not isinstance(event.data, list):
            return

        for client in event.data:
            if not isinstance(client, dict) or not client.get("is_urgent", False):
                continue
            tags = client.get("tags", [])
            if isinstance(tags, list) and tags:
                return self.urgent(tags[0])
        return

    def do_action_next(self):
        next_tag = self._active_tag + 1
        if next_tag >= self._tag_start + self._tag_count:
            next_tag = self._tag_start
        return self.connection.send_command(f"dispatch view,{next_tag}")

    def do_action_previous(self):
        prev_tag = self._active_tag - 1
        if prev_tag < self._tag_start:
            prev_tag = self._tag_start + self._tag_count - 1
        return self.connection.send_command(f"dispatch view,{prev_tag}")

    def do_button_clicked(self, button: WorkspaceButton):
        return self.connection.send_command(f"dispatch view,{button.id}")


class MangoActiveWindow(ActiveWindow):
    def __init__(
        self,
        formatter: FormattedString = FormattedString(
            "{'Desktop' if not win_title else truncate(win_title, 42)}",
            truncate=truncate,
        ),
        **kwargs,
    ):
        super().__init__(formatter, **kwargs)

        self.connection = get_mango_connection()
        bulk_connect(
            self.connection,
            {
                "event::focusing-client": self.on_focusing_client,
            },
        )

        if self.connection.ready:
            self.on_ready()
        else:
            self.connection.connect("event::ready", self.on_ready)

    def on_ready(self):
        return self.do_initialize(), logger.info(
            "[ActiveWindow] Connected to the mango socket"
        )

    def on_focusing_client(self, _, event: MangoEvent):
        if not isinstance(event.data, dict) or not event.data:
            return self.window_activated("", "Desktop"), logger.info(
                "[ActiveWindow] Activated window Desktop"
            )

        win_class = event.data.get("class", "unknown")
        win_title = event.data.get("title", win_class)

        return self.window_activated(win_class, win_title), logger.info(
            f"[ActiveWindow] Activated window {win_class}, {win_title}"
        )

    def do_initialize(self):
        client = self.connection.send_command("get focusing-client").parsed_reply
        if not isinstance(client, dict) or not client:
            return self.window_activated("", "Desktop")

        win_class = client.get("class", "unknown")
        win_title = client.get("title", win_class)

        return self.window_activated(win_class, win_title)


class MangoLanguage(Language):
    def __init__(
        self,
        keyboard: str = ".*",
        formatter: FormattedString = FormattedString("{language}"),
        **kwargs,
    ):
        super().__init__(keyboard, formatter, **kwargs)

        self.connection = get_mango_connection()
        self.connection.connect("event::keyboardlayout", self.on_keyboard_layout)

        if self.connection.ready:
            self.on_ready()
        else:
            self.connection.connect("event::ready", self.on_ready)

    def on_ready(self):
        return self.do_initialize(), logger.info(
            "[Language] Connected to the mango socket"
        )

    def on_keyboard_layout(self, _, event: MangoEvent):
        keyboard, language = self._parse_layout(event.data)
        if not language:
            return logger.warning(
                f"[Language] got invalid event data from mango, raw data is\n{event.data}"
            )

        return self.layout_changed(language, keyboard)

    def do_initialize(self):
        raw = self.connection.send_command("get keyboardlayout").parsed_reply
        keyboard, language = self._parse_layout(raw)
        if not language:
            return logger.warning(
                f"[Language] coulnd't get devices from mango, gotten data\n{raw}"
            )

        self.layout_changed(language, keyboard)
        return logger.info(
            f"[Language] Set language: {language} for keyboard: {keyboard or self.keyboard}"
        )

    @staticmethod
    def _parse_layout(data: object) -> tuple[str, str]:
        if isinstance(data, dict):
            return (
                data.get("keyboard", ""),
                data.get("language", data.get("layout", "")),
            )
        if isinstance(data, str):
            return ("", data)
        return ("", "")


__all__ = [
    "MangoWorkspaces",
    "MangoActiveWindow",
    "MangoLanguage",
    "WorkspaceButton",
    "get_mango_connection",
    "Language",
    "Workspaces",
    "ActiveWindow",
]
