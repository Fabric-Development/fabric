from loguru import logger
from typing import Callable
from fabric.service import *
from fabric.utils.enum import ValueEnum
from fabric.utils.helpers import invoke_repeater, exec_shell_command


class PollingMode(ValueEnum):
    NONE = 0
    FUNCTION = 1
    SHELL_COMMAND = 2


class Fabricate(Service):
    __gsignals__ = SignalContainer(
        Signal("changed", "run-first", None, (object,)),
        Signal("polling", "run-first", None, (object, object, int, object)),
        Signal("polling-function", "run-first", None, (object,)),
        Signal("polling-shell-command", "run-first", None, (object,)),
        Signal("polling-done", "run-first", None, (object,)),
    )

    def __init__(
        self,
        value: object | None = None,
        poll_from: Callable | str | None = False,
        interval: int | None = None,
        stop_when: object | None = None,
        initial_poll: bool = True,
        *data,
        **kwargs,
    ):
        super().__init__(
            **kwargs,
        )
        self._value = value
        self._poll_from = poll_from
        self._interval = interval
        self._stop_when = stop_when
        self._initial_poll = initial_poll
        self._data = data
        self._poll = True
        self._polling_mode = {
            "none": PollingMode.NONE,
            "function": PollingMode.FUNCTION,
            "shell-command": PollingMode.SHELL_COMMAND,
        }.get(
            "shell-command"
            if isinstance(poll_from, str)
            else "function"
            if callable(poll_from)
            else "none",
            PollingMode.NONE,
        )
        self.poll(
            self._polling_mode, self._poll_from, self._interval, self, *self._data
        )

    def poll(
        self, mode: PollingMode, callable: Callable, interval: int | None = None, *args
    ):
        if mode == PollingMode.NONE:
            self.emit("polling-done", callable)
            return logger.info("[Fabricator] Polling mode is set to None, skipping...")
        elif mode == PollingMode.FUNCTION:
            self.emit("polling-function", callable)
            return (
                self.invoke_function_with_interval(callable, interval, *args),
                self.do_invoke_function(callable, *args)
                if self._initial_poll is True
                else None,
            )
        elif mode == PollingMode.SHELL_COMMAND:
            self.emit("polling-shell-command", callable)
            return (
                self.invoke_shell_with_interval(callable, interval),
                self.do_invoke_shell(callable) if self._initial_poll is True else None,
            )

    def invoke_shell_with_interval(self, cmd: str, interval: int):
        return invoke_repeater(
            interval,
            self.do_invoke_shell,
            cmd,
        )

    def do_invoke_shell(self, cmd: str):
        self.emit("polling", self._polling_mode, cmd, self._interval, ())
        if self._poll is True:
            value = exec_shell_command(cmd)
            if value == self._stop_when:
                self.emit("polling-done", value)
                return False
            self.value = value
            return True
        else:
            return False

    def invoke_function_with_interval(self, callable: Callable, interval: int, *args):
        return invoke_repeater(interval, self.do_invoke_function, callable, *args)

    def do_invoke_function(self, callable: Callable, *args):
        self.emit("polling", self._polling_mode, callable, self._interval, args)
        if self._poll is True:
            value = callable(*args)
            if value == self._stop_when:
                self.emit("polling-done", value)
                return False
            self.value = value
            return True
        else:
            return False

    @Property(value_type=object)
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.emit("changed", value)
        return

    def stop_polling(self):
        self._poll = False
        return
