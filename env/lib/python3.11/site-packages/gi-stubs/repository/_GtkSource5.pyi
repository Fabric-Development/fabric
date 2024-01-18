from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type

from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Pango

_namespace: str = "GtkSource"
_version: str = "5"

def encoding_get_all() -> list[Encoding]: ...
def encoding_get_current() -> Encoding: ...
def encoding_get_default_candidates() -> list[Encoding]: ...
def encoding_get_from_charset(charset: str) -> Optional[Encoding]: ...
def encoding_get_utf8() -> Encoding: ...
def file_loader_error_quark() -> int: ...
def file_saver_error_quark() -> int: ...
def finalize() -> None: ...
def init() -> None: ...
def scheduler_add(callback: Callable[..., bool], *user_data: Any) -> int: ...
def scheduler_add_full(callback: Callable[..., bool], *user_data: Any) -> int: ...
def scheduler_remove(handler_id: int) -> None: ...
def utils_escape_search_text(text: str) -> str: ...
def utils_unescape_search_text(text: str) -> str: ...

class Buffer(Gtk.TextBuffer):
    class Props:
        highlight_matching_brackets: bool
        highlight_syntax: bool
        implicit_trailing_newline: bool
        language: Language
        style_scheme: StyleScheme
        can_redo: bool
        can_undo: bool
        cursor_position: int
        enable_undo: bool
        has_selection: bool
        tag_table: Gtk.TextTagTable
        text: str
    props: Props = ...
    parent_instance: Gtk.TextBuffer = ...
    def __init__(
        self,
        highlight_matching_brackets: bool = ...,
        highlight_syntax: bool = ...,
        implicit_trailing_newline: bool = ...,
        language: Language = ...,
        style_scheme: StyleScheme = ...,
        enable_undo: bool = ...,
        tag_table: Gtk.TextTagTable = ...,
        text: str = ...,
    ): ...
    def backward_iter_to_source_mark(
        self, category: Optional[str] = None
    ) -> Tuple[bool, Gtk.TextIter]: ...
    def change_case(
        self, case_type: ChangeCaseType, start: Gtk.TextIter, end: Gtk.TextIter
    ) -> None: ...
    def create_source_mark(
        self, name: Optional[str], category: str, where: Gtk.TextIter
    ) -> Mark: ...
    def do_bracket_matched(
        self, iter: Gtk.TextIter, state: BracketMatchType
    ) -> None: ...
    def ensure_highlight(self, start: Gtk.TextIter, end: Gtk.TextIter) -> None: ...
    def forward_iter_to_source_mark(
        self, category: Optional[str] = None
    ) -> Tuple[bool, Gtk.TextIter]: ...
    def get_context_classes_at_iter(self, iter: Gtk.TextIter) -> list[str]: ...
    def get_highlight_matching_brackets(self) -> bool: ...
    def get_highlight_syntax(self) -> bool: ...
    def get_implicit_trailing_newline(self) -> bool: ...
    def get_language(self) -> Optional[Language]: ...
    def get_source_marks_at_iter(
        self, iter: Gtk.TextIter, category: Optional[str] = None
    ) -> list[Mark]: ...
    def get_source_marks_at_line(
        self, line: int, category: Optional[str] = None
    ) -> list[Mark]: ...
    def get_style_scheme(self) -> Optional[StyleScheme]: ...
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
    def remove_source_marks(
        self, start: Gtk.TextIter, end: Gtk.TextIter, category: Optional[str] = None
    ) -> None: ...
    def set_highlight_matching_brackets(self, highlight: bool) -> None: ...
    def set_highlight_syntax(self, highlight: bool) -> None: ...
    def set_implicit_trailing_newline(
        self, implicit_trailing_newline: bool
    ) -> None: ...
    def set_language(self, language: Optional[Language] = None) -> None: ...
    def set_style_scheme(self, scheme: Optional[StyleScheme] = None) -> None: ...
    def sort_lines(
        self, start: Gtk.TextIter, end: Gtk.TextIter, flags: SortFlags, column: int
    ) -> None: ...

class BufferClass(GObject.GPointer):
    parent_class: Gtk.TextBufferClass = ...
    bracket_matched: Callable[[Buffer, Gtk.TextIter, BracketMatchType], None] = ...
    _reserved: list[None] = ...

class Completion(GObject.Object):
    class Props:
        buffer: Gtk.TextView
        page_size: int
        remember_info_visibility: bool
        select_on_show: bool
        show_icons: bool
        view: View
    props: Props = ...
    def __init__(
        self,
        page_size: int = ...,
        remember_info_visibility: bool = ...,
        select_on_show: bool = ...,
        show_icons: bool = ...,
        view: View = ...,
    ): ...
    def add_provider(self, provider: CompletionProvider) -> None: ...
    def block_interactive(self) -> None: ...
    @staticmethod
    def fuzzy_highlight(
        haystack: str, casefold_query: str
    ) -> Optional[Pango.AttrList]: ...
    @staticmethod
    def fuzzy_match(
        haystack: Optional[str], casefold_needle: str
    ) -> Tuple[bool, int]: ...
    def get_buffer(self) -> Buffer: ...
    def get_page_size(self) -> int: ...
    def get_view(self) -> View: ...
    def hide(self) -> None: ...
    def remove_provider(self, provider: CompletionProvider) -> None: ...
    def set_page_size(self, page_size: int) -> None: ...
    def show(self) -> None: ...
    def unblock_interactive(self) -> None: ...

class CompletionCell(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        column: CompletionColumn
        markup: str
        paintable: Gdk.Paintable
        text: str
        widget: Gtk.Widget
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Gtk.LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Gtk.Widget
        receives_default: bool
        root: Gtk.Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        column: CompletionColumn = ...,
        markup: str = ...,
        paintable: Gdk.Paintable = ...,
        text: str = ...,
        widget: Gtk.Widget = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_column(self) -> CompletionColumn: ...
    def get_widget(self) -> Optional[Gtk.Widget]: ...
    def set_gicon(self, gicon: Gio.Icon) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_markup(self, markup: str) -> None: ...
    def set_paintable(self, paintable: Gdk.Paintable) -> None: ...
    def set_text(self, text: Optional[str] = None) -> None: ...
    def set_text_with_attributes(self, text: str, attrs: Pango.AttrList) -> None: ...
    def set_widget(self, child: Gtk.Widget) -> None: ...

class CompletionCellClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class CompletionClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class CompletionContext(GObject.Object, Gio.ListModel):
    class Props:
        busy: bool
        completion: Completion
        empty: bool
    props: Props = ...
    def __init__(self, completion: Completion = ...): ...
    def get_activation(self) -> CompletionActivation: ...
    def get_bounds(self) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter]: ...
    def get_buffer(self) -> Optional[Buffer]: ...
    def get_busy(self) -> bool: ...
    def get_completion(self) -> Optional[Completion]: ...
    def get_empty(self) -> bool: ...
    def get_language(self) -> Optional[Language]: ...
    def get_proposals_for_provider(
        self, provider: CompletionProvider
    ) -> Optional[Gio.ListModel]: ...
    def get_view(self) -> Optional[View]: ...
    def get_word(self) -> str: ...
    def list_providers(self) -> Gio.ListModel: ...
    def set_proposals_for_provider(
        self, provider: CompletionProvider, results: Optional[Gio.ListModel] = None
    ) -> None: ...

class CompletionContextClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class CompletionProposal(GObject.GInterface):
    def get_typed_text(self) -> Optional[str]: ...

class CompletionProposalInterface(GObject.GPointer):
    parent_iface: GObject.TypeInterface = ...
    get_typed_text: Callable[[CompletionProposal], Optional[str]] = ...

class CompletionProvider(GObject.GInterface):
    def activate(
        self, context: CompletionContext, proposal: CompletionProposal
    ) -> None: ...
    def display(
        self,
        context: CompletionContext,
        proposal: CompletionProposal,
        cell: CompletionCell,
    ) -> None: ...
    def get_priority(self, context: CompletionContext) -> int: ...
    def get_title(self) -> Optional[str]: ...
    def is_trigger(self, iter: Gtk.TextIter, ch: str) -> bool: ...
    def key_activates(
        self,
        context: CompletionContext,
        proposal: CompletionProposal,
        keyval: int,
        state: Gdk.ModifierType,
    ) -> bool: ...
    def list_alternates(
        self, context: CompletionContext, proposal: CompletionProposal
    ) -> Optional[list[CompletionProposal]]: ...
    def populate_async(
        self,
        context: CompletionContext,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def populate_finish(self, result: Gio.AsyncResult) -> Gio.ListModel: ...
    def refilter(self, context: CompletionContext, model: Gio.ListModel) -> None: ...

class CompletionProviderInterface(GObject.GPointer):
    parent_iface: GObject.TypeInterface = ...
    get_title: Callable[[CompletionProvider], Optional[str]] = ...
    get_priority: Callable[[CompletionProvider, CompletionContext], int] = ...
    is_trigger: Callable[[CompletionProvider, Gtk.TextIter, str], bool] = ...
    key_activates: Callable[
        [
            CompletionProvider,
            CompletionContext,
            CompletionProposal,
            int,
            Gdk.ModifierType,
        ],
        bool,
    ] = ...
    populate: None = ...
    populate_async: Callable[..., None] = ...
    populate_finish: Callable[
        [CompletionProvider, Gio.AsyncResult], Gio.ListModel
    ] = ...
    refilter: Callable[
        [CompletionProvider, CompletionContext, Gio.ListModel], None
    ] = ...
    display: Callable[
        [CompletionProvider, CompletionContext, CompletionProposal, CompletionCell],
        None,
    ] = ...
    activate: Callable[
        [CompletionProvider, CompletionContext, CompletionProposal], None
    ] = ...
    list_alternates: Callable[
        [CompletionProvider, CompletionContext, CompletionProposal],
        Optional[list[CompletionProposal]],
    ] = ...

class CompletionSnippets(GObject.Object, CompletionProvider):
    class Props:
        priority: int
        title: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, priority: int = ..., title: str = ...): ...
    @classmethod
    def new(cls) -> CompletionSnippets: ...

class CompletionSnippetsClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    _reserved: list[None] = ...

class CompletionWords(GObject.Object, CompletionProvider):
    class Props:
        minimum_word_size: int
        priority: int
        proposals_batch_size: int
        scan_batch_size: int
        title: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self,
        minimum_word_size: int = ...,
        priority: int = ...,
        proposals_batch_size: int = ...,
        scan_batch_size: int = ...,
        title: str = ...,
    ): ...
    @classmethod
    def new(cls, title: Optional[str] = None) -> CompletionWords: ...
    def register(self, buffer: Gtk.TextBuffer) -> None: ...
    def unregister(self, buffer: Gtk.TextBuffer) -> None: ...

class CompletionWordsClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    _reserved: list[None] = ...

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
    parent_instance: GObject.Object = ...
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
    _reserved: list[None] = ...

class FileLoader(GObject.Object):
    class Props:
        buffer: Buffer
        file: File
        input_stream: Gio.InputStream
        location: Gio.File
    props: Props = ...
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

class Gutter(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        view: View
        window_type: Gtk.TextWindowType
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Gtk.LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Gtk.Widget
        receives_default: bool
        root: Gtk.Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        view: View = ...,
        window_type: Gtk.TextWindowType = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_view(self) -> View: ...
    def insert(self, renderer: GutterRenderer, position: int) -> bool: ...
    def remove(self, renderer: GutterRenderer) -> None: ...
    def reorder(self, renderer: GutterRenderer, position: int) -> None: ...

class GutterClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class GutterLines(GObject.Object):
    def add_class(self, line: int, name: str) -> None: ...
    def add_qclass(self, line: int, qname: int) -> None: ...
    def get_buffer(self) -> Gtk.TextBuffer: ...
    def get_first(self) -> int: ...
    def get_iter_at_line(self, line: int) -> Gtk.TextIter: ...
    def get_last(self) -> int: ...
    def get_line_yrange(
        self, line: int, mode: GutterRendererAlignmentMode
    ) -> Tuple[int, int]: ...
    def get_view(self) -> Gtk.TextView: ...
    def has_any_class(self, line: int) -> bool: ...
    def has_class(self, line: int, name: str) -> bool: ...
    def has_qclass(self, line: int, qname: int) -> bool: ...
    def is_cursor(self, line: int) -> bool: ...
    def is_prelit(self, line: int) -> bool: ...
    def is_selected(self, line: int) -> bool: ...
    def remove_class(self, line: int, name: str) -> None: ...
    def remove_qclass(self, line: int, qname: int) -> None: ...

class GutterLinesClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class GutterRenderer(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        alignment_mode: GutterRendererAlignmentMode
        lines: GutterLines
        view: Gtk.TextView
        xalign: float
        xpad: int
        yalign: float
        ypad: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Gtk.LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Gtk.Widget
        receives_default: bool
        root: Gtk.Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    parent_instance: Gtk.Widget = ...
    def __init__(
        self,
        alignment_mode: GutterRendererAlignmentMode = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def activate(
        self,
        iter: Gtk.TextIter,
        area: Gdk.Rectangle,
        button: int,
        state: Gdk.ModifierType,
        n_presses: int,
    ) -> None: ...
    def align_cell(
        self, line: int, width: float, height: float
    ) -> Tuple[float, float]: ...
    def do_activate(
        self,
        iter: Gtk.TextIter,
        area: Gdk.Rectangle,
        button: int,
        state: Gdk.ModifierType,
        n_presses: int,
    ) -> None: ...
    def do_begin(self, lines: GutterLines) -> None: ...
    def do_change_buffer(self, old_buffer: Optional[Buffer] = None) -> None: ...
    def do_change_view(self, old_view: Optional[View] = None) -> None: ...
    def do_end(self) -> None: ...
    def do_query_activatable(self, iter: Gtk.TextIter, area: Gdk.Rectangle) -> bool: ...
    def do_query_data(self, lines: GutterLines, line: int) -> None: ...
    def do_snapshot_line(
        self, snapshot: Gtk.Snapshot, lines: GutterLines, line: int
    ) -> None: ...
    def get_alignment_mode(self) -> GutterRendererAlignmentMode: ...
    def get_buffer(self) -> Optional[Buffer]: ...
    def get_view(self) -> View: ...
    def get_xalign(self) -> float: ...
    def get_xpad(self) -> int: ...
    def get_yalign(self) -> float: ...
    def get_ypad(self) -> int: ...
    def query_activatable(self, iter: Gtk.TextIter, area: Gdk.Rectangle) -> bool: ...
    def set_alignment_mode(self, mode: GutterRendererAlignmentMode) -> None: ...
    def set_xalign(self, xalign: float) -> None: ...
    def set_xpad(self, xpad: int) -> None: ...
    def set_yalign(self, yalign: float) -> None: ...
    def set_ypad(self, ypad: int) -> None: ...

class GutterRendererClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...
    query_data: Callable[[GutterRenderer, GutterLines, int], None] = ...
    begin: Callable[[GutterRenderer, GutterLines], None] = ...
    snapshot_line: Callable[
        [GutterRenderer, Gtk.Snapshot, GutterLines, int], None
    ] = ...
    end: Callable[[GutterRenderer], None] = ...
    change_view: Callable[[GutterRenderer, Optional[View]], None] = ...
    change_buffer: Callable[[GutterRenderer, Optional[Buffer]], None] = ...
    query_activatable: Callable[
        [GutterRenderer, Gtk.TextIter, Gdk.Rectangle], bool
    ] = ...
    activate: Callable[
        [GutterRenderer, Gtk.TextIter, Gdk.Rectangle, int, Gdk.ModifierType, int], None
    ] = ...
    _reserved: list[None] = ...

class GutterRendererPixbuf(
    GutterRenderer, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget
):
    class Props:
        gicon: Gio.Icon
        icon_name: str
        paintable: Gdk.Paintable
        pixbuf: GdkPixbuf.Pixbuf
        alignment_mode: GutterRendererAlignmentMode
        lines: GutterLines
        view: Gtk.TextView
        xalign: float
        xpad: int
        yalign: float
        ypad: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Gtk.LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Gtk.Widget
        receives_default: bool
        root: Gtk.Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    parent_instance: GutterRenderer = ...
    def __init__(
        self,
        gicon: Gio.Icon = ...,
        icon_name: str = ...,
        paintable: Gdk.Paintable = ...,
        pixbuf: GdkPixbuf.Pixbuf = ...,
        alignment_mode: GutterRendererAlignmentMode = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_gicon(self) -> Gio.Icon: ...
    def get_icon_name(self) -> str: ...
    def get_paintable(self) -> Optional[Gdk.Paintable]: ...
    def get_pixbuf(self) -> GdkPixbuf.Pixbuf: ...
    @classmethod
    def new(cls) -> GutterRendererPixbuf: ...
    def overlay_paintable(self, paintable: Gdk.Paintable) -> None: ...
    def set_gicon(self, icon: Optional[Gio.Icon] = None) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_paintable(self, paintable: Optional[Gdk.Paintable] = None) -> None: ...
    def set_pixbuf(self, pixbuf: Optional[GdkPixbuf.Pixbuf] = None) -> None: ...

class GutterRendererPixbufClass(GObject.GPointer):
    parent_class: GutterRendererClass = ...
    _reserved: list[None] = ...

class GutterRendererText(
    GutterRenderer, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget
):
    class Props:
        markup: str
        text: str
        alignment_mode: GutterRendererAlignmentMode
        lines: GutterLines
        view: Gtk.TextView
        xalign: float
        xpad: int
        yalign: float
        ypad: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Gtk.LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Gtk.Widget
        receives_default: bool
        root: Gtk.Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    parent_instance: GutterRenderer = ...
    def __init__(
        self,
        markup: str = ...,
        text: str = ...,
        alignment_mode: GutterRendererAlignmentMode = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def measure(self, text: str) -> Tuple[int, int]: ...
    def measure_markup(self, markup: str) -> Tuple[int, int]: ...
    @classmethod
    def new(cls) -> GutterRendererText: ...
    def set_markup(self, markup: str, length: int) -> None: ...
    def set_text(self, text: str, length: int) -> None: ...

class GutterRendererTextClass(GObject.GPointer):
    parent_class: GutterRendererClass = ...
    _reserved: list[None] = ...

class Hover(GObject.Object):
    class Props:
        hover_delay: int
    props: Props = ...
    def __init__(self, hover_delay: int = ...): ...
    def add_provider(self, provider: HoverProvider) -> None: ...
    def remove_provider(self, provider: HoverProvider) -> None: ...

class HoverClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class HoverContext(GObject.Object):
    def get_bounds(self) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter]: ...
    def get_buffer(self) -> Buffer: ...
    def get_iter(self, iter: Gtk.TextIter) -> bool: ...
    def get_view(self) -> View: ...

class HoverContextClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class HoverDisplay(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Gtk.LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Gtk.Widget
        receives_default: bool
        root: Gtk.Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def append(self, child: Gtk.Widget) -> None: ...
    def insert_after(self, child: Gtk.Widget, sibling: Gtk.Widget) -> None: ...
    def prepend(self, child: Gtk.Widget) -> None: ...
    def remove(self, child: Gtk.Widget) -> None: ...

class HoverDisplayClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class HoverProvider(GObject.GInterface):
    def populate_async(
        self,
        context: HoverContext,
        display: HoverDisplay,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def populate_finish(self, result: Gio.AsyncResult) -> bool: ...

class HoverProviderInterface(GObject.GPointer):
    parent_iface: GObject.TypeInterface = ...
    populate: Callable[[HoverProvider, HoverContext, HoverDisplay], bool] = ...
    populate_async: Callable[..., None] = ...
    populate_finish: Callable[[HoverProvider, Gio.AsyncResult], bool] = ...

class Indenter(GObject.GInterface):
    def indent(self, view: View) -> Gtk.TextIter: ...
    def is_trigger(
        self, view: View, location: Gtk.TextIter, state: Gdk.ModifierType, keyval: int
    ) -> bool: ...

class IndenterInterface(GObject.GPointer):
    parent_iface: GObject.TypeInterface = ...
    is_trigger: Callable[
        [Indenter, View, Gtk.TextIter, Gdk.ModifierType, int], bool
    ] = ...
    indent: Callable[[Indenter, View], Gtk.TextIter] = ...

class Language(GObject.Object):
    class Props:
        hidden: bool
        id: str
        name: str
        section: str
    props: Props = ...
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

class LanguageManager(GObject.Object):
    class Props:
        language_ids: list[str]
        search_path: list[str]
    props: Props = ...
    def __init__(self, search_path: Sequence[str] = ...): ...
    def append_search_path(self, path: str) -> None: ...
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
    def prepend_search_path(self, path: str) -> None: ...
    def set_search_path(self, dirs: Optional[Sequence[str]] = None) -> None: ...

class LanguageManagerClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class Map(View, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Scrollable):
    class Props:
        font_desc: Pango.FontDescription
        view: View
        auto_indent: bool
        background_pattern: BackgroundPatternType
        completion: Completion
        enable_snippets: bool
        highlight_current_line: bool
        indent_on_tab: bool
        indent_width: int
        indenter: Indenter
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
        extra_menu: Gio.MenuModel
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
        right_margin: int
        tabs: Pango.TabArray
        top_margin: int
        wrap_mode: Gtk.WrapMode
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Gtk.LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Gtk.Widget
        receives_default: bool
        root: Gtk.Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
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
        enable_snippets: bool = ...,
        highlight_current_line: bool = ...,
        indent_on_tab: bool = ...,
        indent_width: int = ...,
        indenter: Indenter = ...,
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
        extra_menu: Gio.MenuModel = ...,
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
        right_margin: int = ...,
        tabs: Pango.TabArray = ...,
        top_margin: int = ...,
        wrap_mode: Gtk.WrapMode = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
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
    _reserved: list[None] = ...

class Mark(Gtk.TextMark):
    class Props:
        category: str
        left_gravity: bool
        name: str
    props: Props = ...
    parent_instance: Gtk.TextMark = ...
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
    def render_icon(self, widget: Gtk.Widget, size: int) -> Gdk.Paintable: ...
    def set_background(self, background: Gdk.RGBA) -> None: ...
    def set_gicon(self, gicon: Gio.Icon) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_pixbuf(self, pixbuf: GdkPixbuf.Pixbuf) -> None: ...

class MarkAttributesClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class MarkClass(GObject.GPointer):
    parent_class: Gtk.TextMarkClass = ...
    _reserved: list[None] = ...

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
    def ignore_tag(self, tag: Gtk.TextTag) -> None: ...
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
    _reserved: list[None] = ...

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
    _reserved: list[None] = ...

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
        regex_error: GLib.Error
        settings: SearchSettings
    props: Props = ...
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

class SearchSettings(GObject.Object):
    class Props:
        at_word_boundaries: bool
        case_sensitive: bool
        regex_enabled: bool
        search_text: str
        wrap_around: bool
    props: Props = ...
    parent_instance: GObject.Object = ...
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
    _reserved: list[None] = ...

class Snippet(GObject.Object):
    class Props:
        buffer: Gtk.TextBuffer
        description: str
        focus_position: int
        language_id: str
        name: str
        trigger: str
    props: Props = ...
    def __init__(
        self,
        description: str = ...,
        language_id: str = ...,
        name: str = ...,
        trigger: str = ...,
    ): ...
    def add_chunk(self, chunk: SnippetChunk) -> None: ...
    def copy(self) -> Snippet: ...
    def get_context(self) -> Optional[SnippetContext]: ...
    def get_description(self) -> str: ...
    def get_focus_position(self) -> int: ...
    def get_language_id(self) -> str: ...
    def get_n_chunks(self) -> int: ...
    def get_name(self) -> str: ...
    def get_nth_chunk(self, nth: int) -> SnippetChunk: ...
    def get_trigger(self) -> Optional[str]: ...
    @classmethod
    def new(
        cls, trigger: Optional[str] = None, language_id: Optional[str] = None
    ) -> Snippet: ...
    @classmethod
    def new_parsed(cls, text: str) -> Snippet: ...
    def set_description(self, description: str) -> None: ...
    def set_language_id(self, language_id: str) -> None: ...
    def set_name(self, name: str) -> None: ...
    def set_trigger(self, trigger: str) -> None: ...

class SnippetChunk(GObject.InitiallyUnowned):
    class Props:
        context: SnippetContext
        focus_position: int
        spec: str
        text: str
        text_set: bool
        tooltip_text: str
    props: Props = ...
    def __init__(
        self,
        context: SnippetContext = ...,
        focus_position: int = ...,
        spec: str = ...,
        text: str = ...,
        text_set: bool = ...,
        tooltip_text: str = ...,
    ): ...
    def copy(self) -> SnippetChunk: ...
    def get_context(self) -> SnippetContext: ...
    def get_focus_position(self) -> int: ...
    def get_spec(self) -> Optional[str]: ...
    def get_text(self) -> str: ...
    def get_text_set(self) -> bool: ...
    def get_tooltip_text(self) -> str: ...
    @classmethod
    def new(cls) -> SnippetChunk: ...
    def set_context(self, context: SnippetContext) -> None: ...
    def set_focus_position(self, focus_position: int) -> None: ...
    def set_spec(self, spec: str) -> None: ...
    def set_text(self, text: str) -> None: ...
    def set_text_set(self, text_set: bool) -> None: ...
    def set_tooltip_text(self, tooltip_text: str) -> None: ...

class SnippetChunkClass(GObject.GPointer):
    parent_class: GObject.InitiallyUnownedClass = ...

class SnippetClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class SnippetContext(GObject.Object):
    def clear_variables(self) -> None: ...
    def expand(self, input: str) -> str: ...
    def get_variable(self, key: str) -> Optional[str]: ...
    @classmethod
    def new(cls) -> SnippetContext: ...
    def set_constant(self, key: str, value: str) -> None: ...
    def set_line_prefix(self, line_prefix: str) -> None: ...
    def set_tab_width(self, tab_width: int) -> None: ...
    def set_use_spaces(self, use_spaces: bool) -> None: ...
    def set_variable(self, key: str, value: str) -> None: ...

class SnippetContextClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class SnippetManager(GObject.Object):
    class Props:
        search_path: list[str]
    props: Props = ...
    def __init__(self, search_path: Sequence[str] = ...): ...
    @staticmethod
    def get_default() -> SnippetManager: ...
    def get_search_path(self) -> list[str]: ...
    def get_snippet(
        self, group: Optional[str], language_id: Optional[str], trigger: str
    ) -> Optional[Snippet]: ...
    def list_all(self) -> Gio.ListModel: ...
    def list_groups(self) -> list[str]: ...
    def list_matching(
        self,
        group: Optional[str] = None,
        language_id: Optional[str] = None,
        trigger_prefix: Optional[str] = None,
    ) -> Gio.ListModel: ...
    def set_search_path(self, dirs: Optional[Sequence[str]] = None) -> None: ...

class SnippetManagerClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class SpaceDrawer(GObject.Object):
    class Props:
        enable_matrix: bool
        matrix: GLib.Variant
    props: Props = ...
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
        weight: Pango.Weight
        weight_set: bool
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
        weight: Pango.Weight = ...,
        weight_set: bool = ...,
    ): ...
    def apply(self, tag: Gtk.TextTag) -> None: ...
    def copy(self) -> Style: ...

class StyleClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class StyleScheme(GObject.Object):
    class Props:
        description: str
        filename: str
        id: str
        name: str
    props: Props = ...
    def __init__(self, id: str = ...): ...
    def get_authors(self) -> Optional[list[str]]: ...
    def get_description(self) -> Optional[str]: ...
    def get_filename(self) -> Optional[str]: ...
    def get_id(self) -> str: ...
    def get_metadata(self, name: str) -> Optional[str]: ...
    def get_name(self) -> str: ...
    def get_style(self, style_id: str) -> Optional[Style]: ...

class StyleSchemeChooser(GObject.GInterface):
    def get_style_scheme(self) -> StyleScheme: ...
    def set_style_scheme(self, scheme: StyleScheme) -> None: ...

class StyleSchemeChooserButton(
    Gtk.Button,
    Gtk.Accessible,
    Gtk.Actionable,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    StyleSchemeChooser,
):
    class Props:
        child: Gtk.Widget
        has_frame: bool
        icon_name: str
        label: str
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Gtk.LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Gtk.Widget
        receives_default: bool
        root: Gtk.Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: str
        action_target: GLib.Variant
        style_scheme: StyleScheme
    props: Props = ...
    parent_instance: Gtk.Button = ...
    def __init__(
        self,
        child: Gtk.Widget = ...,
        has_frame: bool = ...,
        icon_name: str = ...,
        label: str = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
        style_scheme: StyleScheme = ...,
    ): ...
    @classmethod
    def new(cls) -> StyleSchemeChooserButton: ...

class StyleSchemeChooserButtonClass(GObject.GPointer):
    parent: Gtk.ButtonClass = ...
    _reserved: list[None] = ...

class StyleSchemeChooserInterface(GObject.GPointer):
    base_interface: GObject.TypeInterface = ...
    get_style_scheme: Callable[[StyleSchemeChooser], StyleScheme] = ...
    set_style_scheme: Callable[[StyleSchemeChooser, StyleScheme], None] = ...
    _reserved: list[None] = ...

class StyleSchemeChooserWidget(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, StyleSchemeChooser
):
    class Props:
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Gtk.LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Gtk.Widget
        receives_default: bool
        root: Gtk.Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        style_scheme: StyleScheme
    props: Props = ...
    parent_instance: Gtk.Widget = ...
    def __init__(
        self,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        style_scheme: StyleScheme = ...,
    ): ...
    @classmethod
    def new(cls) -> StyleSchemeChooserWidget: ...

class StyleSchemeChooserWidgetClass(GObject.GPointer):
    parent: Gtk.WidgetClass = ...
    _reserved: list[None] = ...

class StyleSchemeClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class StyleSchemeManager(GObject.Object):
    class Props:
        scheme_ids: list[str]
        search_path: list[str]
    props: Props = ...
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

class StyleSchemePreview(
    Gtk.Widget, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    class Props:
        scheme: StyleScheme
        selected: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Gtk.LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Gtk.Widget
        receives_default: bool
        root: Gtk.Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: str
        action_target: GLib.Variant
    props: Props = ...
    def __init__(
        self,
        scheme: StyleScheme = ...,
        selected: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def get_scheme(self) -> StyleScheme: ...
    def get_selected(self) -> bool: ...
    @classmethod
    def new(cls, scheme: StyleScheme) -> StyleSchemePreview: ...
    def set_selected(self, selected: bool) -> None: ...

class StyleSchemePreviewClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class Tag(Gtk.TextTag):
    class Props:
        draw_spaces: bool
        draw_spaces_set: bool
        accumulative_margin: bool
        allow_breaks: bool
        allow_breaks_set: bool
        background: str
        background_full_height: bool
        background_full_height_set: bool
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
        foreground_rgba: Gdk.RGBA
        foreground_set: bool
        indent: int
        indent_set: bool
        insert_hyphens: bool
        insert_hyphens_set: bool
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
        line_height: float
        line_height_set: bool
        name: str
        overline: Pango.Overline
        overline_rgba: Gdk.RGBA
        overline_rgba_set: bool
        overline_set: bool
        paragraph_background: str
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
        sentence: bool
        sentence_set: bool
        show_spaces: Pango.ShowFlags
        show_spaces_set: bool
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
        text_transform: Pango.TextTransform
        text_transform_set: bool
        underline: Pango.Underline
        underline_rgba: Gdk.RGBA
        underline_rgba_set: bool
        underline_set: bool
        variant: Pango.Variant
        variant_set: bool
        weight: int
        weight_set: bool
        word: bool
        word_set: bool
        wrap_mode: Gtk.WrapMode
        wrap_mode_set: bool
    props: Props = ...
    parent_instance: Gtk.TextTag = ...
    def __init__(
        self,
        draw_spaces: bool = ...,
        draw_spaces_set: bool = ...,
        accumulative_margin: bool = ...,
        allow_breaks: bool = ...,
        allow_breaks_set: bool = ...,
        background: str = ...,
        background_full_height: bool = ...,
        background_full_height_set: bool = ...,
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
        foreground_rgba: Gdk.RGBA = ...,
        foreground_set: bool = ...,
        indent: int = ...,
        indent_set: bool = ...,
        insert_hyphens: bool = ...,
        insert_hyphens_set: bool = ...,
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
        line_height: float = ...,
        line_height_set: bool = ...,
        name: str = ...,
        overline: Pango.Overline = ...,
        overline_rgba: Gdk.RGBA = ...,
        overline_rgba_set: bool = ...,
        overline_set: bool = ...,
        paragraph_background: str = ...,
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
        sentence: bool = ...,
        sentence_set: bool = ...,
        show_spaces: Pango.ShowFlags = ...,
        show_spaces_set: bool = ...,
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
        text_transform: Pango.TextTransform = ...,
        text_transform_set: bool = ...,
        underline: Pango.Underline = ...,
        underline_rgba: Gdk.RGBA = ...,
        underline_rgba_set: bool = ...,
        underline_set: bool = ...,
        variant: Pango.Variant = ...,
        variant_set: bool = ...,
        weight: int = ...,
        weight_set: bool = ...,
        word: bool = ...,
        word_set: bool = ...,
        wrap_mode: Gtk.WrapMode = ...,
        wrap_mode_set: bool = ...,
    ): ...
    @classmethod
    def new(cls, name: Optional[str] = None) -> Tag: ...

class TagClass(GObject.GPointer):
    parent_class: Gtk.TextTagClass = ...
    _reserved: list[None] = ...

class View(
    Gtk.TextView, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Scrollable
):
    class Props:
        auto_indent: bool
        background_pattern: BackgroundPatternType
        completion: Completion
        enable_snippets: bool
        highlight_current_line: bool
        indent_on_tab: bool
        indent_width: int
        indenter: Indenter
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
        extra_menu: Gio.MenuModel
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
        right_margin: int
        tabs: Pango.TabArray
        top_margin: int
        wrap_mode: Gtk.WrapMode
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Gtk.LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Gtk.Widget
        receives_default: bool
        root: Gtk.Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        hadjustment: Gtk.Adjustment
        hscroll_policy: Gtk.ScrollablePolicy
        vadjustment: Gtk.Adjustment
        vscroll_policy: Gtk.ScrollablePolicy
    props: Props = ...
    parent_instance: Gtk.TextView = ...
    def __init__(
        self,
        auto_indent: bool = ...,
        background_pattern: BackgroundPatternType = ...,
        enable_snippets: bool = ...,
        highlight_current_line: bool = ...,
        indent_on_tab: bool = ...,
        indent_width: int = ...,
        indenter: Indenter = ...,
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
        extra_menu: Gio.MenuModel = ...,
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
        right_margin: int = ...,
        tabs: Pango.TabArray = ...,
        top_margin: int = ...,
        wrap_mode: Gtk.WrapMode = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        hadjustment: Gtk.Adjustment = ...,
        hscroll_policy: Gtk.ScrollablePolicy = ...,
        vadjustment: Gtk.Adjustment = ...,
        vscroll_policy: Gtk.ScrollablePolicy = ...,
    ): ...
    def do_line_mark_activated(
        self, iter: Gtk.TextIter, button: int, state: Gdk.ModifierType, n_presses: int
    ) -> None: ...
    def do_move_lines(self, down: bool) -> None: ...
    def do_move_words(self, step: int) -> None: ...
    def do_push_snippet(
        self, snippet: Snippet, location: Optional[Gtk.TextIter] = None
    ) -> None: ...
    def do_show_completion(self) -> None: ...
    def get_auto_indent(self) -> bool: ...
    def get_background_pattern(self) -> BackgroundPatternType: ...
    # override
    def get_buffer(self) -> Buffer: ...
    def get_completion(self) -> Completion: ...
    def get_enable_snippets(self) -> bool: ...
    def get_gutter(self, window_type: Gtk.TextWindowType) -> Gutter: ...
    def get_highlight_current_line(self) -> bool: ...
    def get_hover(self) -> Hover: ...
    def get_indent_on_tab(self) -> bool: ...
    def get_indent_width(self) -> int: ...
    def get_indenter(self) -> Optional[Indenter]: ...
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
    def push_snippet(
        self, snippet: Snippet, location: Optional[Gtk.TextIter] = None
    ) -> None: ...
    def set_auto_indent(self, enable: bool) -> None: ...
    def set_background_pattern(
        self, background_pattern: BackgroundPatternType
    ) -> None: ...
    def set_enable_snippets(self, enable_snippets: bool) -> None: ...
    def set_highlight_current_line(self, highlight: bool) -> None: ...
    def set_indent_on_tab(self, enable: bool) -> None: ...
    def set_indent_width(self, width: int) -> None: ...
    def set_indenter(self, indenter: Optional[Indenter] = None) -> None: ...
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
    line_mark_activated: Callable[
        [View, Gtk.TextIter, int, Gdk.ModifierType, int], None
    ] = ...
    show_completion: Callable[[View], None] = ...
    move_lines: Callable[[View, bool], None] = ...
    move_words: Callable[[View, int], None] = ...
    push_snippet: Callable[[View, Snippet, Optional[Gtk.TextIter]], None] = ...
    _reserved: list[None] = ...

class VimIMContext(Gtk.IMContext):
    class Props:
        command_bar_text: str
        command_text: str
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
    props: Props = ...
    def __init__(
        self, input_hints: Gtk.InputHints = ..., input_purpose: Gtk.InputPurpose = ...
    ): ...
    def execute_command(self, command: str) -> None: ...
    def get_command_bar_text(self) -> str: ...
    def get_command_text(self) -> str: ...
    @classmethod
    def new(cls) -> VimIMContext: ...

class VimIMContextClass(GObject.GPointer):
    parent_class: Gtk.IMContextClass = ...

class FileSaverFlags(GObject.GFlags):
    CREATE_BACKUP = 4
    IGNORE_INVALID_CHARS = 1
    IGNORE_MODIFICATION_TIME = 2
    NONE = 0

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

class CompletionActivation(GObject.GEnum):
    INTERACTIVE = 1
    NONE = 0
    USER_REQUESTED = 2

class CompletionColumn(GObject.GEnum):
    AFTER = 3
    BEFORE = 1
    COMMENT = 4
    DETAILS = 5
    ICON = 0
    TYPED_TEXT = 2

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
