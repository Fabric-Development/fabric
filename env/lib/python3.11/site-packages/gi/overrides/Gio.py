# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
#
# Copyright (C) 2010 Ignacio Casal Quinteiro <icq@gnome.org>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA

import warnings

from .._ossighelper import wakeup_on_signal, register_sigint_fallback
from ..overrides import override, deprecated_init, wrap_list_store_sort_func
from ..module import get_introspection_module
from gi import PyGIWarning

from gi.repository import GLib

import sys

Gio = get_introspection_module('Gio')

__all__ = []


class Application(Gio.Application):

    def run(self, *args, **kwargs):
        with register_sigint_fallback(self.quit):
            with wakeup_on_signal():
                return Gio.Application.run(self, *args, **kwargs)


Application = override(Application)
__all__.append('Application')


def _warn_init(cls, instead=None):

    def new_init(self, *args, **kwargs):
        super(cls, self).__init__(*args, **kwargs)
        name = cls.__module__.rsplit(".", 1)[-1] + "." + cls.__name__
        if instead:
            warnings.warn(
                ("%s shouldn't be instantiated directly, "
                 "use %s instead." % (name, instead)),
                PyGIWarning, stacklevel=2)
        else:
            warnings.warn(
                "%s shouldn't be instantiated directly." % (name,),
                PyGIWarning, stacklevel=2)

    return new_init


@override
class VolumeMonitor(Gio.VolumeMonitor):
    # https://bugzilla.gnome.org/show_bug.cgi?id=744690
    __init__ = _warn_init(Gio.VolumeMonitor, "Gio.VolumeMonitor.get()")


__all__.append('VolumeMonitor')


@override
class DBusAnnotationInfo(Gio.DBusAnnotationInfo):
    __init__ = _warn_init(Gio.DBusAnnotationInfo)


__all__.append('DBusAnnotationInfo')


@override
class DBusArgInfo(Gio.DBusArgInfo):
    __init__ = _warn_init(Gio.DBusArgInfo)


__all__.append('DBusArgInfo')


@override
class DBusMethodInfo(Gio.DBusMethodInfo):
    __init__ = _warn_init(Gio.DBusMethodInfo)


__all__.append('DBusMethodInfo')


@override
class DBusSignalInfo(Gio.DBusSignalInfo):
    __init__ = _warn_init(Gio.DBusSignalInfo)


__all__.append('DBusSignalInfo')


@override
class DBusInterfaceInfo(Gio.DBusInterfaceInfo):
    __init__ = _warn_init(Gio.DBusInterfaceInfo)


__all__.append('DBusInterfaceInfo')


@override
class DBusNodeInfo(Gio.DBusNodeInfo):
    __init__ = _warn_init(Gio.DBusNodeInfo)


__all__.append('DBusNodeInfo')


class ActionMap(Gio.ActionMap):
    def add_action_entries(self, entries, user_data=None):
        """
        The add_action_entries() method is a convenience function for creating
        multiple Gio.SimpleAction instances and adding them to a Gio.ActionMap.
        Each action is constructed as per one entry.

        :param list entries:
            List of entry tuples for add_action() method. The entry tuple can
            vary in size with the following information:

                * The name of the action. Must be specified.
                * The callback to connect to the "activate" signal of the
                  action. Since GLib 2.40, this can be None for stateful
                  actions, in which case the default handler is used. For
                  boolean-stated actions with no parameter, this is a toggle.
                  For other state types (and parameter type equal to the state
                  type) this will be a function that just calls change_state
                  (which you should provide).
                * The type of the parameter that must be passed to the activate
                  function for this action, given as a single GLib.Variant type
                  string (or None for no parameter)
                * The initial state for this action, given in GLib.Variant text
                  format. The state is parsed with no extra type information, so
                  type tags must be added to the string if they are necessary.
                  Stateless actions should give None here.
                * The callback to connect to the "change-state" signal of the
                  action. All stateful actions should provide a handler here;
                  stateless actions should not.

        :param user_data:
            The user data for signal connections, or None
        """
        try:
            iter(entries)
        except (TypeError):
            raise TypeError('entries must be iterable')

        def _process_action(name, activate=None, parameter_type=None,
                            state=None, change_state=None):
            if parameter_type:
                if not GLib.VariantType.string_is_valid(parameter_type):
                    raise TypeError("The type string '%s' given as the "
                                    "parameter type for action '%s' is "
                                    "not a valid GVariant type string. " %
                                    (parameter_type, name))
                variant_parameter = GLib.VariantType.new(parameter_type)
            else:
                variant_parameter = None

            if state is not None:
                # stateful action
                variant_state = GLib.Variant.parse(None, state, None, None)
                action = Gio.SimpleAction.new_stateful(name, variant_parameter,
                                                       variant_state)
                if change_state is not None:
                    action.connect('change-state', change_state, user_data)
            else:
                # stateless action
                if change_state is not None:
                    raise ValueError("Stateless action '%s' should give "
                                     "None for 'change_state', not '%s'." %
                                     (name, change_state))
                action = Gio.SimpleAction(name=name, parameter_type=variant_parameter)

            if activate is not None:
                action.connect('activate', activate, user_data)
            self.add_action(action)

        for entry in entries:
            # using inner function above since entries can leave out optional arguments
            _process_action(*entry)


ActionMap = override(ActionMap)
__all__.append('ActionMap')


class FileEnumerator(Gio.FileEnumerator):
    def __iter__(self):
        return self

    def __next__(self):
        file_info = self.next_file(None)

        if file_info is not None:
            return file_info
        else:
            raise StopIteration

    # python 2 compat for the iter protocol
    next = __next__


FileEnumerator = override(FileEnumerator)
__all__.append('FileEnumerator')


class MenuItem(Gio.MenuItem):
    def set_attribute(self, attributes):
        for (name, format_string, value) in attributes:
            self.set_attribute_value(name, GLib.Variant(format_string, value))


MenuItem = override(MenuItem)
__all__.append('MenuItem')


class Settings(Gio.Settings):
    '''Provide dictionary-like access to GLib.Settings.'''

    __init__ = deprecated_init(Gio.Settings.__init__,
                               arg_names=('schema', 'path', 'backend'))

    def __contains__(self, key):
        return key in self.list_keys()

    def __len__(self):
        return len(self.list_keys())

    def __iter__(self):
        for key in self.list_keys():
            yield key

    def __bool__(self):
        # for "if mysettings" we don't want a dictionary-like test here, just
        # if the object isn't None
        return True

    # alias for Python 2.x object protocol
    __nonzero__ = __bool__

    def __getitem__(self, key):
        # get_value() aborts the program on an unknown key
        if key not in self:
            raise KeyError('unknown key: %r' % (key,))

        return self.get_value(key).unpack()

    def __setitem__(self, key, value):
        # set_value() aborts the program on an unknown key
        if key not in self:
            raise KeyError('unknown key: %r' % (key,))

        # determine type string of this key
        range = self.get_range(key)
        type_ = range.get_child_value(0).get_string()
        v = range.get_child_value(1)
        if type_ == 'type':
            # v is boxed empty array, type of its elements is the allowed value type
            type_str = v.get_child_value(0).get_type_string()
            assert type_str.startswith('a')
            type_str = type_str[1:]
        elif type_ == 'enum':
            # v is an array with the allowed values
            assert v.get_child_value(0).get_type_string().startswith('a')
            type_str = v.get_child_value(0).get_child_value(0).get_type_string()
            allowed = v.unpack()
            if value not in allowed:
                raise ValueError('value %s is not an allowed enum (%s)' % (value, allowed))
        elif type_ == 'range':
            tuple_ = v.get_child_value(0)
            type_str = tuple_.get_child_value(0).get_type_string()
            min_, max_ = tuple_.unpack()
            if value < min_ or value > max_:
                raise ValueError(
                    'value %s not in range (%s - %s)' % (value, min_, max_))
        else:
            raise NotImplementedError('Cannot handle allowed type range class ' + str(type_))

        self.set_value(key, GLib.Variant(type_str, value))

    def keys(self):
        return self.list_keys()


Settings = override(Settings)
__all__.append('Settings')


class _DBusProxyMethodCall:
    '''Helper class to implement DBusProxy method calls.'''

    def __init__(self, dbus_proxy, method_name):
        self.dbus_proxy = dbus_proxy
        self.method_name = method_name

    def __async_result_handler(self, obj, result, user_data):
        (result_callback, error_callback, real_user_data) = user_data
        try:
            ret = obj.call_finish(result)
        except Exception:
            etype, e = sys.exc_info()[:2]
            # return exception as value
            if error_callback:
                error_callback(obj, e, real_user_data)
            else:
                result_callback(obj, e, real_user_data)
            return

        result_callback(obj, self._unpack_result(ret), real_user_data)

    def __call__(self, *args, **kwargs):
        # the first positional argument is the signature, unless we are calling
        # a method without arguments; then signature is implied to be '()'.
        if args:
            signature = args[0]
            args = args[1:]
            if not isinstance(signature, str):
                raise TypeError('first argument must be the method signature string: %r' % signature)
        else:
            signature = '()'

        arg_variant = GLib.Variant(signature, tuple(args))

        if 'result_handler' in kwargs:
            # asynchronous call
            user_data = (kwargs['result_handler'],
                         kwargs.get('error_handler'),
                         kwargs.get('user_data'))
            self.dbus_proxy.call(self.method_name, arg_variant,
                                 kwargs.get('flags', 0), kwargs.get('timeout', -1), None,
                                 self.__async_result_handler, user_data)
        else:
            # synchronous call
            result = self.dbus_proxy.call_sync(self.method_name, arg_variant,
                                               kwargs.get('flags', 0),
                                               kwargs.get('timeout', -1),
                                               None)
            return self._unpack_result(result)

    @classmethod
    def _unpack_result(klass, result):
        '''Convert a D-BUS return variant into an appropriate return value'''

        result = result.unpack()

        # to be compatible with standard Python behaviour, unbox
        # single-element tuples and return None for empty result tuples
        if len(result) == 1:
            result = result[0]
        elif len(result) == 0:
            result = None

        return result


class DBusProxy(Gio.DBusProxy):
    '''Provide comfortable and pythonic method calls.

    This marshalls the method arguments into a GVariant, invokes the
    call_sync() method on the DBusProxy object, and unmarshalls the result
    GVariant back into a Python tuple.

    The first argument always needs to be the D-Bus signature tuple of the
    method call. Example:

      proxy = Gio.DBusProxy.new_sync(...)
      result = proxy.MyMethod('(is)', 42, 'hello')

    The exception are methods which take no arguments, like
    proxy.MyMethod('()'). For these you can omit the signature and just write
    proxy.MyMethod().

    Optional keyword arguments:

    - timeout: timeout for the call in milliseconds (default to D-Bus timeout)

    - flags: Combination of Gio.DBusCallFlags.*

    - result_handler: Do an asynchronous method call and invoke
         result_handler(proxy_object, result, user_data) when it finishes.

    - error_handler: If the asynchronous call raises an exception,
      error_handler(proxy_object, exception, user_data) is called when it
      finishes. If error_handler is not given, result_handler is called with
      the exception object as result instead.

    - user_data: Optional user data to pass to result_handler for
      asynchronous calls.

    Example for asynchronous calls:

      def mymethod_done(proxy, result, user_data):
          if isinstance(result, Exception):
              # handle error
          else:
              # do something with result

      proxy.MyMethod('(is)', 42, 'hello',
          result_handler=mymethod_done, user_data='data')
    '''
    def __getattr__(self, name):
        return _DBusProxyMethodCall(self, name)


DBusProxy = override(DBusProxy)
__all__.append('DBusProxy')


class ListModel(Gio.ListModel):

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self.get_item(i) for i in range(*key.indices(len(self)))]
        elif isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0:
                raise IndexError
            ret = self.get_item(key)
            if ret is None:
                raise IndexError
            return ret
        else:
            raise TypeError

    def __contains__(self, item):
        pytype = self.get_item_type().pytype
        if not isinstance(item, pytype):
            raise TypeError(
                "Expected type %s.%s" % (pytype.__module__, pytype.__name__))
        for i in self:
            if i == item:
                return True
        return False

    def __len__(self):
        return self.get_n_items()

    def __iter__(self):
        for i in range(len(self)):
            yield self.get_item(i)


ListModel = override(ListModel)
__all__.append('ListModel')


if (GLib.MAJOR_VERSION, GLib.MINOR_VERSION, GLib.MICRO_VERSION) < (2, 57, 1):
    # The "additions" functionality in splice() was broken in older glib
    # https://bugzilla.gnome.org/show_bug.cgi?id=795307
    # This is a slower fallback which emits a signal per added item
    def _list_store_splice(self, position, n_removals, additions):
        self.splice(position, n_removals, [])
        for v in reversed(additions):
            self.insert(position, v)
else:
    def _list_store_splice(self, position, n_removals, additions):
        self.splice(position, n_removals, additions)


class ListStore(Gio.ListStore):

    def sort(self, compare_func, *user_data):
        compare_func = wrap_list_store_sort_func(compare_func)
        return super(ListStore, self).sort(compare_func, *user_data)

    def insert_sorted(self, item, compare_func, *user_data):
        compare_func = wrap_list_store_sort_func(compare_func)
        return super(ListStore, self).insert_sorted(
            item, compare_func, *user_data)

    def __delitem__(self, key):
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            if step == 1:
                _list_store_splice(self, start, max(stop - start, 0), [])
            elif step == -1:
                _list_store_splice(self, stop + 1, max(start - stop, 0), [])
            else:
                for i in sorted(range(start, stop, step), reverse=True):
                    self.remove(i)
        elif isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError
            self.remove(key)
        else:
            raise TypeError

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            pytype = self.get_item_type().pytype
            valuelist = []
            for v in value:
                if not isinstance(v, pytype):
                    raise TypeError(
                        "Expected type %s.%s" % (
                            pytype.__module__, pytype.__name__))
                valuelist.append(v)

            start, stop, step = key.indices(len(self))
            if step == 1:
                _list_store_splice(
                    self, start, max(stop - start, 0), valuelist)
            else:
                indices = list(range(start, stop, step))
                if len(indices) != len(valuelist):
                    raise ValueError

                if step == -1:
                    _list_store_splice(
                        self, stop + 1, max(start - stop, 0), valuelist[::-1])
                else:
                    for i, v in zip(indices, valuelist):
                        _list_store_splice(self, i, 1, [v])
        elif isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError

            pytype = self.get_item_type().pytype
            if not isinstance(value, pytype):
                raise TypeError(
                    "Expected type %s.%s" % (
                        pytype.__module__, pytype.__name__))

            _list_store_splice(self, key, 1, [value])
        else:
            raise TypeError


ListStore = override(ListStore)
__all__.append('ListStore')
