# Copyright 2015 Dustin Spicuzza <dustin@virtualroadside.com>
#           2018 Nikita Churaev <lamefun.x0r@gmail.com>
#           2018 Christoph Reiter <reiter.christoph@gmail.com>
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

import os
from collections import abc
from functools import partial

from gi.repository import GLib, GObject, Gio


def _extract_handler_and_args(obj_or_map, handler_name):
    handler = None
    if isinstance(obj_or_map, abc.Mapping):
        handler = obj_or_map.get(handler_name, None)
    else:
        handler = getattr(obj_or_map, handler_name, None)

    if handler is None:
        raise AttributeError('Handler %s not found' % handler_name)

    args = ()
    if isinstance(handler, abc.Sequence):
        if len(handler) == 0:
            raise TypeError("Handler %s tuple can not be empty" % handler)
        args = handler[1:]
        handler = handler[0]

    elif not callable(handler):
        raise TypeError('Handler %s is not a method, function or tuple' % handler)

    return handler, args


def define_builder_scope():
    from gi.repository import Gtk

    class BuilderScope(GObject.GObject, Gtk.BuilderScope):

        def __init__(self, scope_object=None):
            super().__init__()
            self._scope_object = scope_object

        def do_create_closure(self, builder, func_name, flags, obj):
            current_object = builder.get_current_object() or self._scope_object

            if not self._scope_object:
                current_object = builder.get_current_object()
                if func_name not in current_object.__gtktemplate_methods__:
                    return None

                current_object.__gtktemplate_handlers__.add(func_name)
                handler_name = current_object.__gtktemplate_methods__[func_name]
            else:
                current_object = self._scope_object
                handler_name = func_name

            swapped = int(flags & Gtk.BuilderClosureFlags.SWAPPED)
            if swapped:
                raise RuntimeError(
                    "%r not supported" % GObject.ConnectFlags.SWAPPED)
                return None

            handler, args = _extract_handler_and_args(current_object, handler_name)

            if obj:
                p = partial(handler, *args, swap_data=obj)
            else:
                p = partial(handler, *args)

            p.__gtk_template__ = True
            return p

    return BuilderScope


def connect_func(builder, obj, signal_name, handler_name,
                 connect_object, flags, cls):

    if handler_name not in cls.__gtktemplate_methods__:
        return

    method_name = cls.__gtktemplate_methods__[handler_name]
    template_inst = builder.get_object(cls.__gtype_name__)
    template_inst.__gtktemplate_handlers__.add(handler_name)
    handler = getattr(template_inst, method_name)

    after = int(flags & GObject.ConnectFlags.AFTER)
    swapped = int(flags & GObject.ConnectFlags.SWAPPED)
    if swapped:
        raise RuntimeError(
            "%r not supported" % GObject.ConnectFlags.SWAPPED)

    if connect_object is not None:
        if after:
            func = obj.connect_object_after
        else:
            func = obj.connect_object
        func(signal_name, handler, connect_object)
    else:
        if after:
            func = obj.connect_after
        else:
            func = obj.connect
        func(signal_name, handler)


def register_template(cls):
    from gi.repository import Gtk

    bound_methods = {}
    bound_widgets = {}

    for attr_name, obj in list(cls.__dict__.items()):
        if isinstance(obj, CallThing):
            setattr(cls, attr_name, obj._func)
            handler_name = obj._name
            if handler_name is None:
                handler_name = attr_name

            if handler_name in bound_methods:
                old_attr_name = bound_methods[handler_name]
                raise RuntimeError(
                    "Error while exposing handler %r as %r, "
                    "already available as %r" % (
                        handler_name, attr_name, old_attr_name))
            else:
                bound_methods[handler_name] = attr_name
        elif isinstance(obj, Child):
            widget_name = obj._name
            if widget_name is None:
                widget_name = attr_name

            if widget_name in bound_widgets:
                old_attr_name = bound_widgets[widget_name]
                raise RuntimeError(
                    "Error while exposing child %r as %r, "
                    "already available as %r" % (
                        widget_name, attr_name, old_attr_name))
            else:
                bound_widgets[widget_name] = attr_name
                cls.bind_template_child_full(widget_name, obj._internal, 0)

    cls.__gtktemplate_methods__ = bound_methods
    cls.__gtktemplate_widgets__ = bound_widgets

    if Gtk._version == "4.0":
        BuilderScope = define_builder_scope()
        cls.set_template_scope(BuilderScope())
    else:
        cls.set_connect_func(connect_func, cls)

    base_init_template = cls.init_template
    cls.__dontuse_ginstance_init__ = \
        lambda s: init_template(s, cls, base_init_template)
    # To make this file work with older PyGObject we expose our init code
    # as init_template() but make it a noop when we call it ourselves first
    cls.init_template = cls.__dontuse_ginstance_init__


def init_template(self, cls, base_init_template):
    self.init_template = lambda: None

    if self.__class__ is not cls:
        raise TypeError(
            "Inheritance from classes with @Gtk.Template decorators "
            "is not allowed at this time")

    self.__gtktemplate_handlers__ = set()

    base_init_template(self)

    for widget_name, attr_name in self.__gtktemplate_widgets__.items():
        self.__dict__[attr_name] = self.get_template_child(cls, widget_name)

    for handler_name, attr_name in self.__gtktemplate_methods__.items():
        if handler_name not in self.__gtktemplate_handlers__:
            raise RuntimeError(
                "Handler '%s' was declared with @Gtk.Template.Callback "
                "but was not present in template" % handler_name)


class Child(object):

    def __init__(self, name=None, **kwargs):
        self._name = name
        self._internal = kwargs.pop("internal", False)
        if kwargs:
            raise TypeError("Unhandled arguments: %r" % kwargs)


class CallThing(object):

    def __init__(self, name, func):
        self._name = name
        self._func = func


class Callback(object):

    def __init__(self, name=None):
        self._name = name

    def __call__(self, func):
        return CallThing(self._name, func)


def validate_resource_path(path):
    """Raises GLib.Error in case the resource doesn't exist"""

    try:
        Gio.resources_get_info(path, Gio.ResourceLookupFlags.NONE)
    except GLib.Error:
        # resources_get_info() doesn't handle overlays but we keep using it
        # as a fast path.
        # https://gitlab.gnome.org/GNOME/pygobject/issues/230
        Gio.resources_lookup_data(path, Gio.ResourceLookupFlags.NONE)


class Template(object):

    def __init__(self, **kwargs):
        self.string = None
        self.filename = None
        self.resource_path = None
        if "string" in kwargs:
            self.string = kwargs.pop("string")
        elif "filename" in kwargs:
            self.filename = kwargs.pop("filename")
        elif "resource_path" in kwargs:
            self.resource_path = kwargs.pop("resource_path")
        else:
            raise TypeError(
                "Requires one of the following arguments: "
                "string, filename, resource_path")

        if kwargs:
            raise TypeError("Unhandled keyword arguments %r" % kwargs)

    @classmethod
    def from_file(cls, filename):
        return cls(filename=filename)

    @classmethod
    def from_string(cls, string):
        return cls(string=string)

    @classmethod
    def from_resource(cls, resource_path):
        return cls(resource_path=resource_path)

    Callback = Callback

    Child = Child

    def __call__(self, cls):
        from gi.repository import Gtk

        if not isinstance(cls, type) or not issubclass(cls, Gtk.Widget):
            raise TypeError("Can only use @Gtk.Template on Widgets")

        if "__gtype_name__" not in cls.__dict__:
            raise TypeError(
                "%r does not have a __gtype_name__. Set it to the name "
                "of the class in your template" % cls.__name__)

        if hasattr(cls, "__gtktemplate_methods__"):
            raise TypeError("Cannot nest template classes")

        if self.string is not None:
            data = self.string
            if not isinstance(data, bytes):
                data = data.encode("utf-8")
            bytes_ = GLib.Bytes.new(data)
            cls.set_template(bytes_)
            register_template(cls)
            return cls
        elif self.resource_path is not None:
            validate_resource_path(self.resource_path)
            cls.set_template_from_resource(self.resource_path)
            register_template(cls)
            return cls
        else:
            assert self.filename is not None
            file_ = Gio.File.new_for_path(os.fspath(self.filename))
            bytes_ = GLib.Bytes.new(file_.load_contents()[1])
            cls.set_template(bytes_)
            register_template(cls)
            return cls


__all__ = ["Template"]
