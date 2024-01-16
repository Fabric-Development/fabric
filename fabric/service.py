from dataclasses import dataclass
from typing import Literal, Type, Callable
from gi.repository import GObject


@dataclass
class Signal:
    name: str
    flags: Literal[
        "run-last",
        "run-first",
        "run-cleanup",
        "no-recurse",
        "detailed",
        "action",
        "no-hooks",
        "must-collect",
        "deprecated",
        "accumulator-first-run",
    ] | GObject.SignalFlags = "run-first"
    rtype: Type | object = None
    args: tuple[Type | object] = ()


@dataclass(frozen=True)
class SignalCallback:
    name: str
    callback: Callable


class Service(GObject.Object):
    def __init__(self, signals: list[Signal] | Signal):
        self.__gsignals__: dict
        if not isinstance(signals, list) and isinstance(signals, Signal):
            signals = [signals]
        for signal in signals:
            self.__gsignals__[signal.name] = (
                signal.flags
                if isinstance(signal.flags, GObject.SignalFlags) == True
                else {
                    "run-last": GObject.SignalFlags.RUN_LAST,
                    "run-first": GObject.SignalFlags.RUN_FIRST,
                    "run-cleanup": GObject.SignalFlags.RUN_CLEANUP,
                    "no-recurse": GObject.SignalFlags.NO_RECURSE,
                    "detailed": GObject.SignalFlags.DETAILED,
                    "action": GObject.SignalFlags.ACTION,
                    "no-hooks": GObject.SignalFlags.NO_HOOKS,
                    "must-collect": GObject.SignalFlags.MUST_COLLECT,
                    "deprecated": GObject.SignalFlags.DEPRECATED,
                    "accumulator-first-run": GObject.SignalFlags.ACCUMULATOR_FIRST_RUN,
                }.get(
                    signal.flags, GObject.SignalFlags.RUN_FIRST
                ),  # no inline switch? (FIXME: use getattr)
                signal.rtype,
                signal.args,
            )
        for signal in self.__gsignals__.keys():
            GObject.signal_new(
                signal,
                self.__class__,
                self.__gsignals__[signal][0],
                self.__gsignals__[signal][1],
                self.__gsignals__[signal][2],
            )
        super().__init__()
        self.registered_signals: list[SignalCallback] = []

    def disconnect(self, reference: SignalCallback | Callable | str) -> list[int]:
        """disconnects a signal
        by passing the `SignalCallback` to `reference` the callback function will gets disconnected.

        passing a function or a callable makes the method search the props looking for a
        matching object and disconnect it

        if passed a string it will disconnect every callback uses the same signal string

        :param reference: a `SignalCallback`, the callback function or a string contains the signal name
        :type reference: SignalCallback | Callable | str
        :raises HyprlandReferenceError: if no matches for the reference passed
        :return: a list of results of the disconnect function for everything have something to do with passed reference
        :rtype: list[int]
        """
        signal_objects = []
        if isinstance(reference, SignalCallback):
            if reference in self.registered_signals:
                signal_objects.append(signal)
        elif isinstance(reference, Callable):  # reference is a function.
            for signal in self.registered_signals:
                if signal.callback == reference:
                    signal_objects.append(signal)
                    break
        else:  # maybe its a string, if string so remove every object with same string.
            for signal in self.registered_signals:
                if signal.name == reference:
                    signal_objects.append(signal)
        if len(signal_objects) > 0:
            [self.registered_signals.remove(x) for x in signal_objects]
            return [self.disconnect_by_func(x.reference) for x in signal_objects]
        else:
            raise ReferenceError(
                f"reference {reference} haven't been registered here before."
            )

    def connect(
        self, signal_spec: str, callback: Callable
    ) -> tuple[object, SignalCallback]:
        """
        connects you to a signal
        requires you passing the signal name as a string
        and passing the callback function

        :param signal_spec: the name of the signal you want to connect
        :type signal_spec: str
        :param callback: the callback function that will get called whenever the signal gets emitted, note that this should at least have one argument
        :type callback: Callable
        :return: a tuple contains the returned data of the connect method and the SignalCallback object that makes you able to disconnect later
        :rtype: tuple[object, SignalCallback]
        """
        sc = SignalCallback(name=signal_spec, callback=callback)
        self.registered_signals.append(sc)
        return super().connect(signal_spec, callback), sc
