# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
#
# Copyright (C) 2014 Simon Feltman <sfeltman@gnome.org>
#
#   _error.py: GError Python implementation
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


# NOTE: This file should not have any dependencies on introspection libs
# like gi.repository.GLib because it would cause a circular dependency.
# Developers wanting to use the GError class in their applications should
# use gi.repository.GLib.GError


class GError(RuntimeError):
    def __init__(self, message='unknown error', domain='pygi-error', code=0):
        super(GError, self).__init__(message)
        self.message = message
        self.domain = domain
        self.code = code

    def __str__(self):
        return "%s: %s (%d)" % (self.domain, self.message, self.code)

    def __repr__(self):
        return "%s.%s('%s', '%s', %d)" % (
            GError.__module__.rsplit(".", 1)[-1], GError.__name__,
            self.message, self.domain, self.code)

    def copy(self):
        return GError(self.message, self.domain, self.code)

    def matches(self, domain, code):
        """Placeholder that will be monkey patched in GLib overrides."""
        raise NotImplementedError

    @staticmethod
    def new_literal(domain, message, code):
        """Placeholder that will be monkey patched in GLib overrides."""
        raise NotImplementedError
