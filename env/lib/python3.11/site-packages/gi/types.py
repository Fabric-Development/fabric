# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
#
# Copyright (C) 2005-2009 Johan Dahlin <johan@gnome.org>
#
#   types.py: base types for introspected items.
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

import re

from ._constants import TYPE_INVALID
from .docstring import generate_doc_string

from ._gi import \
    InterfaceInfo, \
    ObjectInfo, \
    StructInfo, \
    VFuncInfo, \
    register_interface_info, \
    hook_up_vfunc_implementation, \
    GInterface
from . import _gi

StructInfo, GInterface  # pyflakes

from . import _propertyhelper as propertyhelper
from . import _signalhelper as signalhelper


def snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class MetaClassHelper(object):
    def _setup_methods(cls):
        for method_info in cls.__info__.get_methods():
            setattr(cls, method_info.__name__, method_info)

    def _setup_class_methods(cls):
        info = cls.__info__
        class_struct = info.get_class_struct()
        if class_struct is None:
            return
        for method_info in class_struct.get_methods():
            name = method_info.__name__
            # Don't mask regular methods or base class methods with TypeClass methods.
            if not hasattr(cls, name):
                setattr(cls, name, classmethod(method_info))

    def _setup_fields(cls):
        for field_info in cls.__info__.get_fields():
            name = field_info.get_name().replace('-', '_')
            setattr(cls, name, property(field_info.get_value, field_info.set_value))

    def _setup_constants(cls):
        for constant_info in cls.__info__.get_constants():
            name = constant_info.get_name()
            value = constant_info.get_value()
            setattr(cls, name, value)

    def _setup_vfuncs(cls):
        for vfunc_name, py_vfunc in cls.__dict__.items():
            if not vfunc_name.startswith("do_") or not callable(py_vfunc):
                continue

            skip_ambiguity_check = False

            # If a method name starts with "do_" assume it is a vfunc, and search
            # in the base classes for a method with the same name to override.
            # Recursion is necessary as overriden methods in most immediate parent
            # classes may shadow vfuncs from classes higher in the hierarchy.
            vfunc_info = None
            for base in cls.__mro__:
                method = getattr(base, vfunc_name, None)
                if method is not None and isinstance(method, VFuncInfo):
                    vfunc_info = method
                    break

                if not hasattr(base, '__info__') or not hasattr(base.__info__, 'get_vfuncs'):
                    continue

                base_name = snake_case(base.__info__.get_type_name())

                for v in base.__info__.get_vfuncs():
                    if vfunc_name == 'do_%s_%s' % (base_name, v.get_name()):
                        vfunc_info = v
                        skip_ambiguity_check = True
                        break

                if vfunc_info:
                    break

            # If we did not find a matching method name in the bases, we might
            # be overriding an interface virtual method. Since interfaces do not
            # provide implementations, there will be no method attribute installed
            # on the object. Instead we have to search through
            # InterfaceInfo.get_vfuncs(). Note that the infos returned by
            # get_vfuncs() use the C vfunc name (ie. there is no "do_" prefix).
            if vfunc_info is None:
                vfunc_info = find_vfunc_info_in_interface(cls.__bases__, vfunc_name[len("do_"):])

            if vfunc_info is not None:
                # Check to see if there are vfuncs with the same name in the bases.
                # We have no way of specifying which one we are supposed to override.
                if not skip_ambiguity_check:
                    ambiguous_base = find_vfunc_conflict_in_bases(vfunc_info, cls.__bases__)
                    if ambiguous_base is not None:
                        base_info = vfunc_info.get_container()
                        raise TypeError('Method %s() on class %s.%s is ambiguous '
                                        'with methods in base classes %s.%s and %s.%s' %
                                        (vfunc_name,
                                         cls.__info__.get_namespace(),
                                         cls.__info__.get_name(),
                                         base_info.get_namespace(),
                                         base_info.get_name(),
                                         ambiguous_base.__info__.get_namespace(),
                                         ambiguous_base.__info__.get_name()
                                        ))
                hook_up_vfunc_implementation(vfunc_info, cls.__gtype__,
                                             py_vfunc)

    def _setup_native_vfuncs(cls):
        # Only InterfaceInfo and ObjectInfo have the get_vfuncs() method.
        # We skip InterfaceInfo because interfaces have no implementations for vfuncs.
        # Also check if __info__ in __dict__, not hasattr('__info__', ...)
        # because we do not want to accidentally retrieve __info__ from a base class.
        class_info = cls.__dict__.get('__info__')
        if class_info is None or not isinstance(class_info, ObjectInfo):
            return

        # Special case skipping of vfuncs for GObject.Object because they will break
        # the static bindings which will try to use them.
        if cls.__module__ == 'gi.repository.GObject' and cls.__name__ == 'Object':
            return

        for vfunc_info in class_info.get_vfuncs():
            name = 'do_%s' % vfunc_info.__name__
            setattr(cls, name, vfunc_info)


def find_vfunc_info_in_interface(bases, vfunc_name):
    for base in bases:
        # All wrapped interfaces inherit from GInterface.
        # This can be seen in IntrospectionModule.__getattr__() in module.py.
        # We do not need to search regular classes here, only wrapped interfaces.
        # We also skip GInterface, because it is not wrapped and has no __info__ attr.
        # Skip bases without __info__ (static _gi.GObject)
        if base is GInterface or\
                not issubclass(base, GInterface) or\
                not hasattr(base, '__info__'):
            continue

        # Only look at this classes vfuncs if it is an interface.
        if isinstance(base.__info__, InterfaceInfo):
            for vfunc in base.__info__.get_vfuncs():
                if vfunc.get_name() == vfunc_name:
                    return vfunc

        # Recurse into the parent classes
        vfunc = find_vfunc_info_in_interface(base.__bases__, vfunc_name)
        if vfunc is not None:
            return vfunc

    return None


def find_vfunc_conflict_in_bases(vfunc, bases):
    for klass in bases:
        if not hasattr(klass, '__info__') or \
                not hasattr(klass.__info__, 'get_vfuncs'):
            continue
        vfuncs = klass.__info__.get_vfuncs()
        vfunc_name = vfunc.get_name()
        for v in vfuncs:
            if v.get_name() == vfunc_name and v != vfunc:
                return klass

        aklass = find_vfunc_conflict_in_bases(vfunc, klass.__bases__)
        if aklass is not None:
            return aklass
    return None


class _GObjectMetaBase(type):
    """Metaclass for automatically registering GObject classes."""
    def __init__(cls, name, bases, dict_):
        type.__init__(cls, name, bases, dict_)
        propertyhelper.install_properties(cls)
        signalhelper.install_signals(cls)
        cls._type_register(cls.__dict__)

    def _type_register(cls, namespace):
        # don't register the class if already registered
        if '__gtype__' in namespace:
            return

        # Do not register a new GType for the overrides, as this would sort of
        # defeat the purpose of overrides...
        if cls.__module__.startswith('gi.overrides.'):
            return

        _gi.type_register(cls, namespace.get('__gtype_name__'))


_gi._install_metaclass(_GObjectMetaBase)


class GObjectMeta(_GObjectMetaBase, MetaClassHelper):
    """Meta class used for GI GObject based types."""
    def __init__(cls, name, bases, dict_):
        super(GObjectMeta, cls).__init__(name, bases, dict_)
        is_gi_defined = False
        if cls.__module__ == 'gi.repository.' + cls.__info__.get_namespace():
            is_gi_defined = True

        is_python_defined = False
        if not is_gi_defined and cls.__module__ != GObjectMeta.__module__:
            is_python_defined = True

        if is_python_defined:
            cls._setup_vfuncs()
        elif is_gi_defined:
            if isinstance(cls.__info__, ObjectInfo):
                cls._setup_class_methods()
            cls._setup_methods()
            cls._setup_constants()
            cls._setup_native_vfuncs()

            if isinstance(cls.__info__, ObjectInfo):
                cls._setup_fields()
            elif isinstance(cls.__info__, InterfaceInfo):
                register_interface_info(cls.__info__.get_g_type())

    def mro(cls):
        return mro(cls)

    @property
    def __doc__(cls):
        """Meta class property which shows up on any class using this meta-class."""
        if cls == GObjectMeta:
            return ''

        doc = cls.__dict__.get('__doc__', None)
        if doc is not None:
            return doc

        # For repository classes, dynamically generate a doc string if it wasn't overridden.
        if cls.__module__.startswith(('gi.repository.', 'gi.overrides')):
            return generate_doc_string(cls.__info__)

        return None


def mro(C):
    """Compute the class precedence list (mro) according to C3, with GObject
    interface considerations.

    We override Python's MRO calculation to account for the fact that
    GObject classes are not affected by the diamond problem:
    http://en.wikipedia.org/wiki/Diamond_problem

    Based on http://www.python.org/download/releases/2.3/mro/
    """
    # TODO: If this turns out being too slow, consider using generators
    bases = []
    bases_of_subclasses = [[C]]

    if C.__bases__:
        for base in C.__bases__:
            # Python causes MRO's to be calculated starting with the lowest
            # base class and working towards the descendant, storing the result
            # in __mro__ at each point. Therefore at this point we know that
            # we already have our base class MRO's available to us, there is
            # no need for us to (re)calculate them.
            bases_of_subclasses += [list(base.__mro__)]
        bases_of_subclasses += [list(C.__bases__)]

    while bases_of_subclasses:
        for subclass_bases in bases_of_subclasses:
            candidate = subclass_bases[0]
            not_head = [s for s in bases_of_subclasses if candidate in s[1:]]
            if not_head and GInterface not in candidate.__bases__:
                candidate = None  # conflict, reject candidate
            else:
                break

        if candidate is None:
            raise TypeError('Cannot create a consistent method resolution '
                            'order (MRO)')

        bases.append(candidate)

        for subclass_bases in bases_of_subclasses[:]:  # remove candidate
            if subclass_bases and subclass_bases[0] == candidate:
                del subclass_bases[0]
                if not subclass_bases:
                    bases_of_subclasses.remove(subclass_bases)

    return bases


def nothing(*args, **kwargs):
    pass


class StructMeta(type, MetaClassHelper):
    """Meta class used for GI Struct based types."""

    def __init__(cls, name, bases, dict_):
        super(StructMeta, cls).__init__(name, bases, dict_)

        # Avoid touching anything else than the base class.
        g_type = cls.__info__.get_g_type()
        if g_type != TYPE_INVALID and g_type.pytype is not None:
            return

        cls._setup_fields()
        cls._setup_methods()

        for method_info in cls.__info__.get_methods():
            if method_info.is_constructor() and \
                    method_info.__name__ == 'new' and \
                    (not method_info.get_arguments() or
                     cls.__info__.get_size() == 0):
                cls.__new__ = staticmethod(method_info)
                # Boxed will raise an exception
                # if arguments are given to __init__
                cls.__init__ = nothing
                break

    @property
    def __doc__(cls):
        if cls == StructMeta:
            return ''
        return generate_doc_string(cls.__info__)
