from loguru import logger
from typing import Callable
from fabric.service import *
from fabric.utils import ValueEnum, invoke_repeater, exec_shell_command_async
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
        Signal("polling-done", "run-first", None, (object,)),
    )

    def __init__(
        self,
        poll_from: Callable | str | None = None,
        interval: int | None = None,
        stream: bool = False,
        value: object | None = None,
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
        self.poll(self._polling_mode, self._poll_from, self._interval, *self._data)

    def poll(
        self,
        mode: FabricatorPollingMode,
        poll_from: Callable | str,
        interval: int | None = None,
        *args,
    ):
        self._poll = True
        match mode:
            case FabricatorPollingMode.NONE:
                self.emit("polling-done", poll_from)
                logger.warning(
                    "[Fabricator] polling mode is unknown, probably because of the passed arguments begin wrong, skipping..."
                )
            case FabricatorPollingMode.FUNCTION:
                invoke_repeater(
                    interval, lambda *_: self.do_invoke_function(poll_from, *args)
                )
                self.do_invoke_function(
                    poll_from, *args
                ) if self._initial_poll is True else None
            case FabricatorPollingMode.FUNCTION_STREAM:
                self._stream_thread = GLib.Thread.new(
                    f"fabricator-thread-{self.__str__()}",
                    self.do_read_function_stream,
                    callable,
                    *args,
                )
            case FabricatorPollingMode.SHELL_COMMAND:
                invoke_repeater(
                    interval, lambda *_: self.do_read_shell_command_io(poll_from)
                )
            case FabricatorPollingMode.SHELL_COMMAND_STERAM:
                self.do_read_shell_command_io(poll_from)
        return

    def do_read_shell_command_io(self, cmd: str):
        data = None

        def result_handler(output: str):
            nonlocal data
            if not self._poll:
                self.emit("polling-done", None)
                return process.force_exit()  # sorry
            data = output
            self.value = data

        process, _ = exec_shell_command_async(cmd, result_handler)
        process.wait_async(
            None, lambda *args: self.emit("polling-done", data)
        ) if self._stream is True else None
        return True

    def do_invoke_function(self, callable: Callable, *args):
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
            if not self._poll:
                break
            GLib.idle_add(self.do_set_value_for_stream_thread, data)
        GLib.idle_add(self.emit, "polling-done", data)
        return False

    def do_set_value_for_stream_thread(self, value) -> None:
        self.value = value
        return

    def stop_polling(self) -> None:
        if self._poll is True:
            self._poll = False
            if self._polling_mode is FabricatorPollingMode.FUNCTION_STREAM:
                self._stream_thread.exit() if self._stream_thread is not None else logger.warning(
                    "[Fabricator] can't stop function stream thread, skipping..."
                )
            return
        return logger.warning(
            f"[Fabricator] Fabricator ({self}) is already not polling"
        )

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
