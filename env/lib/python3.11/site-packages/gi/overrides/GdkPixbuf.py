# Copyright 2018 Christoph Reiter <reiter.christoph@gmail.com>
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

from gi import PyGIDeprecationWarning
from gi.repository import GLib

from ..overrides import override
from ..module import get_introspection_module


GdkPixbuf = get_introspection_module('GdkPixbuf')
__all__ = []


@override
class Pixbuf(GdkPixbuf.Pixbuf):

    @classmethod
    def new_from_data(
            cls, data, colorspace, has_alpha, bits_per_sample,
            width, height, rowstride,
            destroy_fn=None, *destroy_fn_data):

        if destroy_fn is not None:
            w = PyGIDeprecationWarning("destroy_fn argument deprecated")
            warnings.warn(w)
        if destroy_fn_data:
            w = PyGIDeprecationWarning("destroy_fn_data argument deprecated")
            warnings.warn(w)

        data = GLib.Bytes.new(data)
        return cls.new_from_bytes(
            data, colorspace, has_alpha, bits_per_sample,
            width, height, rowstride)


__all__.append('Pixbuf')
