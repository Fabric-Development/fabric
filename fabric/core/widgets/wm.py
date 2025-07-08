import gi
import re
from loguru import logger
from typing import Literal
from collections.abc import Iterable, Callable
from fabric.core.service import Signal, Property
from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.eventbox import EventBox
from fabric.utils.helpers import FormattedString, truncate

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


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
        **kwargs,
    ):
        super().__init__(events="scroll")

        self._container = Box(**kwargs)

        self.children = self._container

        self._active_workspace: int | None = None
        self._buttons: dict[int, WorkspaceButton] = {}
        self._buttons_preset: list[WorkspaceButton] = [
            button for button in buttons or ()
        ]
        self._buttons_factory = buttons_factory
        self._invert_scroll = invert_scroll

        for btn in self._buttons_preset:
            self.insert_button(btn)

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
