from dataclasses import dataclass
from typing import Literal, Type, Callable
from gi.repository import GObject
from gi._propertyhelper import Property


class Property(Property):
    """
    replace python's `property` built-in decorator with this decorator
    to get properties into your service object
    """

    def __init__(
        self,
        value_type: Type = str,
        default_value: object | None = None,
        name: str = "",
        description: str = "",
        flags: Literal[
            "r",
            "w",
            "rw",
            "readable",
            "writable",
            "read-write",
            "construct",
            "construct-only",
            "lax-validation",
            "static-name",
            "private",
            "static-nick",
            "static-blurb",
            "explicit-notify",
            "deprecated",
        ]
        | GObject.ParamFlags = "read-write",
        getter: Callable | None = None,
        setter: Callable | None = None,
        minimum: int | None = None,
        maximum: int | None = None,
        **kwargs,
    ):
        flags = (
            flags
            if isinstance(flags, GObject.ParamFlags)
            else {
                "r": GObject.ParamFlags.READABLE,
                "w": GObject.ParamFlags.WRITABLE,
                "rw": GObject.ParamFlags.READWRITE,
                "readable": GObject.ParamFlags.READABLE,
                "writable": GObject.ParamFlags.WRITABLE,
                "read-write": GObject.ParamFlags.READWRITE,
                "construct": GObject.ParamFlags.CONSTRUCT,
                "construct-only": GObject.ParamFlags.CONSTRUCT_ONLY,
                "lax-validation": GObject.ParamFlags.LAX_VALIDATION,
                "static-name": GObject.ParamFlags.STATIC_NAME,
                "private": GObject.ParamFlags.PRIVATE,
                "static-nick": GObject.ParamFlags.STATIC_NICK,
                "static-blurb": GObject.ParamFlags.STATIC_BLURB,
                "explicit-notify": GObject.ParamFlags.EXPLICIT_NOTIFY,
                "deprecated": GObject.ParamFlags.DEPRECATED,
            }.get(flags.lower(), GObject.ParamFlags.READWRITE)
        )
        super().__init__(
            type=value_type,
            default=default_value,
            nick=name,
            blurb=description,
            flags=flags,
            getter=getter,
            setter=setter,
            minimum=minimum,
            maximum=maximum,
            **kwargs,
        )

    def __get__(self, instance, klass):
        return super().__get__(instance, klass)

    def __set__(self, instance, value):
        return super().__set__(instance, value)

    def __call__(self, fget):
        return self.getter(fget)

    def getter(self, fget):
        return super().getter(fget)

    def setter(self, fset):
        return super().setter(fset)


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


class SignalContainer(dict):
    """
    a class that conatins signals to get added later to the __gsignals__ field,
    it provides you a high level of functionality to work with since
    it converts passed `Signal` objects into a `dict` object so
    it can probably be used with __gsignals__
    """

    def __init__(self, *args: list[Signal]):
        _signals = {}
        for sig in args:
            sig: Signal
            if isinstance(sig, Signal) is True:
                _signals[sig.name] = (
                    sig.flags
                    if isinstance(sig.flags, GObject.SignalFlags) is True
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
                        sig.flags, GObject.SignalFlags.RUN_FIRST
                    ),  # no inline switch? (FIXME: use getattr)
                    sig.rtype,
                    sig.args,
                )
            else:
                continue
        super().__init__(_signals)


@dataclass(frozen=True)
class SignalConnection:
    """
    dataclass that holds a reference to a signal and its callback, name and other info
    """

    id: int
    name: str
    callback: Callable
    owner: GObject.Object

    def disconnect(self):
        """disconnects the signal"""
        return self.owner.disconnect(self)


class Service(GObject.Object):
    __gsignals__ = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._registered_signals: list[SignalConnection] = []

    def disconnect(
        self, reference: SignalConnection | Callable | str | int
    ) -> list[int]:
        """
        disconnects a signal
        by passing the `SignalConnection` to `reference` the callback function will gets disconnected.

        passing a function or a callable makes the method search the props looking for a
        matching object and disconnect it

        if passed a string it will disconnect every callback uses the same signal string

        :param reference: a `SignalConnection`, the callback function or a string contains the signal name
        :type reference: SignalConnection | Callable | str | int
        :raises ReferenceError: if no matches for the passed reference
        :return: a list of results of the disconnect function for everything have something to do with passed reference
        :rtype: list[int]
        """
        signal_objects = []
        if isinstance(reference, SignalConnection):
            if reference in self._registered_signals:
                signal_objects.append(reference)
        elif isinstance(reference, Callable):  # reference is a function.
            for signal in self._registered_signals:
                if reference == signal.callback:
                    signal_objects.append(signal)
                    break
        elif isinstance(
            reference, str
        ):  # maybe its a string, if string so remove every object with same string.
            for signal in self._registered_signals:
                if reference == signal.name:
                    signal_objects.append(signal)
                    break
        elif isinstance(reference, int):  # the signal connection id
            for signal in self._registered_signals:
                if reference == signal.id:
                    signal_objects.append(signal)
                    break
        if len(signal_objects) < 1:
            raise ReferenceError(
                f"reference {reference} haven't been registered here before."
            )
        for signal in signal_objects:
            self._registered_signals.remove(signal)
        return [self.disconnect_by_func(x.callback) for x in signal_objects]

    def connect(self, signal_spec: str, callback: Callable) -> SignalConnection:
        """
        connects you to a signal
        requires you passing the signal name as a string
        and passing the callback function

        :param signal_spec: the name of the signal you want to connect
        :type signal_spec: str
        :param callback: the callback function that will get called whenever the signal gets emitted, note that this should at least have one argument
        :type callback: Callable
        :return: the `SignalConnection` object that contains the connection information
        :rtype: SignalConnection
        """
        conn = SignalConnection(
            id=super().connect(signal_spec, callback),
            name=signal_spec,
            callback=callback,
            owner=self,
        )
        self._registered_signals.append(conn)
        return conn
