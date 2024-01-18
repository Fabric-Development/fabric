# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
#
# Copyright (C) 2009 Johan Dahlin <johan@gnome.org>
#               2010 Simon van der Linden <svdlinden@src.gnome.org>
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

import sys
import warnings

from gi.repository import GObject
from .._ossighelper import wakeup_on_signal, register_sigint_fallback
from .._gtktemplate import Template, _extract_handler_and_args
from ..overrides import (override, strip_boolean_result, deprecated_init,
                         wrap_list_store_sort_func)
from ..module import get_introspection_module
from gi import PyGIDeprecationWarning


Gtk = get_introspection_module('Gtk')
GTK3 = Gtk._version == '3.0'
GTK4 = Gtk._version == '4.0'

__all__ = []


Template = Template
__all__.append('Template')

# Exposed for unit-testing.
_extract_handler_and_args = _extract_handler_and_args
__all__.append('_extract_handler_and_args')


class PyGTKDeprecationWarning(PyGIDeprecationWarning):
    pass


__all__.append('PyGTKDeprecationWarning')


if GTK3:
    def _construct_target_list(targets):
        """Create a list of TargetEntry items from a list of tuples in the form (target, flags, info)

        The list can also contain existing TargetEntry items in which case the existing entry
        is re-used in the return list.
        """
        target_entries = []
        for entry in targets:
            if not isinstance(entry, Gtk.TargetEntry):
                entry = Gtk.TargetEntry.new(*entry)
            target_entries.append(entry)
        return target_entries

    __all__.append('_construct_target_list')


def _builder_connect_callback(builder, gobj, signal_name, handler_name, connect_obj, flags, obj_or_map):
    handler, args = _extract_handler_and_args(obj_or_map, handler_name)

    after = flags & GObject.ConnectFlags.AFTER
    if connect_obj is not None:
        if after:
            gobj.connect_object_after(signal_name, handler, connect_obj, *args)
        else:
            gobj.connect_object(signal_name, handler, connect_obj, *args)
    else:
        if after:
            gobj.connect_after(signal_name, handler, *args)
        else:
            gobj.connect(signal_name, handler, *args)


class _FreezeNotifyManager(object):
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self.obj.thaw_child_notify()


class Widget(Gtk.Widget):

    translate_coordinates = strip_boolean_result(Gtk.Widget.translate_coordinates)

    if GTK4:
        def __contains__(self, child):
            return child in list(self)

        def __iter__(self):
            child = self.get_first_child()
            while child:
                yield child
                child = child.get_next_sibling()

    if GTK3:
        def freeze_child_notify(self):
            super(Widget, self).freeze_child_notify()
            return _FreezeNotifyManager(self)

    if GTK3:
        def drag_dest_set_target_list(self, target_list):
            if (target_list is not None) and (not isinstance(target_list, Gtk.TargetList)):
                target_list = Gtk.TargetList.new(_construct_target_list(target_list))
            super(Widget, self).drag_dest_set_target_list(target_list)

    if GTK3:
        def drag_source_set_target_list(self, target_list):
            if (target_list is not None) and (not isinstance(target_list, Gtk.TargetList)):
                target_list = Gtk.TargetList.new(_construct_target_list(target_list))
            super(Widget, self).drag_source_set_target_list(target_list)

    if GTK3:
        def style_get_property(self, property_name, value=None):
            if value is None:
                prop = self.find_style_property(property_name)
                if prop is None:
                    raise ValueError('Class "%s" does not contain style property "%s"' %
                                     (self, property_name))
                value = GObject.Value(prop.value_type)

            Gtk.Widget.style_get_property(self, property_name, value)
            return value.get_value()


Widget = override(Widget)
__all__.append('Widget')


if GTK3:
    class Container(Gtk.Container, Widget):

        def __len__(self):
            return len(self.get_children())

        def __contains__(self, child):
            return child in self.get_children()

        def __iter__(self):
            return iter(self.get_children())

        def __bool__(self):
            return True

        # alias for Python 2.x object protocol
        __nonzero__ = __bool__

        def child_get_property(self, child, property_name, value=None):
            if value is None:
                prop = self.find_child_property(property_name)
                if prop is None:
                    raise ValueError('Class "%s" does not contain child property "%s"' %
                                     (self, property_name))
                value = GObject.Value(prop.value_type)

            Gtk.Container.child_get_property(self, child, property_name, value)
            return value.get_value()

        def child_get(self, child, *prop_names):
            """Returns a list of child property values for the given names."""
            return [self.child_get_property(child, name) for name in prop_names]

        def child_set(self, child, **kwargs):
            """Set a child properties on the given child to key/value pairs."""
            for name, value in kwargs.items():
                name = name.replace('_', '-')
                self.child_set_property(child, name, value)

        get_focus_chain = strip_boolean_result(Gtk.Container.get_focus_chain)

    Container = override(Container)
    __all__.append('Container')
else:
    Container = object


class Editable(Gtk.Editable):

    def insert_text(self, text, position):
        return super(Editable, self).insert_text(text, -1, position)

    get_selection_bounds = strip_boolean_result(Gtk.Editable.get_selection_bounds, fail_ret=())


Editable = override(Editable)
__all__.append("Editable")


if GTK3:
    class Action(Gtk.Action):
        __init__ = deprecated_init(Gtk.Action.__init__,
                                   arg_names=('name', 'label', 'tooltip', 'stock_id'),
                                   category=PyGTKDeprecationWarning)

    Action = override(Action)
    __all__.append("Action")

    class RadioAction(Gtk.RadioAction):
        __init__ = deprecated_init(Gtk.RadioAction.__init__,
                                   arg_names=('name', 'label', 'tooltip', 'stock_id', 'value'),
                                   category=PyGTKDeprecationWarning)

    RadioAction = override(RadioAction)
    __all__.append("RadioAction")

    class ActionGroup(Gtk.ActionGroup):
        __init__ = deprecated_init(Gtk.ActionGroup.__init__,
                                   arg_names=('name',),
                                   category=PyGTKDeprecationWarning)

        def add_actions(self, entries, user_data=None):
            """
            The add_actions() method is a convenience method that creates a number
            of gtk.Action  objects based on the information in the list of action
            entry tuples contained in entries and adds them to the action group.
            The entry tuples can vary in size from one to six items with the
            following information:

                * The name of the action. Must be specified.
                * The stock id for the action. Optional with a default value of None
                  if a label is specified.
                * The label for the action. This field should typically be marked
                  for translation, see the set_translation_domain() method. Optional
                  with a default value of None if a stock id is specified.
                * The accelerator for the action, in the format understood by the
                  gtk.accelerator_parse() function. Optional with a default value of
                  None.
                * The tooltip for the action. This field should typically be marked
                  for translation, see the set_translation_domain() method. Optional
                  with a default value of None.
                * The callback function invoked when the action is activated.
                  Optional with a default value of None.

            The "activate" signals of the actions are connected to the callbacks and
            their accel paths are set to <Actions>/group-name/action-name.
            """
            try:
                iter(entries)
            except (TypeError):
                raise TypeError('entries must be iterable')

            def _process_action(name, stock_id=None, label=None, accelerator=None, tooltip=None, callback=None):
                action = Action(name=name, label=label, tooltip=tooltip, stock_id=stock_id)
                if callback is not None:
                    if user_data is None:
                        action.connect('activate', callback)
                    else:
                        action.connect('activate', callback, user_data)

                self.add_action_with_accel(action, accelerator)

            for e in entries:
                # using inner function above since entries can leave out optional arguments
                _process_action(*e)

        def add_toggle_actions(self, entries, user_data=None):
            """
            The add_toggle_actions() method is a convenience method that creates a
            number of gtk.ToggleAction objects based on the information in the list
            of action entry tuples contained in entries and adds them to the action
            group. The toggle action entry tuples can vary in size from one to seven
            items with the following information:

                * The name of the action. Must be specified.
                * The stock id for the action. Optional with a default value of None
                  if a label is specified.
                * The label for the action. This field should typically be marked
                  for translation, see the set_translation_domain() method. Optional
                  with a default value of None if a stock id is specified.
                * The accelerator for the action, in the format understood by the
                  gtk.accelerator_parse() function. Optional with a default value of
                  None.
                * The tooltip for the action. This field should typically be marked
                  for translation, see the set_translation_domain() method. Optional
                  with a default value of None.
                * The callback function invoked when the action is activated.
                  Optional with a default value of None.
                * A flag indicating whether the toggle action is active. Optional
                  with a default value of False.

            The "activate" signals of the actions are connected to the callbacks and
            their accel paths are set to <Actions>/group-name/action-name.
            """

            try:
                iter(entries)
            except (TypeError):
                raise TypeError('entries must be iterable')

            def _process_action(name, stock_id=None, label=None, accelerator=None, tooltip=None, callback=None, is_active=False):
                action = Gtk.ToggleAction(name=name, label=label, tooltip=tooltip, stock_id=stock_id)
                action.set_active(is_active)
                if callback is not None:
                    if user_data is None:
                        action.connect('activate', callback)
                    else:
                        action.connect('activate', callback, user_data)

                self.add_action_with_accel(action, accelerator)

            for e in entries:
                # using inner function above since entries can leave out optional arguments
                _process_action(*e)

        def add_radio_actions(self, entries, value=None, on_change=None, user_data=None):
            """
            The add_radio_actions() method is a convenience method that creates a
            number of gtk.RadioAction objects based on the information in the list
            of action entry tuples contained in entries and adds them to the action
            group. The entry tuples can vary in size from one to six items with the
            following information:

                * The name of the action. Must be specified.
                * The stock id for the action. Optional with a default value of None
                  if a label is specified.
                * The label for the action. This field should typically be marked
                  for translation, see the set_translation_domain() method. Optional
                  with a default value of None if a stock id is specified.
                * The accelerator for the action, in the format understood by the
                  gtk.accelerator_parse() function. Optional with a default value of
                  None.
                * The tooltip for the action. This field should typically be marked
                  for translation, see the set_translation_domain() method. Optional
                  with a default value of None.
                * The value to set on the radio action. Optional with a default
                  value of 0. Should be specified in applications.

            The value parameter specifies the radio action that should be set
            active. The "changed" signal of the first radio action is connected to
            the on_change callback (if specified and not None) and the accel paths
            of the actions are set to <Actions>/group-name/action-name.
            """
            try:
                iter(entries)
            except (TypeError):
                raise TypeError('entries must be iterable')

            first_action = None

            def _process_action(group_source, name, stock_id=None, label=None, accelerator=None, tooltip=None, entry_value=0):
                action = RadioAction(name=name, label=label, tooltip=tooltip, stock_id=stock_id, value=entry_value)

                if GTK3:
                    action.join_group(group_source)

                if value == entry_value:
                    action.set_active(True)

                self.add_action_with_accel(action, accelerator)
                return action

            for e in entries:
                # using inner function above since entries can leave out optional arguments
                action = _process_action(first_action, *e)
                if first_action is None:
                    first_action = action

            if first_action is not None and on_change is not None:
                if user_data is None:
                    first_action.connect('changed', on_change)
                else:
                    first_action.connect('changed', on_change, user_data)

    ActionGroup = override(ActionGroup)
    __all__.append('ActionGroup')

    class UIManager(Gtk.UIManager):
        def add_ui_from_string(self, buffer):
            if not isinstance(buffer, str):
                raise TypeError('buffer must be a string')

            length = _get_utf8_length(buffer)

            return Gtk.UIManager.add_ui_from_string(self, buffer, length)

        def insert_action_group(self, buffer, length=-1):
            return Gtk.UIManager.insert_action_group(self, buffer, length)

    UIManager = override(UIManager)
    __all__.append('UIManager')


class ComboBox(Gtk.ComboBox, Container):
    get_active_iter = strip_boolean_result(Gtk.ComboBox.get_active_iter)


ComboBox = override(ComboBox)
__all__.append('ComboBox')


if GTK3:
    class Box(Gtk.Box):
        __init__ = deprecated_init(Gtk.Box.__init__,
                                   arg_names=('homogeneous', 'spacing'),
                                   category=PyGTKDeprecationWarning)

    Box = override(Box)
    __all__.append('Box')


if GTK3:
    class SizeGroup(Gtk.SizeGroup):
        __init__ = deprecated_init(Gtk.SizeGroup.__init__,
                                   arg_names=('mode',),
                                   deprecated_defaults={'mode': Gtk.SizeGroupMode.VERTICAL},
                                   category=PyGTKDeprecationWarning)

    SizeGroup = override(SizeGroup)
    __all__.append('SizeGroup')


if GTK3:
    class MenuItem(Gtk.MenuItem):
        __init__ = deprecated_init(Gtk.MenuItem.__init__,
                                   arg_names=('label',),
                                   category=PyGTKDeprecationWarning)

    MenuItem = override(MenuItem)
    __all__.append('MenuItem')


def _get_utf8_length(string):
    assert isinstance(string, str)
    if not isinstance(string, bytes):
        string = string.encode("utf-8")
    return len(string)


class Builder(Gtk.Builder):
    if GTK4:
        from .._gtktemplate import define_builder_scope
        BuilderScope = define_builder_scope()

        def __init__(self, scope_object_or_map=None):
            super(Builder, self).__init__()
            if scope_object_or_map:
                self.set_scope(Builder.BuilderScope(scope_object_or_map))

    else:
        def connect_signals(self, obj_or_map):
            """Connect signals specified by this builder to a name, handler mapping.

            Connect signal, name, and handler sets specified in the builder with
            the given mapping "obj_or_map". The handler/value aspect of the mapping
            can also contain a tuple in the form of (handler [,arg1 [,argN]])
            allowing for extra arguments to be passed to the handler. For example:

            .. code-block:: python

                builder.connect_signals({'on_clicked': (on_clicked, arg1, arg2)})
            """
            self.connect_signals_full(_builder_connect_callback, obj_or_map)

    def add_from_string(self, buffer):
        if not isinstance(buffer, str):
            raise TypeError('buffer must be a string')

        length = _get_utf8_length(buffer)

        return Gtk.Builder.add_from_string(self, buffer, length)

    def add_objects_from_string(self, buffer, object_ids):
        if not isinstance(buffer, str):
            raise TypeError('buffer must be a string')

        length = _get_utf8_length(buffer)

        return Gtk.Builder.add_objects_from_string(self, buffer, length, object_ids)


Builder = override(Builder)
__all__.append('Builder')


# NOTE: This must come before any other Window/Dialog subclassing, to ensure
# that we have a correct inheritance hierarchy.

if GTK4:
    _window_init = Gtk.Window.__init__
else:
    _window_init = deprecated_init(Gtk.Window.__init__,
                                   arg_names=('type',),
                                   category=PyGTKDeprecationWarning,
                                   stacklevel=3)


class Window(Gtk.Window):
    def __init__(self, *args, **kwargs):
        if not initialized:
            raise RuntimeError(
                "Gtk couldn't be initialized. "
                "Use Gtk.init_check() if you want to handle this case.")
        _window_init(self, *args, **kwargs)


Window = override(Window)
__all__.append('Window')


class Dialog(Gtk.Dialog, Container):
    if GTK3:
        _old_arg_names = ('title', 'parent', 'flags', 'buttons', '_buttons_property')
        _init = deprecated_init(Gtk.Dialog.__init__,
                                arg_names=('title', 'transient_for', 'flags',
                                           'add_buttons', 'buttons'),
                                ignore=('flags', 'add_buttons'),
                                deprecated_aliases={'transient_for': 'parent',
                                                    'buttons': '_buttons_property'},
                                category=PyGTKDeprecationWarning)

        def __init__(self, *args, **kwargs):

            new_kwargs = kwargs.copy()
            old_kwargs = dict(zip(self._old_arg_names, args))
            old_kwargs.update(kwargs)

            # Increment the warning stacklevel for sub-classes which implement their own __init__.
            stacklevel = 2
            if self.__class__ != Dialog and self.__class__.__init__ != Dialog.__init__:
                stacklevel += 1

            # buttons was overloaded by PyGtk but is needed for Gtk.MessageDialog
            # as a pass through, so type check the argument and give a deprecation
            # when it is not of type Gtk.ButtonsType
            add_buttons = old_kwargs.get('buttons', None)
            if add_buttons is not None and not isinstance(add_buttons, Gtk.ButtonsType):
                warnings.warn('The "buttons" argument must be a Gtk.ButtonsType enum value. '
                              'Please use the "add_buttons" method for adding buttons. '
                              'See: https://wiki.gnome.org/PyGObject/InitializerDeprecations',
                              PyGTKDeprecationWarning, stacklevel=stacklevel)
                new_kwargs.pop('buttons', None)
            else:
                add_buttons = None

            flags = old_kwargs.get('flags', 0)
            if flags:
                warnings.warn('The "flags" argument for dialog construction is deprecated. '
                              'Please use initializer keywords: modal=True and/or destroy_with_parent=True. '
                              'See: https://wiki.gnome.org/PyGObject/InitializerDeprecations',
                              PyGTKDeprecationWarning, stacklevel=stacklevel)

                if flags & Gtk.DialogFlags.MODAL:
                    new_kwargs['modal'] = True

                if flags & Gtk.DialogFlags.DESTROY_WITH_PARENT:
                    new_kwargs['destroy_with_parent'] = True

            self._init(*args, **new_kwargs)

            if add_buttons:
                self.add_buttons(*add_buttons)

        def run(self, *args, **kwargs):
            with register_sigint_fallback(self.destroy):
                with wakeup_on_signal():
                    return Gtk.Dialog.run(self, *args, **kwargs)

        action_area = property(lambda dialog: dialog.get_action_area())
        vbox = property(lambda dialog: dialog.get_content_area())

    def add_buttons(self, *args):
        """
        The add_buttons() method adds several buttons to the Gtk.Dialog using
        the button data passed as arguments to the method. This method is the
        same as calling the Gtk.Dialog.add_button() repeatedly. The button data
        pairs - button text (or stock ID) and a response ID integer are passed
        individually. For example:

        .. code-block:: python

            dialog.add_buttons(Gtk.STOCK_OPEN, 42, "Close", Gtk.ResponseType.CLOSE)

        will add "Open" and "Close" buttons to dialog.
        """
        def _button(b):
            while b:
                try:
                    t, r = b[0:2]
                except ValueError:
                    raise ValueError('Must pass an even number of arguments')
                b = b[2:]
                yield t, r

        for text, response in _button(args):
            self.add_button(text, response)


Dialog = override(Dialog)
__all__.append('Dialog')


if GTK3:
    class MessageDialog(Gtk.MessageDialog, Dialog):
        __init__ = deprecated_init(Gtk.MessageDialog.__init__,
                                   arg_names=('parent', 'flags', 'message_type',
                                              'buttons', 'message_format'),
                                   deprecated_aliases={'text': 'message_format',
                                                       'message_type': 'type'},
                                   category=PyGTKDeprecationWarning)

        def format_secondary_text(self, message_format):
            self.set_property('secondary-use-markup', False)
            self.set_property('secondary-text', message_format)

        def format_secondary_markup(self, message_format):
            self.set_property('secondary-use-markup', True)
            self.set_property('secondary-text', message_format)

    MessageDialog = override(MessageDialog)
    __all__.append('MessageDialog')


if GTK3:
    class ColorSelectionDialog(Gtk.ColorSelectionDialog):
        __init__ = deprecated_init(Gtk.ColorSelectionDialog.__init__,
                                   arg_names=('title',),
                                   category=PyGTKDeprecationWarning)

    ColorSelectionDialog = override(ColorSelectionDialog)
    __all__.append('ColorSelectionDialog')

    class FileChooserDialog(Gtk.FileChooserDialog):
        __init__ = deprecated_init(Gtk.FileChooserDialog.__init__,
                                   arg_names=('title', 'parent', 'action', 'buttons'),
                                   category=PyGTKDeprecationWarning)

    FileChooserDialog = override(FileChooserDialog)
    __all__.append('FileChooserDialog')


if GTK3:
    class FontSelectionDialog(Gtk.FontSelectionDialog):
        __init__ = deprecated_init(Gtk.FontSelectionDialog.__init__,
                                   arg_names=('title',),
                                   category=PyGTKDeprecationWarning)

    FontSelectionDialog = override(FontSelectionDialog)
    __all__.append('FontSelectionDialog')


if GTK3:
    class RecentChooserDialog(Gtk.RecentChooserDialog):
        # Note, the "manager" keyword must work across the entire 3.x series because
        # "recent_manager" is not backwards compatible with PyGObject versions prior to 3.10.
        __init__ = deprecated_init(Gtk.RecentChooserDialog.__init__,
                                   arg_names=('title', 'parent', 'recent_manager', 'buttons'),
                                   deprecated_aliases={'recent_manager': 'manager'},
                                   category=PyGTKDeprecationWarning)

    RecentChooserDialog = override(RecentChooserDialog)
    __all__.append('RecentChooserDialog')


class IconView(Gtk.IconView):
    if GTK3:
        __init__ = deprecated_init(Gtk.IconView.__init__,
                                   arg_names=('model',),
                                   category=PyGTKDeprecationWarning)

    get_item_at_pos = strip_boolean_result(Gtk.IconView.get_item_at_pos)
    get_visible_range = strip_boolean_result(Gtk.IconView.get_visible_range)
    get_dest_item_at_pos = strip_boolean_result(Gtk.IconView.get_dest_item_at_pos)


IconView = override(IconView)
__all__.append('IconView')


if GTK3:
    class ToolButton(Gtk.ToolButton):
        __init__ = deprecated_init(Gtk.ToolButton.__init__,
                                   arg_names=('stock_id',),
                                   category=PyGTKDeprecationWarning)

    ToolButton = override(ToolButton)
    __all__.append('ToolButton')


class IMContext(Gtk.IMContext):
    get_surrounding = strip_boolean_result(Gtk.IMContext.get_surrounding)


IMContext = override(IMContext)
__all__.append('IMContext')


class RecentInfo(Gtk.RecentInfo):
    get_application_info = strip_boolean_result(Gtk.RecentInfo.get_application_info)


RecentInfo = override(RecentInfo)
__all__.append('RecentInfo')


class TextBuffer(Gtk.TextBuffer):

    def create_tag(self, tag_name=None, **properties):
        """Creates a tag and adds it to the tag table of the TextBuffer.

        :param str tag_name:
            Name of the new tag, or None
        :param **properties:
            Keyword list of properties and their values

        This is equivalent to creating a Gtk.TextTag and then adding the
        tag to the buffer's tag table. The returned tag is owned by
        the buffer's tag table.

        If ``tag_name`` is None, the tag is anonymous.

        If ``tag_name`` is not None, a tag called ``tag_name`` must not already
        exist in the tag table for this buffer.

        Properties are passed as a keyword list of names and values (e.g.
        foreground='DodgerBlue', weight=Pango.Weight.BOLD)

        :returns:
            A new tag.
        """

        tag = Gtk.TextTag(name=tag_name, **properties)
        self.get_tag_table().add(tag)
        return tag

    def create_mark(self, mark_name, where, left_gravity=False):
        return Gtk.TextBuffer.create_mark(self, mark_name, where, left_gravity)

    def set_text(self, text, length=-1):
        Gtk.TextBuffer.set_text(self, text, length)

    def insert(self, iter, text, length=-1):
        if not isinstance(text, str):
            raise TypeError('text must be a string, not %s' % type(text))

        Gtk.TextBuffer.insert(self, iter, text, length)

    def insert_with_tags(self, iter, text, *tags):
        start_offset = iter.get_offset()
        self.insert(iter, text)

        if not tags:
            return

        start = self.get_iter_at_offset(start_offset)

        for tag in tags:
            self.apply_tag(tag, start, iter)

    def insert_with_tags_by_name(self, iter, text, *tags):
        tag_objs = []

        for tag in tags:
            tag_obj = self.get_tag_table().lookup(tag)
            if not tag_obj:
                raise ValueError('unknown text tag: %s' % tag)
            tag_objs.append(tag_obj)

        self.insert_with_tags(iter, text, *tag_objs)

    def insert_at_cursor(self, text, length=-1):
        if not isinstance(text, str):
            raise TypeError('text must be a string, not %s' % type(text))

        Gtk.TextBuffer.insert_at_cursor(self, text, length)

    get_selection_bounds = strip_boolean_result(Gtk.TextBuffer.get_selection_bounds, fail_ret=())


TextBuffer = override(TextBuffer)
__all__.append('TextBuffer')


class TextIter(Gtk.TextIter):
    forward_search = strip_boolean_result(Gtk.TextIter.forward_search)
    backward_search = strip_boolean_result(Gtk.TextIter.backward_search)


TextIter = override(TextIter)
__all__.append('TextIter')


class TreeModel(Gtk.TreeModel):
    def __len__(self):
        return self.iter_n_children(None)

    def __bool__(self):
        return True

    if GTK3:
        # alias for Python 2.x object protocol
        __nonzero__ = __bool__

    def _getiter(self, key):
        if isinstance(key, Gtk.TreeIter):
            return key
        elif isinstance(key, int) and key < 0:
            index = len(self) + key
            if index < 0:
                raise IndexError("row index is out of bounds: %d" % key)
            return self.get_iter(index)
        else:
            try:
                aiter = self.get_iter(key)
            except ValueError:
                raise IndexError("could not find tree path '%s'" % key)
            return aiter

    def sort_new_with_model(self):
        super_object = super(TreeModel, self)
        if hasattr(super_object, "sort_new_with_model"):
            return super_object.sort_new_with_model()
        else:
            return TreeModelSort.new_with_model(self)

    def _coerce_path(self, path):
        if isinstance(path, Gtk.TreePath):
            return path
        else:
            return TreePath(path)

    def __getitem__(self, key):
        aiter = self._getiter(key)
        return TreeModelRow(self, aiter)

    def __setitem__(self, key, value):
        row = self[key]
        self.set_row(row.iter, value)

    def __delitem__(self, key):
        aiter = self._getiter(key)
        self.remove(aiter)

    def __iter__(self):
        return TreeModelRowIter(self, self.get_iter_first())

    get_iter_first = strip_boolean_result(Gtk.TreeModel.get_iter_first)
    iter_children = strip_boolean_result(Gtk.TreeModel.iter_children)
    iter_nth_child = strip_boolean_result(Gtk.TreeModel.iter_nth_child)
    iter_parent = strip_boolean_result(Gtk.TreeModel.iter_parent)
    get_iter_from_string = strip_boolean_result(Gtk.TreeModel.get_iter_from_string,
                                                ValueError, 'invalid tree path')

    def get_iter(self, path):
        path = self._coerce_path(path)
        success, aiter = super(TreeModel, self).get_iter(path)
        if not success:
            raise ValueError("invalid tree path '%s'" % path)
        return aiter

    def iter_next(self, aiter):
        next_iter = aiter.copy()
        success = super(TreeModel, self).iter_next(next_iter)
        if success:
            return next_iter

    def iter_previous(self, aiter):
        prev_iter = aiter.copy()
        success = super(TreeModel, self).iter_previous(prev_iter)
        if success:
            return prev_iter

    def _convert_row(self, row):
        # TODO: Accept a dictionary for row
        # model.append(None,{COLUMN_ICON: icon, COLUMN_NAME: name})
        if isinstance(row, str):
            raise TypeError('Expected a list or tuple, but got str')

        n_columns = self.get_n_columns()
        if len(row) != n_columns:
            raise ValueError('row sequence has the incorrect number of elements')

        result = []
        columns = []
        for cur_col, value in enumerate(row):
            # do not try to set None values, they are causing warnings
            if value is None:
                continue
            result.append(self._convert_value(cur_col, value))
            columns.append(cur_col)
        return (result, columns)

    def set_row(self, treeiter, row):
        converted_row, columns = self._convert_row(row)
        for column in columns:
            self.set_value(treeiter, column, row[column])

    def _convert_value(self, column, value):
        '''Convert value to a GObject.Value of the expected type'''

        if isinstance(value, GObject.Value):
            return value
        return GObject.Value(self.get_column_type(column), value)

    def get(self, treeiter, *columns):
        n_columns = self.get_n_columns()

        values = []
        for col in columns:
            if not isinstance(col, int):
                raise TypeError("column numbers must be ints")

            if col < 0 or col >= n_columns:
                raise ValueError("column number is out of range")

            values.append(self.get_value(treeiter, col))

        return tuple(values)

    #
    # Signals supporting python iterables as tree paths
    #
    def row_changed(self, path, iter):
        return super(TreeModel, self).row_changed(self._coerce_path(path), iter)

    def row_inserted(self, path, iter):
        return super(TreeModel, self).row_inserted(self._coerce_path(path), iter)

    def row_has_child_toggled(self, path, iter):
        return super(TreeModel, self).row_has_child_toggled(self._coerce_path(path),
                                                            iter)

    def row_deleted(self, path):
        return super(TreeModel, self).row_deleted(self._coerce_path(path))

    def rows_reordered(self, path, iter, new_order):
        return super(TreeModel, self).rows_reordered(self._coerce_path(path),
                                                     iter, new_order)


TreeModel = override(TreeModel)
__all__.append('TreeModel')


class TreeSortable(Gtk.TreeSortable, ):

    get_sort_column_id = strip_boolean_result(Gtk.TreeSortable.get_sort_column_id, fail_ret=(None, None))

    def set_sort_func(self, sort_column_id, sort_func, user_data=None):
        super(TreeSortable, self).set_sort_func(sort_column_id, sort_func, user_data)

    def set_default_sort_func(self, sort_func, user_data=None):
        super(TreeSortable, self).set_default_sort_func(sort_func, user_data)


TreeSortable = override(TreeSortable)
__all__.append('TreeSortable')


if GTK3:
    class TreeModelSort(Gtk.TreeModelSort):
        __init__ = deprecated_init(Gtk.TreeModelSort.__init__,
                                   arg_names=('model',),
                                   category=PyGTKDeprecationWarning)

        if not hasattr(Gtk.TreeModelSort, "new_with_model"):
            @classmethod
            def new_with_model(self, child_model):
                return TreeModel.sort_new_with_model(child_model)

    TreeModelSort = override(TreeModelSort)
    __all__.append('TreeModelSort')


class ListStore(Gtk.ListStore, TreeModel, TreeSortable):
    def __init__(self, *column_types):
        Gtk.ListStore.__init__(self)
        self.set_column_types(column_types)

    # insert_with_valuesv got renamed to insert_with_values with 4.1.0
    # https://gitlab.gnome.org/GNOME/gtk/-/commit/a1216599ff6b39bca3e9
    if not hasattr(Gtk.ListStore, "insert_with_valuesv"):
        insert_with_valuesv = Gtk.ListStore.insert_with_values
    elif not hasattr(Gtk.ListStore, "insert_with_values"):
        insert_with_values = Gtk.ListStore.insert_with_valuesv

    def _do_insert(self, position, row):
        if row is not None:
            row, columns = self._convert_row(row)
            treeiter = self.insert_with_values(position, columns, row)
        else:
            treeiter = Gtk.ListStore.insert(self, position)

        return treeiter

    def append(self, row=None):
        if row:
            return self._do_insert(-1, row)
        # gtk_list_store_insert() does not know about the "position == -1"
        # case, so use append() here
        else:
            return Gtk.ListStore.append(self)

    def prepend(self, row=None):
        return self._do_insert(0, row)

    def insert(self, position, row=None):
        return self._do_insert(position, row)

    def insert_before(self, sibling, row=None):
        if row is not None:
            if sibling is None:
                position = -1
            else:
                position = self.get_path(sibling).get_indices()[-1]
            return self._do_insert(position, row)

        return Gtk.ListStore.insert_before(self, sibling)

    def insert_after(self, sibling, row=None):
        if row is not None:
            if sibling is None:
                position = 0
            else:
                position = self.get_path(sibling).get_indices()[-1] + 1
            return self._do_insert(position, row)

        return Gtk.ListStore.insert_after(self, sibling)

    def set_value(self, treeiter, column, value):
        value = self._convert_value(column, value)
        Gtk.ListStore.set_value(self, treeiter, column, value)

    def set(self, treeiter, *args):
        def _set_lists(cols, vals):
            if len(cols) != len(vals):
                raise TypeError('The number of columns do not match the number of values')

            columns = []
            values = []
            for col_num, value in zip(cols, vals):
                if not isinstance(col_num, int):
                    raise TypeError('TypeError: Expected integer argument for column.')

                columns.append(col_num)
                values.append(self._convert_value(col_num, value))

            Gtk.ListStore.set(self, treeiter, columns, values)

        if args:
            if isinstance(args[0], int):
                _set_lists(args[::2], args[1::2])
            elif isinstance(args[0], (tuple, list)):
                if len(args) != 2:
                    raise TypeError('Too many arguments')
                _set_lists(args[0], args[1])
            elif isinstance(args[0], dict):
                _set_lists(list(args[0]), args[0].values())
            else:
                raise TypeError('Argument list must be in the form of (column, value, ...), ((columns,...), (values, ...)) or {column: value}.  No -1 termination is needed.')


ListStore = override(ListStore)
__all__.append('ListStore')


class TreeModelRow(object):

    def __init__(self, model, iter_or_path):
        if not isinstance(model, Gtk.TreeModel):
            raise TypeError("expected Gtk.TreeModel, %s found" % type(model).__name__)
        self.model = model
        if isinstance(iter_or_path, Gtk.TreePath):
            self.iter = model.get_iter(iter_or_path)
        elif isinstance(iter_or_path, Gtk.TreeIter):
            self.iter = iter_or_path
        else:
            raise TypeError("expected Gtk.TreeIter or Gtk.TreePath, "
                            "%s found" % type(iter_or_path).__name__)

    @property
    def path(self):
        return self.model.get_path(self.iter)

    @property
    def next(self):
        return self.get_next()

    @property
    def previous(self):
        return self.get_previous()

    @property
    def parent(self):
        return self.get_parent()

    def get_next(self):
        next_iter = self.model.iter_next(self.iter)
        if next_iter:
            return TreeModelRow(self.model, next_iter)

    def get_previous(self):
        prev_iter = self.model.iter_previous(self.iter)
        if prev_iter:
            return TreeModelRow(self.model, prev_iter)

    def get_parent(self):
        parent_iter = self.model.iter_parent(self.iter)
        if parent_iter:
            return TreeModelRow(self.model, parent_iter)

    def __getitem__(self, key):
        if isinstance(key, int):
            if key >= self.model.get_n_columns():
                raise IndexError("column index is out of bounds: %d" % key)
            elif key < 0:
                key = self._convert_negative_index(key)
            return self.model.get_value(self.iter, key)
        elif isinstance(key, slice):
            start, stop, step = key.indices(self.model.get_n_columns())
            alist = []
            for i in range(start, stop, step):
                alist.append(self.model.get_value(self.iter, i))
            return alist
        elif isinstance(key, tuple):
            return [self[k] for k in key]
        else:
            raise TypeError("indices must be integers, slice or tuple, not %s"
                            % type(key).__name__)

    def __setitem__(self, key, value):
        if isinstance(key, int):
            if key >= self.model.get_n_columns():
                raise IndexError("column index is out of bounds: %d" % key)
            elif key < 0:
                key = self._convert_negative_index(key)
            self.model.set_value(self.iter, key, value)
        elif isinstance(key, slice):
            start, stop, step = key.indices(self.model.get_n_columns())
            indexList = range(start, stop, step)
            if len(indexList) != len(value):
                raise ValueError(
                    "attempt to assign sequence of size %d to slice of size %d"
                    % (len(value), len(indexList)))

            for i, v in enumerate(indexList):
                self.model.set_value(self.iter, v, value[i])
        elif isinstance(key, tuple):
            if len(key) != len(value):
                raise ValueError(
                    "attempt to assign sequence of size %d to sequence of size %d"
                    % (len(value), len(key)))
            for k, v in zip(key, value):
                self[k] = v
        else:
            raise TypeError("indices must be an integer, slice or tuple, not %s"
                            % type(key).__name__)

    def _convert_negative_index(self, index):
        new_index = self.model.get_n_columns() + index
        if new_index < 0:
            raise IndexError("column index is out of bounds: %d" % index)
        return new_index

    def iterchildren(self):
        child_iter = self.model.iter_children(self.iter)
        return TreeModelRowIter(self.model, child_iter)


__all__.append('TreeModelRow')


class TreeModelRowIter(object):

    def __init__(self, model, aiter):
        self.model = model
        self.iter = aiter

    def __next__(self):
        if not self.iter:
            raise StopIteration
        row = TreeModelRow(self.model, self.iter)
        self.iter = self.model.iter_next(self.iter)
        return row

    if GTK3:
        # alias for Python 2.x object protocol
        next = __next__

    def __iter__(self):
        return self


__all__.append('TreeModelRowIter')


class TreePath(Gtk.TreePath):

    def __new__(cls, path=0):
        if isinstance(path, int):
            path = str(path)
        elif not isinstance(path, str):
            path = ":".join(str(val) for val in path)

        if len(path) == 0:
            raise TypeError("could not parse subscript '%s' as a tree path" % path)
        try:
            return TreePath.new_from_string(path)
        except TypeError:
            raise TypeError("could not parse subscript '%s' as a tree path" % path)

    def __init__(self, *args, **kwargs):
        super(TreePath, self).__init__()

    def __str__(self):
        return self.to_string() or ""

    def __lt__(self, other):
        return other is not None and self.compare(other) < 0

    def __le__(self, other):
        return other is not None and self.compare(other) <= 0

    def __eq__(self, other):
        return other is not None and self.compare(other) == 0

    def __ne__(self, other):
        return other is None or self.compare(other) != 0

    def __gt__(self, other):
        return other is None or self.compare(other) > 0

    def __ge__(self, other):
        return other is None or self.compare(other) >= 0

    def __iter__(self):
        return iter(self.get_indices())

    def __len__(self):
        return self.get_depth()

    def __getitem__(self, index):
        return self.get_indices()[index]


TreePath = override(TreePath)
__all__.append('TreePath')


class TreeStore(Gtk.TreeStore, TreeModel, TreeSortable):
    def __init__(self, *column_types):
        Gtk.TreeStore.__init__(self)
        self.set_column_types(column_types)

    def _do_insert(self, parent, position, row):
        if row is not None:
            row, columns = self._convert_row(row)
            treeiter = self.insert_with_values(parent, position, columns, row)
        else:
            treeiter = Gtk.TreeStore.insert(self, parent, position)

        return treeiter

    def append(self, parent, row=None):
        return self._do_insert(parent, -1, row)

    def prepend(self, parent, row=None):
        return self._do_insert(parent, 0, row)

    def insert(self, parent, position, row=None):
        return self._do_insert(parent, position, row)

    def insert_before(self, parent, sibling, row=None):
        if row is not None:
            if sibling is None:
                position = -1
            else:
                if parent is None:
                    parent = self.iter_parent(sibling)
                position = self.get_path(sibling).get_indices()[-1]
            return self._do_insert(parent, position, row)

        return Gtk.TreeStore.insert_before(self, parent, sibling)

    def insert_after(self, parent, sibling, row=None):
        if row is not None:
            if sibling is None:
                position = 0
            else:
                if parent is None:
                    parent = self.iter_parent(sibling)
                position = self.get_path(sibling).get_indices()[-1] + 1
            return self._do_insert(parent, position, row)

        return Gtk.TreeStore.insert_after(self, parent, sibling)

    def set_value(self, treeiter, column, value):
        value = self._convert_value(column, value)
        Gtk.TreeStore.set_value(self, treeiter, column, value)

    def set(self, treeiter, *args):
        def _set_lists(cols, vals):
            if len(cols) != len(vals):
                raise TypeError('The number of columns do not match the number of values')

            columns = []
            values = []
            for col_num, value in zip(cols, vals):
                if not isinstance(col_num, int):
                    raise TypeError('TypeError: Expected integer argument for column.')

                columns.append(col_num)
                values.append(self._convert_value(col_num, value))

            Gtk.TreeStore.set(self, treeiter, columns, values)

        if args:
            if isinstance(args[0], int):
                _set_lists(args[::2], args[1::2])
            elif isinstance(args[0], (tuple, list)):
                if len(args) != 2:
                    raise TypeError('Too many arguments')
                _set_lists(args[0], args[1])
            elif isinstance(args[0], dict):
                _set_lists(args[0].keys(), args[0].values())
            else:
                raise TypeError('Argument list must be in the form of (column, value, ...), ((columns,...), (values, ...)) or {column: value}.  No -1 termination is needed.')


TreeStore = override(TreeStore)
__all__.append('TreeStore')


class TreeView(Gtk.TreeView, Container):
    if GTK3:
        __init__ = deprecated_init(Gtk.TreeView.__init__,
                                   arg_names=('model',),
                                   category=PyGTKDeprecationWarning)

    get_path_at_pos = strip_boolean_result(Gtk.TreeView.get_path_at_pos)
    get_visible_range = strip_boolean_result(Gtk.TreeView.get_visible_range)
    get_dest_row_at_pos = strip_boolean_result(Gtk.TreeView.get_dest_row_at_pos)

    if GTK3:
        def enable_model_drag_source(self, start_button_mask, targets, actions):
            target_entries = _construct_target_list(targets)
            super(TreeView, self).enable_model_drag_source(start_button_mask,
                                                           target_entries,
                                                           actions)

    if GTK3:
        def enable_model_drag_dest(self, targets, actions):
            target_entries = _construct_target_list(targets)
            super(TreeView, self).enable_model_drag_dest(target_entries,
                                                         actions)

    def scroll_to_cell(self, path, column=None, use_align=False, row_align=0.0, col_align=0.0):
        if not isinstance(path, Gtk.TreePath):
            path = TreePath(path)
        super(TreeView, self).scroll_to_cell(path, column, use_align, row_align, col_align)

    def set_cursor(self, path, column=None, start_editing=False):
        if not isinstance(path, Gtk.TreePath):
            path = TreePath(path)
        super(TreeView, self).set_cursor(path, column, start_editing)

    def get_cell_area(self, path, column=None):
        if not isinstance(path, Gtk.TreePath):
            path = TreePath(path)
        return super(TreeView, self).get_cell_area(path, column)

    def insert_column_with_attributes(self, position, title, cell, **kwargs):
        column = TreeViewColumn()
        column.set_title(title)
        column.pack_start(cell, False)
        self.insert_column(column, position)
        column.set_attributes(cell, **kwargs)


TreeView = override(TreeView)
__all__.append('TreeView')


class TreeViewColumn(Gtk.TreeViewColumn):
    def __init__(self, title='',
                 cell_renderer=None,
                 **attributes):
        Gtk.TreeViewColumn.__init__(self, title=title)
        if cell_renderer:
            self.pack_start(cell_renderer, True)

        for (name, value) in attributes.items():
            self.add_attribute(cell_renderer, name, value)

    cell_get_position = strip_boolean_result(Gtk.TreeViewColumn.cell_get_position)

    def set_cell_data_func(self, cell_renderer, func, func_data=None):
        super(TreeViewColumn, self).set_cell_data_func(cell_renderer, func, func_data)

    def set_attributes(self, cell_renderer, **attributes):
        Gtk.CellLayout.clear_attributes(self, cell_renderer)

        for (name, value) in attributes.items():
            Gtk.CellLayout.add_attribute(self, cell_renderer, name, value)


TreeViewColumn = override(TreeViewColumn)
__all__.append('TreeViewColumn')


class TreeSelection(Gtk.TreeSelection):

    def select_path(self, path):
        if not isinstance(path, Gtk.TreePath):
            path = TreePath(path)
        super(TreeSelection, self).select_path(path)

    def get_selected(self):
        success, model, aiter = super(TreeSelection, self).get_selected()
        if success:
            return (model, aiter)
        else:
            return (model, None)

    # for compatibility with PyGtk

    def get_selected_rows(self):
        rows, model = super(TreeSelection, self).get_selected_rows()
        return (model, rows)


TreeSelection = override(TreeSelection)
__all__.append('TreeSelection')


if GTK3:
    class Button(Gtk.Button, Container):
        _init = deprecated_init(Gtk.Button.__init__,
                                arg_names=('label', 'stock', 'use_stock', 'use_underline'),
                                ignore=('stock',),
                                category=PyGTKDeprecationWarning,
                                stacklevel=3)

        def __init__(self, *args, **kwargs):
            # Doubly deprecated initializer, the stock keyword is non-standard.
            # Simply give a warning that stock items are deprecated even though
            # we want to deprecate the non-standard keyword as well here from
            # the overrides.
            if 'stock' in kwargs and kwargs['stock']:
                warnings.warn('Stock items are deprecated. '
                              'Please use: Gtk.Button.new_with_mnemonic(label)',
                              PyGTKDeprecationWarning, stacklevel=2)
                new_kwargs = kwargs.copy()
                new_kwargs['label'] = new_kwargs['stock']
                new_kwargs['use_stock'] = True
                new_kwargs['use_underline'] = True
                del new_kwargs['stock']
                Gtk.Button.__init__(self, **new_kwargs)
            else:
                self._init(*args, **kwargs)

        if hasattr(Gtk.Widget, "set_focus_on_click"):
            def set_focus_on_click(self, *args, **kwargs):
                # Gtk.Widget.set_focus_on_click should be used instead but it's
                # no obvious how because of the shadowed method, so override here
                return Gtk.Widget.set_focus_on_click(self, *args, **kwargs)

        if hasattr(Gtk.Widget, "get_focus_on_click"):
            def get_focus_on_click(self, *args, **kwargs):
                # Gtk.Widget.get_focus_on_click should be used instead but it's
                # no obvious how because of the shadowed method, so override here
                return Gtk.Widget.get_focus_on_click(self, *args, **kwargs)

    Button = override(Button)
    __all__.append('Button')

    class LinkButton(Gtk.LinkButton):
        __init__ = deprecated_init(Gtk.LinkButton.__init__,
                                   arg_names=('uri', 'label'),
                                   category=PyGTKDeprecationWarning)

    LinkButton = override(LinkButton)
    __all__.append('LinkButton')

    class Label(Gtk.Label):
        __init__ = deprecated_init(Gtk.Label.__init__,
                                   arg_names=('label',),
                                   category=PyGTKDeprecationWarning)

    Label = override(Label)
    __all__.append('Label')


class Adjustment(Gtk.Adjustment):
    if GTK3:
        _init = deprecated_init(Gtk.Adjustment.__init__,
                                arg_names=('value', 'lower', 'upper',
                                           'step_increment', 'page_increment', 'page_size'),
                                deprecated_aliases={'page_increment': 'page_incr',
                                                    'step_increment': 'step_incr'},
                                category=PyGTKDeprecationWarning,
                                stacklevel=3)

    def __init__(self, *args, **kwargs):
        if GTK3:
            self._init(*args, **kwargs)
            # The value property is set between lower and (upper - page_size).
            # Just in case lower, upper or page_size was still 0 when value
            # was set, we set it again here.
            if 'value' in kwargs:
                self.set_value(kwargs['value'])
            elif len(args) >= 1:
                self.set_value(args[0])
        else:
            Gtk.Adjustment.__init__(self, *args, **kwargs)

            # The value property is set between lower and (upper - page_size).
            # Just in case lower, upper or page_size was still 0 when value
            # was set, we set it again here.
            if 'value' in kwargs:
                self.set_value(kwargs['value'])


Adjustment = override(Adjustment)
__all__.append('Adjustment')


if GTK3:
    class Table(Gtk.Table, Container):
        __init__ = deprecated_init(Gtk.Table.__init__,
                                   arg_names=('n_rows', 'n_columns', 'homogeneous'),
                                   deprecated_aliases={'n_rows': 'rows', 'n_columns': 'columns'},
                                   category=PyGTKDeprecationWarning)

        def attach(self, child, left_attach, right_attach, top_attach, bottom_attach, xoptions=Gtk.AttachOptions.EXPAND | Gtk.AttachOptions.FILL, yoptions=Gtk.AttachOptions.EXPAND | Gtk.AttachOptions.FILL, xpadding=0, ypadding=0):
            Gtk.Table.attach(self, child, left_attach, right_attach, top_attach, bottom_attach, xoptions, yoptions, xpadding, ypadding)

    Table = override(Table)
    __all__.append('Table')

    class ScrolledWindow(Gtk.ScrolledWindow):
        __init__ = deprecated_init(Gtk.ScrolledWindow.__init__,
                                   arg_names=('hadjustment', 'vadjustment'),
                                   category=PyGTKDeprecationWarning)

    ScrolledWindow = override(ScrolledWindow)
    __all__.append('ScrolledWindow')


if GTK3:
    class HScrollbar(Gtk.HScrollbar):
        __init__ = deprecated_init(Gtk.HScrollbar.__init__,
                                   arg_names=('adjustment',),
                                   category=PyGTKDeprecationWarning)

    HScrollbar = override(HScrollbar)
    __all__.append('HScrollbar')

    class VScrollbar(Gtk.VScrollbar):
        __init__ = deprecated_init(Gtk.VScrollbar.__init__,
                                   arg_names=('adjustment',),
                                   category=PyGTKDeprecationWarning)

    VScrollbar = override(VScrollbar)
    __all__.append('VScrollbar')


if GTK3:
    class Paned(Gtk.Paned):
        def pack1(self, child, resize=False, shrink=True):
            super(Paned, self).pack1(child, resize, shrink)

        def pack2(self, child, resize=True, shrink=True):
            super(Paned, self).pack2(child, resize, shrink)

    Paned = override(Paned)
    __all__.append('Paned')


if GTK3:
    class Arrow(Gtk.Arrow):
        __init__ = deprecated_init(Gtk.Arrow.__init__,
                                   arg_names=('arrow_type', 'shadow_type'),
                                   category=PyGTKDeprecationWarning)

    Arrow = override(Arrow)
    __all__.append('Arrow')

    class IconSet(Gtk.IconSet):
        def __new__(cls, pixbuf=None):
            if pixbuf is not None:
                warnings.warn('Gtk.IconSet(pixbuf) has been deprecated. Please use: '
                              'Gtk.IconSet.new_from_pixbuf(pixbuf)',
                              PyGTKDeprecationWarning, stacklevel=2)
                iconset = Gtk.IconSet.new_from_pixbuf(pixbuf)
            else:
                iconset = Gtk.IconSet.__new__(cls)
            return iconset

        def __init__(self, *args, **kwargs):
            return super(IconSet, self).__init__()

    IconSet = override(IconSet)
    __all__.append('IconSet')

    class Viewport(Gtk.Viewport):
        __init__ = deprecated_init(Gtk.Viewport.__init__,
                                   arg_names=('hadjustment', 'vadjustment'),
                                   category=PyGTKDeprecationWarning)

    Viewport = override(Viewport)
    __all__.append('Viewport')


class TreeModelFilter(Gtk.TreeModelFilter):
    def set_visible_func(self, func, data=None):
        super(TreeModelFilter, self).set_visible_func(func, data)

    def set_value(self, iter, column, value):
        # Delegate to child model
        iter = self.convert_iter_to_child_iter(iter)
        self.get_model().set_value(iter, column, value)


TreeModelFilter = override(TreeModelFilter)
__all__.append('TreeModelFilter')


class CssProvider(Gtk.CssProvider):
    def load_from_data(self, text, length=-1):
        if (Gtk.get_major_version(), Gtk.get_minor_version()) >= (4, 9):
            if isinstance(text, bytes):
                text = text.decode("utf-8")
            super(CssProvider, self).load_from_data(text, length)
        else:
            if isinstance(text, str):
                text = text.encode("utf-8")
            super(CssProvider, self).load_from_data(text)


CssProvider = override(CssProvider)
__all__.append("CssProvider")

if GTK4:
    class CustomSorter(Gtk.CustomSorter):

        @classmethod
        def new(cls, sort_func, user_data=None):
            if sort_func is not None:
                compare_func = wrap_list_store_sort_func(sort_func)
            else:
                compare_func = None

            return Gtk.CustomSorter.new(compare_func, user_data)

        def set_sort_func(self, sort_func, user_data=None):
            if sort_func is not None:
                compare_func = wrap_list_store_sort_func(sort_func)
            else:
                compare_func = None

            return super(CustomSorter, self).set_sort_func(compare_func, user_data)

    CustomSorter = override(CustomSorter)
    __all__.append("CustomSorter")

if GTK3:
    class Menu(Gtk.Menu):
        def popup(self, parent_menu_shell, parent_menu_item, func, data, button, activate_time):
            self.popup_for_device(None, parent_menu_shell, parent_menu_item, func, data, button, activate_time)
    Menu = override(Menu)
    __all__.append('Menu')

if GTK3:
    _Gtk_main_quit = Gtk.main_quit

    @override(Gtk.main_quit)
    def main_quit(*args):
        _Gtk_main_quit()

    _Gtk_main = Gtk.main

    @override(Gtk.main)
    def main(*args, **kwargs):
        with register_sigint_fallback(Gtk.main_quit):
            with wakeup_on_signal():
                return _Gtk_main(*args, **kwargs)


if GTK3:
    stock_lookup = strip_boolean_result(Gtk.stock_lookup)
    __all__.append('stock_lookup')

if GTK4:
    initialized = Gtk.init_check()
else:
    initialized, argv = Gtk.init_check(sys.argv)
    sys.argv = list(argv)
