import functools
import types
import warnings
import importlib
import sys
from pkgutil import get_loader

from gi import PyGIDeprecationWarning
from gi._gi import CallableInfo, pygobject_new_full
from gi._constants import \
    TYPE_NONE, \
    TYPE_INVALID

# support overrides in different directories than our gi module
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)


# namespace -> (attr, replacement)
_deprecated_attrs = {}


class OverridesProxyModule(types.ModuleType):
    """Wraps a introspection module and contains all overrides"""

    def __init__(self, introspection_module):
        super(OverridesProxyModule, self).__init__(
            introspection_module.__name__)
        self._introspection_module = introspection_module

    def __getattr__(self, name):
        return getattr(self._introspection_module, name)

    def __dir__(self):
        result = set(dir(self.__class__))
        result.update(self.__dict__.keys())
        result.update(dir(self._introspection_module))
        return sorted(result)

    def __repr__(self):
        return "<%s %r>" % (type(self).__name__, self._introspection_module)


class _DeprecatedAttribute(object):
    """A deprecation descriptor for OverridesProxyModule subclasses.

    Emits a PyGIDeprecationWarning on every access and tries to act as a
    normal instance attribute (can be replaced and deleted).
    """

    def __init__(self, namespace, attr, value, replacement):
        self._attr = attr
        self._value = value
        self._warning = PyGIDeprecationWarning(
            '%s.%s is deprecated; use %s instead' % (
                namespace, attr, replacement))

    def __get__(self, instance, owner):
        if instance is None:
            raise AttributeError(self._attr)
        warnings.warn(self._warning, stacklevel=2)
        return self._value

    def __set__(self, instance, value):
        attr = self._attr
        # delete the descriptor, then set the instance value
        delattr(type(instance), attr)
        setattr(instance, attr, value)

    def __delete__(self, instance):
        # delete the descriptor
        delattr(type(instance), self._attr)


def load_overrides(introspection_module):
    """Loads overrides for an introspection module.

    Either returns the same module again in case there are no overrides or a
    proxy module including overrides. Doesn't cache the result.
    """

    namespace = introspection_module.__name__.rsplit(".", 1)[-1]
    module_key = 'gi.repository.' + namespace

    # We use sys.modules so overrides can import from gi.repository
    # but restore everything at the end so this doesn't have any side effects
    has_old = module_key in sys.modules
    old_module = sys.modules.get(module_key)

    # Create a new sub type, so we can separate descriptors like
    # _DeprecatedAttribute for each namespace.
    proxy_type = type(namespace + "ProxyModule", (OverridesProxyModule, ), {})

    proxy = proxy_type(introspection_module)
    sys.modules[module_key] = proxy

    # backwards compat:
    # gedit uses gi.importer.modules['Gedit']._introspection_module
    from ..importer import modules
    assert hasattr(proxy, "_introspection_module")
    modules[namespace] = proxy

    try:
        override_package_name = 'gi.overrides.' + namespace

        # http://bugs.python.org/issue14710
        try:
            override_loader = get_loader(override_package_name)

        except AttributeError:
            override_loader = None

        # Avoid checking for an ImportError, an override might
        # depend on a missing module thus causing an ImportError
        if override_loader is None:
            return introspection_module

        override_mod = importlib.import_module(override_package_name)

    finally:
        del modules[namespace]
        del sys.modules[module_key]
        if has_old:
            sys.modules[module_key] = old_module

    # backwards compat: for gst-python/gstmodule.c,
    # which tries to access Gst.Fraction through
    # Gst._overrides_module.Fraction. We assign the proxy instead as that
    # contains all overridden classes like Fraction during import anyway and
    # there is no need to keep the real override module alive.
    proxy._overrides_module = proxy

    override_all = []
    if hasattr(override_mod, "__all__"):
        override_all = override_mod.__all__

    for var in override_all:
        try:
            item = getattr(override_mod, var)
        except (AttributeError, TypeError):
            # Gedit puts a non-string in __all__, so catch TypeError here
            continue
        setattr(proxy, var, item)

    # Replace deprecated module level attributes with a descriptor
    # which emits a warning when accessed.
    for attr, replacement in _deprecated_attrs.pop(namespace, []):
        try:
            value = getattr(proxy, attr)
        except AttributeError:
            raise AssertionError(
                "%s was set deprecated but wasn't added to __all__" % attr)
        delattr(proxy, attr)
        deprecated_attr = _DeprecatedAttribute(
            namespace, attr, value, replacement)
        setattr(proxy_type, attr, deprecated_attr)

    return proxy


def override(type_):
    """Decorator for registering an override.

    Other than objects added to __all__, these can get referenced in the same
    override module via the gi.repository module (get_parent_for_object() does
    for example), so they have to be added to the module immediately.
    """

    if isinstance(type_, CallableInfo):
        func = type_
        namespace = func.__module__.rsplit('.', 1)[-1]
        module = sys.modules["gi.repository." + namespace]

        def wrapper(func):
            setattr(module, func.__name__, func)
            return func

        return wrapper
    elif isinstance(type_, types.FunctionType):
        raise TypeError("func must be a gi function, got %s" % type_)
    else:
        try:
            info = getattr(type_, '__info__')
        except AttributeError:
            raise TypeError(
                'Can not override a type %s, which is not in a gobject '
                'introspection typelib' % type_.__name__)

        if not type_.__module__.startswith('gi.overrides'):
            raise KeyError(
                'You have tried override outside of the overrides module. '
                'This is not allowed (%s, %s)' % (type_, type_.__module__))

        g_type = info.get_g_type()
        assert g_type != TYPE_NONE
        if g_type != TYPE_INVALID:
            g_type.pytype = type_

        namespace = type_.__module__.rsplit(".", 1)[-1]
        module = sys.modules["gi.repository." + namespace]
        setattr(module, type_.__name__, type_)

        return type_


overridefunc = override
"""Deprecated"""


def deprecated(fn, replacement):
    """Decorator for marking methods and classes as deprecated"""
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        warnings.warn('%s is deprecated; use %s instead' % (fn.__name__, replacement),
                      PyGIDeprecationWarning, stacklevel=2)
        return fn(*args, **kwargs)
    return wrapped


def deprecated_attr(namespace, attr, replacement):
    """Marks a module level attribute as deprecated. Accessing it will emit
    a PyGIDeprecationWarning warning.

    e.g. for ``deprecated_attr("GObject", "STATUS_FOO", "GLib.Status.FOO")``
    accessing GObject.STATUS_FOO will emit:

        "GObject.STATUS_FOO is deprecated; use GLib.Status.FOO instead"

    :param str namespace:
        The namespace of the override this is called in.
    :param str namespace:
        The attribute name (which gets added to __all__).
    :param str replacement:
        The replacement text which will be included in the warning.
    """

    _deprecated_attrs.setdefault(namespace, []).append((attr, replacement))


def deprecated_init(super_init_func, arg_names, ignore=tuple(),
                    deprecated_aliases={}, deprecated_defaults={},
                    category=PyGIDeprecationWarning,
                    stacklevel=2):
    """Wrapper for deprecating GObject based __init__ methods which specify
    defaults already available or non-standard defaults.

    :param callable super_init_func:
        Initializer to wrap.
    :param list arg_names:
        Ordered argument name list.
    :param list ignore:
        List of argument names to ignore when calling the wrapped function.
        This is useful for function which take a non-standard keyword that is munged elsewhere.
    :param dict deprecated_aliases:
        Dictionary mapping a keyword alias to the actual g_object_newv keyword.
    :param dict deprecated_defaults:
        Dictionary of non-standard defaults that will be used when the
        keyword is not explicitly passed.
    :param Exception category:
        Exception category of the error.
    :param int stacklevel:
        Stack level for the deprecation passed on to warnings.warn
    :returns: Wrapped version of ``super_init_func`` which gives a deprecation
        warning when non-keyword args or aliases are used.
    :rtype: callable
    """
    # We use a list of argument names to maintain order of the arguments
    # being deprecated. This allows calls with positional arguments to
    # continue working but with a deprecation message.
    def new_init(self, *args, **kwargs):
        """Initializer for a GObject based classes with support for property
        sets through the use of explicit keyword arguments.
        """
        # Print warnings for calls with positional arguments.
        if args:
            warnings.warn('Using positional arguments with the GObject constructor has been deprecated. '
                          'Please specify keyword(s) for "%s" or use a class specific constructor. '
                          'See: https://wiki.gnome.org/PyGObject/InitializerDeprecations' %
                          ', '.join(arg_names[:len(args)]),
                          category, stacklevel=stacklevel)
            new_kwargs = dict(zip(arg_names, args))
        else:
            new_kwargs = {}
        new_kwargs.update(kwargs)

        # Print warnings for alias usage and transfer them into the new key.
        aliases_used = []
        for key, alias in deprecated_aliases.items():
            if alias in new_kwargs:
                new_kwargs[key] = new_kwargs.pop(alias)
                aliases_used.append(key)

        if aliases_used:
            warnings.warn('The keyword(s) "%s" have been deprecated in favor of "%s" respectively. '
                          'See: https://wiki.gnome.org/PyGObject/InitializerDeprecations' %
                          (', '.join(deprecated_aliases[k] for k in sorted(aliases_used)),
                           ', '.join(sorted(aliases_used))),
                          category, stacklevel=stacklevel)

        # Print warnings for defaults different than what is already provided by the property
        defaults_used = []
        for key, value in deprecated_defaults.items():
            if key not in new_kwargs:
                new_kwargs[key] = deprecated_defaults[key]
                defaults_used.append(key)

        if defaults_used:
            warnings.warn('Initializer is relying on deprecated non-standard '
                          'defaults. Please update to explicitly use: %s '
                          'See: https://wiki.gnome.org/PyGObject/InitializerDeprecations' %
                          ', '.join('%s=%s' % (k, deprecated_defaults[k]) for k in sorted(defaults_used)),
                          category, stacklevel=stacklevel)

        # Remove keywords that should be ignored.
        for key in ignore:
            if key in new_kwargs:
                new_kwargs.pop(key)

        return super_init_func(self, **new_kwargs)

    return new_init


def strip_boolean_result(method, exc_type=None, exc_str=None, fail_ret=None):
    """Translate method's return value for stripping off success flag.

    There are a lot of methods which return a "success" boolean and have
    several out arguments. Translate such a method to return the out arguments
    on success and None on failure.
    """
    @functools.wraps(method)
    def wrapped(*args, **kwargs):
        ret = method(*args, **kwargs)
        if ret[0]:
            if len(ret) == 2:
                return ret[1]
            else:
                return ret[1:]
        else:
            if exc_type:
                raise exc_type(exc_str or 'call failed')
            return fail_ret
    return wrapped


def wrap_list_store_sort_func(func):

    def wrap(a, b, *user_data):
        a = pygobject_new_full(a, False)
        b = pygobject_new_full(b, False)
        return func(a, b, *user_data)

    return wrap
