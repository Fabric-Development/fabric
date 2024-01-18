from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Protocol
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from enum import Enum
from enum import Flag

from gi.repository import GLib

_T = TypeVar("_T")

G_MAXDOUBLE: float = 1.7976931348623157e308
G_MAXFLOAT: float = 3.4028234663852886e38
G_MAXINT: int = 2147483647
G_MAXINT16: int = 32767
G_MAXINT32: int = 2147483647
G_MAXINT64: int = 9223372036854775807
G_MAXINT8: int = 127
G_MAXLONG: int = 9223372036854775807
G_MAXOFFSET: int = 9223372036854775807
G_MAXSHORT: int = 32767
G_MAXSIZE: int = 18446744073709551615
G_MAXSSIZE: int = 9223372036854775807
G_MAXUINT: int = 4294967295
G_MAXUINT16: int = 65535
G_MAXUINT32: int = 4294967295
G_MAXUINT64: int = 18446744073709551615
G_MAXUINT8: int = 255
G_MAXULONG: int = 18446744073709551615
G_MAXUSHORT: int = 65535
G_MINDOUBLE: float = 2.2250738585072014e-308
G_MINFLOAT: float = 1.1754943508222875e-38
G_MININT: int = -2147483648
G_MININT16: int = -32768
G_MININT32: int = -2147483648
G_MININT64: int = -9223372036854775808
G_MININT8: int = -128
G_MINLONG: int = -9223372036854775808
G_MINOFFSET: int = -9223372036854775808
G_MINSHORT: int = -32768
G_MINSSIZE: int = -9223372036854775808
IO_ERR: int = 8
IO_FLAG_APPEND: int = 1
IO_FLAG_GET_MASK: int = 31
IO_FLAG_IS_READABLE: int = 4
IO_FLAG_IS_SEEKABLE: int = 16
IO_FLAG_IS_WRITEABLE: int = 8
IO_FLAG_MASK: int = 31
IO_FLAG_NONBLOCK: int = 2
IO_FLAG_SET_MASK: int = 3
IO_HUP: int = 16
IO_IN: int = 1
IO_NVAL: int = 32
IO_OUT: int = 4
IO_PRI: int = 2
IO_STATUS_AGAIN: int = 3
IO_STATUS_EOF: int = 2
IO_STATUS_ERROR: int = 0
IO_STATUS_NORMAL: int = 1
OPTION_ERROR_BAD_VALUE: int = 1
OPTION_ERROR_FAILED: int = 2
OPTION_ERROR_UNKNOWN_OPTION: int = 0
OPTION_FLAG_FILENAME: int = 16
OPTION_FLAG_HIDDEN: int = 1
OPTION_FLAG_IN_MAIN: int = 2
OPTION_FLAG_NOALIAS: int = 64
OPTION_FLAG_NO_ARG: int = 8
OPTION_FLAG_OPTIONAL_ARG: int = 32
OPTION_FLAG_REVERSE: int = 4
OPTION_REMAINING: str = ""
PARAM_CONSTRUCT: int = 4
PARAM_CONSTRUCT_ONLY: int = 8
PARAM_LAX_VALIDATION: int = 16
PARAM_MASK: int = 255
PARAM_READABLE: int = 1
PARAM_READWRITE: int = 3
PARAM_STATIC_STRINGS: int = 224
PARAM_USER_SHIFT: int = 8
PARAM_WRITABLE: int = 2
PRIORITY_DEFAULT: int = 0
PRIORITY_DEFAULT_IDLE: int = 200
PRIORITY_HIGH: int = -100
PRIORITY_HIGH_IDLE: int = 100
PRIORITY_LOW: int = 300
SIGNAL_ACTION: int = 32
SIGNAL_DETAILED: int = 16
SIGNAL_FLAGS_MASK: int = 511
SIGNAL_MATCH_MASK: int = 63
SIGNAL_NO_HOOKS: int = 64
SIGNAL_NO_RECURSE: int = 8
SIGNAL_RUN_CLEANUP: int = 4
SIGNAL_RUN_FIRST: int = 1
SIGNAL_RUN_LAST: int = 2
SPAWN_CHILD_INHERITS_STDIN: int = 32
SPAWN_DO_NOT_REAP_CHILD: int = 2
SPAWN_FILE_AND_ARGV_ZERO: int = 64
SPAWN_LEAVE_DESCRIPTORS_OPEN: int = 1
SPAWN_SEARCH_PATH: int = 4
SPAWN_STDERR_TO_DEV_NULL: int = 16
SPAWN_STDOUT_TO_DEV_NULL: int = 8
TYPE_BOOLEAN = ...  # FIXME Constant
TYPE_BOXED = ...  # FIXME Constant
TYPE_CHAR = ...  # FIXME Constant
TYPE_DOUBLE = ...  # FIXME Constant
TYPE_ENUM = ...  # FIXME Constant
TYPE_FLAGS = ...  # FIXME Constant
TYPE_FLAG_RESERVED_ID_BIT: int = 1
TYPE_FLOAT = ...  # FIXME Constant
TYPE_FUNDAMENTAL_MAX: int = 255
TYPE_FUNDAMENTAL_SHIFT: int = 2
TYPE_GSTRING = ...  # FIXME Constant
TYPE_GTYPE = ...  # FIXME Constant
TYPE_INT = ...  # FIXME Constant
TYPE_INT64 = ...  # FIXME Constant
TYPE_INTERFACE = ...  # FIXME Constant
TYPE_INVALID = ...  # FIXME Constant
TYPE_LONG = ...  # FIXME Constant
TYPE_NONE = ...  # FIXME Constant
TYPE_OBJECT = ...  # FIXME Constant
TYPE_PARAM = ...  # FIXME Constant
TYPE_POINTER = ...  # FIXME Constant
TYPE_PYOBJECT = ...  # FIXME Constant
TYPE_RESERVED_BSE_FIRST: int = 32
TYPE_RESERVED_BSE_LAST: int = 48
TYPE_RESERVED_GLIB_FIRST: int = 22
TYPE_RESERVED_GLIB_LAST: int = 31
TYPE_RESERVED_USER_FIRST: int = 49
TYPE_STRING = ...  # FIXME Constant
TYPE_STRV = ...  # FIXME Constant
TYPE_UCHAR = ...  # FIXME Constant
TYPE_UINT = ...  # FIXME Constant
TYPE_UINT64 = ...  # FIXME Constant
TYPE_ULONG = ...  # FIXME Constant
TYPE_UNICHAR = ...  # FIXME Constant
TYPE_VALUE = ...  # FIXME Constant
TYPE_VARIANT = ...  # FIXME Constant
VALUE_INTERNED_STRING: int = 268435456
VALUE_NOCOPY_CONTENTS: int = 134217728
_introspection_module = ...  # FIXME Constant
_lock = ...  # FIXME Constant
_namespace: str = "GObject"
_overrides_module = ...  # FIXME Constant
_version: str = "2.0"
features = ...  # FIXME Constant
glib_version = ...  # FIXME Constant
# override
pygobject_version: tuple[int, int, int, int, int] = ...

def add_emission_hook(*args, **kwargs): ...  # FIXME Function
def boxed_copy(boxed_type: Type, src_boxed: None) -> None: ...
def boxed_free(boxed_type: Type, boxed: None) -> None: ...
def cclosure_marshal_BOOLEAN__BOXED_BOXED(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_BOOLEAN__FLAGS(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_STRING__OBJECT_POINTER(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__BOOLEAN(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__BOXED(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__CHAR(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__DOUBLE(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__ENUM(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__FLAGS(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__FLOAT(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__INT(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__LONG(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__OBJECT(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__PARAM(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__POINTER(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__STRING(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__UCHAR(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__UINT(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__UINT_POINTER(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__ULONG(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__VARIANT(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__VOID(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_generic(
    closure: Callable[..., Any],
    return_gvalue: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def child_watch_add(*args, **kwargs): ...  # FIXME Function
def clear_signal_handler(handler_id_ptr: int, instance: Object) -> None: ...
def enum_complete_type_info(g_enum_type: Type, const_values: EnumValue) -> TypeInfo: ...
def enum_get_value(enum_class: EnumClass, value: int) -> Optional[EnumValue]: ...
def enum_get_value_by_name(enum_class: EnumClass, name: str) -> Optional[EnumValue]: ...
def enum_get_value_by_nick(enum_class: EnumClass, nick: str) -> Optional[EnumValue]: ...
def enum_register_static(name: str, const_static_values: EnumValue) -> Type: ...
def enum_to_string(g_enum_type: Type, value: int) -> str: ...
def filename_display_basename(filename: str) -> str: ...
def filename_display_name(filename: str) -> str: ...
def filename_from_utf8(utf8string, len=-1): ...  # FIXME Function
def flags_complete_type_info(
    g_flags_type: Type, const_values: FlagsValue
) -> TypeInfo: ...
def flags_get_first_value(
    flags_class: FlagsClass, value: int
) -> Optional[FlagsValue]: ...
def flags_get_value_by_name(
    flags_class: FlagsClass, name: str
) -> Optional[FlagsValue]: ...
def flags_get_value_by_nick(
    flags_class: FlagsClass, nick: str
) -> Optional[FlagsValue]: ...
def flags_register_static(name: str, const_static_values: FlagsValue) -> Type: ...
def flags_to_string(flags_type: Type, value: int) -> str: ...
def get_application_name() -> Optional[str]: ...
def get_current_time(): ...  # FIXME Function
def get_prgname() -> Optional[str]: ...
def gtype_get_type() -> Type: ...
def idle_add(function, *user_data, **kwargs): ...  # FIXME Function
def io_add_watch(*args, **kwargs): ...  # FIXME Function
def list_properties(*args, **kwargs): ...  # FIXME Function
def main_context_default() -> GLib.MainContext: ...
def main_depth() -> int: ...
def markup_escape_text(text, length=-1): ...  # FIXME Function
def new(*args, **kwargs): ...  # FIXME Function
def param_spec_boolean(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    default_value: bool,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_boxed(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    boxed_type: Type,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_char(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_double(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    minimum: float,
    maximum: float,
    default_value: float,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_enum(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    enum_type: Type,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_flags(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    flags_type: Type,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_float(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    minimum: float,
    maximum: float,
    default_value: float,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_gtype(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    is_a_type: Type,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_int(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_int64(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_long(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_object(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    object_type: Type,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_param(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    param_type: Type,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_pointer(
    name: str, nick: Optional[str], blurb: Optional[str], flags: ParamFlags
) -> ParamSpec: ...
def param_spec_string(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    default_value: Optional[str],
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_uchar(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_uint(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_uint64(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_ulong(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_unichar(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    default_value: str,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_variant(
    name: str,
    nick: Optional[str],
    blurb: Optional[str],
    type: GLib.VariantType,
    default_value: Optional[GLib.Variant],
    flags: ParamFlags,
) -> ParamSpec: ...
def param_type_register_static(name: str, pspec_info: ParamSpecTypeInfo) -> Type: ...
def param_value_convert(
    pspec: ParamSpec, src_value: Any, dest_value: Any, strict_validation: bool
) -> bool: ...
def param_value_defaults(pspec: ParamSpec, value: Any) -> bool: ...
def param_value_is_valid(pspec: ParamSpec, value: Any) -> bool: ...
def param_value_set_default(pspec: ParamSpec, value: Any) -> None: ...
def param_value_validate(pspec: ParamSpec, value: Any) -> bool: ...
def param_values_cmp(pspec: ParamSpec, value1: Any, value2: Any) -> int: ...
def pointer_type_register_static(name: str) -> Type: ...
def remove_emission_hook(obj, detailed_signal, hook_id): ...  # FIXME Function
def set_application_name(application_name: str) -> None: ...
def set_prgname(prgname: str) -> None: ...
def signal_accumulator_first_wins(
    ihint, return_accu, handler_return, user_data=None
): ...  # FIXME Function
def signal_accumulator_true_handled(
    ihint, return_accu, handler_return, user_data=None
): ...  # FIXME Function
def signal_add_emission_hook(
    signal_id: int, detail: int, hook_func: Callable[..., bool], *hook_data: Any
) -> int: ...
def signal_chain_from_overridden(
    instance_and_params: Sequence[Any], return_value: Any
) -> None: ...
def signal_connect_closure(
    instance: Object, detailed_signal: str, closure: Callable[..., Any], after: bool
) -> int: ...
def signal_connect_closure_by_id(
    instance: Object,
    signal_id: int,
    detail: int,
    closure: Callable[..., Any],
    after: bool,
) -> int: ...
def signal_emitv(
    instance_and_params: Sequence[Any], signal_id: int, detail: int
) -> Any: ...
def signal_get_invocation_hint(instance: Object) -> Optional[SignalInvocationHint]: ...
def signal_handler_block(obj, handler_id): ...  # FIXME Function
def signal_handler_disconnect(instance: Object, handler_id: int) -> None: ...

# override
def signal_handler_find(
    instance: Object,
    mask: SignalMatchType,
    signal_id: int,
    detail: int,
    _closure: Optional[Callable[..., Any]],
    func: None,
    data: None,
    *closure: Any,
) -> int: ...
def signal_handler_is_connected(instance: Object, handler_id: int) -> bool: ...
def signal_handler_unblock(instance: Object, handler_id: int) -> None: ...

# override
def signal_handlers_block_matched(
    instance: Object,
    mask: SignalMatchType,
    signal_id: int,
    detail: int,
    _closure: Optional[Callable[..., Any]],
    func: None,
    data: None,
    *closure: Any,
) -> int: ...
def signal_handlers_destroy(instance: Object) -> None: ...

# override
def signal_handlers_disconnect_matched(
    instance: Object,
    mask: SignalMatchType,
    signal_id: int,
    detail: int,
    _closure: Optional[Callable[..., Any]],
    func: None,
    data: None,
    *closure: Any,
) -> int: ...

# override
def signal_handlers_unblock_matched(
    instance: Object,
    mask: SignalMatchType,
    signal_id: int,
    detail: int,
    _closure: Optional[Callable[..., Any]],
    func: None,
    data: None,
    *closure: Any,
) -> int: ...
def signal_has_handler_pending(
    instance: Object, signal_id: int, detail: int, may_be_blocked: bool
) -> bool: ...
def signal_is_valid_name(name: str) -> bool: ...
def signal_list_ids(type_): ...  # FIXME Function
def signal_list_names(type_): ...  # FIXME Function
def signal_lookup(name, type_): ...  # FIXME Function
def signal_name(signal_id: int) -> Optional[str]: ...
def signal_new(*args, **kwargs): ...  # FIXME Function
def signal_override_class_closure(
    signal_id: int, instance_type: Type, class_closure: Callable[..., Any]
) -> None: ...
def signal_parse_name(detailed_signal, itype, force_detail_quark): ...  # FIXME Function
def signal_query(id_or_name, type_=None): ...  # FIXME Function
def signal_remove_emission_hook(signal_id: int, hook_id: int) -> None: ...
def signal_set_va_marshaller(
    signal_id: int, instance_type: Type, va_marshaller: VaClosureMarshal
) -> None: ...
def signal_stop_emission(instance: Object, signal_id: int, detail: int) -> None: ...
def signal_stop_emission_by_name(instance: Object, detailed_signal: str) -> None: ...
def signal_type_cclosure_new(itype: Type, struct_offset: int) -> Callable[..., Any]: ...
def source_remove(tag: int) -> bool: ...
def source_set_closure(source: GLib.Source, closure: Callable[..., Any]) -> None: ...
def source_set_dummy_callback(source: GLib.Source) -> None: ...
def spawn_async(*args, **kwargs): ...  # FIXME Function
def strdup_value_contents(value: Any) -> str: ...
def threads_init(): ...  # FIXME Function
def timeout_add(interval, function, *user_data, **kwargs): ...  # FIXME Function
def timeout_add_seconds(interval, function, *user_data, **kwargs): ...  # FIXME Function
def type_add_class_private(class_type: Type, private_size: int) -> None: ...
def type_add_instance_private(class_type: Type, private_size: int) -> int: ...
def type_add_interface_dynamic(
    instance_type: Type, interface_type: Type, plugin: TypePlugin
) -> None: ...
def type_add_interface_static(
    instance_type: Type, interface_type: Type, info: InterfaceInfo
) -> None: ...
def type_check_class_is_a(g_class: TypeClass, is_a_type: Type) -> bool: ...
def type_check_instance(instance: TypeInstance) -> bool: ...
def type_check_instance_is_a(instance: TypeInstance, iface_type: Type) -> bool: ...
def type_check_instance_is_fundamentally_a(
    instance: TypeInstance, fundamental_type: Type
) -> bool: ...
def type_check_is_value_type(type: Type) -> bool: ...
def type_check_value(value: Any) -> bool: ...
def type_check_value_holds(value: Any, type: Type) -> bool: ...
def type_children(type: Type) -> list[Type]: ...
def type_class_adjust_private_offset(
    g_class: None, private_size_or_offset: int
) -> None: ...
def type_class_peek(type: Type) -> TypeClass: ...
def type_class_peek_static(type: Type) -> TypeClass: ...
def type_class_ref(type: Type) -> TypeClass: ...
def type_default_interface_peek(g_type: Type) -> TypeInterface: ...
def type_default_interface_ref(g_type: Type) -> TypeInterface: ...
def type_default_interface_unref(g_iface: TypeInterface) -> None: ...
def type_depth(type: Type) -> int: ...
def type_ensure(type: Type) -> None: ...
def type_free_instance(instance: TypeInstance) -> None: ...
def type_from_name(name): ...  # FIXME Function
def type_fundamental(type_id: Type) -> Type: ...
def type_fundamental_next() -> Type: ...
def type_get_instance_count(type: Type) -> int: ...
def type_get_plugin(type: Type) -> TypePlugin: ...
def type_get_qdata(type: Type, quark: int) -> None: ...
def type_get_type_registration_serial() -> int: ...
def type_init() -> None: ...
def type_init_with_debug_flags(debug_flags: TypeDebugFlags) -> None: ...
def type_interface_add_prerequisite(
    interface_type: Type, prerequisite_type: Type
) -> None: ...
def type_interface_get_plugin(
    instance_type: Type, interface_type: Type
) -> TypePlugin: ...
def type_interface_instantiatable_prerequisite(interface_type: Type) -> Type: ...
def type_interface_peek(
    instance_class: TypeClass, iface_type: Type
) -> TypeInterface: ...
def type_interface_prerequisites(interface_type: Type) -> list[Type]: ...
def type_interfaces(type: Type) -> list[Type]: ...
def type_is_a(type: Type, is_a_type: Type) -> bool: ...
def type_name(type: Type) -> Optional[str]: ...
def type_name_from_class(g_class: TypeClass) -> str: ...
def type_name_from_instance(instance: TypeInstance) -> str: ...
def type_next_base(leaf_type: Type, root_type: Type) -> Type: ...
def type_parent(type_): ...  # FIXME Function
def type_qname(type: Type) -> int: ...
def type_query(type: Type) -> TypeQuery: ...
def type_register(*args, **kwargs): ...  # FIXME Function
def type_register_dynamic(
    parent_type: Type, type_name: str, plugin: TypePlugin, flags: TypeFlags
) -> Type: ...
def type_register_fundamental(
    type_id: Type,
    type_name: str,
    info: TypeInfo,
    finfo: TypeFundamentalInfo,
    flags: TypeFlags,
) -> Type: ...
def type_register_static(
    parent_type: Type, type_name: str, info: TypeInfo, flags: TypeFlags
) -> Type: ...
def type_set_qdata(type: Type, quark: int, data: None) -> None: ...
def type_test_flags(type: Type, flags: int) -> bool: ...
def uri_list_extract_uris(uri_list: str) -> list[str]: ...
def value_type_compatible(src_type: Type, dest_type: Type) -> bool: ...
def value_type_transformable(src_type: Type, dest_type: Type) -> bool: ...

# override
class _HandlerBlockManager:
    def __init__(self, obj, handler_id: int) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

class Binding(Object):
    """
    :Constructors:

    ::

        Binding(**properties)

    Object GBinding

    Properties from GBinding:
      source -> GObject: Source
        The source of the binding
      target -> GObject: Target
        The target of the binding
      source-property -> gchararray: Source Property
        The property on the source to bind
      target-property -> gchararray: Target Property
        The property on the target to bind
      flags -> GBindingFlags: Flags
        The binding flags

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        flags: BindingFlags
        source: Optional[Object]
        source_property: str
        target: Optional[Object]
        target_property: str
    props: Props = ...
    def __init__(
        self,
        flags: BindingFlags = ...,
        source: Object = ...,
        source_property: str = ...,
        target: Object = ...,
        target_property: str = ...,
    ): ...
    def dup_source(self) -> Optional[Object]: ...
    def dup_target(self) -> Optional[Object]: ...
    def get_flags(self) -> BindingFlags: ...
    def get_source(self) -> Optional[Object]: ...
    def get_source_property(self) -> str: ...
    def get_target(self) -> Optional[Object]: ...
    def get_target_property(self) -> str: ...
    def unbind(self): ...  # FIXME Function

class BindingGroup(Object):
    """
    :Constructors:

    ::

        BindingGroup(**properties)
        new() -> GObject.BindingGroup

    Object GBindingGroup

    Properties from GBindingGroup:
      source -> GObject: Source
        The source GObject used for binding properties.

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        source: Optional[Object]
    props: Props = ...
    def __init__(self, source: Optional[Object] = ...): ...
    def bind(
        self,
        source_property: str,
        target: Object,
        target_property: str,
        flags: BindingFlags,
    ) -> None: ...
    def bind_full(
        self,
        source_property: str,
        target: Object,
        target_property: str,
        flags: BindingFlags,
        transform_to: Optional[Callable[..., Any]] = None,
        transform_from: Optional[Callable[..., Any]] = None,
    ) -> None: ...
    def dup_source(self) -> Optional[Object]: ...
    @classmethod
    def new(cls) -> BindingGroup: ...
    def set_source(self, source: Optional[Object] = None) -> None: ...

class CClosure(GPointer):
    """
    :Constructors:

    ::

        CClosure()
    """

    closure: Callable[..., Any] = ...
    callback: None = ...
    @staticmethod
    def marshal_BOOLEAN__BOXED_BOXED(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_BOOLEAN__FLAGS(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_STRING__OBJECT_POINTER(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__BOOLEAN(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__BOXED(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__CHAR(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__DOUBLE(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__ENUM(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__FLAGS(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__FLOAT(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__INT(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__LONG(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__OBJECT(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__PARAM(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__POINTER(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__STRING(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__UCHAR(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__UINT(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__UINT_POINTER(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__ULONG(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__VARIANT(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__VOID(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_generic(
        closure: Callable[..., Any],
        return_gvalue: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...

class Closure(GBoxed):
    """
    :Constructors:

    ::

        Closure()
        new_object(sizeof_closure:int, object:GObject.Object) -> GObject.Closure
        new_simple(sizeof_closure:int, data=None) -> GObject.Closure
    """

    ref_count: int = ...
    meta_marshal_nouse: int = ...
    n_guards: int = ...
    n_fnotifiers: int = ...
    n_inotifiers: int = ...
    in_inotify: int = ...
    floating: int = ...
    derivative_flag: int = ...
    in_marshal: int = ...
    is_invalid: int = ...
    marshal: Callable[[Callable[..., Any], Any, int, Any, None, None], None] = ...
    data: None = ...
    notifiers: ClosureNotifyData = ...
    def invalidate(self) -> None: ...
    def invoke(
        self, n_param_values: int, param_values: Sequence[Any], invocation_hint: None
    ) -> Any: ...
    @classmethod
    def new_object(cls, sizeof_closure: int, object: Object) -> Closure: ...
    @classmethod
    def new_simple(cls, sizeof_closure: int, data: None) -> Closure: ...
    def ref(self) -> Callable[..., Any]: ...
    def sink(self) -> None: ...
    def unref(self) -> None: ...

class ClosureNotifyData(GPointer):
    """
    :Constructors:

    ::

        ClosureNotifyData()
    """

    data: None = ...
    notify: Callable[[None, Callable[..., Any]], None] = ...

class EnumClass(GPointer):
    """
    :Constructors:

    ::

        EnumClass()
    """

    g_type_class: TypeClass = ...
    minimum: int = ...
    maximum: int = ...
    n_values: int = ...
    values: EnumValue = ...

class EnumValue(GPointer):
    """
    :Constructors:

    ::

        EnumValue()
    """

    value: int = ...
    value_name: str = ...
    value_nick: str = ...

class FlagsClass(GPointer):
    """
    :Constructors:

    ::

        FlagsClass()
    """

    g_type_class: TypeClass = ...
    mask: int = ...
    n_values: int = ...
    values: FlagsValue = ...

class FlagsValue(GPointer):
    """
    :Constructors:

    ::

        FlagsValue()
    """

    value: int = ...
    value_name: str = ...
    value_nick: str = ...

class GBoxed:
    """ """

    def copy(self, *args, **kwargs): ...  # FIXME Function

class GError:
    """ """

    def copy(self): ...  # FIXME Function
    def matches(self, domain, code): ...  # FIXME Function
    def new_literal(domain, message, code): ...  # FIXME Function

# override
class GInterface(Protocol):
    # Copy pasted from Object

    g_type_instance: TypeInstance = ...
    ref_count: int = ...
    qdata: GLib.Data = ...
    props = ...  # FIXME Constant

    # override
    def bind_property(
        self,
        source_property: str,
        target: Object,
        target_property: str,
        flags: BindingFlags = BindingFlags.DEFAULT,
        transform_to: Optional[Callable[..., Any]] = None,
        transform_from: Optional[Callable[..., Any]] = None,
        user_data: Optional[Any] = None,
    ) -> Binding: ...
    def bind_property_full(self, *args, **kargs): ...  # FIXME Function
    def chain(self, *args, **kwargs): ...  # FIXME Function
    def compat_control(self, *args, **kargs): ...  # FIXME Function
    # override
    def connect(
        self, detailed_signal: str, handler: Callable[..., Any], *args: Any
    ) -> int: ...
    # override
    def connect_after(
        self, detailed_signal: str, handler: Callable[..., Any], *args: Any
    ) -> int: ...
    def connect_data(
        self, detailed_signal, handler, *data, **kwargs
    ): ...  # FIXME Function
    def connect_object(self, *args, **kwargs): ...  # FIXME Function
    def connect_object_after(self, *args, **kwargs): ...  # FIXME Function
    # override
    def disconnect(self, id: int) -> None: ...
    def disconnect_by_func(self, *args, **kwargs): ...  # FIXME Function
    # override
    def emit(self, signal_name: str, *args: Any) -> None: ...
    def emit_stop_by_name(self, detailed_signal): ...  # FIXME Function
    def find_property(self, property_name: str) -> ParamSpec: ...
    def force_floating(self, *args, **kargs): ...  # FIXME Function
    def freeze_notify(self): ...  # FIXME Function
    def get_data(self, *args, **kargs): ...  # FIXME Function
    def get_properties(self, *args, **kwargs): ...  # FIXME Function
    # override
    def get_property(self, property_name: str) -> Any: ...
    def get_qdata(self, *args, **kargs): ...  # FIXME Function
    def getv(
        self, n_properties: int, names: Sequence[str], values: Sequence[Any]
    ) -> None: ...
    # override
    def handler_block(self, handler_id: int) -> _HandlerBlockManager: ...
    def handler_block_by_func(self, *args, **kwargs): ...  # FIXME Function
    def handler_disconnect(self, *args, **kwargs): ...  # FIXME Function
    # override
    def handler_is_connected(self, id: int) -> bool: ...
    def handler_unblock(self, *args, **kwargs): ...  # FIXME Function
    def handler_unblock_by_func(self, *args, **kwargs): ...  # FIXME Function
    def install_properties(
        self, n_pspecs: int, pspecs: Sequence[ParamSpec]
    ) -> None: ...
    def install_property(self, property_id: int, pspec: ParamSpec) -> None: ...
    def interface_find_property(self, *args, **kargs): ...  # FIXME Function
    def interface_install_property(self, *args, **kargs): ...  # FIXME Function
    def interface_list_properties(self, *args, **kargs): ...  # FIXME Function
    def is_floating(self) -> bool: ...
    def list_properties(self) -> list[ParamSpec]: ...
    @classmethod
    def newv(
        cls, object_type: Type, n_parameters: int, parameters: Sequence[Parameter]
    ) -> Object: ...
    def notify(self, property_name: str) -> None: ...
    def notify_by_pspec(self, *args, **kargs): ...  # FIXME Function
    def override_property(self, property_id: int, name: str) -> None: ...
    def ref(self, *args, **kargs): ...  # FIXME Function
    def ref_sink(self, *args, **kargs): ...  # FIXME Function
    def replace_data(self, *args, **kargs): ...  # FIXME Function
    def replace_qdata(self, *args, **kargs): ...  # FIXME Function
    def run_dispose(self) -> None: ...
    def set_data(self, *args, **kargs): ...  # FIXME Function
    def set_properties(self, *args, **kwargs): ...  # FIXME Function
    # override
    def set_property(self, property_name: str, value: object) -> None: ...
    def steal_data(self, *args, **kargs): ...  # FIXME Function
    def steal_qdata(self, *args, **kargs): ...  # FIXME Function
    def stop_emission(self, detailed_signal): ...  # FIXME Function
    # override
    def stop_emission_by_name(self, detailed_signal: str) -> None: ...
    def thaw_notify(self) -> None: ...
    def unref(self, *args, **kargs): ...  # FIXME Function
    def watch_closure(self, *args, **kargs): ...  # FIXME Function
    # override
    def weak_ref(self, callback: Callable[..., Any], *args: Any) -> None: ...

# override
class GObject(Object): ...

class GObjectWeakRef:
    """
    A GObject weak reference
    """

    def unref(self, *args, **kwargs): ...  # FIXME Function

class GParamSpec: ...
class GPointer: ...

class GType:
    """ """

    children = ...  # FIXME Constant
    depth = ...  # FIXME Constant
    fundamental = ...  # FIXME Constant
    interfaces = ...  # FIXME Constant
    name = ...  # FIXME Constant
    parent = ...  # FIXME Constant
    pytype = ...  # FIXME Constant

    def from_name(self, *args, **kwargs): ...  # FIXME Function
    def has_value_table(self, *args, **kwargs): ...  # FIXME Function
    def is_a(self, *args, **kwargs): ...  # FIXME Function
    def is_abstract(self, *args, **kwargs): ...  # FIXME Function
    def is_classed(self, *args, **kwargs): ...  # FIXME Function
    def is_deep_derivable(self, *args, **kwargs): ...  # FIXME Function
    def is_derivable(self, *args, **kwargs): ...  # FIXME Function
    def is_instantiatable(self, *args, **kwargs): ...  # FIXME Function
    def is_interface(self, *args, **kwargs): ...  # FIXME Function
    def is_value_abstract(self, *args, **kwargs): ...  # FIXME Function
    def is_value_type(self, *args, **kwargs): ...  # FIXME Function

class Idle(GBoxed):
    """
    :Constructors:

    ::

        Source()
        new(source_funcs:GLib.SourceFuncs, struct_size:int) -> GLib.Source
    """

    callback_data: None = ...
    callback_funcs: GLib.SourceCallbackFuncs = ...
    source_funcs: GLib.SourceFuncs = ...
    ref_count: int = ...
    context: GLib.MainContext = ...
    priority: int = ...
    flags: int = ...
    source_id: int = ...
    poll_fds: list[None] = ...
    prev: GLib.Source = ...
    next: GLib.Source = ...
    name: str = ...
    priv: GLib.SourcePrivate = ...
    can_recurse = ...  # FIXME Constant

    def add_child_source(self, child_source: GLib.Source) -> None: ...
    def add_poll(self, fd: GLib.PollFD) -> None: ...
    def add_unix_fd(self, fd: int, events: GLib.IOCondition) -> None: ...
    def attach(self, context: Optional[GLib.MainContext] = None) -> int: ...
    def destroy(self) -> None: ...
    def get_can_recurse(self) -> bool: ...
    def get_context(self) -> Optional[GLib.MainContext]: ...
    def get_current_time(self): ...  # FIXME Function
    def get_id(self) -> int: ...
    def get_name(self) -> Optional[str]: ...
    def get_priority(self) -> int: ...
    def get_ready_time(self) -> int: ...
    def get_time(self) -> int: ...
    def is_destroyed(self) -> bool: ...
    def modify_unix_fd(self, tag: None, new_events: GLib.IOCondition) -> None: ...
    @classmethod
    def new(cls, source_funcs: GLib.SourceFuncs, struct_size: int) -> Source: ...
    def query_unix_fd(self, tag: None) -> GLib.IOCondition: ...
    def ref(self) -> GLib.Source: ...
    @staticmethod
    def remove(tag: int) -> bool: ...
    @staticmethod
    def remove_by_funcs_user_data(funcs: GLib.SourceFuncs, user_data: None) -> bool: ...
    @staticmethod
    def remove_by_user_data(user_data: None) -> bool: ...
    def remove_child_source(self, child_source: GLib.Source) -> None: ...
    def remove_poll(self, fd: GLib.PollFD) -> None: ...
    def remove_unix_fd(self, tag: None) -> None: ...
    def set_callback(self, fn, user_data=None): ...  # FIXME Function
    def set_callback_indirect(
        self, callback_data: None, callback_funcs: GLib.SourceCallbackFuncs
    ) -> None: ...
    def set_can_recurse(self, can_recurse: bool) -> None: ...
    def set_funcs(self, funcs: GLib.SourceFuncs) -> None: ...
    def set_name(self, name: str) -> None: ...
    @staticmethod
    def set_name_by_id(tag: int, name: str) -> None: ...
    def set_priority(self, priority: int) -> None: ...
    def set_ready_time(self, ready_time: int) -> None: ...
    def set_static_name(self, name: str) -> None: ...
    def unref(self) -> None: ...

class InitiallyUnowned(Object):
    """
    :Constructors:

    ::

        InitiallyUnowned(**properties)

    Object GInitiallyUnowned

    Signals from GObject:
      notify (GParam)
    """

    g_type_instance: TypeInstance = ...
    ref_count: int = ...
    qdata: GLib.Data = ...

class InitiallyUnownedClass(GPointer):
    """
    :Constructors:

    ::

        InitiallyUnownedClass()
    """

    g_type_class: TypeClass = ...
    construct_properties: list[None] = ...
    constructor: None = ...
    set_property: Callable[[Object, int, Any, ParamSpec], None] = ...
    get_property: Callable[[Object, int, Any, ParamSpec], None] = ...
    dispose: Callable[[Object], None] = ...
    finalize: Callable[[Object], None] = ...
    dispatch_properties_changed: Callable[[Object, int, ParamSpec], None] = ...
    notify: Callable[[Object, ParamSpec], None] = ...
    constructed: Callable[[Object], None] = ...
    flags: int = ...
    n_construct_properties: int = ...
    pspecs: None = ...
    n_pspecs: int = ...
    pdummy: list[None] = ...

class InterfaceInfo(GPointer):
    """
    :Constructors:

    ::

        InterfaceInfo()
    """

    interface_init: Callable[[TypeInterface, None], None] = ...
    interface_finalize: Callable[[TypeInterface, None], None] = ...
    interface_data: None = ...

class MainContext(GBoxed):
    """
    :Constructors:

    ::

        new() -> GLib.MainContext
        new_with_flags(flags:GLib.MainContextFlags) -> GLib.MainContext
    """

    def acquire(self) -> bool: ...
    def add_poll(self, fd: GLib.PollFD, priority: int) -> None: ...
    def check(self, max_priority: int, fds: Sequence[GLib.PollFD]) -> bool: ...
    @staticmethod
    def default() -> GLib.MainContext: ...
    def dispatch(self) -> None: ...
    def find_source_by_funcs_user_data(
        self, funcs: GLib.SourceFuncs, user_data: None
    ) -> GLib.Source: ...
    def find_source_by_id(self, source_id: int) -> GLib.Source: ...
    def find_source_by_user_data(self, user_data: None) -> GLib.Source: ...
    @staticmethod
    def get_thread_default() -> Optional[GLib.MainContext]: ...
    def invoke_full(
        self, priority: int, function: Callable[..., bool], *data: Any
    ) -> None: ...
    def is_owner(self) -> bool: ...
    def iteration(self, may_block=True): ...  # FIXME Function
    @classmethod
    def new(cls) -> MainContext: ...
    @classmethod
    def new_with_flags(cls, flags: GLib.MainContextFlags) -> MainContext: ...
    def pending(self) -> bool: ...
    def pop_thread_default(self) -> None: ...
    def prepare(self) -> Tuple[bool, int]: ...
    def push_thread_default(self) -> None: ...
    def query(self, max_priority: int) -> Tuple[int, int, list[GLib.PollFD]]: ...
    def ref(self) -> GLib.MainContext: ...
    @staticmethod
    def ref_thread_default() -> GLib.MainContext: ...
    def release(self) -> None: ...
    def remove_poll(self, fd: GLib.PollFD) -> None: ...
    def unref(self) -> None: ...
    def wait(self, cond: GLib.Cond, mutex: GLib.Mutex) -> bool: ...
    def wakeup(self) -> None: ...

class MainLoop(GBoxed):
    """
    :Constructors:

    ::

        new(context:GLib.MainContext=None, is_running:bool) -> GLib.MainLoop
    """

    def get_context(self) -> GLib.MainContext: ...
    def is_running(self) -> bool: ...
    @classmethod
    def new(cls, context: Optional[GLib.MainContext], is_running: bool) -> MainLoop: ...
    def quit(self) -> None: ...
    def ref(self) -> GLib.MainLoop: ...
    def run(self): ...  # FIXME Function
    def unref(self) -> None: ...

class Object:
    """
    :Constructors:

    ::

        Object(**properties)
        newv(object_type:GType, parameters:list) -> GObject.Object

    Object GObject

    Signals from GObject:
      notify (GParam)
    """

    g_type_instance: TypeInstance = ...
    ref_count: int = ...
    qdata: GLib.Data = ...
    props = ...  # FIXME Constant

    # override
    def bind_property(
        self,
        source_property: str,
        target: Object,
        target_property: str,
        flags: BindingFlags = BindingFlags.DEFAULT,
        transform_to: Optional[Callable[..., Any]] = None,
        transform_from: Optional[Callable[..., Any]] = None,
        user_data: Optional[Any] = None,
    ) -> Binding: ...
    def bind_property_full(self, *args, **kargs): ...  # FIXME Function
    def chain(self, *args, **kwargs): ...  # FIXME Function
    def compat_control(self, *args, **kargs): ...  # FIXME Function
    # override
    def connect(
        self, detailed_signal: str, handler: Callable[..., Any], *args: Any
    ) -> int: ...
    # override
    def connect_after(
        self, detailed_signal: str, handler: Callable[..., Any], *args: Any
    ) -> int: ...
    def connect_data(
        self, detailed_signal, handler, *data, **kwargs
    ): ...  # FIXME Function
    def connect_object(self, *args, **kwargs): ...  # FIXME Function
    def connect_object_after(self, *args, **kwargs): ...  # FIXME Function
    # override
    def disconnect(self, id: int) -> None: ...
    def disconnect_by_func(self, *args, **kwargs): ...  # FIXME Function
    # override
    def emit(self, signal_name: str, *args: Any) -> Any: ...
    def emit_stop_by_name(self, detailed_signal): ...  # FIXME Function
    def find_property(self, property_name: str) -> ParamSpec: ...
    def force_floating(self, *args, **kargs): ...  # FIXME Function
    def freeze_notify(self): ...  # FIXME Function
    def get_data(self, *args, **kargs): ...  # FIXME Function
    def get_properties(self, *args, **kwargs): ...  # FIXME Function
    # override
    def get_property(self, property_name: str) -> Any: ...
    def get_qdata(self, *args, **kargs): ...  # FIXME Function
    def getv(
        self, n_properties: int, names: Sequence[str], values: Sequence[Any]
    ) -> None: ...
    # override
    def handler_block(self, handler_id: int) -> _HandlerBlockManager: ...
    def handler_block_by_func(self, *args, **kwargs): ...  # FIXME Function
    def handler_disconnect(self, *args, **kwargs): ...  # FIXME Function
    # override
    def handler_is_connected(self, id: int) -> bool: ...
    def handler_unblock(self, *args, **kwargs): ...  # FIXME Function
    def handler_unblock_by_func(self, *args, **kwargs): ...  # FIXME Function
    def install_properties(
        self, n_pspecs: int, pspecs: Sequence[ParamSpec]
    ) -> None: ...
    def install_property(self, property_id: int, pspec: ParamSpec) -> None: ...
    def interface_find_property(self, *args, **kargs): ...  # FIXME Function
    def interface_install_property(self, *args, **kargs): ...  # FIXME Function
    def interface_list_properties(self, *args, **kargs): ...  # FIXME Function
    def is_floating(self) -> bool: ...
    def list_properties(self) -> list[ParamSpec]: ...
    @classmethod
    def newv(
        cls, object_type: Type, n_parameters: int, parameters: Sequence[Parameter]
    ) -> Object: ...
    def notify(self, property_name: str) -> None: ...
    def notify_by_pspec(self, *args, **kargs): ...  # FIXME Function
    def override_property(self, property_id: int, name: str) -> None: ...
    def ref(self, *args, **kargs): ...  # FIXME Function
    def ref_sink(self, *args, **kargs): ...  # FIXME Function
    def replace_data(self, *args, **kargs): ...  # FIXME Function
    def replace_qdata(self, *args, **kargs): ...  # FIXME Function
    def run_dispose(self) -> None: ...
    def set_data(self, *args, **kargs): ...  # FIXME Function
    def set_properties(self, *args, **kwargs): ...  # FIXME Function
    # override
    def set_property(self, property_name: str, value: object) -> None: ...
    def steal_data(self, *args, **kargs): ...  # FIXME Function
    def steal_qdata(self, *args, **kargs): ...  # FIXME Function
    def stop_emission(self, detailed_signal): ...  # FIXME Function
    # override
    def stop_emission_by_name(self, detailed_signal: str) -> None: ...
    def thaw_notify(self) -> None: ...
    def unref(self, *args, **kargs): ...  # FIXME Function
    def watch_closure(self, *args, **kargs): ...  # FIXME Function
    # override
    def weak_ref(self, callback: Callable[..., Any], *args: Any) -> None: ...

class ObjectClass(GPointer):
    """
    :Constructors:

    ::

        ObjectClass()
    """

    g_type_class: TypeClass = ...
    construct_properties: list[None] = ...
    constructor: None = ...
    set_property: Callable[[Object, int, Any, ParamSpec], None] = ...
    get_property: Callable[[Object, int, Any, ParamSpec], None] = ...
    dispose: Callable[[Object], None] = ...
    finalize: Callable[[Object], None] = ...
    dispatch_properties_changed: Callable[[Object, int, ParamSpec], None] = ...
    notify: Callable[[Object, ParamSpec], None] = ...
    constructed: Callable[[Object], None] = ...
    flags: int = ...
    n_construct_properties: int = ...
    pspecs: None = ...
    n_pspecs: int = ...
    pdummy: list[None] = ...
    def find_property(self, property_name: str) -> ParamSpec: ...
    def install_properties(
        self, n_pspecs: int, pspecs: Sequence[ParamSpec]
    ) -> None: ...
    def install_property(self, property_id: int, pspec: ParamSpec) -> None: ...
    def list_properties(self) -> list[ParamSpec]: ...
    def override_property(self, property_id: int, name: str) -> None: ...

class ObjectConstructParam(GPointer):
    """
    :Constructors:

    ::

        ObjectConstructParam()
    """

    pspec: ParamSpec = ...
    value: Any = ...

class OptionContext:
    """ """

    def add_group(self, *args, **kwargs): ...  # FIXME Function
    def get_help_enabled(self, *args, **kwargs): ...  # FIXME Function
    def get_ignore_unknown_options(self, *args, **kwargs): ...  # FIXME Function
    def get_main_group(self, *args, **kwargs): ...  # FIXME Function
    def parse(self, *args, **kwargs): ...  # FIXME Function
    def set_help_enabled(self, *args, **kwargs): ...  # FIXME Function
    def set_ignore_unknown_options(self, *args, **kwargs): ...  # FIXME Function
    def set_main_group(self, *args, **kwargs): ...  # FIXME Function

class OptionGroup:
    """ """

    def add_entries(self, *args, **kwargs): ...  # FIXME Function
    def set_translation_domain(self, *args, **kwargs): ...  # FIXME Function

class ParamSpec:
    """
    :Constructors:

    ::

        ParamSpec(**properties)
    """

    g_type_instance: TypeInstance = ...
    name: str = ...
    flags: ParamFlags = ...
    value_type: Type = ...
    owner_type: Type = ...
    _nick: str = ...
    _blurb: str = ...
    qdata: GLib.Data = ...
    ref_count: int = ...
    param_id: int = ...
    def do_finalize(self) -> None: ...
    def do_value_is_valid(self, value: Any) -> bool: ...
    def do_value_set_default(self, value: Any) -> None: ...
    def do_value_validate(self, value: Any) -> bool: ...
    def do_values_cmp(self, value1: Any, value2: Any) -> int: ...
    def get_blurb(self) -> Optional[str]: ...
    def get_default_value(self) -> Any: ...
    def get_name(self) -> str: ...
    def get_name_quark(self) -> int: ...
    def get_nick(self) -> str: ...
    def get_qdata(self, quark: int) -> None: ...
    def get_redirect_target(self) -> Optional[ParamSpec]: ...
    @staticmethod
    def is_valid_name(name: str) -> bool: ...
    def set_qdata(self, quark: int, data: None) -> None: ...
    def sink(self) -> None: ...
    def steal_qdata(self, quark: int) -> None: ...

class ParamSpecBoolean(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecBoolean(**properties)
    """

    parent_instance: ParamSpec = ...
    default_value: bool = ...

class ParamSpecBoxed(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecBoxed(**properties)
    """

    parent_instance: ParamSpec = ...

class ParamSpecChar(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecChar(**properties)
    """

    parent_instance: ParamSpec = ...
    minimum: int = ...
    maximum: int = ...
    default_value: int = ...

class ParamSpecClass(GPointer):
    """
    :Constructors:

    ::

        ParamSpecClass()
    """

    g_type_class: TypeClass = ...
    value_type: Type = ...
    finalize: Callable[[ParamSpec], None] = ...
    value_set_default: Callable[[ParamSpec, Any], None] = ...
    value_validate: Callable[[ParamSpec, Any], bool] = ...
    values_cmp: Callable[[ParamSpec, Any, Any], int] = ...
    value_is_valid: Callable[[ParamSpec, Any], bool] = ...
    dummy: list[None] = ...

class ParamSpecDouble(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecDouble(**properties)
    """

    parent_instance: ParamSpec = ...
    minimum: float = ...
    maximum: float = ...
    default_value: float = ...
    epsilon: float = ...

class ParamSpecEnum(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecEnum(**properties)
    """

    parent_instance: ParamSpec = ...
    enum_class: EnumClass = ...
    default_value: int = ...

class ParamSpecFlags(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecFlags(**properties)
    """

    parent_instance: ParamSpec = ...
    flags_class: FlagsClass = ...
    default_value: int = ...

class ParamSpecFloat(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecFloat(**properties)
    """

    parent_instance: ParamSpec = ...
    minimum: float = ...
    maximum: float = ...
    default_value: float = ...
    epsilon: float = ...

class ParamSpecGType(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecGType(**properties)
    """

    parent_instance: ParamSpec = ...
    is_a_type: Type = ...

class ParamSpecInt(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecInt(**properties)
    """

    parent_instance: ParamSpec = ...
    minimum: int = ...
    maximum: int = ...
    default_value: int = ...

class ParamSpecInt64(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecInt64(**properties)
    """

    parent_instance: ParamSpec = ...
    minimum: int = ...
    maximum: int = ...
    default_value: int = ...

class ParamSpecLong(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecLong(**properties)
    """

    parent_instance: ParamSpec = ...
    minimum: int = ...
    maximum: int = ...
    default_value: int = ...

class ParamSpecObject(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecObject(**properties)
    """

    parent_instance: ParamSpec = ...

class ParamSpecOverride(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecOverride(**properties)
    """

    parent_instance: ParamSpec = ...
    overridden: ParamSpec = ...

class ParamSpecParam(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecParam(**properties)
    """

    parent_instance: ParamSpec = ...

class ParamSpecPointer(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecPointer(**properties)
    """

    parent_instance: ParamSpec = ...

class ParamSpecPool(GPointer):
    """ """

    def insert(self, pspec: ParamSpec, owner_type: Type) -> None: ...
    def list(self, owner_type: Type) -> list[ParamSpec]: ...
    def list_owned(self, owner_type: Type) -> list[ParamSpec]: ...
    def lookup(
        self, param_name: str, owner_type: Type, walk_ancestors: bool
    ) -> Optional[ParamSpec]: ...
    def remove(self, pspec: ParamSpec) -> None: ...

class ParamSpecString(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecString(**properties)
    """

    parent_instance: ParamSpec = ...
    default_value: str = ...
    cset_first: str = ...
    cset_nth: str = ...
    substitutor: int = ...
    null_fold_if_empty: int = ...
    ensure_non_null: int = ...

class ParamSpecTypeInfo(GPointer):
    """
    :Constructors:

    ::

        ParamSpecTypeInfo()
    """

    instance_size: int = ...
    n_preallocs: int = ...
    instance_init: Callable[[ParamSpec], None] = ...
    value_type: Type = ...
    finalize: Callable[[ParamSpec], None] = ...
    value_set_default: Callable[[ParamSpec, Any], None] = ...
    value_validate: Callable[[ParamSpec, Any], bool] = ...
    values_cmp: Callable[[ParamSpec, Any, Any], int] = ...

class ParamSpecUChar(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecUChar(**properties)
    """

    parent_instance: ParamSpec = ...
    minimum: int = ...
    maximum: int = ...
    default_value: int = ...

class ParamSpecUInt(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecUInt(**properties)
    """

    parent_instance: ParamSpec = ...
    minimum: int = ...
    maximum: int = ...
    default_value: int = ...

class ParamSpecUInt64(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecUInt64(**properties)
    """

    parent_instance: ParamSpec = ...
    minimum: int = ...
    maximum: int = ...
    default_value: int = ...

class ParamSpecULong(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecULong(**properties)
    """

    parent_instance: ParamSpec = ...
    minimum: int = ...
    maximum: int = ...
    default_value: int = ...

class ParamSpecUnichar(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecUnichar(**properties)
    """

    parent_instance: ParamSpec = ...
    default_value: str = ...

class ParamSpecValueArray(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecValueArray(**properties)
    """

    parent_instance: ParamSpec = ...
    element_spec: ParamSpec = ...
    fixed_n_elements: int = ...

class ParamSpecVariant(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecVariant(**properties)
    """

    parent_instance: ParamSpec = ...
    type: GLib.VariantType = ...
    default_value: GLib.Variant = ...
    padding: list[None] = ...

class Parameter(GPointer):
    """
    :Constructors:

    ::

        Parameter()
    """

    name: str = ...
    value: Any = ...

class Pid:
    """ """

    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, *args, **kwargs): ...  # FIXME Method
    def bit_count(self, *args, **kwargs): ...  # FIXME Method
    def bit_length(self, *args, **kwargs): ...  # FIXME Method
    def close(self, *args, **kwargs): ...  # FIXME Method
    def conjugate(self, *args, **kwargs): ...  # FIXME Method
    def from_bytes(self, *args, **kwargs): ...  # FIXME Method
    def to_bytes(self, *args, **kwargs): ...  # FIXME Method

class PollFD(GBoxed):
    """
    :Constructors:

    ::

        PollFD()
    """

    fd: int = ...
    events: int = ...
    revents: int = ...

# override
class Property:
    def __init__(
        self,
        getter: Optional[Callable] = None,
        setter: Optional[Callable] = None,
        type: Type = None,
        default: Any = None,
        nick: str = "",
        blurb: str = "",
        flags: int = PARAM_READWRITE,
        minimum: Any = None,
        maximum: Any = None,
    ): ...
    def __call__(self, fget: Callable) -> Property: ...
    def __get__(self, instance: Object, klass: Any): ...
    def __set__(self, instance: Object, value: Any): ...
    def get_pspec_args(self): ...
    def getter(self, fget: Callable) -> Property: ...
    def setter(self, fset: Callable) -> Property: ...

# override
class Signal(str):
    def __new__(cls, name: Any = "", *args, **kargs): ...
    def __init__(
        self,
        name: Any = "",
        func: Optional[Callable] = None,
        flags: int = SIGNAL_RUN_FIRST,
        return_type: Optional[Type] = None,
        arg_types: Optional[Sequence[Type]] = None,
        doc: str = "",
        accumulator: Optional[Callable] = None,
        accu_data: Any = None,
    ): ...
    def __call__(self, obj: Any, *args, **kargs): ...
    def __get__(
        self, instance: Optional[Object], owner: Optional[Object] = None
    ) -> BoundSignal: ...
    def copy(self, newName: Optional[str] = None): ...
    def get_signal_args(self): ...

    class BoundSignal(str):
        def __new__(cls, name: str, *args, **kargs): ...
        def __init__(self, signal: Signal, gobj: Object): ...
        def __call__(self, *args, **kargs): ...
        def connect(self, callback: Callable, *args, **kargs) -> int: ...
        def connect_detailed(
            self, callback: Callable, detail: str, *args, **kargs
        ) -> int: ...
        def disconnect(self, handler_id: int): ...
        def emit(self, *args, **kargs): ...

class SignalGroup(Object):
    """
    :Constructors:

    ::

        SignalGroup(**properties)
        new(target_type:GType) -> GObject.SignalGroup

    Object GSignalGroup

    Signals from GSignalGroup:
      bind (GObject)
      unbind ()

    Properties from GSignalGroup:
      target -> GObject: Target
        The target instance used when connecting signals.
      target-type -> GType: Target Type
        The GType of the target property.

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        target: Optional[Object]
        target_type: Type
    props: Props = ...
    def __init__(self, target: Optional[Object] = ..., target_type: Type = ...): ...
    def block(self) -> None: ...
    def connect_closure(
        self, detailed_signal: str, closure: Callable[..., Any], after: bool
    ) -> None: ...
    def connect_data(
        self,
        detailed_signal: str,
        c_handler: Callable[..., None],
        flags: ConnectFlags,
        *data: Any,
    ) -> None: ...
    def connect_swapped(
        self, detailed_signal: str, c_handler: Callable[..., None], *data: Any
    ) -> None: ...
    def dup_target(self) -> Optional[Object]: ...
    @classmethod
    def new(cls, target_type: Type) -> SignalGroup: ...
    def set_target(self, target: Optional[Object] = None) -> None: ...
    def unblock(self) -> None: ...

class SignalInvocationHint(GPointer):
    """
    :Constructors:

    ::

        SignalInvocationHint()
    """

    signal_id: int = ...
    detail: int = ...
    run_type: SignalFlags = ...

# override
class SignalOverride(Signal):
    def get_signal_args(self) -> Literal["override"]: ...

class SignalQuery(GPointer):
    """
    :Constructors:

    ::

        SignalQuery()
    """

    signal_id: int = ...
    signal_name: str = ...
    itype: Type = ...
    signal_flags: SignalFlags = ...
    return_type: Type = ...
    n_params: int = ...
    param_types: list[Type] = ...

class Source(GBoxed):
    """
    :Constructors:

    ::

        Source()
        new(source_funcs:GLib.SourceFuncs, struct_size:int) -> GLib.Source
    """

    callback_data: None = ...
    callback_funcs: GLib.SourceCallbackFuncs = ...
    source_funcs: GLib.SourceFuncs = ...
    ref_count: int = ...
    context: GLib.MainContext = ...
    priority: int = ...
    flags: int = ...
    source_id: int = ...
    poll_fds: list[None] = ...
    prev: GLib.Source = ...
    next: GLib.Source = ...
    name: str = ...
    priv: GLib.SourcePrivate = ...
    can_recurse = ...  # FIXME Constant

    def add_child_source(self, child_source: GLib.Source) -> None: ...
    def add_poll(self, fd: GLib.PollFD) -> None: ...
    def add_unix_fd(self, fd: int, events: GLib.IOCondition) -> None: ...
    def attach(self, context: Optional[GLib.MainContext] = None) -> int: ...
    def destroy(self) -> None: ...
    def get_can_recurse(self) -> bool: ...
    def get_context(self) -> Optional[GLib.MainContext]: ...
    def get_current_time(self): ...  # FIXME Function
    def get_id(self) -> int: ...
    def get_name(self) -> Optional[str]: ...
    def get_priority(self) -> int: ...
    def get_ready_time(self) -> int: ...
    def get_time(self) -> int: ...
    def is_destroyed(self) -> bool: ...
    def modify_unix_fd(self, tag: None, new_events: GLib.IOCondition) -> None: ...
    @classmethod
    def new(cls, source_funcs: GLib.SourceFuncs, struct_size: int) -> Source: ...
    def query_unix_fd(self, tag: None) -> GLib.IOCondition: ...
    def ref(self) -> GLib.Source: ...
    @staticmethod
    def remove(tag: int) -> bool: ...
    @staticmethod
    def remove_by_funcs_user_data(funcs: GLib.SourceFuncs, user_data: None) -> bool: ...
    @staticmethod
    def remove_by_user_data(user_data: None) -> bool: ...
    def remove_child_source(self, child_source: GLib.Source) -> None: ...
    def remove_poll(self, fd: GLib.PollFD) -> None: ...
    def remove_unix_fd(self, tag: None) -> None: ...
    def set_callback(self, fn, user_data=None): ...  # FIXME Function
    def set_callback_indirect(
        self, callback_data: None, callback_funcs: GLib.SourceCallbackFuncs
    ) -> None: ...
    def set_can_recurse(self, can_recurse: bool) -> None: ...
    def set_funcs(self, funcs: GLib.SourceFuncs) -> None: ...
    def set_name(self, name: str) -> None: ...
    @staticmethod
    def set_name_by_id(tag: int, name: str) -> None: ...
    def set_priority(self, priority: int) -> None: ...
    def set_ready_time(self, ready_time: int) -> None: ...
    def set_static_name(self, name: str) -> None: ...
    def unref(self) -> None: ...

class Timeout(GBoxed):
    """
    :Constructors:

    ::

        Source()
        new(source_funcs:GLib.SourceFuncs, struct_size:int) -> GLib.Source
    """

    callback_data: None = ...
    callback_funcs: GLib.SourceCallbackFuncs = ...
    source_funcs: GLib.SourceFuncs = ...
    ref_count: int = ...
    context: GLib.MainContext = ...
    priority: int = ...
    flags: int = ...
    source_id: int = ...
    poll_fds: list[None] = ...
    prev: GLib.Source = ...
    next: GLib.Source = ...
    name: str = ...
    priv: GLib.SourcePrivate = ...
    can_recurse = ...  # FIXME Constant

    def add_child_source(self, child_source: GLib.Source) -> None: ...
    def add_poll(self, fd: GLib.PollFD) -> None: ...
    def add_unix_fd(self, fd: int, events: GLib.IOCondition) -> None: ...
    def attach(self, context: Optional[GLib.MainContext] = None) -> int: ...
    def destroy(self) -> None: ...
    def get_can_recurse(self) -> bool: ...
    def get_context(self) -> Optional[GLib.MainContext]: ...
    def get_current_time(self): ...  # FIXME Function
    def get_id(self) -> int: ...
    def get_name(self) -> Optional[str]: ...
    def get_priority(self) -> int: ...
    def get_ready_time(self) -> int: ...
    def get_time(self) -> int: ...
    def is_destroyed(self) -> bool: ...
    def modify_unix_fd(self, tag: None, new_events: GLib.IOCondition) -> None: ...
    @classmethod
    def new(cls, source_funcs: GLib.SourceFuncs, struct_size: int) -> Source: ...
    def query_unix_fd(self, tag: None) -> GLib.IOCondition: ...
    def ref(self) -> GLib.Source: ...
    @staticmethod
    def remove(tag: int) -> bool: ...
    @staticmethod
    def remove_by_funcs_user_data(funcs: GLib.SourceFuncs, user_data: None) -> bool: ...
    @staticmethod
    def remove_by_user_data(user_data: None) -> bool: ...
    def remove_child_source(self, child_source: GLib.Source) -> None: ...
    def remove_poll(self, fd: GLib.PollFD) -> None: ...
    def remove_unix_fd(self, tag: None) -> None: ...
    def set_callback(self, fn, user_data=None): ...  # FIXME Function
    def set_callback_indirect(
        self, callback_data: None, callback_funcs: GLib.SourceCallbackFuncs
    ) -> None: ...
    def set_can_recurse(self, can_recurse: bool) -> None: ...
    def set_funcs(self, funcs: GLib.SourceFuncs) -> None: ...
    def set_name(self, name: str) -> None: ...
    @staticmethod
    def set_name_by_id(tag: int, name: str) -> None: ...
    def set_priority(self, priority: int) -> None: ...
    def set_ready_time(self, ready_time: int) -> None: ...
    def set_static_name(self, name: str) -> None: ...
    def unref(self) -> None: ...

class TypeCValue(GPointer): ...

class TypeClass(GPointer):
    """
    :Constructors:

    ::

        TypeClass()
    """

    g_type: Type = ...
    def add_private(self, private_size: int) -> None: ...
    @staticmethod
    def adjust_private_offset(g_class: None, private_size_or_offset: int) -> None: ...
    def get_private(self, private_type: Type) -> None: ...
    @staticmethod
    def peek(type: Type) -> TypeClass: ...
    def peek_parent(self) -> TypeClass: ...
    @staticmethod
    def peek_static(type: Type) -> TypeClass: ...
    @staticmethod
    def ref(type: Type) -> TypeClass: ...
    def unref(self) -> None: ...

class TypeFundamentalInfo(GPointer):
    """
    :Constructors:

    ::

        TypeFundamentalInfo()
    """

    type_flags: TypeFundamentalFlags = ...

class TypeInfo(GPointer):
    """
    :Constructors:

    ::

        TypeInfo()
    """

    class_size: int = ...
    base_init: Callable[[TypeClass], None] = ...
    base_finalize: Callable[[TypeClass], None] = ...
    class_init: Callable[[TypeClass, None], None] = ...
    class_finalize: Callable[[TypeClass, None], None] = ...
    class_data: None = ...
    instance_size: int = ...
    n_preallocs: int = ...
    instance_init: Callable[[TypeInstance, TypeClass], None] = ...
    value_table: TypeValueTable = ...

class TypeInstance(GPointer):
    """
    :Constructors:

    ::

        TypeInstance()
    """

    g_class: TypeClass = ...
    def get_private(self, private_type: Type) -> None: ...

class TypeInterface(GPointer):
    """
    :Constructors:

    ::

        TypeInterface()
    """

    g_type: Type = ...
    g_instance_type: Type = ...
    @staticmethod
    def add_prerequisite(interface_type: Type, prerequisite_type: Type) -> None: ...
    @staticmethod
    def get_plugin(instance_type: Type, interface_type: Type) -> TypePlugin: ...
    @staticmethod
    def instantiatable_prerequisite(interface_type: Type) -> Type: ...
    @staticmethod
    def peek(instance_class: TypeClass, iface_type: Type) -> TypeInterface: ...
    def peek_parent(self) -> TypeInterface: ...
    @staticmethod
    def prerequisites(interface_type: Type) -> list[Type]: ...

# override
class TypeModule(TypePlugin):
    parent_instance: Object = ...
    use_count: int = ...
    type_infos: list[None] = ...
    interface_infos: list[None] = ...
    name: str = ...

    def add_interface(
        self, instance_type: Type, interface_type: Type, interface_info: InterfaceInfo
    ) -> None: ...
    def do_load(self) -> bool: ...
    def do_unload(self) -> None: ...
    def register_enum(self, name: str, const_static_values: EnumValue) -> Type: ...
    def register_flags(self, name: str, const_static_values: FlagsValue) -> Type: ...
    def register_type(
        self, parent_type: Type, type_name: str, type_info: TypeInfo, flags: TypeFlags
    ) -> Type: ...
    def set_name(self, name: str) -> None: ...
    def unuse(self) -> None: ...
    def use(self) -> bool: ...

class TypeModuleClass(GPointer):
    """
    :Constructors:

    ::

        TypeModuleClass()
    """

    parent_class: ObjectClass = ...
    load: Callable[[TypeModule], bool] = ...
    unload: Callable[[TypeModule], None] = ...
    reserved1: Callable[[], None] = ...
    reserved2: Callable[[], None] = ...
    reserved3: Callable[[], None] = ...
    reserved4: Callable[[], None] = ...

class TypePlugin(Object):
    """
    Interface GTypePlugin
    """

    def complete_interface_info(
        self, instance_type: Type, interface_type: Type, info: InterfaceInfo
    ) -> None: ...
    def complete_type_info(
        self, g_type: Type, info: TypeInfo, value_table: TypeValueTable
    ) -> None: ...
    def unuse(self) -> None: ...
    def use(self) -> None: ...

class TypePluginClass(GPointer):
    """
    :Constructors:

    ::

        TypePluginClass()
    """

    base_iface: TypeInterface = ...
    use_plugin: Callable[[TypePlugin], None] = ...
    unuse_plugin: Callable[[TypePlugin], None] = ...
    complete_type_info: Callable[
        [TypePlugin, Type, TypeInfo, TypeValueTable], None
    ] = ...
    complete_interface_info: Callable[
        [TypePlugin, Type, Type, InterfaceInfo], None
    ] = ...

class TypeQuery(GPointer):
    """
    :Constructors:

    ::

        TypeQuery()
    """

    type: Type = ...
    type_name: str = ...
    class_size: int = ...
    instance_size: int = ...

class TypeValueTable(GPointer):
    """
    :Constructors:

    ::

        TypeValueTable()
    """

    value_init: Callable[[Any], None] = ...
    value_free: Callable[[Any], None] = ...
    value_copy: Callable[[Any, Any], None] = ...
    value_peek_pointer: Callable[[Any], None] = ...
    collect_format: str = ...
    collect_value: Callable[[Any, int, TypeCValue, int], str] = ...
    lcopy_format: str = ...
    lcopy_value: Callable[[Any, int, TypeCValue, int], str] = ...

class Value(GBoxed):
    """
    :Constructors:

    ::

        Value()
    """

    g_type: Type = ...
    data: list[_Value__data__union] = ...
    _Value__g_type = ...  # FIXME Constant

    def copy(self, dest_value: Any) -> None: ...
    def dup_object(self) -> Optional[Object]: ...
    def dup_string(self) -> Optional[str]: ...
    def dup_variant(self) -> Optional[GLib.Variant]: ...
    def fits_pointer(self) -> bool: ...
    def get_boolean(self) -> bool: ...
    def get_boxed(self): ...  # FIXME Function
    def get_char(self) -> int: ...
    def get_double(self) -> float: ...
    def get_enum(self) -> int: ...
    def get_flags(self) -> int: ...
    def get_float(self) -> float: ...
    def get_gtype(self) -> Type: ...
    def get_int(self) -> int: ...
    def get_int64(self) -> int: ...
    def get_long(self) -> int: ...
    def get_object(self) -> Optional[Object]: ...
    def get_param(self) -> ParamSpec: ...
    def get_pointer(self) -> None: ...
    def get_schar(self) -> int: ...
    def get_string(self) -> Optional[str]: ...
    def get_uchar(self) -> int: ...
    def get_uint(self) -> int: ...
    def get_uint64(self) -> int: ...
    def get_ulong(self) -> int: ...
    def get_value(self): ...  # FIXME Function
    def get_variant(self) -> Optional[GLib.Variant]: ...
    def init(self, g_type: Type) -> Any: ...
    def init_from_instance(self, instance: TypeInstance) -> None: ...
    def peek_pointer(self) -> None: ...
    def reset(self) -> Any: ...
    def set_boolean(self, v_boolean: bool) -> None: ...
    def set_boxed(self, boxed): ...  # FIXME Function
    def set_boxed_take_ownership(self, v_boxed: None) -> None: ...
    def set_char(self, v_char: int) -> None: ...
    def set_double(self, v_double: float) -> None: ...
    def set_enum(self, v_enum: int) -> None: ...
    def set_flags(self, v_flags: int) -> None: ...
    def set_float(self, v_float: float) -> None: ...
    def set_gtype(self, v_gtype: Type) -> None: ...
    def set_instance(self, instance: None) -> None: ...
    def set_int(self, v_int: int) -> None: ...
    def set_int64(self, v_int64: int) -> None: ...
    def set_interned_string(self, v_string: Optional[str] = None) -> None: ...
    def set_long(self, v_long: int) -> None: ...
    def set_object(self, v_object: Optional[Object] = None) -> None: ...
    def set_param(self, param: Optional[ParamSpec] = None) -> None: ...
    def set_pointer(self, v_pointer: None) -> None: ...
    def set_schar(self, v_char: int) -> None: ...
    def set_static_boxed(self, v_boxed: None) -> None: ...
    def set_static_string(self, v_string: Optional[str] = None) -> None: ...
    def set_string(self, v_string: Optional[str] = None) -> None: ...
    def set_string_take_ownership(self, v_string: Optional[str] = None) -> None: ...
    def set_uchar(self, v_uchar: int) -> None: ...
    def set_uint(self, v_uint: int) -> None: ...
    def set_uint64(self, v_uint64: int) -> None: ...
    def set_ulong(self, v_ulong: int) -> None: ...
    def set_value(self, py_value): ...  # FIXME Function
    def set_variant(self, variant: Optional[GLib.Variant] = None) -> None: ...
    def take_boxed(self, v_boxed: None) -> None: ...
    def take_string(self, v_string: Optional[str] = None) -> None: ...
    def take_variant(self, variant: Optional[GLib.Variant] = None) -> None: ...
    def transform(self, dest_value: Any) -> bool: ...
    @staticmethod
    def type_compatible(src_type: Type, dest_type: Type) -> bool: ...
    @staticmethod
    def type_transformable(src_type: Type, dest_type: Type) -> bool: ...
    def unset(self) -> None: ...

class ValueArray(GBoxed):
    """
    :Constructors:

    ::

        ValueArray()
        new(n_prealloced:int) -> GObject.ValueArray
    """

    n_values: int = ...
    values: Any = ...
    n_prealloced: int = ...
    def append(self, value: Optional[Any] = None) -> ValueArray: ...
    def copy(self) -> ValueArray: ...
    def get_nth(self, index_: int) -> Any: ...
    def insert(self, index_: int, value: Optional[Any] = None) -> ValueArray: ...
    @classmethod
    def new(cls, n_prealloced: int) -> ValueArray: ...
    def prepend(self, value: Optional[Any] = None) -> ValueArray: ...
    def remove(self, index_: int) -> ValueArray: ...
    def sort(self, compare_func: Callable[..., int], *user_data: Any) -> ValueArray: ...

class Warning:
    """ """

    args = ...  # FIXME Constant

    def add_note(self, *args, **kwargs): ...  # FIXME Function
    def with_traceback(self, *args, **kwargs): ...  # FIXME Function

class WeakRef(GPointer): ...

class _Value__data__union(GPointer):
    """ """

    v_double = ...  # FIXME Constant
    v_float = ...  # FIXME Constant
    v_int = ...  # FIXME Constant
    v_int64 = ...  # FIXME Constant
    v_long = ...  # FIXME Constant
    v_pointer = ...  # FIXME Constant
    v_uint = ...  # FIXME Constant
    v_uint64 = ...  # FIXME Constant
    v_ulong = ...  # FIXME Constant

class property:
    """
    Creates a new Property which when used in conjunction with
        GObject subclass will create a Python property accessor for the
        GObject ParamSpec.

        :param callable getter:
            getter to get the value of the property
        :param callable setter:
            setter to set the value of the property
        :param type type:
            type of property
        :param default:
            default value, must match the property type.
        :param str nick:
            short description
        :param str blurb:
            long description
        :param GObject.ParamFlags flags:
            parameter flags
        :keyword minimum:
            minimum allowed value (int, float, long only)
        :keyword maximum:
            maximum allowed value (int, float, long only)

        .. code-block:: python

             class MyObject(GObject.Object):
                 prop = GObject.Property(type=str)

             obj = MyObject()
             obj.prop = 'value'

             obj.prop  # now is 'value'

        The API is similar to the builtin :py:func:`property`:

        .. code-block:: python

            class AnotherObject(GObject.Object):
                value = 0

                @GObject.Property
                def prop(self):
                    'Read only property.'
                    return 1

                @GObject.Property(type=int)
                def propInt(self):
                    'Read-write integer property.'
                    return self.value

                @propInt.setter
                def propInt(self, value):
                    self.value = value
    """

    _default_lookup = ...  # FIXME Constant
    _max_value_lookup = ...  # FIXME Constant
    _min_value_lookup = ...  # FIXME Constant
    _type_from_pytype_lookup = ...  # FIXME Constant

    def get_pspec_args(self): ...  # FIXME Function
    def getter(self, fget): ...  # FIXME Function
    def setter(self, fset): ...  # FIXME Function

class BindingFlags(GFlags):
    BIDIRECTIONAL = 1
    DEFAULT = 0
    INVERT_BOOLEAN = 4
    SYNC_CREATE = 2

class ConnectFlags(GFlags):
    AFTER = 1
    DEFAULT = 0
    SWAPPED = 2

# IntFlag is close enough to whatever GFlags does
# override
class GFlags(int, Flag):
    __gtype__: GType
    first_value_name: str
    first_value_nick: str
    value_names: list[str]
    value_nicks: list[str]

    def __new__(cls: Type[_T], value: int | _T) -> _T: ...
    def __or__(self: _T, other: int | _T) -> _T: ...
    def __and__(self: _T, other: int | _T) -> _T: ...
    def __xor__(self: _T, other: int | _T) -> _T: ...
    def __ror__(self: _T, n: int | _T) -> _T: ...
    def __rand__(self: _T, n: int | _T) -> _T: ...
    def __rxor__(self: _T, n: int | _T) -> _T: ...

class ParamFlags(GFlags):
    CONSTRUCT = 4
    CONSTRUCT_ONLY = 8
    DEPRECATED = 2147483648
    EXPLICIT_NOTIFY = 1073741824
    LAX_VALIDATION = 16
    PRIVATE = 32
    READABLE = 1
    READWRITE = 3
    STATIC_BLURB = 128
    STATIC_NAME = 32
    STATIC_NICK = 64
    WRITABLE = 2

class SignalFlags(GFlags):
    ACCUMULATOR_FIRST_RUN = 131072
    ACTION = 32
    DEPRECATED = 256
    DETAILED = 16
    MUST_COLLECT = 128
    NO_HOOKS = 64
    NO_RECURSE = 8
    RUN_CLEANUP = 4
    RUN_FIRST = 1
    RUN_LAST = 2

class SignalMatchType(GFlags):
    CLOSURE = 4
    DATA = 16
    DETAIL = 2
    FUNC = 8
    ID = 1
    UNBLOCKED = 32

class TypeDebugFlags(GFlags):
    INSTANCE_COUNT = 4
    MASK = 7
    NONE = 0
    OBJECTS = 1
    SIGNALS = 2

class TypeFlags(GFlags):
    ABSTRACT = 16
    DEPRECATED = 128
    FINAL = 64
    NONE = 0
    VALUE_ABSTRACT = 32

class TypeFundamentalFlags(GFlags):
    CLASSED = 1
    DEEP_DERIVABLE = 8
    DERIVABLE = 4
    INSTANTIATABLE = 2

# IntEnum is close enough to whatever GEnum does
# override
class GEnum(int, Enum):
    __gtype__: GType
    value_name: str
    value_nick: str
