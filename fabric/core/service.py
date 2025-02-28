# GObject must be imported first so the overrides can be imported
from gi.repository import GObject

# all aboard...
import gi.overrides
import gi._signalhelper
import gi._propertyhelper
import gi.overrides.GObject

from dataclasses import dataclass
from collections.abc import Callable
from typing import (
    overload,
    Concatenate,
    ParamSpec,
    Generator,
    Optional,
    Generic,
    TypeVar,
    Literal,
    Union,
    Self,
    Any,
)
from fabric.utils.helpers import (
    get_enum_member,
    snake_case_to_kebab_case,
    kebab_case_to_snake_case,
    get_function_annotations,
)

OldSignal = gi._signalhelper.Signal
OldProperty = gi._propertyhelper.Property
OldGObject = gi.overrides.GObject.Object

old_signal_installer = gi._signalhelper.install_signals
old_property_installer = gi._propertyhelper.install_properties


P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")
G = TypeVar("G", bound=GObject.Object)


def override(parent: object, child_name: str):
    def inner(obj: T) -> T:
        setattr(parent, child_name, obj)
        return obj

    return inner


# TODO: improve the structure of this class
@override(GObject, "Property")
@override(gi._propertyhelper, "Property")
class Property(OldProperty, Generic[T]):
    """
    replace Python's `property` built-in decorator
    with this decorator to get properties in your service
    """

    name: str
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE
    install: bool = True

    def __init__(
        self,
        type: type[T],
        flags: Union[
            Literal[
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
            ],
            GObject.ParamFlags,
        ] = GObject.ParamFlags.READWRITE,
        nickname: Optional[str] = None,
        description: str = "",
        # boolean types
        default_value: Optional[T] = None,
        # int types
        minimum: Optional[int] = None,
        maximum: Optional[int] = None,
        getter: Optional[Callable] = None,
        setter: Optional[Callable] = None,
        install: bool = True,
        **kwargs,
    ):
        self.install = install
        flags = get_enum_member(
            GObject.ParamFlags,
            flags,
            {
                "r": "readable",
                "w": "writeable",
                "rw": "readwrite",
                "read-write": "readwrite",
            },
        )

        if not self.install:
            self.__setattr__(
                "_setter_middle_gate",
                lambda instance, value: self.fset(instance, value),  # type: ignore
            )
        try:
            _type = type if issubclass(type, (bool, int, float, str)) else object
        except TypeError:
            _type = object

        super().__init__(
            type=_type,
            default=default_value,
            nick=nickname or "",
            blurb=description,
            flags=flags,
            getter=getter,
            setter=setter,
            minimum=minimum,
            maximum=maximum,
            **kwargs,
        )

    def _default_getter(self, instance) -> T:
        return getattr(instance, ("_property_helper_" + self.name), self.default)

    def _default_setter(self, instance, value: T) -> None:
        return setattr(instance, ("_property_helper_" + self.name), value)

    def getter(self, fget: Callable[..., T]) -> Self:
        return super().getter(fget)

    def setter(self, fset: Callable) -> Self:
        return super().setter(fset)

    def __call__(self, fget: Callable[..., T]) -> Self:
        return self.getter(fget)

    def __get__(self, instance, klass=None) -> T:
        # Property -> get current value of self
        return super().__get__(instance, klass)  # type: ignore

    def __set__(self, instance, value) -> None:
        # Property = X -> set X as the current value of the property
        return self._setter_middle_gate(instance, value)

    def _setter_middle_gate(self, instance, value) -> None:
        return super().__set__(instance, value)

    @staticmethod
    @override(gi._propertyhelper, "install_properties")
    def installer(klass):
        klass_dict: dict[str, Any] = klass.__dict__.copy()
        klass_properties: dict[str, tuple] = klass_dict.get("__gproperties__", {})
        scanned_properties: list[OldProperty] = []

        for iklass in reversed(
            klass.__mro__
        ):  # fix what pygobject missed, inheriting properties
            for name, value in iklass.__dict__.copy().items():
                if not isinstance(value, OldProperty):
                    continue

                if isinstance(value, Property) and not value.install:
                    continue

                if not value.name:
                    value.name = snake_case_to_kebab_case(name)

                # we will encounter the same property multiple times in case of
                # custom setter methods
                if value.name in klass_properties:
                    if klass_properties[value.name] == value.get_pspec_args():
                        continue
                    raise ValueError(
                        f"Property {value.name} was already found in __gproperties__"
                    )
                klass_properties[value.name] = value.get_pspec_args()
                scanned_properties.append(value)

        for prop in scanned_properties:
            if prop.fget is prop._default_getter or prop.fset is prop._default_setter:
                raise TypeError(
                    f"GObject subclass {klass.__name__} defines do_get/set_property"
                    + " and it also uses a property with a custom setter"
                    + " or getter. This is not allowed"
                )

            setattr(
                klass,
                f"get_{kebab_case_to_snake_case(prop.name)}",  # type: ignore
                lambda self, *args, _prop=prop, **kwargs: Service.get_property(
                    self,
                    _prop.name,  # type: ignore
                    *args,
                    **kwargs,
                ),
            )
            setattr(
                klass,
                f"set_{kebab_case_to_snake_case(prop.name)}",  # type: ignore
                lambda self, value, *args, _prop=prop, **kwargs: Service.set_property(
                    self,
                    _prop.name,  # type: ignore
                    value,
                    *args,
                    **kwargs,
                ),
            )

        # all aboard...
        def property_do_get(self, pspec):
            return getattr(self, kebab_case_to_snake_case(pspec.name), None)

        def property_do_set(self, pspec, value):
            prop = getattr(klass, kebab_case_to_snake_case(pspec.name), None)
            prop.fset(self, value) if prop is not None else None

        setattr(klass, "do_get_property", property_do_get)
        setattr(klass, "do_set_property", property_do_set)
        setattr(klass, "__gproperties__", klass_properties)


@dataclass
class SignalWrapper(Generic[G, P, R]):
    name: str
    instance: G
    func: Optional[Callable[Concatenate[G, P], R]] = None

    def __call__(self, /, *args: P.args, **kwargs: P.kwargs) -> Optional[R]:
        return self.emit(*args, **kwargs)

    def emit(self, /, *args: P.args, **kwargs: P.kwargs) -> Optional[R]:
        rvalue: Optional[R] = (
            self.func(self.instance, *args, **kwargs) if self.func is not None else None
        )
        self.instance.emit(self.name, *args, **kwargs)  # type: ignore
        return rvalue

    # TODO: make it hint self's instance for the callback
    def connect(
        self, callback: Callable[Concatenate[GObject.Object, P], Any], *args, **kwargs
    ) -> int:
        return self.instance.connect(self.name, callback)  # type: ignore


class Signal(Generic[G, P, R]):
    name: str
    flags: GObject.SignalFlags = GObject.SignalFlags.RUN_FIRST
    arg_types: tuple = ()
    rtype: Any = None
    install: bool = True

    # private, kinda
    func: Optional[Callable[Concatenate[G, P], R]] = None

    def __init__(
        self,
        name: Union[str, Callable[Concatenate[G, P], R]],
        flags: Union[
            Literal[
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
            ],
            GObject.SignalFlags,
        ] = GObject.SignalFlags.RUN_FIRST,
        rtype: Any = None,
        arg_types: tuple = (),
        install: bool = True,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.flags = get_enum_member(GObject.SignalFlags, flags)
        self.install = install
        if callable(name):
            self.func = name
            self.name = snake_case_to_kebab_case(self.func.__name__)
            fanno = get_function_annotations(self.func)
            self.arg_types, self.rtype = (
                tuple(filter(lambda x: x is not Any, fanno[0].values())),
                fanno[1],
            )
            return
        self.name = name
        self.arg_types, self.rtype = arg_types, rtype
        return

    def __call__(self, func: Callable[Concatenate[G, P], R]) -> "Signal[G, P, R]":
        rsignal = Signal(func, self.flags, install=self.install)
        rsignal.name = self.name or rsignal.name
        return rsignal

    def __get__(self, instance: G, owner: type[G]) -> SignalWrapper[G, P, R]:
        # looks like we have an initialized object now...
        return SignalWrapper(
            self.name,
            instance,
            self.func,
        )

    def detail(self, detail_name) -> "Signal[G, P, R]":
        # a decorator for creating detailed signals
        if (GObject.SignalFlags.DETAILED & self.flags) != GObject.SignalFlags.DETAILED:  # type: ignore
            self.flags = self.flags | GObject.SignalFlags.DETAILED  # type: ignore
        rsignal = Signal(
            self.name + "::" + detail_name,
            self.flags,
            self.arg_types,
            self.rtype,
            False,
        )
        rsignal.func = self.func
        return rsignal

    def serialize(
        self,
    ) -> dict[str, tuple[GObject.SignalFlags, Any, tuple[Any]]]:
        if not self.name:
            return {}  # i don't even know
        return {f"{self.name}": (self.flags, self.rtype, self.arg_types)}

    @staticmethod
    @override(gi._signalhelper, "install_signals")
    def installer(klass):
        klass_dict: dict[str, Any] = klass.__dict__.copy()
        klass_signals: dict[str, tuple] = klass_dict.get("__gsignals__", {})
        scanned_signals: list[Signal] = []
        for name, value in klass_dict.items():
            if isinstance(value, OldSignal):
                # for compatibility with legacy modules
                old_signal_installer(klass)
                continue
            if not isinstance(value, Signal) or not value.install:
                continue

            if not value.name:
                # the name is missing (for some reason)
                # we add it manually from the variable name
                value.name = snake_case_to_kebab_case(name)
            if value.name in klass_signals:
                raise ValueError(f"Signal {value.name} has already been registered.")
            klass_signals = klass_signals | value.serialize()
            scanned_signals.append(value)

        for signal in scanned_signals:
            if not signal.func:
                continue
            fname = "do_" + name
            if not hasattr(klass, fname):
                setattr(klass, fname, signal.func)

        # all aboard...
        setattr(klass, "__gsignals__", klass_signals)


@dataclass
class Builder(Generic[G]):
    parent: G

    def unwrap(self) -> G:
        return self.parent

    def __getattr__(self, name: str):
        return lambda *args, **kwargs: (
            getattr(self.parent, name)(*args, **kwargs),
            self,
        )[1]


@override(GObject, "Object")
@override(gi.overrides.GObject, "Object")
class Service(GObject.Object, Generic[P, T]):
    """
    Base service class

    Handles constructor connections, bindings and builders
    """

    __gsignals__ = {}
    __gproperties__ = {}
    props: list[Any]

    def __init__(self, **kwargs):
        """Default service constructor (base constructor)

        :param **kwargs: mapped to signal connections (e.g. `on_clicked=lambda *_: ...` connects the given function to the signal "clicked", `notify_my_property=my_func` connects the given function to the signal "notify::my-property")
        """
        super().__init__(**self.filter_kwargs(kwargs))
        self._builder: Optional[Builder] = None
        self.do_connect_kwargs(kwargs)

    @overload
    def build(
        self,
        callback: None = None,
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> Builder[Self]: ...

    @overload
    def build(
        self,
        callback: Callable[Concatenate[Self, Builder[Self], P], Any],
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> Self: ...

    def build(
        self,
        callback: Optional[Callable[Concatenate[Self, Builder[Self], P], Any]] = None,
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> Union[Builder[Self], Self]:
        """Get an instance of a `Builder` that holds a reference to this service

        Builders enable you of doing extra configuration after the initialization
        of a service with ease, it makes you able to either have a callback function
        that does all the extra setup or chain all your setup calls at once

        **Examples:**

        .. code-block:: python

            my_service = (
                MyService()
                .build()
                # beginning of method chaining
                .useful_method()
                .other_useful_method()
                .set_something("something")
                .unwrap() # unwrap self (the service) and get a reference to it
            )

            # when passing a setup function it returns self by default
            my_service = MyService().build(lambda self, builder: self.do_something())
            my_service = MyService().build(
                lambda self, builder: (
                    builder.useful_method()
                    .other_useful_method()
                    .set_something("something")
                    # no need to do `.unwrap()` since we don't really need the value of self
                )
            )


        :param callback: an optional callback to use instead of chaining method calls, defaults to None
        :type callback: Optional[Callable[Concatenate[Self, Builder[Self], P], Any]], optional
        :return: a newly created builder (or a cached one if found)
        :rtype: Union[Builder[Self], Self]
        """
        if not self._builder:
            self._builder = Builder(self)
        if callable and callable(callback):
            callback(self, self._builder, *args, **kwargs)
            return self
        return self._builder

    def bind(
        self,
        source_property: str,
        target_property: str,
        target_object: GObject.Object,
        transform_to: Callable[[GObject.Binding, Any], Any] | None = None,
        transform_from: Callable[[GObject.Binding, Any], Any] | None = None,
        flags: Literal["default", "bidirectional", "sync-create", "invert-boolean"]
        | GObject.BindingFlags = GObject.BindingFlags.DEFAULT,
    ):
        return self.bind_property(
            source_property,
            target_object,
            target_property,
            get_enum_member(
                GObject.BindingFlags, flags, default=GObject.BindingFlags.DEFAULT
            ),
            transform_to or (lambda _, v: v),
            transform_from or (lambda _, v: v),
        )

    def emit(self, signal_name: str, *args, **kwargs) -> None:
        return super().emit(signal_name, *args, **kwargs)  # type: ignore

    def connect(
        self,
        signal_name: str,
        callback: Callable[Concatenate[Self, P], Any],
        *args,
        **kwargs,
    ) -> int:
        return super().connect(signal_name, callback, *args, **kwargs)  # type: ignore

    @staticmethod
    def filter_kwargs(kwargs: dict[str, Any]) -> dict[str, Any]:
        return {
            k: v
            for k, v in kwargs.items()
            if not k.lower().startswith(("on_", "notify_"))
        }

    @staticmethod
    def get_connectables_for_kwargs(
        kwargs: dict[str, Any],
    ) -> Generator[tuple[str, Callable[..., Any]], None, None]:
        for key, value in zip(kwargs.keys(), kwargs.values()):
            if key.startswith("on_"):
                yield snake_case_to_kebab_case(key[3:]), value
            elif key.startswith("notify_"):
                # yield a connectable property
                yield f"notify::{snake_case_to_kebab_case(key[7:])}", value
        return

    def do_connect_kwargs(self, kwargs: dict[str, Any]) -> None:
        for name, callback in self.get_connectables_for_kwargs(kwargs):
            self.connect(name, callback)  # type: ignore
        return

    # set/get properties via [] accessor
    def __getitem__(self, key: str) -> Any:
        assert isinstance(key, str)
        return self.get_property(key)

    def __setitem__(self, key: str, value: Any) -> None:
        assert isinstance(key, str)
        return self.set_property(key, value)

    def __len__(self) -> int:
        return len(self.get_properties()) + len(self.get_signal_names())

    def __int__(self) -> int:
        return self.__len__()

    def set_property(self, property_name: str, value: Any) -> None:
        return super().set_property(property_name, value)  # type: ignore

    def get_property(self, property_name: str) -> Any:
        return super().get_property(property_name)  # type: ignore

    def set_properties(self, *args, **kwargs) -> None:
        return super().set_properties(*args, **kwargs)  # type: ignore

    def get_signal_names(self) -> list[str]:
        return GObject.signal_list_names(self)  # type: ignore

    def get_signal_ids(self) -> list[int]:
        return GObject.signal_list_ids(self)  # type: ignore

    def get_properties(self) -> list[GObject.ParamSpec]:
        return GObject.list_properties(self)  # type: ignore


__all__ = ["Signal", "Property", "Builder", "Service"]
