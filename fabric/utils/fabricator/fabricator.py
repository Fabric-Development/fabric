import shlex
import subprocess
from loguru import logger
from typing import Callable
from fabric.service import *
from fabric.utils import ValueEnum
from fabric.utils import invoke_repeater, exec_shell_command
from gi.repository import GLib


class FabricatorPollingMode(ValueEnum):
    NONE = 0
    FUNCTION = 1
    SHELL_COMMAND = 2
    FUNCTION_STREAM = 3
    SHELL_COMMAND_STERAM = 4


class Fabricator(Service):
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
        stream: bool = False,
        interval: int | None = None,
        initial_poll: bool = True,
        *data,
        **kwargs,
    ):
        super().__init__(
            **kwargs,
        )
        self._value = value
        self._value_str = str(value)
        self._poll_from = poll_from
        self._interval = interval
        self._initial_poll = initial_poll
        self._data = data
        self._poll = True
        self._stream = stream
        self._stream_thread: GLib.Thread = None
        self._polling_mode = (
            FabricatorPollingMode.FUNCTION
            if callable(poll_from) and stream is False
            else FabricatorPollingMode.FUNCTION_STREAM
            if callable(poll_from) and stream is True
            else FabricatorPollingMode.SHELL_COMMAND
            if isinstance(poll_from, str) and stream is False
            else FabricatorPollingMode.SHELL_COMMAND_STERAM
            if isinstance(poll_from, str) and stream is True
            else FabricatorPollingMode.NONE
        )
        self.poll(
            self._polling_mode, self._poll_from, self._interval, self, *self._data
        )

    def poll(
        self,
        mode: FabricatorPollingMode,
        callable: Callable,
        interval: int | None = None,
        *args,
    ):
        if mode == FabricatorPollingMode.NONE:
            self.emit("polling-done", callable)
            return logger.warning(
                "[Fabricator] Polling mode is unknown, probably because of the passed arguments begin wrong, skipping..."
            )
        if (
            self._stream is not True
        ):  # TODO: i don't like nested "if" statments, one day i'll get rid of this...
            if mode == FabricatorPollingMode.FUNCTION:
                self.emit("polling-function", callable)
                return (
                    self.invoke_function_with_interval(callable, interval, *args),
                    self.do_invoke_function(callable, *args)
                    if self._initial_poll is True
                    else None,
                )
            elif mode == FabricatorPollingMode.SHELL_COMMAND:
                self.emit("polling-shell-command", callable)
                return (
                    self.invoke_shell_with_interval(callable, interval),
                    self.do_invoke_shell(callable)
                    if self._initial_poll is True
                    else None,
                )
        elif self._stream is True:
            if mode == FabricatorPollingMode.FUNCTION_STREAM:
                self._stream_thread = GLib.Thread.new(
                    f"fabricator-thread-{self.__str__()}",
                    self.do_read_function_stream,
                    callable,
                    *args,
                )
                self.emit("polling-function", callable)
            elif mode == FabricatorPollingMode.SHELL_COMMAND_STERAM:
                self._stream_thread = GLib.Thread.new(
                    f"fabricator-thread-{self.__str__()}",
                    self.do_read_shell_stream,
                    callable,
                )
                self.emit("polling-shell-command", callable)
        self._poll = True
        return

    def invoke_shell_with_interval(self, cmd: str, interval: int):
        return invoke_repeater(
            interval,
            lambda *_: self.do_invoke_shell(cmd),
        )

    def do_invoke_shell(self, cmd: str):
        self.emit("polling", self._polling_mode, cmd, self._interval, ())
        if self._poll is not True:
            self.emit("polling-done", None)
            return False
        value = exec_shell_command(cmd)
        self.value = value
        return True

    def do_read_shell_stream(self, cmd: str):
        # TODO: implement this using Gio/GLib
        data = None
        with subprocess.Popen(
            shlex.split(cmd, True, True),
            stdout=subprocess.PIPE,
            # shell=True,
            text=True,
        ) as stream:
            for data in stream.stdout:
                data = data.strip()
                if self._poll is False or self._poll is None:
                    break
                GLib.idle_add(self.set_value_for_stream_thread, data)
        GLib.idle_add(self.emit, "polling-done", data)
        return False

    def invoke_function_with_interval(self, callable: Callable, interval: int, *args):
        return invoke_repeater(
            interval, lambda *_: self.do_invoke_function(callable, *args)
        )

    def do_invoke_function(self, callable: Callable, *args):
        self.emit("polling", self._polling_mode, callable, self._interval, args)
        if self._poll is not True:
            self.emit("polling-done", None)
            return False
        value = callable(*args)
        self.value = value
        return True

    def do_read_function_stream(self, callable: Callable, *args):
        # this should get called in a new thread, else the main thread will not execute
        data = None
        for data in callable(*args):
            if self._poll is False or self._poll is None:
                break
            GLib.idle_add(self.set_value_for_stream_thread, data)
        GLib.idle_add(self.emit, "polling-done", data)
        return False

    def stop_polling(self):
        if self._poll is True:
            self._poll = False
            if self._polling_mode in (
                FabricatorPollingMode.FUNCTION_STREAM,
                FabricatorPollingMode.SHELL_COMMAND_STERAM,
            ):
                self._stream_thread.exit() if self._stream_thread is not None else logger.warning(
                    "[Fabricator] Tried to remove/stop a stream reader thread but the `_stream_thread` was unset, this probably means that something went wrong, skipping..."
                )
            return
        return logger.warning(
            f"[Fabricator] This fabricator ({self}) is already not polling."
        )

    def set_value_for_stream_thread(self, value) -> None:
        self.value = value
        return

    @Property(value_type=object, flags="read-write")
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.value_str = str(value)
        self.emit("changed", value)
        return

    @Property(value_type=str, flags="read-write")
    def value_str(self):
        return self._value_str

    @value_str.setter
    def value_str(self, value: str):
        self._value_str = str(value)
        return
