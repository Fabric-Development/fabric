# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
#
# Copyright (C) 2010 Simon van der Linden <svdlinden@src.gnome.org>
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

from ..overrides import override
from ..module import get_introspection_module

GIMarshallingTests = get_introspection_module('GIMarshallingTests')

__all__ = []

OVERRIDES_CONSTANT = 7
__all__.append('OVERRIDES_CONSTANT')


class OverridesStruct(GIMarshallingTests.OverridesStruct):

    def __new__(cls, long_):
        return GIMarshallingTests.OverridesStruct.__new__(cls)

    def __init__(self, long_):
        GIMarshallingTests.OverridesStruct.__init__(self)
        self.long_ = long_

    def method(self):
        return GIMarshallingTests.OverridesStruct.method(self) / 7


OverridesStruct = override(OverridesStruct)
__all__.append('OverridesStruct')


class OverridesObject(GIMarshallingTests.OverridesObject):

    def __new__(cls, long_):
        return GIMarshallingTests.OverridesObject.__new__(cls)

    def __init__(self, long_):
        GIMarshallingTests.OverridesObject.__init__(self)
        # FIXME: doesn't work yet
        # self.long_ = long_

    @classmethod
    def new(cls, long_):
        self = GIMarshallingTests.OverridesObject.new()
        # FIXME: doesn't work yet
        # self.long_ = long_
        return self

    def method(self):
        """Overridden doc string."""
        return GIMarshallingTests.OverridesObject.method(self) / 7


OverridesObject = override(OverridesObject)
__all__.append('OverridesObject')
