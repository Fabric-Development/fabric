# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
#
# Copyright (C) 2011-2012 Johan Dahlin <johan@gnome.org>
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

"""
PyGTK compatibility layer.

This modules goes a little bit longer to maintain PyGTK compatibility than
the normal overrides system.

It is recommended to not depend on this layer, but only use it as an
intermediate step when porting your application to PyGI.

Compatibility might never be 100%, but the aim is to make it possible to run
a well behaved PyGTK application mostly unmodified on top of PyGI.

"""

import sys
import warnings
from collections import UserList

import gi
from gi.repository import GObject


_patches = []
_module_patches = []
_unset = object()
_enabled_registry = {}


def _patch(obj, name, new_value):
    old_value = getattr(obj, name, _unset)
    setattr(obj, name, new_value)
    _patches.append((obj, name, old_value))


def _patch_module(name, new_value):
    old_value = sys.modules.get(name, _unset)
    sys.modules[name] = new_value
    _module_patches.append((name, old_value))


def _install_enums(module, dest=None, strip=''):
    if dest is None:
        dest = module
    modname = dest.__name__.rsplit('.', 1)[1].upper()
    for attr in dir(module):
        try:
            obj = getattr(module, attr, None)
        except:
            continue
        try:
            if issubclass(obj, GObject.GEnum):
                for value, enum in obj.__enum_values__.items():
                    name = enum.value_name
                    name = name.replace(modname + '_', '')
                    if strip and name.startswith(strip):
                        name = name[len(strip):]
                    _patch(dest, name, enum)
        except TypeError:
            continue
        try:
            if issubclass(obj, GObject.GFlags):
                for value, flag in obj.__flags_values__.items():
                    try:
                        name = flag.value_names[-1].replace(modname + '_', '')
                    except IndexError:
                        # FIXME: this happens for some large flags which do not
                        # fit into a long on 32 bit systems
                        continue
                    _patch(dest, name, flag)
        except TypeError:
            continue


def _check_enabled(name, version=None):
    """Returns True in case it is already enabled"""

    if name in _enabled_registry:
        enabled_version = _enabled_registry[name]
        if enabled_version != version:
            raise ValueError(
                "%r already enabled with different version (%r)" % (
                    name, enabled_version))
        return True
    else:
        _enabled_registry[name] = version
        return False


def enable():
    if _check_enabled(""):
        return

    # gobject
    from gi.repository import GLib
    _patch_module('glib', GLib)

    # gobject
    from gi.repository import GObject
    _patch_module('gobject', GObject)
    from gi import _propertyhelper
    _patch_module('gobject.propertyhelper', _propertyhelper)

    # gio
    from gi.repository import Gio
    _patch_module('gio', Gio)


def _disable_all():
    """Reverse all effects of the enable_xxx() calls except for
    require_version() calls and imports.
    """

    _enabled_registry.clear()

    for obj, name, old_value in reversed(_patches):
        if old_value is _unset:
            delattr(obj, name)
        else:
            # try if deleting is enough (for override proxies)
            delattr(obj, name)
            if getattr(obj, name, _unset) is not old_value:
                setattr(obj, name, old_value)
    del _patches[:]

    for name, old_value in reversed(_module_patches):
        if old_value is _unset:
            del sys.modules[name]
        else:
            sys.modules[name] = old_value
    del _module_patches[:]


def enable_gtk(version='3.0'):
    if _check_enabled("gtk", version):
        return

    if version == "4.0":
        raise ValueError("version 4.0 not supported")

    # atk
    gi.require_version('Atk', '1.0')
    from gi.repository import Atk
    _patch_module('atk', Atk)
    _install_enums(Atk)

    # pango
    gi.require_version('Pango', '1.0')
    from gi.repository import Pango
    _patch_module('pango', Pango)
    _install_enums(Pango)

    # pangocairo
    gi.require_version('PangoCairo', '1.0')
    from gi.repository import PangoCairo
    _patch_module('pangocairo', PangoCairo)

    # gdk
    gi.require_version('Gdk', version)
    gi.require_version('GdkPixbuf', '2.0')
    from gi.repository import Gdk
    from gi.repository import GdkPixbuf
    _patch_module('gtk.gdk', Gdk)
    _install_enums(Gdk)
    _install_enums(GdkPixbuf, dest=Gdk)
    _patch(Gdk, "_2BUTTON_PRESS", 5)
    _patch(Gdk, "BUTTON_PRESS", 4)

    _patch(Gdk, "screen_get_default", Gdk.Screen.get_default)
    _patch(Gdk, "Pixbuf", GdkPixbuf.Pixbuf)
    _patch(Gdk, "PixbufLoader", GdkPixbuf.PixbufLoader.new_with_type)
    _patch(Gdk, "pixbuf_new_from_data", GdkPixbuf.Pixbuf.new_from_data)
    _patch(Gdk, "pixbuf_new_from_file", GdkPixbuf.Pixbuf.new_from_file)
    _patch(Gdk, "pixbuf_new_from_file_at_scale", GdkPixbuf.Pixbuf.new_from_file_at_scale)
    _patch(Gdk, "pixbuf_new_from_file_at_size", GdkPixbuf.Pixbuf.new_from_file_at_size)
    _patch(Gdk, "pixbuf_new_from_inline", GdkPixbuf.Pixbuf.new_from_inline)
    _patch(Gdk, "pixbuf_new_from_stream", GdkPixbuf.Pixbuf.new_from_stream)
    _patch(Gdk, "pixbuf_new_from_stream_at_scale", GdkPixbuf.Pixbuf.new_from_stream_at_scale)
    _patch(Gdk, "pixbuf_new_from_xpm_data", GdkPixbuf.Pixbuf.new_from_xpm_data)
    _patch(Gdk, "pixbuf_get_file_info", GdkPixbuf.Pixbuf.get_file_info)

    orig_get_formats = GdkPixbuf.Pixbuf.get_formats

    def get_formats():
        formats = orig_get_formats()
        result = []

        def make_dict(format_):
            result = {}
            result['description'] = format_.get_description()
            result['name'] = format_.get_name()
            result['mime_types'] = format_.get_mime_types()
            result['extensions'] = format_.get_extensions()
            return result

        for format_ in formats:
            result.append(make_dict(format_))
        return result

    _patch(Gdk, "pixbuf_get_formats", get_formats)

    orig_get_origin = Gdk.Window.get_origin

    def get_origin(self):
        return orig_get_origin(self)[1:]
    _patch(Gdk.Window, "get_origin", get_origin)

    _patch(Gdk, "screen_width", Gdk.Screen.width)
    _patch(Gdk, "screen_height", Gdk.Screen.height)

    orig_gdk_window_get_geometry = Gdk.Window.get_geometry

    def gdk_window_get_geometry(window):
        return orig_gdk_window_get_geometry(window) + (window.get_visual().get_best_depth(),)
    _patch(Gdk.Window, "get_geometry", gdk_window_get_geometry)

    # gtk
    gi.require_version('Gtk', version)
    from gi.repository import Gtk
    _patch_module('gtk', Gtk)
    _patch(Gtk, "gdk", Gdk)

    _patch(Gtk, "pygtk_version", (2, 99, 0))

    _patch(Gtk, "gtk_version", (Gtk.MAJOR_VERSION,
                                Gtk.MINOR_VERSION,
                                Gtk.MICRO_VERSION))
    _install_enums(Gtk)

    # Action

    def set_tool_item_type(menuaction, gtype):
        warnings.warn('set_tool_item_type() is not supported',
                      gi.PyGIDeprecationWarning, stacklevel=2)
    _patch(Gtk.Action, "set_tool_item_type", classmethod(set_tool_item_type))

    # Alignment

    orig_Alignment = Gtk.Alignment

    class Alignment(orig_Alignment):
        def __init__(self, xalign=0.0, yalign=0.0, xscale=0.0, yscale=0.0):
            orig_Alignment.__init__(self)
            self.props.xalign = xalign
            self.props.yalign = yalign
            self.props.xscale = xscale
            self.props.yscale = yscale

    _patch(Gtk, "Alignment", Alignment)

    # Box

    orig_pack_end = Gtk.Box.pack_end

    def pack_end(self, child, expand=True, fill=True, padding=0):
        orig_pack_end(self, child, expand, fill, padding)
    _patch(Gtk.Box, "pack_end", pack_end)

    orig_pack_start = Gtk.Box.pack_start

    def pack_start(self, child, expand=True, fill=True, padding=0):
        orig_pack_start(self, child, expand, fill, padding)
    _patch(Gtk.Box, "pack_start", pack_start)

    # TreeViewColumn

    orig_tree_view_column_pack_end = Gtk.TreeViewColumn.pack_end

    def tree_view_column_pack_end(self, cell, expand=True):
        orig_tree_view_column_pack_end(self, cell, expand)
    _patch(Gtk.TreeViewColumn, "pack_end", tree_view_column_pack_end)

    orig_tree_view_column_pack_start = Gtk.TreeViewColumn.pack_start

    def tree_view_column_pack_start(self, cell, expand=True):
        orig_tree_view_column_pack_start(self, cell, expand)
    _patch(Gtk.TreeViewColumn, "pack_start", tree_view_column_pack_start)

    # CellLayout

    orig_cell_pack_end = Gtk.CellLayout.pack_end

    def cell_pack_end(self, cell, expand=True):
        orig_cell_pack_end(self, cell, expand)
    _patch(Gtk.CellLayout, "pack_end", cell_pack_end)

    orig_cell_pack_start = Gtk.CellLayout.pack_start

    def cell_pack_start(self, cell, expand=True):
        orig_cell_pack_start(self, cell, expand)
    _patch(Gtk.CellLayout, "pack_start", cell_pack_start)

    orig_set_cell_data_func = Gtk.CellLayout.set_cell_data_func

    def set_cell_data_func(self, cell, func, user_data=_unset):
        def callback(*args):
            if args[-1] == _unset:
                args = args[:-1]
            return func(*args)
        orig_set_cell_data_func(self, cell, callback, user_data)
    _patch(Gtk.CellLayout, "set_cell_data_func", set_cell_data_func)

    # CellRenderer

    class GenericCellRenderer(Gtk.CellRenderer):
        pass
    _patch(Gtk, "GenericCellRenderer", GenericCellRenderer)

    # ComboBox

    orig_combo_row_separator_func = Gtk.ComboBox.set_row_separator_func

    def combo_row_separator_func(self, func, user_data=_unset):
        def callback(*args):
            if args[-1] == _unset:
                args = args[:-1]
            return func(*args)
        orig_combo_row_separator_func(self, callback, user_data)
    _patch(Gtk.ComboBox, "set_row_separator_func", combo_row_separator_func)

    # ComboBoxEntry

    class ComboBoxEntry(Gtk.ComboBox):
        def __init__(self, **kwds):
            Gtk.ComboBox.__init__(self, has_entry=True, **kwds)

        def set_text_column(self, text_column):
            self.set_entry_text_column(text_column)

        def get_text_column(self):
            return self.get_entry_text_column()
    _patch(Gtk, "ComboBoxEntry", ComboBoxEntry)

    def combo_box_entry_new():
        return Gtk.ComboBoxEntry()
    _patch(Gtk, "combo_box_entry_new", combo_box_entry_new)

    def combo_box_entry_new_with_model(model):
        return Gtk.ComboBoxEntry(model=model)
    _patch(Gtk, "combo_box_entry_new_with_model", combo_box_entry_new_with_model)

    # Container

    def install_child_property(container, flag, pspec):
        warnings.warn('install_child_property() is not supported',
                      gi.PyGIDeprecationWarning, stacklevel=2)
    _patch(Gtk.Container, "install_child_property", classmethod(install_child_property))

    def new_text():
        combo = Gtk.ComboBox()
        model = Gtk.ListStore(str)
        combo.set_model(model)
        combo.set_entry_text_column(0)
        return combo
    _patch(Gtk, "combo_box_new_text", new_text)

    def append_text(self, text):
        model = self.get_model()
        model.append([text])
    _patch(Gtk.ComboBox, "append_text", append_text)
    _patch(Gtk, "expander_new_with_mnemonic", Gtk.Expander.new_with_mnemonic)
    _patch(Gtk, "icon_theme_get_default", Gtk.IconTheme.get_default)
    _patch(Gtk, "image_new_from_pixbuf", Gtk.Image.new_from_pixbuf)
    _patch(Gtk, "image_new_from_stock", Gtk.Image.new_from_stock)
    _patch(Gtk, "image_new_from_animation", Gtk.Image.new_from_animation)
    _patch(Gtk, "image_new_from_icon_set", Gtk.Image.new_from_icon_set)
    _patch(Gtk, "image_new_from_file", Gtk.Image.new_from_file)
    _patch(Gtk, "settings_get_default", Gtk.Settings.get_default)
    _patch(Gtk, "window_set_default_icon", Gtk.Window.set_default_icon)
    _patch(Gtk, "clipboard_get", Gtk.Clipboard.get)

    # AccelGroup
    _patch(Gtk.AccelGroup, "connect_group", Gtk.AccelGroup.connect)

    # StatusIcon
    _patch(Gtk, "status_icon_position_menu", Gtk.StatusIcon.position_menu)
    _patch(Gtk.StatusIcon, "set_tooltip", Gtk.StatusIcon.set_tooltip_text)

    # Scale

    orig_HScale = Gtk.HScale
    orig_VScale = Gtk.VScale

    class HScale(orig_HScale):
        def __init__(self, adjustment=None):
            orig_HScale.__init__(self, adjustment=adjustment)
    _patch(Gtk, "HScale", HScale)

    class VScale(orig_VScale):
        def __init__(self, adjustment=None):
            orig_VScale.__init__(self, adjustment=adjustment)
    _patch(Gtk, "VScale", VScale)

    _patch(Gtk, "stock_add", lambda items: None)

    # Widget

    _patch(Gtk.Widget, "window", property(fget=Gtk.Widget.get_window))

    _patch(Gtk, "widget_get_default_direction", Gtk.Widget.get_default_direction)
    orig_size_request = Gtk.Widget.size_request

    def size_request(widget):
        class SizeRequest(UserList):
            def __init__(self, req):
                self.height = req.height
                self.width = req.width
                UserList.__init__(self, [self.width, self.height])
        return SizeRequest(orig_size_request(widget))
    _patch(Gtk.Widget, "size_request", size_request)
    _patch(Gtk.Widget, "hide_all", Gtk.Widget.hide)

    class BaseGetter(object):
        def __init__(self, context):
            self.context = context

        def __getitem__(self, state):
            color = self.context.get_background_color(state)
            return Gdk.Color(red=int(color.red * 65535),
                             green=int(color.green * 65535),
                             blue=int(color.blue * 65535))

    class Styles(object):
        def __init__(self, widget):
            context = widget.get_style_context()
            self.base = BaseGetter(context)
            self.black = Gdk.Color(red=0, green=0, blue=0)

    class StyleDescriptor(object):
        def __get__(self, instance, class_):
            return Styles(instance)
    _patch(Gtk.Widget, "style", StyleDescriptor())

    # TextView

    orig_text_view_scroll_to_mark = Gtk.TextView.scroll_to_mark

    def text_view_scroll_to_mark(self, mark, within_margin,
                                 use_align=False, xalign=0.5, yalign=0.5):
        return orig_text_view_scroll_to_mark(self, mark, within_margin,
                                             use_align, xalign, yalign)
    _patch(Gtk.TextView, "scroll_to_mark", text_view_scroll_to_mark)

    # Window

    orig_set_geometry_hints = Gtk.Window.set_geometry_hints

    def set_geometry_hints(self, geometry_widget=None,
                           min_width=-1, min_height=-1, max_width=-1, max_height=-1,
                           base_width=-1, base_height=-1, width_inc=-1, height_inc=-1,
                           min_aspect=-1.0, max_aspect=-1.0):

        geometry = Gdk.Geometry()
        geom_mask = Gdk.WindowHints(0)

        if min_width >= 0 or min_height >= 0:
            geometry.min_width = max(min_width, 0)
            geometry.min_height = max(min_height, 0)
            geom_mask |= Gdk.WindowHints.MIN_SIZE

        if max_width >= 0 or max_height >= 0:
            geometry.max_width = max(max_width, 0)
            geometry.max_height = max(max_height, 0)
            geom_mask |= Gdk.WindowHints.MAX_SIZE

        if base_width >= 0 or base_height >= 0:
            geometry.base_width = max(base_width, 0)
            geometry.base_height = max(base_height, 0)
            geom_mask |= Gdk.WindowHints.BASE_SIZE

        if width_inc >= 0 or height_inc >= 0:
            geometry.width_inc = max(width_inc, 0)
            geometry.height_inc = max(height_inc, 0)
            geom_mask |= Gdk.WindowHints.RESIZE_INC

        if min_aspect >= 0.0 or max_aspect >= 0.0:
            if min_aspect <= 0.0 or max_aspect <= 0.0:
                raise TypeError("aspect ratios must be positive")

            geometry.min_aspect = min_aspect
            geometry.max_aspect = max_aspect
            geom_mask |= Gdk.WindowHints.ASPECT

        return orig_set_geometry_hints(self, geometry_widget, geometry, geom_mask)

    _patch(Gtk.Window, "set_geometry_hints", set_geometry_hints)
    _patch(Gtk, "window_list_toplevels", Gtk.Window.list_toplevels)
    _patch(Gtk, "window_set_default_icon_name", Gtk.Window.set_default_icon_name)

    # gtk.unixprint

    class UnixPrint(object):
        pass
    unixprint = UnixPrint()
    _patch_module('gtkunixprint', unixprint)

    # gtk.keysyms

    with warnings.catch_warnings():
        warnings.simplefilter('ignore', category=RuntimeWarning)
        from gi.overrides import keysyms

    _patch_module('gtk.keysyms', keysyms)
    _patch(Gtk, "keysyms", keysyms)

    from . import generictreemodel
    _patch(Gtk, "GenericTreeModel", generictreemodel.GenericTreeModel)


def enable_vte():
    if _check_enabled("vte"):
        return

    gi.require_version('Vte', '0.0')
    from gi.repository import Vte
    _patch_module('vte', Vte)


def enable_poppler():
    if _check_enabled("poppler"):
        return

    gi.require_version('Poppler', '0.18')
    from gi.repository import Poppler
    _patch_module('poppler', Poppler)

    _patch(Poppler, "pypoppler_version", (1, 0, 0))


def enable_webkit(version='1.0'):
    if _check_enabled("webkit", version):
        return

    gi.require_version('WebKit', version)
    from gi.repository import WebKit
    _patch_module('webkit', WebKit)

    _patch(WebKit.WebView, "get_web_inspector", WebKit.WebView.get_inspector)


def enable_gudev():
    if _check_enabled("gudev"):
        return

    gi.require_version('GUdev', '1.0')
    from gi.repository import GUdev
    _patch_module('gudev', GUdev)


def enable_gst():
    if _check_enabled("gst"):
        return

    gi.require_version('Gst', '0.10')
    from gi.repository import Gst
    _patch_module('gst', Gst)
    _install_enums(Gst)

    _patch(Gst, "registry_get_default", Gst.Registry.get_default)
    _patch(Gst, "element_register", Gst.Element.register)
    _patch(Gst, "element_factory_make", Gst.ElementFactory.make)
    _patch(Gst, "caps_new_any", Gst.Caps.new_any)
    _patch(Gst, "get_pygst_version", lambda: (0, 10, 19))
    _patch(Gst, "get_gst_version", lambda: (0, 10, 40))

    from gi.repository import GstInterfaces
    _patch_module('gst.interfaces', GstInterfaces)
    _install_enums(GstInterfaces)

    from gi.repository import GstAudio
    _patch_module('gst.audio', GstAudio)
    _install_enums(GstAudio)

    from gi.repository import GstVideo
    _patch_module('gst.video', GstVideo)
    _install_enums(GstVideo)

    from gi.repository import GstBase
    _patch_module('gst.base', GstBase)
    _install_enums(GstBase)

    _patch(Gst, "BaseTransform", GstBase.BaseTransform)
    _patch(Gst, "BaseSink", GstBase.BaseSink)

    from gi.repository import GstController
    _patch_module('gst.controller', GstController)
    _install_enums(GstController, dest=Gst)

    from gi.repository import GstPbutils
    _patch_module('gst.pbutils', GstPbutils)
    _install_enums(GstPbutils)


def enable_goocanvas():
    if _check_enabled("goocanvas"):
        return

    gi.require_version('GooCanvas', '2.0')
    from gi.repository import GooCanvas
    _patch_module('goocanvas', GooCanvas)
    _install_enums(GooCanvas, strip='GOO_CANVAS_')

    _patch(GooCanvas, "ItemSimple", GooCanvas.CanvasItemSimple)
    _patch(GooCanvas, "Item", GooCanvas.CanvasItem)
    _patch(GooCanvas, "Image", GooCanvas.CanvasImage)
    _patch(GooCanvas, "Group", GooCanvas.CanvasGroup)
    _patch(GooCanvas, "Rect", GooCanvas.CanvasRect)
