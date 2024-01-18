# -*- Mode: Python; py-indent-offset: 4 -*-
# pygobject - Python bindings for the GObject library
# Copyright (C) 2006-2007 Johan Dahlin
#
#   gi/_constants.py: GObject type constants
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
# License along with this library; if not, see <http://www.gnu.org/licenses/>.

from . import _gi

TYPE_INVALID = _gi.TYPE_INVALID
TYPE_NONE = _gi.GType.from_name('void')
TYPE_INTERFACE = _gi.GType.from_name('GInterface')
TYPE_CHAR = _gi.GType.from_name('gchar')
TYPE_UCHAR = _gi.GType.from_name('guchar')
TYPE_BOOLEAN = _gi.GType.from_name('gboolean')
TYPE_INT = _gi.GType.from_name('gint')
TYPE_UINT = _gi.GType.from_name('guint')
TYPE_LONG = _gi.GType.from_name('glong')
TYPE_ULONG = _gi.GType.from_name('gulong')
TYPE_INT64 = _gi.GType.from_name('gint64')
TYPE_UINT64 = _gi.GType.from_name('guint64')
TYPE_ENUM = _gi.GType.from_name('GEnum')
TYPE_FLAGS = _gi.GType.from_name('GFlags')
TYPE_FLOAT = _gi.GType.from_name('gfloat')
TYPE_DOUBLE = _gi.GType.from_name('gdouble')
TYPE_STRING = _gi.GType.from_name('gchararray')
TYPE_POINTER = _gi.GType.from_name('gpointer')
TYPE_BOXED = _gi.GType.from_name('GBoxed')
TYPE_PARAM = _gi.GType.from_name('GParam')
TYPE_OBJECT = _gi.GType.from_name('GObject')
TYPE_PYOBJECT = _gi.GType.from_name('PyObject')
TYPE_GTYPE = _gi.GType.from_name('GType')
TYPE_STRV = _gi.GType.from_name('GStrv')
TYPE_VARIANT = _gi.GType.from_name('GVariant')
TYPE_UNICHAR = TYPE_UINT
