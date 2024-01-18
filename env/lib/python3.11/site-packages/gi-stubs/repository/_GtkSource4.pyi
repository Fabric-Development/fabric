from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

import cairo
from gi.repository import Atk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Pango

_SomeSurface = TypeVar("_SomeSurface", bound=cairo.Surface)

_namespace: str = "GtkSource"
_version: str = "4"

def completion_error_quark() -> int: ...
def encoding_get_all() -> list[Encoding]: ...
def encoding_get_current() -> Encoding: ...
def encoding_get_default_candidates() -> list[Encoding]: ...
def encoding_get_from_charset(charset: str) -> Optional[Encoding]: ...
def encoding_get_utf8() -> Encoding: ...
def file_loader_error_quark() -> int: ...
def file_saver_error_quark() -> int: ...
def finalize() -> None: ...
def init() -> None: ...
def utils_escape_search_text(text: str) -> str: ...
def utils_unescape_search_text(text: str) -> str: ...

class Buffer(Gtk.TextBuffer):
    class Props:
        can_redo: bool
        can_undo: bool
        highlight_matching_brackets: bool
        highlight_syntax: bool
        implicit_trailing_newline: bool
        language: Language
        max_undo_levels: int
        style_scheme: StyleScheme
        undo_manager: UndoManager
        copy_target_list: Gtk.TargetList
        cursor_position: int
        has_selection: bool
        paste_target_list: Gtk.TargetList
        tag_table: Gtk.TextTagTable
        text: str
    props: Props = ...
    parent_instance: Gtk.TextBuffer = ...
    priv: BufferPrivate = ...
    def __init__(
        self,
        highlight_matching_brackets: bool = ...,
        highlight_syntax: bool = ...,
        implicit_trailing_newline: bool = ...,
        language: Language = ...,
        max_undo_levels: int = ...,
        style_scheme: StyleScheme = ...,
        undo_manager: UndoManager = ...,
        tag_table: Gtk.TextTagTable = ...,
        text: str = ...,
    ): ...
    def backward_iter_to_source_mark(
        self, category: Optional[str] = None
    ) -> Tuple[bool, Gtk.TextIter]: ...
    def begin_not_undoable_action(self) -> None: ...
    def can_redo(self) -> bool: ...
    def can_undo(self) -> bool: ...
    def change_case(
        self, case_type: ChangeCaseType, start: Gtk.TextIter, end: Gtk.TextIter
    ) -> None: ...
    def create_source_mark(
        self, name: Optional[str], category: str, where: Gtk.TextIter
    ) -> Mark: ...
    def do_bracket_matched(
        self, iter: Gtk.TextIter, state: BracketMatchType
    ) -> None: ...
    def do_redo(self) -> None: ...
    def do_undo(self) -> None: ...
    def end_not_undoable_action(self) -> None: ...
    def ensure_highlight(self, start: Gtk.TextIter, end: Gtk.TextIter) -> None: ...
    def forward_iter_to_source_mark(
        self, category: Optional[str] = None
    ) -> Tuple[bool, Gtk.TextIter]: ...
    def get_context_classes_at_iter(self, iter: Gtk.TextIter) -> list[str]: ...
    def get_highlight_matching_brackets(self) -> bool: ...
    def get_highlight_syntax(self) -> bool: ...
    def get_implicit_trailing_newline(self) -> bool: ...
    def get_language(self) -> Optional[Language]: ...
    def get_max_undo_levels(self) -> int: ...
    def get_source_marks_at_iter(
        self, iter: Gtk.TextIter, category: Optional[str] = None
    ) -> list[Mark]: ...
    def get_source_marks_at_line(
        self, line: int, category: Optional[str] = None
    ) -> list[Mark]: ...
    def get_style_scheme(self) -> Optional[StyleScheme]: ...
    def get_undo_manager(self) -> Optional[UndoManager]: ...
    def iter_backward_to_context_class_toggle(
        self, context_class: str
    ) -> Tuple[bool, Gtk.TextIter]: ...
    def iter_forward_to_context_class_toggle(
        self, context_class: str
    ) -> Tuple[bool, Gtk.TextIter]: ...
    def iter_has_context_class(
        self, iter: Gtk.TextIter, context_class: str
    ) -> bool: ...
    def join_lines(self, start: Gtk.TextIter, end: Gtk.TextIter) -> None: ...
    @classmethod
    def new(cls, table: Optional[Gtk.TextTagTable] = None) -> Buffer: ...
    @classmethod
    def new_with_language(cls, language: Language) -> Buffer: ...
    def redo(self) -> None: ...
    def remove_source_marks(
        self, start: Gtk.TextIter, end: Gtk.TextIter, category: Optional[str] = None
    ) -> None: ...
    def set_highlight_matching_brackets(self, highlight: bool) -> None: ...
    def set_highlight_syntax(self, highlight: bool) -> None: ...
    def set_implicit_trailing_newline(
        self, implicit_trailing_newline: bool
    ) -> None: ...
    def set_language(self, language: Optional[Language] = None) -> None: ...
    def set_max_undo_levels(self, max_undo_levels: int) -> None: ...
    def set_style_scheme(self, scheme: Optional[StyleScheme] = None) -> None: ...
    def set_undo_manager(self, manager: Optional[UndoManager] = None) -> None: ...
    def sort_lines(
        self, start: Gtk.TextIter, end: Gtk.TextIter, flags: SortFlags, column: int
    ) -> None: ...
    def undo(self) -> None: ...

class BufferClass(GObject.GPointer):
    parent_class: Gtk.TextBufferClass = ...
    undo: Callable[[Buffer], None] = ...
    redo: Callable[[Buffer], None] = ...
    bracket_matched: Callable[[Buffer, Gtk.TextIter, BracketMatchType], None] = ...
    padding: list[None] = ...

class BufferPrivate(GObject.GPointer): ...

class Completion(GObject.Object, Gtk.Buildable):
    class Props:
        accelerators: int
        auto_complete_delay: int
        proposal_page_size: int
        provider_page_size: int
        remember_info_visibility: bool
        select_on_show: bool
        show_headers: bool
        show_icons: bool
        view: View
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: CompletionPrivate = ...
    def __init__(
        self,
        accelerators: int = ...,
        auto_complete_delay: int = ...,
        proposal_page_size: int = ...,
        provider_page_size: int = ...,
        remember_info_visibility: bool = ...,
        select_on_show: bool = ...,
        show_headers: bool = ...,
        show_icons: bool = ...,
        view: View = ...,
    ): ...
    def add_provider(self, provider: CompletionProvider) -> bool: ...
    def block_interactive(self) -> None: ...
    def create_context(
        self, position: Optional[Gtk.TextIter] = None
    ) -> CompletionContext: ...
    def do_activate_proposal(self) -> None: ...
    def do_hide(self) -> None: ...
    def do_move_cursor(self, step: Gtk.ScrollStep, num: int) -> None: ...
    def do_move_page(self, step: Gtk.ScrollStep, num: int) -> None: ...
    def do_populate_context(self, context: CompletionContext) -> None: ...
    def do_proposal_activated(
        self, provider: CompletionProvider, proposal: CompletionProposal
    ) -> bool: ...
    def do_show(self) -> None: ...
    def get_info_window(self) -> CompletionInfo: ...
    def get_providers(self) -> list[CompletionProvider]: ...
    def get_view(self) -> Optional[View]: ...
    def hide(self) -> None: ...
    def remove_provider(self, provider: CompletionProvider) -> bool: ...
    def start(
        self, providers: Optional[list[CompletionProvider]], context: CompletionContext
    ) -> bool: ...
    def unblock_interactive(self) -> None: ...

class CompletionClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    proposal_activated: Callable[
        [Completion, CompletionProvider, CompletionProposal], bool
    ] = ...
    show: Callable[[Completion], None] = ...
    hide: Callable[[Completion], None] = ...
    populate_context: Callable[[Completion, CompletionContext], None] = ...
    move_cursor: Callable[[Completion, Gtk.ScrollStep, int], None] = ...
    move_page: Callable[[Completion, Gtk.ScrollStep, int], None] = ...
    activate_proposal: Callable[[Completion], None] = ...
    padding: list[None] = ...

class CompletionContext(GObject.InitiallyUnowned):
    class Props:
        activation: CompletionActivation
        completion: Completion
        iter: Gtk.TextIter
    props: Props = ...
    parent: GObject.InitiallyUnowned = ...
    priv: CompletionContextPrivate = ...
    def __init__(
        self,
        activation: CompletionActivation = ...,
        completion: Completion = ...,
        iter: Gtk.TextIter = ...,
    ): ...
    def add_proposals(
        self,
        provider: CompletionProvider,
        proposals: Optional[list[CompletionProposal]],
        finished: bool,
    ) -> None: ...
    def do_cancelled(self) -> None: ...
    def get_activation(self) -> CompletionActivation: ...
    def get_iter(self) -> Tuple[bool, Gtk.TextIter]: ...

class CompletionContextClass(GObject.GPointer):
    parent_class: GObject.InitiallyUnownedClass = ...
    cancelled: Callable[[CompletionContext], None] = ...
    padding: list[None] = ...

class CompletionContextPrivate(GObject.GPointer): ...

class CompletionInfo(Gtk.Window, Atk.ImplementorIface, Gtk.Buildable):
    class Props:
        accept_focus: bool
        application: Gtk.Application
        attached_to: Gtk.Widget
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: GdkPixbuf.Pixbuf
        icon_name: str
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: str
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        startup_id: str
        title: str
        transient_for: Gtk.Window
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        child: Gtk.Widget
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Gtk.Container
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Gdk.Window
    props: Props = ...
    parent: Gtk.Window = ...
    priv: CompletionInfoPrivate = ...
    def __init__(
        self,
        accept_focus: bool = ...,
        application: Gtk.Application = ...,
        attached_to: Gtk.Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        focus_on_map: bool = ...,
        focus_visible: bool = ...,
        gravity: Gdk.Gravity = ...,
        has_resize_grip: bool = ...,
        hide_titlebar_when_maximized: bool = ...,
        icon: GdkPixbuf.Pixbuf = ...,
        icon_name: str = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        role: str = ...,
        screen: Gdk.Screen = ...,
        skip_pager_hint: bool = ...,
        skip_taskbar_hint: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: Gtk.Window = ...,
        type: Gtk.WindowType = ...,
        type_hint: Gdk.WindowTypeHint = ...,
        urgency_hint: bool = ...,
        window_position: Gtk.WindowPosition = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Gtk.Style = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def move_to_iter(
        self, view: Gtk.TextView, iter: Optional[Gtk.TextIter] = None
    ) -> None: ...
    @classmethod
    def new(cls) -> CompletionInfo: ...

class CompletionInfoClass(GObject.GPointer):
    parent_class: Gtk.WindowClass = ...
    padding: list[None] = ...

class CompletionInfoPrivate(GObject.GPointer): ...

class CompletionItem(GObject.Object, CompletionProposal):
    class Props:
        gicon: Gio.Icon
        icon: GdkPixbuf.Pixbuf
        icon_name: str
        info: str
        label: str
        markup: str
        text: str
    props: Props = ...
    parent: GObject.Object = ...
    priv: CompletionItemPrivate = ...
    def __init__(
        self,
        gicon: Gio.Icon = ...,
        icon: GdkPixbuf.Pixbuf = ...,
        icon_name: str = ...,
        info: str = ...,
        label: str = ...,
        markup: str = ...,
        text: str = ...,
    ): ...
    @classmethod
    def new(cls) -> CompletionItem: ...
    def set_gicon(self, gicon: Optional[Gio.Icon] = None) -> None: ...
    def set_icon(self, icon: Optional[GdkPixbuf.Pixbuf] = None) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_info(self, info: Optional[str] = None) -> None: ...
    def set_label(self, label: Optional[str] = None) -> None: ...
    def set_markup(self, markup: Optional[str] = None) -> None: ...
    def set_text(self, text: Optional[str] = None) -> None: ...

class CompletionItemClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class CompletionItemPrivate(GObject.GPointer): ...
class CompletionPrivate(GObject.GPointer): ...

class CompletionProposal(GObject.GInterface):
    def changed(self) -> None: ...
    def equal(self, other: CompletionProposal) -> bool: ...
    def get_gicon(self) -> Optional[Gio.Icon]: ...
    def get_icon(self) -> Optional[GdkPixbuf.Pixbuf]: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_info(self) -> Optional[str]: ...
    def get_label(self) -> str: ...
    def get_markup(self) -> str: ...
    def get_text(self) -> str: ...
    def hash(self) -> int: ...

class CompletionProposalIface(GObject.GPointer):
    parent: GObject.TypeInterface = ...
    get_label: Callable[[CompletionProposal], str] = ...
    get_markup: Callable[[CompletionProposal], str] = ...
    get_text: Callable[[CompletionProposal], str] = ...
    get_icon: Callable[[CompletionProposal], Optional[GdkPixbuf.Pixbuf]] = ...
    get_icon_name: Callable[[CompletionProposal], Optional[str]] = ...
    get_gicon: Callable[[CompletionProposal], Optional[Gio.Icon]] = ...
    get_info: Callable[[CompletionProposal], Optional[str]] = ...
    hash: Callable[[CompletionProposal], int] = ...
    equal: Callable[[CompletionProposal, CompletionProposal], bool] = ...
    changed: Callable[[CompletionProposal], None] = ...

class CompletionProvider(GObject.GInterface):
    def activate_proposal(
        self, proposal: CompletionProposal, iter: Gtk.TextIter
    ) -> bool: ...
    def get_activation(self) -> CompletionActivation: ...
    def get_gicon(self) -> Optional[Gio.Icon]: ...
    def get_icon(self) -> Optional[GdkPixbuf.Pixbuf]: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_info_widget(self, proposal: CompletionProposal) -> Optional[Gtk.Widget]: ...
    def get_interactive_delay(self) -> int: ...
    def get_name(self) -> str: ...
    def get_priority(self) -> int: ...
    def get_start_iter(
        self, context: CompletionContext, proposal: CompletionProposal
    ) -> Tuple[bool, Gtk.TextIter]: ...
    def match(self, context: CompletionContext) -> bool: ...
    def populate(self, context: CompletionContext) -> None: ...
    def update_info(
        self, proposal: CompletionProposal, info: CompletionInfo
    ) -> None: ...

class CompletionProviderIface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    get_name: Callable[[CompletionProvider], str] = ...
    get_icon: Callable[[CompletionProvider], Optional[GdkPixbuf.Pixbuf]] = ...
    get_icon_name: Callable[[CompletionProvider], Optional[str]] = ...
    get_gicon: Callable[[CompletionProvider], Optional[Gio.Icon]] = ...
    populate: Callable[[CompletionProvider, CompletionContext], None] = ...
    match: Callable[[CompletionProvider, CompletionContext], bool] = ...
    get_activation: Callable[[CompletionProvider], CompletionActivation] = ...
    get_info_widget: Callable[
        [CompletionProvider, CompletionProposal], Optional[Gtk.Widget]
    ] = ...
    update_info: Callable[
        [CompletionProvider, CompletionProposal, CompletionInfo], None
    ] = ...
    get_start_iter: Callable[
        [CompletionProvider, CompletionContext, CompletionProposal],
        Tuple[bool, Gtk.TextIter],
    ] = ...
    activate_proposal: Callable[
        [CompletionProvider, CompletionProposal, Gtk.TextIter], bool
    ] = ...
    get_interactive_delay: Callable[[CompletionProvider], int] = ...
    get_priority: Callable[[CompletionProvider], int] = ...

class CompletionWords(GObject.Object, CompletionProvider):
    class Props:
        activation: CompletionActivation
        icon: GdkPixbuf.Pixbuf
        interactive_delay: int
        minimum_word_size: int
        name: str
        priority: int
        proposals_batch_size: int
        scan_batch_size: int
    props: Props = ...
    parent: GObject.Object = ...
    priv: CompletionWordsPrivate = ...
    def __init__(
        self,
        activation: CompletionActivation = ...,
        icon: GdkPixbuf.Pixbuf = ...,
        interactive_delay: int = ...,
        minimum_word_size: int = ...,
        name: str = ...,
        priority: int = ...,
        proposals_batch_size: int = ...,
        scan_batch_size: int = ...,
    ): ...
    @classmethod
    def new(
        cls, name: Optional[str] = None, icon: Optional[GdkPixbuf.Pixbuf] = None
    ) -> CompletionWords: ...
    def register(self, buffer: Gtk.TextBuffer) -> None: ...
    def unregister(self, buffer: Gtk.TextBuffer) -> None: ...

class CompletionWordsClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class CompletionWordsPrivate(GObject.GPointer): ...

class Encoding(GObject.GBoxed):
    def copy(self) -> Encoding: ...
    def free(self) -> None: ...
    @staticmethod
    def get_all() -> list[Encoding]: ...
    def get_charset(self) -> str: ...
    @staticmethod
    def get_current() -> Encoding: ...
    @staticmethod
    def get_default_candidates() -> list[Encoding]: ...
    @staticmethod
    def get_from_charset(charset: str) -> Optional[Encoding]: ...
    def get_name(self) -> str: ...
    @staticmethod
    def get_utf8() -> Encoding: ...
    def to_string(self) -> str: ...

class File(GObject.Object):
    class Props:
        compression_type: CompressionType
        encoding: Encoding
        location: Gio.File
        newline_type: NewlineType
        read_only: bool
    props: Props = ...
    parent: GObject.Object = ...
    priv: FilePrivate = ...
    def __init__(self, location: Gio.File = ...): ...
    def check_file_on_disk(self) -> None: ...
    def get_compression_type(self) -> CompressionType: ...
    def get_encoding(self) -> Encoding: ...
    def get_location(self) -> Gio.File: ...
    def get_newline_type(self) -> NewlineType: ...
    def is_deleted(self) -> bool: ...
    def is_externally_modified(self) -> bool: ...
    def is_local(self) -> bool: ...
    def is_readonly(self) -> bool: ...
    @classmethod
    def new(cls) -> File: ...
    def set_location(self, location: Optional[Gio.File] = None) -> None: ...

class FileClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class FileLoader(GObject.Object):
    class Props:
        buffer: Buffer
        file: File
        input_stream: Gio.InputStream
        location: Gio.File
    props: Props = ...
    parent: GObject.Object = ...
    priv: FileLoaderPrivate = ...
    def __init__(
        self,
        buffer: Buffer = ...,
        file: File = ...,
        input_stream: Gio.InputStream = ...,
        location: Gio.File = ...,
    ): ...
    def get_buffer(self) -> Buffer: ...
    def get_compression_type(self) -> CompressionType: ...
    def get_encoding(self) -> Encoding: ...
    def get_file(self) -> File: ...
    def get_input_stream(self) -> Optional[Gio.InputStream]: ...
    def get_location(self) -> Optional[Gio.File]: ...
    def get_newline_type(self) -> NewlineType: ...
    def load_async(
        self,
        io_priority: int,
        cancellable: Optional[Gio.Cancellable] = None,
        progress_callback: Optional[Callable[..., None]] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def load_finish(self, result: Gio.AsyncResult) -> bool: ...
    @classmethod
    def new(cls, buffer: Buffer, file: File) -> FileLoader: ...
    @classmethod
    def new_from_stream(
        cls, buffer: Buffer, file: File, stream: Gio.InputStream
    ) -> FileLoader: ...
    def set_candidate_encodings(self, candidate_encodings: list[Encoding]) -> None: ...

class FileLoaderClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class FileLoaderPrivate(GObject.GPointer): ...
class FilePrivate(GObject.GPointer): ...

class FileSaver(GObject.Object):
    class Props:
        buffer: Buffer
        compression_type: CompressionType
        encoding: Encoding
        file: File
        flags: FileSaverFlags
        location: Gio.File
        newline_type: NewlineType
    props: Props = ...
    object: GObject.Object = ...
    priv: FileSaverPrivate = ...
    def __init__(
        self,
        buffer: Buffer = ...,
        compression_type: CompressionType = ...,
        encoding: Encoding = ...,
        file: File = ...,
        flags: FileSaverFlags = ...,
        location: Gio.File = ...,
        newline_type: NewlineType = ...,
    ): ...
    def get_buffer(self) -> Buffer: ...
    def get_compression_type(self) -> CompressionType: ...
    def get_encoding(self) -> Encoding: ...
    def get_file(self) -> File: ...
    def get_flags(self) -> FileSaverFlags: ...
    def get_location(self) -> Gio.File: ...
    def get_newline_type(self) -> NewlineType: ...
    @classmethod
    def new(cls, buffer: Buffer, file: File) -> FileSaver: ...
    @classmethod
    def new_with_target(
        cls, buffer: Buffer, file: File, target_location: Gio.File
    ) -> FileSaver: ...
    def save_async(
        self,
        io_priority: int,
        cancellable: Optional[Gio.Cancellable] = None,
        progress_callback: Optional[Callable[..., None]] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def save_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_compression_type(self, compression_type: CompressionType) -> None: ...
    def set_encoding(self, encoding: Optional[Encoding] = None) -> None: ...
    def set_flags(self, flags: FileSaverFlags) -> None: ...
    def set_newline_type(self, newline_type: NewlineType) -> None: ...

class FileSaverClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class FileSaverPrivate(GObject.GPointer): ...

class Gutter(GObject.Object):
    class Props:
        view: View
        window_type: Gtk.TextWindowType
    props: Props = ...
    parent: GObject.Object = ...
    priv: GutterPrivate = ...
    def __init__(self, view: View = ..., window_type: Gtk.TextWindowType = ...): ...
    def get_renderer_at_pos(self, x: int, y: int) -> Optional[GutterRenderer]: ...
    def get_view(self) -> View: ...
    def get_window_type(self) -> Gtk.TextWindowType: ...
    def insert(self, renderer: GutterRenderer, position: int) -> bool: ...
    def queue_draw(self) -> None: ...
    def remove(self, renderer: GutterRenderer) -> None: ...
    def reorder(self, renderer: GutterRenderer, position: int) -> None: ...

class GutterClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class GutterPrivate(GObject.GPointer): ...

class GutterRenderer(GObject.InitiallyUnowned):
    class Props:
        alignment_mode: GutterRendererAlignmentMode
        background_rgba: Gdk.RGBA
        background_set: bool
        size: int
        view: Gtk.TextView
        visible: bool
        window_type: Gtk.TextWindowType
        xalign: float
        xpad: int
        yalign: float
        ypad: int
    props: Props = ...
    parent: GObject.InitiallyUnowned = ...
    priv: GutterRendererPrivate = ...
    def __init__(
        self,
        alignment_mode: GutterRendererAlignmentMode = ...,
        background_rgba: Gdk.RGBA = ...,
        background_set: bool = ...,
        size: int = ...,
        visible: bool = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ): ...
    def activate(
        self, iter: Gtk.TextIter, area: Gdk.Rectangle, event: Gdk.Event
    ) -> None: ...
    def begin(
        self,
        cr: cairo.Context[_SomeSurface],
        background_area: Gdk.Rectangle,
        cell_area: Gdk.Rectangle,
        start: Gtk.TextIter,
        end: Gtk.TextIter,
    ) -> None: ...
    def do_activate(
        self, iter: Gtk.TextIter, area: Gdk.Rectangle, event: Gdk.Event
    ) -> None: ...
    def do_begin(
        self,
        cr: cairo.Context[_SomeSurface],
        background_area: Gdk.Rectangle,
        cell_area: Gdk.Rectangle,
        start: Gtk.TextIter,
        end: Gtk.TextIter,
    ) -> None: ...
    def do_change_buffer(self, old_buffer: Optional[Gtk.TextBuffer] = None) -> None: ...
    def do_change_view(self, old_view: Optional[Gtk.TextView] = None) -> None: ...
    def do_draw(
        self,
        cr: cairo.Context[_SomeSurface],
        background_area: Gdk.Rectangle,
        cell_area: Gdk.Rectangle,
        start: Gtk.TextIter,
        end: Gtk.TextIter,
        state: GutterRendererState,
    ) -> None: ...
    def do_end(self) -> None: ...
    def do_query_activatable(
        self, iter: Gtk.TextIter, area: Gdk.Rectangle, event: Gdk.Event
    ) -> bool: ...
    def do_query_data(
        self, start: Gtk.TextIter, end: Gtk.TextIter, state: GutterRendererState
    ) -> None: ...
    def do_query_tooltip(
        self,
        iter: Gtk.TextIter,
        area: Gdk.Rectangle,
        x: int,
        y: int,
        tooltip: Gtk.Tooltip,
    ) -> bool: ...
    def do_queue_draw(self) -> None: ...
    def draw(
        self,
        cr: cairo.Context[_SomeSurface],
        background_area: Gdk.Rectangle,
        cell_area: Gdk.Rectangle,
        start: Gtk.TextIter,
        end: Gtk.TextIter,
        state: GutterRendererState,
    ) -> None: ...
    def end(self) -> None: ...
    def get_alignment(self) -> Tuple[float, float]: ...
    def get_alignment_mode(self) -> GutterRendererAlignmentMode: ...
    def get_background(self) -> Tuple[bool, Gdk.RGBA]: ...
    def get_padding(self) -> Tuple[int, int]: ...
    def get_size(self) -> int: ...
    def get_view(self) -> Gtk.TextView: ...
    def get_visible(self) -> bool: ...
    def get_window_type(self) -> Gtk.TextWindowType: ...
    def query_activatable(
        self, iter: Gtk.TextIter, area: Gdk.Rectangle, event: Gdk.Event
    ) -> bool: ...
    def query_data(
        self, start: Gtk.TextIter, end: Gtk.TextIter, state: GutterRendererState
    ) -> None: ...
    def query_tooltip(
        self,
        iter: Gtk.TextIter,
        area: Gdk.Rectangle,
        x: int,
        y: int,
        tooltip: Gtk.Tooltip,
    ) -> bool: ...
    def queue_draw(self) -> None: ...
    def set_alignment(self, xalign: float, yalign: float) -> None: ...
    def set_alignment_mode(self, mode: GutterRendererAlignmentMode) -> None: ...
    def set_background(self, color: Optional[Gdk.RGBA] = None) -> None: ...
    def set_padding(self, xpad: int, ypad: int) -> None: ...
    def set_size(self, size: int) -> None: ...
    def set_visible(self, visible: bool) -> None: ...

class GutterRendererClass(GObject.GPointer):
    parent_class: GObject.InitiallyUnownedClass = ...
    begin: Callable[
        [
            GutterRenderer,
            cairo.Context[_SomeSurface],
            Gdk.Rectangle,
            Gdk.Rectangle,
            Gtk.TextIter,
            Gtk.TextIter,
        ],
        None,
    ] = ...
    draw: Callable[
        [
            GutterRenderer,
            cairo.Context[_SomeSurface],
            Gdk.Rectangle,
            Gdk.Rectangle,
            Gtk.TextIter,
            Gtk.TextIter,
            GutterRendererState,
        ],
        None,
    ] = ...
    end: Callable[[GutterRenderer], None] = ...
    change_view: Callable[[GutterRenderer, Optional[Gtk.TextView]], None] = ...
    change_buffer: Callable[[GutterRenderer, Optional[Gtk.TextBuffer]], None] = ...
    query_activatable: Callable[
        [GutterRenderer, Gtk.TextIter, Gdk.Rectangle, Gdk.Event], bool
    ] = ...
    activate: Callable[
        [GutterRenderer, Gtk.TextIter, Gdk.Rectangle, Gdk.Event], None
    ] = ...
    queue_draw: Callable[[GutterRenderer], None] = ...
    query_tooltip: Callable[
        [GutterRenderer, Gtk.TextIter, Gdk.Rectangle, int, int, Gtk.Tooltip], bool
    ] = ...
    query_data: Callable[
        [GutterRenderer, Gtk.TextIter, Gtk.TextIter, GutterRendererState], None
    ] = ...
    padding: list[None] = ...

class GutterRendererPixbuf(GutterRenderer):
    class Props:
        gicon: Gio.Icon
        icon_name: str
        pixbuf: GdkPixbuf.Pixbuf
        alignment_mode: GutterRendererAlignmentMode
        background_rgba: Gdk.RGBA
        background_set: bool
        size: int
        view: Gtk.TextView
        visible: bool
        window_type: Gtk.TextWindowType
        xalign: float
        xpad: int
        yalign: float
        ypad: int
    props: Props = ...
    parent: GutterRenderer = ...
    priv: GutterRendererPixbufPrivate = ...
    def __init__(
        self,
        gicon: Gio.Icon = ...,
        icon_name: str = ...,
        pixbuf: GdkPixbuf.Pixbuf = ...,
        alignment_mode: GutterRendererAlignmentMode = ...,
        background_rgba: Gdk.RGBA = ...,
        background_set: bool = ...,
        size: int = ...,
        visible: bool = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ): ...
    def get_gicon(self) -> Gio.Icon: ...
    def get_icon_name(self) -> str: ...
    def get_pixbuf(self) -> GdkPixbuf.Pixbuf: ...
    @classmethod
    def new(cls) -> GutterRendererPixbuf: ...
    def set_gicon(self, icon: Optional[Gio.Icon] = None) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_pixbuf(self, pixbuf: Optional[GdkPixbuf.Pixbuf] = None) -> None: ...

class GutterRendererPixbufClass(GObject.GPointer):
    parent_class: GutterRendererClass = ...
    padding: list[None] = ...

class GutterRendererPixbufPrivate(GObject.GPointer): ...
class GutterRendererPrivate(GObject.GPointer): ...

class GutterRendererText(GutterRenderer):
    class Props:
        markup: str
        text: str
        alignment_mode: GutterRendererAlignmentMode
        background_rgba: Gdk.RGBA
        background_set: bool
        size: int
        view: Gtk.TextView
        visible: bool
        window_type: Gtk.TextWindowType
        xalign: float
        xpad: int
        yalign: float
        ypad: int
    props: Props = ...
    parent: GutterRenderer = ...
    priv: GutterRendererTextPrivate = ...
    def __init__(
        self,
        markup: str = ...,
        text: str = ...,
        alignment_mode: GutterRendererAlignmentMode = ...,
        background_rgba: Gdk.RGBA = ...,
        background_set: bool = ...,
        size: int = ...,
        visible: bool = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ): ...
    def measure(self, text: str) -> Tuple[int, int]: ...
    def measure_markup(self, markup: str) -> Tuple[int, int]: ...
    @classmethod
    def new(cls) -> GutterRendererText: ...
    def set_markup(self, markup: str, length: int) -> None: ...
    def set_text(self, text: str, length: int) -> None: ...

class GutterRendererTextClass(GObject.GPointer):
    parent_class: GutterRendererClass = ...
    padding: list[None] = ...

class GutterRendererTextPrivate(GObject.GPointer): ...

class Language(GObject.Object):
    class Props:
        hidden: bool
        id: str
        name: str
        section: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: LanguagePrivate = ...
    def get_globs(self) -> Optional[list[str]]: ...
    def get_hidden(self) -> bool: ...
    def get_id(self) -> str: ...
    def get_metadata(self, name: str) -> Optional[str]: ...
    def get_mime_types(self) -> Optional[list[str]]: ...
    def get_name(self) -> str: ...
    def get_section(self) -> str: ...
    def get_style_fallback(self, style_id: str) -> Optional[str]: ...
    def get_style_ids(self) -> Optional[list[str]]: ...
    def get_style_name(self, style_id: str) -> Optional[str]: ...

class LanguageClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class LanguageManager(GObject.Object):
    class Props:
        language_ids: list[str]
        search_path: list[str]
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: LanguageManagerPrivate = ...
    def __init__(self, search_path: Sequence[str] = ...): ...
    @staticmethod
    def get_default() -> LanguageManager: ...
    def get_language(self, id: str) -> Optional[Language]: ...
    def get_language_ids(self) -> Optional[list[str]]: ...
    def get_search_path(self) -> list[str]: ...
    def guess_language(
        self, filename: Optional[str] = None, content_type: Optional[str] = None
    ) -> Optional[Language]: ...
    @classmethod
    def new(cls) -> LanguageManager: ...
    def set_search_path(self, dirs: Optional[Sequence[str]] = None) -> None: ...

class LanguageManagerClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class LanguageManagerPrivate(GObject.GPointer): ...
class LanguagePrivate(GObject.GPointer): ...

class Map(View, Atk.ImplementorIface, Gtk.Buildable, Gtk.Scrollable):
    class Props:
        font_desc: Pango.FontDescription
        view: View
        auto_indent: bool
        background_pattern: BackgroundPatternType
        completion: Completion
        highlight_current_line: bool
        indent_on_tab: bool
        indent_width: int
        insert_spaces_instead_of_tabs: bool
        right_margin_position: int
        show_line_marks: bool
        show_line_numbers: bool
        show_right_margin: bool
        smart_backspace: bool
        smart_home_end: SmartHomeEndType
        space_drawer: SpaceDrawer
        tab_width: int
        accepts_tab: bool
        bottom_margin: int
        buffer: Gtk.TextBuffer
        cursor_visible: bool
        editable: bool
        im_module: str
        indent: int
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
        justification: Gtk.Justification
        left_margin: int
        monospace: bool
        overwrite: bool
        pixels_above_lines: int
        pixels_below_lines: int
        pixels_inside_wrap: int
        populate_all: bool
        right_margin: int
        tabs: Pango.TabArray
        top_margin: int
        wrap_mode: Gtk.WrapMode
        border_width: int
        child: Gtk.Widget
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Gtk.Container
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Gdk.Window
        hadjustment: Gtk.Adjustment
        hscroll_policy: Gtk.ScrollablePolicy
        vadjustment: Gtk.Adjustment
        vscroll_policy: Gtk.ScrollablePolicy
    props: Props = ...
    parent_instance: View = ...
    def __init__(
        self,
        font_desc: Pango.FontDescription = ...,
        view: View = ...,
        auto_indent: bool = ...,
        background_pattern: BackgroundPatternType = ...,
        highlight_current_line: bool = ...,
        indent_on_tab: bool = ...,
        indent_width: int = ...,
        insert_spaces_instead_of_tabs: bool = ...,
        right_margin_position: int = ...,
        show_line_marks: bool = ...,
        show_line_numbers: bool = ...,
        show_right_margin: bool = ...,
        smart_backspace: bool = ...,
        smart_home_end: SmartHomeEndType = ...,
        tab_width: int = ...,
        accepts_tab: bool = ...,
        bottom_margin: int = ...,
        buffer: Gtk.TextBuffer = ...,
        cursor_visible: bool = ...,
        editable: bool = ...,
        im_module: str = ...,
        indent: int = ...,
        input_hints: Gtk.InputHints = ...,
        input_purpose: Gtk.InputPurpose = ...,
        justification: Gtk.Justification = ...,
        left_margin: int = ...,
        monospace: bool = ...,
        overwrite: bool = ...,
        pixels_above_lines: int = ...,
        pixels_below_lines: int = ...,
        pixels_inside_wrap: int = ...,
        populate_all: bool = ...,
        right_margin: int = ...,
        tabs: Pango.TabArray = ...,
        top_margin: int = ...,
        wrap_mode: Gtk.WrapMode = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Gtk.Style = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        hadjustment: Gtk.Adjustment = ...,
        hscroll_policy: Gtk.ScrollablePolicy = ...,
        vadjustment: Gtk.Adjustment = ...,
        vscroll_policy: Gtk.ScrollablePolicy = ...,
    ): ...
    def get_view(self) -> Optional[View]: ...
    @classmethod
    def new(cls) -> Map: ...
    def set_view(self, view: View) -> None: ...

class MapClass(GObject.GPointer):
    parent_class: ViewClass = ...
    padding: list[None] = ...

class Mark(Gtk.TextMark):
    class Props:
        category: str
        left_gravity: bool
        name: str
    props: Props = ...
    parent_instance: Gtk.TextMark = ...
    priv: MarkPrivate = ...
    def __init__(
        self, category: str = ..., left_gravity: bool = ..., name: str = ...
    ): ...
    def get_category(self) -> str: ...
    @classmethod
    def new(cls, name: Optional[str], category: str) -> Mark: ...
    def next(self, category: Optional[str] = None) -> Optional[Mark]: ...
    def prev(self, category: str) -> Optional[Mark]: ...

class MarkAttributes(GObject.Object):
    class Props:
        background: Gdk.RGBA
        gicon: Gio.Icon
        icon_name: str
        pixbuf: GdkPixbuf.Pixbuf
    props: Props = ...
    parent: GObject.Object = ...
    priv: MarkAttributesPrivate = ...
    def __init__(
        self,
        background: Gdk.RGBA = ...,
        gicon: Gio.Icon = ...,
        icon_name: str = ...,
        pixbuf: GdkPixbuf.Pixbuf = ...,
    ): ...
    def get_background(self) -> Tuple[bool, Gdk.RGBA]: ...
    def get_gicon(self) -> Gio.Icon: ...
    def get_icon_name(self) -> str: ...
    def get_pixbuf(self) -> GdkPixbuf.Pixbuf: ...
    def get_tooltip_markup(self, mark: Mark) -> str: ...
    def get_tooltip_text(self, mark: Mark) -> str: ...
    @classmethod
    def new(cls) -> MarkAttributes: ...
    def render_icon(self, widget: Gtk.Widget, size: int) -> GdkPixbuf.Pixbuf: ...
    def set_background(self, background: Gdk.RGBA) -> None: ...
    def set_gicon(self, gicon: Gio.Icon) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_pixbuf(self, pixbuf: GdkPixbuf.Pixbuf) -> None: ...

class MarkAttributesClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class MarkAttributesPrivate(GObject.GPointer): ...

class MarkClass(GObject.GPointer):
    parent_class: Gtk.TextMarkClass = ...
    padding: list[None] = ...

class MarkPrivate(GObject.GPointer): ...

class PrintCompositor(GObject.Object):
    class Props:
        body_font_name: str
        buffer: Buffer
        footer_font_name: str
        header_font_name: str
        highlight_syntax: bool
        line_numbers_font_name: str
        n_pages: int
        print_footer: bool
        print_header: bool
        print_line_numbers: int
        tab_width: int
        wrap_mode: Gtk.WrapMode
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: PrintCompositorPrivate = ...
    def __init__(
        self,
        body_font_name: str = ...,
        buffer: Buffer = ...,
        footer_font_name: str = ...,
        header_font_name: str = ...,
        highlight_syntax: bool = ...,
        line_numbers_font_name: str = ...,
        print_footer: bool = ...,
        print_header: bool = ...,
        print_line_numbers: int = ...,
        tab_width: int = ...,
        wrap_mode: Gtk.WrapMode = ...,
    ): ...
    def draw_page(self, context: Gtk.PrintContext, page_nr: int) -> None: ...
    def get_body_font_name(self) -> str: ...
    def get_bottom_margin(self, unit: Gtk.Unit) -> float: ...
    def get_buffer(self) -> Buffer: ...
    def get_footer_font_name(self) -> str: ...
    def get_header_font_name(self) -> str: ...
    def get_highlight_syntax(self) -> bool: ...
    def get_left_margin(self, unit: Gtk.Unit) -> float: ...
    def get_line_numbers_font_name(self) -> str: ...
    def get_n_pages(self) -> int: ...
    def get_pagination_progress(self) -> float: ...
    def get_print_footer(self) -> bool: ...
    def get_print_header(self) -> bool: ...
    def get_print_line_numbers(self) -> int: ...
    def get_right_margin(self, unit: Gtk.Unit) -> float: ...
    def get_tab_width(self) -> int: ...
    def get_top_margin(self, unit: Gtk.Unit) -> float: ...
    def get_wrap_mode(self) -> Gtk.WrapMode: ...
    @classmethod
    def new(cls, buffer: Buffer) -> PrintCompositor: ...
    @classmethod
    def new_from_view(cls, view: View) -> PrintCompositor: ...
    def paginate(self, context: Gtk.PrintContext) -> bool: ...
    def set_body_font_name(self, font_name: str) -> None: ...
    def set_bottom_margin(self, margin: float, unit: Gtk.Unit) -> None: ...
    def set_footer_font_name(self, font_name: Optional[str] = None) -> None: ...
    def set_footer_format(
        self,
        separator: bool,
        left: Optional[str] = None,
        center: Optional[str] = None,
        right: Optional[str] = None,
    ) -> None: ...
    def set_header_font_name(self, font_name: Optional[str] = None) -> None: ...
    def set_header_format(
        self,
        separator: bool,
        left: Optional[str] = None,
        center: Optional[str] = None,
        right: Optional[str] = None,
    ) -> None: ...
    def set_highlight_syntax(self, highlight: bool) -> None: ...
    def set_left_margin(self, margin: float, unit: Gtk.Unit) -> None: ...
    def set_line_numbers_font_name(self, font_name: Optional[str] = None) -> None: ...
    def set_print_footer(self, print_: bool) -> None: ...
    def set_print_header(self, print_: bool) -> None: ...
    def set_print_line_numbers(self, interval: int) -> None: ...
    def set_right_margin(self, margin: float, unit: Gtk.Unit) -> None: ...
    def set_tab_width(self, width: int) -> None: ...
    def set_top_margin(self, margin: float, unit: Gtk.Unit) -> None: ...
    def set_wrap_mode(self, wrap_mode: Gtk.WrapMode) -> None: ...

class PrintCompositorClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class PrintCompositorPrivate(GObject.GPointer): ...

class Region(GObject.Object):
    class Props:
        buffer: Gtk.TextBuffer
    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, buffer: Gtk.TextBuffer = ...): ...
    def add_region(self, region_to_add: Optional[Region] = None) -> None: ...
    def add_subregion(self, _start: Gtk.TextIter, _end: Gtk.TextIter) -> None: ...
    def get_bounds(self) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter]: ...
    def get_buffer(self) -> Optional[Gtk.TextBuffer]: ...
    def get_start_region_iter(self) -> RegionIter: ...
    def intersect_region(
        self, region2: Optional[Region] = None
    ) -> Optional[Region]: ...
    def intersect_subregion(
        self, _start: Gtk.TextIter, _end: Gtk.TextIter
    ) -> Optional[Region]: ...
    def is_empty(self) -> bool: ...
    @classmethod
    def new(cls, buffer: Gtk.TextBuffer) -> Region: ...
    def subtract_region(self, region_to_subtract: Optional[Region] = None) -> None: ...
    def subtract_subregion(self, _start: Gtk.TextIter, _end: Gtk.TextIter) -> None: ...
    def to_string(self) -> Optional[str]: ...

class RegionClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class RegionIter(GObject.GPointer):
    dummy1: None = ...
    dummy2: int = ...
    dummy3: None = ...
    def get_subregion(self) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter]: ...
    def is_end(self) -> bool: ...
    def next(self) -> bool: ...

class SearchContext(GObject.Object):
    class Props:
        buffer: Buffer
        highlight: bool
        match_style: Style
        occurrences_count: int
        regex_error: None
        settings: SearchSettings
    props: Props = ...
    parent: GObject.Object = ...
    priv: SearchContextPrivate = ...
    def __init__(
        self,
        buffer: Buffer = ...,
        highlight: bool = ...,
        match_style: Style = ...,
        settings: SearchSettings = ...,
    ): ...
    def backward(
        self, iter: Gtk.TextIter
    ) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter, bool]: ...
    def backward_async(
        self,
        iter: Gtk.TextIter,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def backward_finish(
        self, result: Gio.AsyncResult
    ) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter, bool]: ...
    def forward(
        self, iter: Gtk.TextIter
    ) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter, bool]: ...
    def forward_async(
        self,
        iter: Gtk.TextIter,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def forward_finish(
        self, result: Gio.AsyncResult
    ) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter, bool]: ...
    def get_buffer(self) -> Buffer: ...
    def get_highlight(self) -> bool: ...
    def get_match_style(self) -> Style: ...
    def get_occurrence_position(
        self, match_start: Gtk.TextIter, match_end: Gtk.TextIter
    ) -> int: ...
    def get_occurrences_count(self) -> int: ...
    def get_regex_error(self) -> Optional[GLib.Error]: ...
    def get_settings(self) -> SearchSettings: ...
    @classmethod
    def new(
        cls, buffer: Buffer, settings: Optional[SearchSettings] = None
    ) -> SearchContext: ...
    def replace(
        self,
        match_start: Gtk.TextIter,
        match_end: Gtk.TextIter,
        replace: str,
        replace_length: int,
    ) -> bool: ...
    def replace_all(self, replace: str, replace_length: int) -> int: ...
    def set_highlight(self, highlight: bool) -> None: ...
    def set_match_style(self, match_style: Optional[Style] = None) -> None: ...

class SearchContextClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class SearchContextPrivate(GObject.GPointer): ...

class SearchSettings(GObject.Object):
    class Props:
        at_word_boundaries: bool
        case_sensitive: bool
        regex_enabled: bool
        search_text: str
        wrap_around: bool
    props: Props = ...
    parent: GObject.Object = ...
    priv: SearchSettingsPrivate = ...
    def __init__(
        self,
        at_word_boundaries: bool = ...,
        case_sensitive: bool = ...,
        regex_enabled: bool = ...,
        search_text: str = ...,
        wrap_around: bool = ...,
    ): ...
    def get_at_word_boundaries(self) -> bool: ...
    def get_case_sensitive(self) -> bool: ...
    def get_regex_enabled(self) -> bool: ...
    def get_search_text(self) -> Optional[str]: ...
    def get_wrap_around(self) -> bool: ...
    @classmethod
    def new(cls) -> SearchSettings: ...
    def set_at_word_boundaries(self, at_word_boundaries: bool) -> None: ...
    def set_case_sensitive(self, case_sensitive: bool) -> None: ...
    def set_regex_enabled(self, regex_enabled: bool) -> None: ...
    def set_search_text(self, search_text: Optional[str] = None) -> None: ...
    def set_wrap_around(self, wrap_around: bool) -> None: ...

class SearchSettingsClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class SearchSettingsPrivate(GObject.GPointer): ...

class SpaceDrawer(GObject.Object):
    class Props:
        enable_matrix: bool
        matrix: GLib.Variant
    props: Props = ...
    parent: GObject.Object = ...
    priv: SpaceDrawerPrivate = ...
    def __init__(self, enable_matrix: bool = ..., matrix: GLib.Variant = ...): ...
    def bind_matrix_setting(
        self, settings: Gio.Settings, key: str, flags: Gio.SettingsBindFlags
    ) -> None: ...
    def get_enable_matrix(self) -> bool: ...
    def get_matrix(self) -> GLib.Variant: ...
    def get_types_for_locations(
        self, locations: SpaceLocationFlags
    ) -> SpaceTypeFlags: ...
    @classmethod
    def new(cls) -> SpaceDrawer: ...
    def set_enable_matrix(self, enable_matrix: bool) -> None: ...
    def set_matrix(self, matrix: Optional[GLib.Variant] = None) -> None: ...
    def set_types_for_locations(
        self, locations: SpaceLocationFlags, types: SpaceTypeFlags
    ) -> None: ...

class SpaceDrawerClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class SpaceDrawerPrivate(GObject.GPointer): ...

class Style(GObject.Object):
    class Props:
        background: str
        background_set: bool
        bold: bool
        bold_set: bool
        foreground: str
        foreground_set: bool
        italic: bool
        italic_set: bool
        line_background: str
        line_background_set: bool
        pango_underline: Pango.Underline
        scale: str
        scale_set: bool
        strikethrough: bool
        strikethrough_set: bool
        underline_color: str
        underline_color_set: bool
        underline_set: bool
    props: Props = ...
    def __init__(
        self,
        background: str = ...,
        background_set: bool = ...,
        bold: bool = ...,
        bold_set: bool = ...,
        foreground: str = ...,
        foreground_set: bool = ...,
        italic: bool = ...,
        italic_set: bool = ...,
        line_background: str = ...,
        line_background_set: bool = ...,
        pango_underline: Pango.Underline = ...,
        scale: str = ...,
        scale_set: bool = ...,
        strikethrough: bool = ...,
        strikethrough_set: bool = ...,
        underline_color: str = ...,
        underline_color_set: bool = ...,
        underline_set: bool = ...,
    ): ...
    def apply(self, tag: Gtk.TextTag) -> None: ...
    def copy(self) -> Style: ...

class StyleClass(GObject.GPointer): ...

class StyleScheme(GObject.Object):
    class Props:
        description: str
        filename: str
        id: str
        name: str
    props: Props = ...
    base: GObject.Object = ...
    priv: StyleSchemePrivate = ...
    def __init__(self, id: str = ...): ...
    def get_authors(self) -> Optional[list[str]]: ...
    def get_description(self) -> Optional[str]: ...
    def get_filename(self) -> Optional[str]: ...
    def get_id(self) -> str: ...
    def get_name(self) -> str: ...
    def get_style(self, style_id: str) -> Optional[Style]: ...

class StyleSchemeChooser(GObject.GInterface):
    def get_style_scheme(self) -> StyleScheme: ...
    def set_style_scheme(self, scheme: StyleScheme) -> None: ...

class StyleSchemeChooserButton(
    Gtk.Button,
    Atk.ImplementorIface,
    Gtk.Actionable,
    Gtk.Activatable,
    Gtk.Buildable,
    StyleSchemeChooser,
):
    class Props:
        always_show_image: bool
        image: Gtk.Widget
        image_position: Gtk.PositionType
        label: str
        relief: Gtk.ReliefStyle
        use_stock: bool
        use_underline: bool
        xalign: float
        yalign: float
        border_width: int
        child: Gtk.Widget
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Gtk.Container
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Gdk.Window
        action_name: str
        action_target: GLib.Variant
        related_action: Gtk.Action
        use_action_appearance: bool
        style_scheme: StyleScheme
    props: Props = ...
    parent: Gtk.Button = ...
    def __init__(
        self,
        always_show_image: bool = ...,
        image: Gtk.Widget = ...,
        image_position: Gtk.PositionType = ...,
        label: str = ...,
        relief: Gtk.ReliefStyle = ...,
        use_stock: bool = ...,
        use_underline: bool = ...,
        xalign: float = ...,
        yalign: float = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Gtk.Style = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
        related_action: Gtk.Action = ...,
        use_action_appearance: bool = ...,
        style_scheme: StyleScheme = ...,
    ): ...
    @classmethod
    def new(cls) -> StyleSchemeChooserButton: ...

class StyleSchemeChooserButtonClass(GObject.GPointer):
    parent: Gtk.ButtonClass = ...
    padding: list[None] = ...

class StyleSchemeChooserInterface(GObject.GPointer):
    base_interface: GObject.TypeInterface = ...
    get_style_scheme: Callable[[StyleSchemeChooser], StyleScheme] = ...
    set_style_scheme: Callable[[StyleSchemeChooser, StyleScheme], None] = ...
    padding: list[None] = ...

class StyleSchemeChooserWidget(
    Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable, StyleSchemeChooser
):
    class Props:
        border_width: int
        child: Gtk.Widget
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Gtk.Container
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Gdk.Window
        style_scheme: StyleScheme
    props: Props = ...
    parent: Gtk.Bin = ...
    def __init__(
        self,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Gtk.Style = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        style_scheme: StyleScheme = ...,
    ): ...
    @classmethod
    def new(cls) -> StyleSchemeChooserWidget: ...

class StyleSchemeChooserWidgetClass(GObject.GPointer):
    parent: Gtk.BinClass = ...
    padding: list[None] = ...

class StyleSchemeClass(GObject.GPointer):
    base_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class StyleSchemeManager(GObject.Object):
    class Props:
        scheme_ids: list[str]
        search_path: list[str]
    props: Props = ...
    parent: GObject.Object = ...
    priv: StyleSchemeManagerPrivate = ...
    def __init__(self, search_path: Sequence[str] = ...): ...
    def append_search_path(self, path: str) -> None: ...
    def force_rescan(self) -> None: ...
    @staticmethod
    def get_default() -> StyleSchemeManager: ...
    def get_scheme(self, scheme_id: str) -> Optional[StyleScheme]: ...
    def get_scheme_ids(self) -> Optional[list[str]]: ...
    def get_search_path(self) -> list[str]: ...
    @classmethod
    def new(cls) -> StyleSchemeManager: ...
    def prepend_search_path(self, path: str) -> None: ...
    def set_search_path(self, path: Optional[Sequence[str]] = None) -> None: ...

class StyleSchemeManagerClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class StyleSchemeManagerPrivate(GObject.GPointer): ...
class StyleSchemePrivate(GObject.GPointer): ...

class Tag(Gtk.TextTag):
    class Props:
        draw_spaces: bool
        draw_spaces_set: bool
        accumulative_margin: bool
        background: str
        background_full_height: bool
        background_full_height_set: bool
        background_gdk: Gdk.Color
        background_rgba: Gdk.RGBA
        background_set: bool
        direction: Gtk.TextDirection
        editable: bool
        editable_set: bool
        fallback: bool
        fallback_set: bool
        family: str
        family_set: bool
        font: str
        font_desc: Pango.FontDescription
        font_features: str
        font_features_set: bool
        foreground: str
        foreground_gdk: Gdk.Color
        foreground_rgba: Gdk.RGBA
        foreground_set: bool
        indent: int
        indent_set: bool
        invisible: bool
        invisible_set: bool
        justification: Gtk.Justification
        justification_set: bool
        language: str
        language_set: bool
        left_margin: int
        left_margin_set: bool
        letter_spacing: int
        letter_spacing_set: bool
        name: str
        paragraph_background: str
        paragraph_background_gdk: Gdk.Color
        paragraph_background_rgba: Gdk.RGBA
        paragraph_background_set: bool
        pixels_above_lines: int
        pixels_above_lines_set: bool
        pixels_below_lines: int
        pixels_below_lines_set: bool
        pixels_inside_wrap: int
        pixels_inside_wrap_set: bool
        right_margin: int
        right_margin_set: bool
        rise: int
        rise_set: bool
        scale: float
        scale_set: bool
        size: int
        size_points: float
        size_set: bool
        stretch: Pango.Stretch
        stretch_set: bool
        strikethrough: bool
        strikethrough_rgba: Gdk.RGBA
        strikethrough_rgba_set: bool
        strikethrough_set: bool
        style: Pango.Style
        style_set: bool
        tabs: Pango.TabArray
        tabs_set: bool
        underline: Pango.Underline
        underline_rgba: Gdk.RGBA
        underline_rgba_set: bool
        underline_set: bool
        variant: Pango.Variant
        variant_set: bool
        weight: int
        weight_set: bool
        wrap_mode: Gtk.WrapMode
        wrap_mode_set: bool
    props: Props = ...
    parent_instance: Gtk.TextTag = ...
    def __init__(
        self,
        draw_spaces: bool = ...,
        draw_spaces_set: bool = ...,
        accumulative_margin: bool = ...,
        background: str = ...,
        background_full_height: bool = ...,
        background_full_height_set: bool = ...,
        background_gdk: Gdk.Color = ...,
        background_rgba: Gdk.RGBA = ...,
        background_set: bool = ...,
        direction: Gtk.TextDirection = ...,
        editable: bool = ...,
        editable_set: bool = ...,
        fallback: bool = ...,
        fallback_set: bool = ...,
        family: str = ...,
        family_set: bool = ...,
        font: str = ...,
        font_desc: Pango.FontDescription = ...,
        font_features: str = ...,
        font_features_set: bool = ...,
        foreground: str = ...,
        foreground_gdk: Gdk.Color = ...,
        foreground_rgba: Gdk.RGBA = ...,
        foreground_set: bool = ...,
        indent: int = ...,
        indent_set: bool = ...,
        invisible: bool = ...,
        invisible_set: bool = ...,
        justification: Gtk.Justification = ...,
        justification_set: bool = ...,
        language: str = ...,
        language_set: bool = ...,
        left_margin: int = ...,
        left_margin_set: bool = ...,
        letter_spacing: int = ...,
        letter_spacing_set: bool = ...,
        name: str = ...,
        paragraph_background: str = ...,
        paragraph_background_gdk: Gdk.Color = ...,
        paragraph_background_rgba: Gdk.RGBA = ...,
        paragraph_background_set: bool = ...,
        pixels_above_lines: int = ...,
        pixels_above_lines_set: bool = ...,
        pixels_below_lines: int = ...,
        pixels_below_lines_set: bool = ...,
        pixels_inside_wrap: int = ...,
        pixels_inside_wrap_set: bool = ...,
        right_margin: int = ...,
        right_margin_set: bool = ...,
        rise: int = ...,
        rise_set: bool = ...,
        scale: float = ...,
        scale_set: bool = ...,
        size: int = ...,
        size_points: float = ...,
        size_set: bool = ...,
        stretch: Pango.Stretch = ...,
        stretch_set: bool = ...,
        strikethrough: bool = ...,
        strikethrough_rgba: Gdk.RGBA = ...,
        strikethrough_rgba_set: bool = ...,
        strikethrough_set: bool = ...,
        style: Pango.Style = ...,
        style_set: bool = ...,
        tabs: Pango.TabArray = ...,
        tabs_set: bool = ...,
        underline: Pango.Underline = ...,
        underline_rgba: Gdk.RGBA = ...,
        underline_rgba_set: bool = ...,
        underline_set: bool = ...,
        variant: Pango.Variant = ...,
        variant_set: bool = ...,
        weight: int = ...,
        weight_set: bool = ...,
        wrap_mode: Gtk.WrapMode = ...,
        wrap_mode_set: bool = ...,
    ): ...
    @classmethod
    def new(cls, name: Optional[str] = None) -> Tag: ...

class TagClass(GObject.GPointer):
    parent_class: Gtk.TextTagClass = ...
    padding: list[None] = ...

class UndoManager(GObject.GInterface):
    def begin_not_undoable_action(self) -> None: ...
    def can_redo(self) -> bool: ...
    def can_redo_changed(self) -> None: ...
    def can_undo(self) -> bool: ...
    def can_undo_changed(self) -> None: ...
    def end_not_undoable_action(self) -> None: ...
    def redo(self) -> None: ...
    def undo(self) -> None: ...

class UndoManagerIface(GObject.GPointer):
    parent: GObject.TypeInterface = ...
    can_undo: Callable[[UndoManager], bool] = ...
    can_redo: Callable[[UndoManager], bool] = ...
    undo: Callable[[UndoManager], None] = ...
    redo: Callable[[UndoManager], None] = ...
    begin_not_undoable_action: Callable[[UndoManager], None] = ...
    end_not_undoable_action: Callable[[UndoManager], None] = ...
    can_undo_changed: Callable[[UndoManager], None] = ...
    can_redo_changed: Callable[[UndoManager], None] = ...

class View(Gtk.TextView, Atk.ImplementorIface, Gtk.Buildable, Gtk.Scrollable):
    class Props:
        auto_indent: bool
        background_pattern: BackgroundPatternType
        completion: Completion
        highlight_current_line: bool
        indent_on_tab: bool
        indent_width: int
        insert_spaces_instead_of_tabs: bool
        right_margin_position: int
        show_line_marks: bool
        show_line_numbers: bool
        show_right_margin: bool
        smart_backspace: bool
        smart_home_end: SmartHomeEndType
        space_drawer: SpaceDrawer
        tab_width: int
        accepts_tab: bool
        bottom_margin: int
        buffer: Gtk.TextBuffer
        cursor_visible: bool
        editable: bool
        im_module: str
        indent: int
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
        justification: Gtk.Justification
        left_margin: int
        monospace: bool
        overwrite: bool
        pixels_above_lines: int
        pixels_below_lines: int
        pixels_inside_wrap: int
        populate_all: bool
        right_margin: int
        tabs: Pango.TabArray
        top_margin: int
        wrap_mode: Gtk.WrapMode
        border_width: int
        child: Gtk.Widget
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Gtk.Container
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Gdk.Window
        hadjustment: Gtk.Adjustment
        hscroll_policy: Gtk.ScrollablePolicy
        vadjustment: Gtk.Adjustment
        vscroll_policy: Gtk.ScrollablePolicy
    props: Props = ...
    parent: Gtk.TextView = ...
    priv: ViewPrivate = ...
    def __init__(
        self,
        auto_indent: bool = ...,
        background_pattern: BackgroundPatternType = ...,
        highlight_current_line: bool = ...,
        indent_on_tab: bool = ...,
        indent_width: int = ...,
        insert_spaces_instead_of_tabs: bool = ...,
        right_margin_position: int = ...,
        show_line_marks: bool = ...,
        show_line_numbers: bool = ...,
        show_right_margin: bool = ...,
        smart_backspace: bool = ...,
        smart_home_end: SmartHomeEndType = ...,
        tab_width: int = ...,
        accepts_tab: bool = ...,
        bottom_margin: int = ...,
        buffer: Gtk.TextBuffer = ...,
        cursor_visible: bool = ...,
        editable: bool = ...,
        im_module: str = ...,
        indent: int = ...,
        input_hints: Gtk.InputHints = ...,
        input_purpose: Gtk.InputPurpose = ...,
        justification: Gtk.Justification = ...,
        left_margin: int = ...,
        monospace: bool = ...,
        overwrite: bool = ...,
        pixels_above_lines: int = ...,
        pixels_below_lines: int = ...,
        pixels_inside_wrap: int = ...,
        populate_all: bool = ...,
        right_margin: int = ...,
        tabs: Pango.TabArray = ...,
        top_margin: int = ...,
        wrap_mode: Gtk.WrapMode = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Gtk.Style = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        hadjustment: Gtk.Adjustment = ...,
        hscroll_policy: Gtk.ScrollablePolicy = ...,
        vadjustment: Gtk.Adjustment = ...,
        vscroll_policy: Gtk.ScrollablePolicy = ...,
    ): ...
    def do_line_mark_activated(self, iter: Gtk.TextIter, event: Gdk.Event) -> None: ...
    def do_move_lines(self, down: bool) -> None: ...
    def do_move_words(self, step: int) -> None: ...
    def do_redo(self) -> None: ...
    def do_show_completion(self) -> None: ...
    def do_undo(self) -> None: ...
    def get_auto_indent(self) -> bool: ...
    def get_background_pattern(self) -> BackgroundPatternType: ...
    # override
    def get_buffer(self) -> Buffer: ...
    def get_completion(self) -> Completion: ...
    def get_gutter(self, window_type: Gtk.TextWindowType) -> Gutter: ...
    def get_highlight_current_line(self) -> bool: ...
    def get_indent_on_tab(self) -> bool: ...
    def get_indent_width(self) -> int: ...
    def get_insert_spaces_instead_of_tabs(self) -> bool: ...
    def get_mark_attributes(self, category: str, priority: int) -> MarkAttributes: ...
    def get_right_margin_position(self) -> int: ...
    def get_show_line_marks(self) -> bool: ...
    def get_show_line_numbers(self) -> bool: ...
    def get_show_right_margin(self) -> bool: ...
    def get_smart_backspace(self) -> bool: ...
    def get_smart_home_end(self) -> SmartHomeEndType: ...
    def get_space_drawer(self) -> SpaceDrawer: ...
    def get_tab_width(self) -> int: ...
    def get_visual_column(self, iter: Gtk.TextIter) -> int: ...
    def indent_lines(self, start: Gtk.TextIter, end: Gtk.TextIter) -> None: ...
    @classmethod
    def new(cls) -> View: ...
    @classmethod
    def new_with_buffer(cls, buffer: Buffer) -> View: ...
    def set_auto_indent(self, enable: bool) -> None: ...
    def set_background_pattern(
        self, background_pattern: BackgroundPatternType
    ) -> None: ...
    def set_highlight_current_line(self, highlight: bool) -> None: ...
    def set_indent_on_tab(self, enable: bool) -> None: ...
    def set_indent_width(self, width: int) -> None: ...
    def set_insert_spaces_instead_of_tabs(self, enable: bool) -> None: ...
    def set_mark_attributes(
        self, category: str, attributes: MarkAttributes, priority: int
    ) -> None: ...
    def set_right_margin_position(self, pos: int) -> None: ...
    def set_show_line_marks(self, show: bool) -> None: ...
    def set_show_line_numbers(self, show: bool) -> None: ...
    def set_show_right_margin(self, show: bool) -> None: ...
    def set_smart_backspace(self, smart_backspace: bool) -> None: ...
    def set_smart_home_end(self, smart_home_end: SmartHomeEndType) -> None: ...
    def set_tab_width(self, width: int) -> None: ...
    def unindent_lines(self, start: Gtk.TextIter, end: Gtk.TextIter) -> None: ...

class ViewClass(GObject.GPointer):
    parent_class: Gtk.TextViewClass = ...
    undo: Callable[[View], None] = ...
    redo: Callable[[View], None] = ...
    line_mark_activated: Callable[[View, Gtk.TextIter, Gdk.Event], None] = ...
    show_completion: Callable[[View], None] = ...
    move_lines: Callable[[View, bool], None] = ...
    move_words: Callable[[View, int], None] = ...
    padding: list[None] = ...

class ViewPrivate(GObject.GPointer): ...

class CompletionActivation(GObject.GFlags):
    INTERACTIVE = 1
    NONE = 0
    USER_REQUESTED = 2

class FileSaverFlags(GObject.GFlags):
    CREATE_BACKUP = 4
    IGNORE_INVALID_CHARS = 1
    IGNORE_MODIFICATION_TIME = 2
    NONE = 0

class GutterRendererState(GObject.GFlags):
    CURSOR = 1
    NORMAL = 0
    PRELIT = 2
    SELECTED = 4

class SortFlags(GObject.GFlags):
    CASE_SENSITIVE = 1
    NONE = 0
    REMOVE_DUPLICATES = 4
    REVERSE_ORDER = 2

class SpaceLocationFlags(GObject.GFlags):
    ALL = 7
    INSIDE_TEXT = 2
    LEADING = 1
    NONE = 0
    TRAILING = 4

class SpaceTypeFlags(GObject.GFlags):
    ALL = 15
    NBSP = 8
    NEWLINE = 4
    NONE = 0
    SPACE = 1
    TAB = 2

class BackgroundPatternType(GObject.GEnum):
    GRID = 1
    NONE = 0

class BracketMatchType(GObject.GEnum):
    FOUND = 3
    NONE = 0
    NOT_FOUND = 2
    OUT_OF_RANGE = 1

class ChangeCaseType(GObject.GEnum):
    LOWER = 0
    TITLE = 3
    TOGGLE = 2
    UPPER = 1

class CompletionError(GObject.GEnum):
    ALREADY_BOUND = 0
    NOT_BOUND = 1
    @staticmethod
    def quark() -> int: ...

class CompressionType(GObject.GEnum):
    GZIP = 1
    NONE = 0

class FileLoaderError(GObject.GEnum):
    CONVERSION_FALLBACK = 2
    ENCODING_AUTO_DETECTION_FAILED = 1
    TOO_BIG = 0
    @staticmethod
    def quark() -> int: ...

class FileSaverError(GObject.GEnum):
    EXTERNALLY_MODIFIED = 1
    INVALID_CHARS = 0
    @staticmethod
    def quark() -> int: ...

class GutterRendererAlignmentMode(GObject.GEnum):
    CELL = 0
    FIRST = 1
    LAST = 2

class NewlineType(GObject.GEnum):
    CR = 1
    CR_LF = 2
    LF = 0

class SmartHomeEndType(GObject.GEnum):
    AFTER = 2
    ALWAYS = 3
    BEFORE = 1
    DISABLED = 0

class ViewGutterPosition(GObject.GEnum):
    LINES = -30
    MARKS = -20
