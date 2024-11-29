from loguru import logger
from collections.abc import Callable
from typing import (
    cast,
    overload,
    Concatenate,
    ParamSpec,
    Generic,
    TypeVar,
    Self,
    Any,
)
from fabric.core.service import Service, Signal, Property
from fabric.utils.helpers import invoke_repeater, exec_shell_command_async, idle_add
from gi.repository import GLib, Gio

T = TypeVar("T")
P = ParamSpec("P")
MISSING = TypeVar("MISSING")


# TODO: improve typing...
class Fabricator(Service, Generic[T]):
    @Signal
    def changed(self, value: object) -> None: ...

    @Signal
    def polling_done(self, last_value: object) -> None: ...

    @Property(type[T], flags="read-write")
    def value(self) -> type[T]:
        return self._value  # type: ignore

    @value.setter
    def value(self, value):
        self._value = value
        return self.changed(value)

    @overload
    def __init__(
        self,
        poll_from: Callable[Concatenate[Self, P], T],
        interval: int = 1000,
        stream: bool = False,
        default_value: T | Any = None,
        initial_poll: bool = True,
        *data,
        **kwargs,
    ): ...

    @overload
    def __init__(
        self,
        poll_from: Callable[Concatenate[Self, P], T],
        interval: int = 1000,
        stream: bool = True,
        default_value: T | Any = None,
        initial_poll: bool = True,
        *data,
        **kwargs,
    ): ...

    @overload
    def __init__(
        self,
        poll_from: str,
        interval: int = 1000,
        stream: bool = False,
        default_value: str | Any = None,
        initial_poll: bool = True,
        *args,
        **kwargs,
    ): ...

    @overload
    def __init__(
        self,
        poll_from: str,
        interval: int = 1000,
        stream: bool = True,
        default_value: str | Any = None,
        initial_poll: bool = True,
        *args,
        **kwargs,
    ): ...

    def __init__(
        self,
        poll_from: Callable[Concatenate[Self, P], T] | str,
        interval: int = 1000,
        stream: bool = False,
        default_value: T | str | Any = None,
        initial_poll: bool = True,
        *data,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self._value = default_value
        self._poll_from = poll_from
        self._interval = interval
        self._initial_poll = initial_poll
        self._data = data
        self._poll = True
        self._stream = stream
        self._stream_thread: GLib.Thread | None = None

        self.start() if initial_poll is True else None

    def start(self):
        self._poll = True
        is_callable = callable(self._poll_from)
        if is_callable and not self._stream:
            invoke_repeater(self._interval, self.do_invoke_function)

        elif is_callable and self._stream:
            self._stream_thread = GLib.Thread.new(
                f"fabricator-thread-{self.__str__()}",
                self.do_read_function_stream,
                *self._data,
            )

        elif not is_callable and not self._stream:
            invoke_repeater(self._interval, self.do_read_shell_command_io)

        elif not is_callable and self._stream:
            self.do_read_shell_command_io()

        else:
            self.emit("polling-done", None)
            logger.warning(
                "[Fabricator] polling mode is unknown, probably because of the passed arguments begin wrong, skipping..."
            )

    def stop(self) -> None:
        if self._poll is True:
            self._poll = False
            if self._stream_thread:
                self._stream_thread.exit()
            return
        return logger.warning(
            f"[Fabricator] Fabricator ({self}) is already not polling"
        )

    def do_read_shell_command_io(self):
        data = None

        def result_handler(output: str):
            nonlocal data
            if not self._poll:
                self.emit("polling-done", None)
                return cast(Gio.Subprocess, process).force_exit()  # sorry
            data = output
            self.value = data

        process, _ = exec_shell_command_async(
            cast(str, self._poll_from), result_handler
        )
        process.wait_async(
            None, lambda *_: self.emit("polling-done", data)
        ) if process and self._stream else None
        return True

    def do_invoke_function(self):
        if self._poll is not True:
            self.emit("polling-done", None)
            return False
        value = cast(Callable, self._poll_from)(self, *self._data)
        self.value = value
        return True

    def do_read_function_stream(self, *func_data):
        # this should get called in a new thread, else the main thread will be blocked
        data = None
        for data in cast(Callable, self._poll_from)(self, *func_data):
            if not self._poll:
                break
            idle_add(self.set_value, data)
        idle_add(self.emit, "polling-done", data)
        return False
