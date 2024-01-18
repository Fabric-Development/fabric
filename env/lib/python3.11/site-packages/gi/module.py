# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
#
# Copyright (C) 2007-2009 Johan Dahlin <johan@gnome.org>
#
#   module.py: dynamic module for introspected libraries.
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

import importlib
from threading import Lock

import gi

from ._gi import \
    Repository, \
    FunctionInfo, \
    RegisteredTypeInfo, \
    EnumInfo, \
    ObjectInfo, \
    InterfaceInfo, \
    ConstantInfo, \
    StructInfo, \
    UnionInfo, \
    CallbackInfo, \
    Struct, \
    Boxed, \
    CCallback, \
    enum_add, \
    enum_register_new_gtype_and_add, \
    flags_add, \
    flags_register_new_gtype_and_add, \
    GInterface
from .types import \
    GObjectMeta, \
    StructMeta

from ._constants import \
    TYPE_NONE, \
    TYPE_BOXED, \
    TYPE_POINTER, \
    TYPE_ENUM, \
    TYPE_FLAGS


repository = Repository.get_default()

# Cache of IntrospectionModules that have been loaded.
_introspection_modules = {}


def get_parent_for_object(object_info):
    parent_object_info = object_info.get_parent()

    if not parent_object_info:
        # If we reach the end of the introspection info class hierarchy, look
        # for an existing wrapper on the GType and use it as a base for the
        # new introspection wrapper. This allows static C wrappers already
        # registered with the GType to be used as the introspection base
        # (_gi.GObject for example)
        gtype = object_info.get_g_type()
        if gtype and gtype.pytype:
            return gtype.pytype

        # Otherwise use builtins.object as the base
        return object

    namespace = parent_object_info.get_namespace()
    name = parent_object_info.get_name()

    module = importlib.import_module('gi.repository.' + namespace)
    return getattr(module, name)


def get_interfaces_for_object(object_info):
    interfaces = []
    for interface_info in object_info.get_interfaces():
        namespace = interface_info.get_namespace()
        name = interface_info.get_name()

        module = importlib.import_module('gi.repository.' + namespace)
        interfaces.append(getattr(module, name))
    return interfaces


class IntrospectionModule(object):
    """An object which wraps an introspection typelib.

    This wrapping creates a python module like representation of the typelib
    using gi repository as a foundation. Accessing attributes of the module
    will dynamically pull them in and create wrappers for the members.
    These members are then cached on this introspection module.
    """
    def __init__(self, namespace, version=None):
        """Might raise gi._gi.RepositoryError"""

        repository.require(namespace, version)
        self._namespace = namespace
        self._version = version
        self.__name__ = 'gi.repository.' + namespace

        path = repository.get_typelib_path(self._namespace)
        self.__path__ = [path]

        if self._version is None:
            self._version = repository.get_version(self._namespace)

        self._lock = Lock()

    def __getattr__(self, name):
        info = repository.find_by_name(self._namespace, name)
        if not info:
            raise AttributeError("%r object has no attribute %r" % (
                                 self.__name__, name))

        if isinstance(info, EnumInfo):
            g_type = info.get_g_type()

            with self._lock:
                wrapper = g_type.pytype

                if wrapper is None:
                    if info.is_flags():
                        if g_type.is_a(TYPE_FLAGS):
                            wrapper = flags_add(g_type)
                        else:
                            assert g_type == TYPE_NONE
                            wrapper = flags_register_new_gtype_and_add(info)
                    else:
                        if g_type.is_a(TYPE_ENUM):
                            wrapper = enum_add(g_type)
                        else:
                            assert g_type == TYPE_NONE
                            wrapper = enum_register_new_gtype_and_add(info)

                    wrapper.__info__ = info
                    wrapper.__module__ = 'gi.repository.' + info.get_namespace()

                    # Don't use upper() here to avoid locale specific
                    # identifier conversion (e. g. in Turkish 'i'.upper() == 'i')
                    # see https://bugzilla.gnome.org/show_bug.cgi?id=649165
                    ascii_upper_trans = ''.maketrans(
                        'abcdefgjhijklmnopqrstuvwxyz',
                        'ABCDEFGJHIJKLMNOPQRSTUVWXYZ')
                    for value_info in info.get_values():
                        value_name = value_info.get_name_unescaped().translate(ascii_upper_trans)
                        setattr(wrapper, value_name, wrapper(value_info.get_value()))
                    for method_info in info.get_methods():
                        setattr(wrapper, method_info.__name__, method_info)

                if g_type != TYPE_NONE:
                    g_type.pytype = wrapper

        elif isinstance(info, RegisteredTypeInfo):
            g_type = info.get_g_type()

            # Create a wrapper.
            if isinstance(info, ObjectInfo):
                parent = get_parent_for_object(info)
                interfaces = tuple(interface for interface in get_interfaces_for_object(info)
                                   if not issubclass(parent, interface))
                bases = (parent,) + interfaces
                metaclass = GObjectMeta
            elif isinstance(info, CallbackInfo):
                bases = (CCallback,)
                metaclass = GObjectMeta
            elif isinstance(info, InterfaceInfo):
                bases = (GInterface,)
                metaclass = GObjectMeta
            elif isinstance(info, (StructInfo, UnionInfo)):
                if g_type.is_a(TYPE_BOXED):
                    bases = (Boxed,)
                elif (g_type.is_a(TYPE_POINTER) or
                      g_type == TYPE_NONE or
                      g_type.fundamental == g_type):
                    bases = (Struct,)
                else:
                    raise TypeError("unable to create a wrapper for %s.%s" % (info.get_namespace(), info.get_name()))
                metaclass = StructMeta
            else:
                raise NotImplementedError(info)

            with self._lock:
                # Check if there is already a Python wrapper that is not a parent class
                # of the wrapper being created. If it is a parent, it is ok to clobber
                # g_type.pytype with a new child class wrapper of the existing parent.
                # Note that the return here never occurs under normal circumstances due
                # to caching on the __dict__ itself.
                if g_type != TYPE_NONE:
                    type_ = g_type.pytype
                    if type_ is not None and type_ not in bases:
                        self.__dict__[name] = type_
                        return type_

                dict_ = {
                    '__info__': info,
                    '__module__': 'gi.repository.' + self._namespace,
                    '__gtype__': g_type
                }
                wrapper = metaclass(name, bases, dict_)

                # Register the new Python wrapper.
                if g_type != TYPE_NONE:
                    g_type.pytype = wrapper

        elif isinstance(info, FunctionInfo):
            wrapper = info
        elif isinstance(info, ConstantInfo):
            wrapper = info.get_value()
        else:
            raise NotImplementedError(info)

        # Cache the newly created wrapper which will then be
        # available directly on this introspection module instead of being
        # lazily constructed through the __getattr__ we are currently in.
        self.__dict__[name] = wrapper
        return wrapper

    def __repr__(self):
        path = repository.get_typelib_path(self._namespace)
        return "<IntrospectionModule %r from %r>" % (self._namespace, path)

    def __dir__(self):
        # Python's default dir() is just dir(self.__class__) + self.__dict__.keys()
        result = set(dir(self.__class__))
        result.update(self.__dict__.keys())

        # update *set* because some repository attributes have already been
        # wrapped by __getattr__() and included in self.__dict__; but skip
        # Callback types, as these are not real objects which we can actually
        # get
        namespace_infos = repository.get_infos(self._namespace)
        result.update(info.get_name() for info in namespace_infos if
                      not isinstance(info, CallbackInfo))

        return list(result)


def get_introspection_module(namespace):
    """
    :Returns:
        An object directly wrapping the gi module without overrides.

    Might raise gi._gi.RepositoryError
    """
    if namespace in _introspection_modules:
        return _introspection_modules[namespace]

    version = gi.get_required_version(namespace)
    module = IntrospectionModule(namespace, version)
    _introspection_modules[namespace] = module
    return module
