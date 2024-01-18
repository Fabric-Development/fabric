# Copyright 2017 Christoph Reiter
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

from __future__ import print_function

import os
import socket
import signal
import threading
from contextlib import closing, contextmanager

from . import _gi


def ensure_socket_not_inheritable(sock):
    """Ensures that the socket is not inherited by child processes

    Raises:
        EnvironmentError
        NotImplementedError: With Python <3.4 on Windows
    """

    if hasattr(sock, "set_inheritable"):
        sock.set_inheritable(False)
    else:
        try:
            import fcntl
        except ImportError:
            raise NotImplementedError(
                "Not implemented for older Python on Windows")
        else:
            fd = sock.fileno()
            flags = fcntl.fcntl(fd, fcntl.F_GETFD)
            fcntl.fcntl(fd, fcntl.F_SETFD, flags | fcntl.FD_CLOEXEC)


_wakeup_fd_is_active = False
"""Since we can't check if set_wakeup_fd() is already used for nested event
loops without introducing a race condition we keep track of it globally.
"""


@contextmanager
def wakeup_on_signal():
    """A decorator for functions which create a glib event loop to keep
    Python signal handlers working while the event loop is idling.

    In case an OS signal is received will wake the default event loop up
    shortly so that any registered Python signal handlers registered through
    signal.signal() can run.

    In case the wrapped function is not called from the main thread it will be
    called as is and it will not wake up the default loop for signals.
    """

    global _wakeup_fd_is_active

    if _wakeup_fd_is_active:
        yield
        return

    from gi.repository import GLib

    read_socket, write_socket = socket.socketpair()
    with closing(read_socket), closing(write_socket):

        for sock in [read_socket, write_socket]:
            sock.setblocking(False)
            ensure_socket_not_inheritable(sock)

        try:
            orig_fd = signal.set_wakeup_fd(write_socket.fileno())
        except ValueError:
            # Raised in case this is not the main thread -> give up.
            yield
            return
        else:
            _wakeup_fd_is_active = True

        def signal_notify(source, condition):
            if condition & GLib.IO_IN:
                try:
                    return bool(read_socket.recv(1))
                except EnvironmentError as e:
                    print(e)
                    return False
                return True
            else:
                return False

        try:
            if os.name == "nt":
                channel = GLib.IOChannel.win32_new_socket(
                    read_socket.fileno())
            else:
                channel = GLib.IOChannel.unix_new(read_socket.fileno())

            source_id = GLib.io_add_watch(
                channel,
                GLib.PRIORITY_DEFAULT,
                (GLib.IOCondition.IN | GLib.IOCondition.HUP |
                 GLib.IOCondition.NVAL | GLib.IOCondition.ERR),
                signal_notify)
            try:
                yield
            finally:
                GLib.source_remove(source_id)
        finally:
            write_fd = signal.set_wakeup_fd(orig_fd)
            if write_fd != write_socket.fileno():
                # Someone has called set_wakeup_fd while func() was active,
                # so let's re-revert again.
                signal.set_wakeup_fd(write_fd)
            _wakeup_fd_is_active = False


PyOS_getsig = _gi.pyos_getsig

# We save the signal pointer so we can detect if glib has changed the
# signal handler behind Python's back (GLib.unix_signal_add)
if signal.getsignal(signal.SIGINT) is signal.default_int_handler:
    startup_sigint_ptr = PyOS_getsig(signal.SIGINT)
else:
    # Something has set the handler before import, we can't get a ptr
    # for the default handler so make sure the pointer will never match.
    startup_sigint_ptr = -1


def sigint_handler_is_default():
    """Returns if on SIGINT the default Python handler would be called"""

    return (signal.getsignal(signal.SIGINT) is signal.default_int_handler and
            PyOS_getsig(signal.SIGINT) == startup_sigint_ptr)


@contextmanager
def sigint_handler_set_and_restore_default(handler):
    """Context manager for saving/restoring the SIGINT handler default state.

    Will only restore the default handler again if the handler is not changed
    while the context is active.
    """

    assert sigint_handler_is_default()

    signal.signal(signal.SIGINT, handler)
    sig_ptr = PyOS_getsig(signal.SIGINT)
    try:
        yield
    finally:
        if signal.getsignal(signal.SIGINT) is handler and \
                PyOS_getsig(signal.SIGINT) == sig_ptr:
            signal.signal(signal.SIGINT, signal.default_int_handler)


def is_main_thread():
    """Returns True in case the function is called from the main thread"""

    return threading.current_thread().name == "MainThread"


_callback_stack = []
_sigint_called = False


@contextmanager
def register_sigint_fallback(callback):
    """Installs a SIGINT signal handler in case the default Python one is
    active which calls 'callback' in case the signal occurs.

    Only does something if called from the main thread.

    In case of nested context managers the signal handler will be only
    installed once and the callbacks will be called in the reverse order
    of their registration.

    The old signal handler will be restored in case no signal handler is
    registered while the context is active.
    """

    # To handle multiple levels of event loops we need to call the last
    # callback first, wait until the inner most event loop returns control
    # and only then call the next callback, and so on... until we
    # reach the outer most which manages the signal handler and raises
    # in the end

    global _callback_stack, _sigint_called

    if not is_main_thread():
        yield
        return

    if not sigint_handler_is_default():
        if _callback_stack:
            # This is an inner event loop, append our callback
            # to the stack so the parent context can call it.
            _callback_stack.append(callback)
            try:
                yield
            finally:
                cb = _callback_stack.pop()
                if _sigint_called:
                    cb()
        else:
            # There is a signal handler set by the user, just do nothing
            yield
        return

    _sigint_called = False

    def sigint_handler(sig_num, frame):
        global _callback_stack, _sigint_called

        if _sigint_called:
            return
        _sigint_called = True
        _callback_stack.pop()()

    _callback_stack.append(callback)
    try:
        with sigint_handler_set_and_restore_default(sigint_handler):
            yield
    finally:
        if _sigint_called:
            signal.default_int_handler(signal.SIGINT, None)
        else:
            _callback_stack.pop()
