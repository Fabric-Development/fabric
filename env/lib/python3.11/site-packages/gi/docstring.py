# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
#
# Copyright (C) 2013 Simon Feltman <sfeltman@gnome.org>
#
#   docstring.py: documentation string generator for gi.
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

from ._gi import \
    VFuncInfo, \
    FunctionInfo, \
    CallableInfo, \
    ObjectInfo, \
    StructInfo, \
    Direction, \
    TypeTag


#: Module storage for currently registered doc string generator function.
_generate_doc_string_func = None


def set_doc_string_generator(func):
    """Set doc string generator function

    :param callable func:
        Callable which takes a GIInfoStruct and returns documentation for it.
    """
    global _generate_doc_string_func
    _generate_doc_string_func = func


def get_doc_string_generator():
    """Returns the currently registered doc string generator."""
    return _generate_doc_string_func


def generate_doc_string(info):
    """Generate a doc string given a GIInfoStruct.

    :param gi.types.BaseInfo info:
        GI info instance to generate documentation for.
    :returns:
        Generated documentation as a string.
    :rtype: str

    This passes the info struct to the currently registered doc string
    generator and returns the result.
    """
    return _generate_doc_string_func(info)


_type_tag_to_py_type = {TypeTag.BOOLEAN: bool,
                        TypeTag.INT8: int,
                        TypeTag.UINT8: int,
                        TypeTag.INT16: int,
                        TypeTag.UINT16: int,
                        TypeTag.INT32: int,
                        TypeTag.UINT32: int,
                        TypeTag.INT64: int,
                        TypeTag.UINT64: int,
                        TypeTag.FLOAT: float,
                        TypeTag.DOUBLE: float,
                        TypeTag.GLIST: list,
                        TypeTag.GSLIST: list,
                        TypeTag.ARRAY: list,
                        TypeTag.GHASH: dict,
                        TypeTag.UTF8: str,
                        TypeTag.FILENAME: str,
                        TypeTag.UNICHAR: str,
                        TypeTag.INTERFACE: None,
                        TypeTag.GTYPE: None,
                        TypeTag.ERROR: None,
                        TypeTag.VOID: None,
                        }


def _get_pytype_hint(gi_type):
    type_tag = gi_type.get_tag()
    py_type = _type_tag_to_py_type.get(type_tag, None)

    if py_type and hasattr(py_type, '__name__'):
        return py_type.__name__
    elif type_tag == TypeTag.INTERFACE:
        iface = gi_type.get_interface()

        info_name = iface.get_name()
        if not info_name:
            return gi_type.get_tag_as_string()

        return '%s.%s' % (iface.get_namespace(), info_name)

    return gi_type.get_tag_as_string()


def _generate_callable_info_doc(info):
    in_args_strs = []
    if isinstance(info, VFuncInfo):
        in_args_strs = ['self']
    elif isinstance(info, FunctionInfo):
        if info.is_method():
            in_args_strs = ['self']

    args = info.get_arguments()
    hint_blacklist = ('void',)

    # Build lists of indices prior to adding the docs because it is possible
    # the index retrieved comes before input arguments being used.
    ignore_indices = {info.get_return_type().get_array_length()}
    user_data_indices = set()
    for arg in args:
        ignore_indices.add(arg.get_destroy())
        ignore_indices.add(arg.get_type().get_array_length())
        user_data_indices.add(arg.get_closure())

    # Build input argument strings
    for i, arg in enumerate(args):
        if arg.get_direction() == Direction.OUT:
            continue  # skip exclusively output args
        if i in ignore_indices:
            continue
        argstr = arg.get_name()
        hint = _get_pytype_hint(arg.get_type())
        if hint not in hint_blacklist:
            argstr += ':' + hint
        if arg.may_be_null() or i in user_data_indices:
            # allow-none or user_data from a closure
            argstr += '=None'
        elif arg.is_optional():
            argstr += '=<optional>'
        in_args_strs.append(argstr)
    in_args_str = ', '.join(in_args_strs)

    # Build return + output argument strings
    out_args_strs = []
    return_hint = _get_pytype_hint(info.get_return_type())
    if not info.skip_return() and return_hint and return_hint not in hint_blacklist:
        argstr = return_hint
        if info.may_return_null():
            argstr += ' or None'
        out_args_strs.append(argstr)

    for i, arg in enumerate(args):
        if arg.get_direction() == Direction.IN:
            continue  # skip exclusively input args
        if i in ignore_indices:
            continue
        argstr = arg.get_name()
        hint = _get_pytype_hint(arg.get_type())
        if hint not in hint_blacklist:
            argstr += ':' + hint
        out_args_strs.append(argstr)

    if out_args_strs:
        return '%s(%s) -> %s' % (info.__name__, in_args_str, ', '.join(out_args_strs))
    else:
        return '%s(%s)' % (info.__name__, in_args_str)


def _generate_class_info_doc(info):
    header = '\n:Constructors:\n\n::\n\n'  # start with \n to avoid auto indent of other lines
    doc = ''

    if isinstance(info, StructInfo):
        # Don't show default constructor for disguised (0 length) structs
        if info.get_size() > 0:
            doc += '    ' + info.get_name() + '()\n'
    else:
        doc += '    ' + info.get_name() + '(**properties)\n'

    for method_info in info.get_methods():
        if method_info.is_constructor():
            doc += '    ' + _generate_callable_info_doc(method_info) + '\n'

    if doc:
        return header + doc
    else:
        return ''


def _generate_doc_dispatch(info):
    if isinstance(info, (ObjectInfo, StructInfo)):
        return _generate_class_info_doc(info)

    elif isinstance(info, CallableInfo):
        return _generate_callable_info_doc(info)

    return ''


set_doc_string_generator(_generate_doc_dispatch)
