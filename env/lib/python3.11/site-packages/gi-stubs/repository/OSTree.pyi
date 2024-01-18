from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

COMMIT_GVARIANT_STRING: str = "(a{sv}aya(say)sstayay)"
COMMIT_META_KEY_ARCHITECTURE: str = "ostree.architecture"
COMMIT_META_KEY_COLLECTION_BINDING: str = "ostree.collection-binding"
COMMIT_META_KEY_ENDOFLIFE: str = "ostree.endoflife"
COMMIT_META_KEY_ENDOFLIFE_REBASE: str = "ostree.endoflife-rebase"
COMMIT_META_KEY_REF_BINDING: str = "ostree.ref-binding"
COMMIT_META_KEY_SOURCE_TITLE: str = "ostree.source-title"
COMMIT_META_KEY_VERSION: str = "version"
DIRMETA_GVARIANT_STRING: str = "(uuua(ayay))"
FILEMETA_GVARIANT_STRING: str = "(uuua(ayay))"
GPG_KEY_GVARIANT_STRING: str = "(aa{sv}aa{sv}a{sv})"
MAX_METADATA_SIZE: int = 134217728
MAX_METADATA_WARN_SIZE: int = 7340032
METADATA_KEY_BOOTABLE: str = "ostree.bootable"
METADATA_KEY_LINUX: str = "ostree.linux"
META_KEY_DEPLOY_COLLECTION_ID: str = "ostree.deploy-collection-id"
ORIGIN_TRANSIENT_GROUP: str = "libostree-transient"
PATH_BOOTED: str = "/run/ostree-booted"
RELEASE_VERSION: int = 4
REPO_METADATA_REF: str = "ostree-metadata"
SHA256_DIGEST_LEN: int = 32
SHA256_STRING_LEN: int = 64
SIGN_NAME_ED25519: str = "ed25519"
SUMMARY_GVARIANT_STRING: str = "(a(s(taya{sv}))a{sv})"
SUMMARY_SIG_GVARIANT_STRING: str = "a{sv}"
TIMESTAMP: int = 0
TREE_GVARIANT_STRING: str = "(a(say)a(sayay))"
VERSION: float = 2023.4
VERSION_S: str = "2023.4"
YEAR_VERSION: int = 2023
_lock = ...  # FIXME Constant
_namespace: str = "OSTree"
_version: str = "1.0"

def break_hardlink(
    dfd: int,
    path: str,
    skip_xattrs: bool,
    cancellable: Optional[Gio.Cancellable] = None,
) -> bool: ...
def check_version(required_year: int, required_release: int) -> bool: ...
def checksum_b64_from_bytes(csum: Sequence[int]) -> str: ...
def checksum_b64_to_bytes(checksum: str) -> bytes: ...
def checksum_bytes_peek(bytes: GLib.Variant) -> bytes: ...
def checksum_bytes_peek_validate(bytes: GLib.Variant) -> bytes: ...
def checksum_file(
    f: Gio.File, objtype: ObjectType, cancellable: Optional[Gio.Cancellable] = None
) -> Tuple[bool, bytes]: ...
def checksum_file_async(
    f: Gio.File,
    objtype: ObjectType,
    io_priority: int,
    cancellable: Optional[Gio.Cancellable] = None,
    callback: Optional[Callable[..., None]] = None,
    *user_data: Any,
) -> None: ...
def checksum_file_async_finish(
    f: Gio.File, result: Gio.AsyncResult
) -> Tuple[bool, bytes]: ...
def checksum_file_at(
    dfd: int,
    path: str,
    stbuf: None,
    objtype: ObjectType,
    flags: ChecksumFlags,
    out_checksum: str,
    cancellable: Optional[Gio.Cancellable] = None,
) -> bool: ...
def checksum_file_from_input(
    file_info: Gio.FileInfo,
    xattrs: Optional[GLib.Variant],
    in_: Optional[Gio.InputStream],
    objtype: ObjectType,
    cancellable: Optional[Gio.Cancellable] = None,
) -> Tuple[bool, bytes]: ...
def checksum_from_bytes(csum: Sequence[int]) -> str: ...
def checksum_from_bytes_v(csum_v: GLib.Variant) -> str: ...
def checksum_inplace_to_bytes(checksum: str, buf: int) -> None: ...
def checksum_to_bytes(checksum: str) -> bytes: ...
def checksum_to_bytes_v(checksum: str) -> GLib.Variant: ...
def cmp_checksum_bytes(a: int, b: int) -> int: ...
def collection_ref_dupv(refs: Sequence[CollectionRef]) -> list[CollectionRef]: ...
def collection_ref_freev(refs: Sequence[CollectionRef]) -> None: ...
def commit_get_content_checksum(commit_variant: GLib.Variant) -> Optional[str]: ...
def commit_get_object_sizes(
    commit_variant: GLib.Variant,
) -> Tuple[bool, list[CommitSizesEntry]]: ...
def commit_get_parent(commit_variant: GLib.Variant) -> Optional[str]: ...
def commit_get_timestamp(commit_variant: GLib.Variant) -> int: ...
def commit_metadata_for_bootable(
    root: Gio.File,
    dict: GLib.VariantDict,
    cancellable: Optional[Gio.Cancellable] = None,
) -> bool: ...
def content_file_parse(
    compressed: bool,
    content_path: Gio.File,
    trusted: bool,
    cancellable: Optional[Gio.Cancellable] = None,
) -> Tuple[bool, Gio.InputStream, Gio.FileInfo, GLib.Variant]: ...
def content_file_parse_at(
    compressed: bool,
    parent_dfd: int,
    path: str,
    trusted: bool,
    cancellable: Optional[Gio.Cancellable] = None,
) -> Tuple[bool, Gio.InputStream, Gio.FileInfo, GLib.Variant]: ...
def content_stream_parse(
    compressed: bool,
    input: Gio.InputStream,
    input_length: int,
    trusted: bool,
    cancellable: Optional[Gio.Cancellable] = None,
) -> Tuple[bool, Gio.InputStream, Gio.FileInfo, GLib.Variant]: ...
def create_directory_metadata(
    dir_info: Gio.FileInfo, xattrs: Optional[GLib.Variant] = None
) -> GLib.Variant: ...
def diff_dirs(
    flags: DiffFlags,
    a: Gio.File,
    b: Gio.File,
    modified: Sequence[DiffItem],
    removed: Sequence[Gio.File],
    added: Sequence[Gio.File],
    cancellable: Optional[Gio.Cancellable] = None,
) -> bool: ...
def diff_dirs_with_options(
    flags: DiffFlags,
    a: Gio.File,
    b: Gio.File,
    modified: Sequence[DiffItem],
    removed: Sequence[Gio.File],
    added: Sequence[Gio.File],
    options: Optional[DiffDirsOptions] = None,
    cancellable: Optional[Gio.Cancellable] = None,
) -> bool: ...
def diff_print(
    a: Gio.File,
    b: Gio.File,
    modified: Sequence[DiffItem],
    removed: Sequence[Gio.File],
    added: Sequence[Gio.File],
) -> None: ...
def fs_get_all_xattrs(
    fd: int, cancellable: Optional[Gio.Cancellable] = None
) -> GLib.Variant: ...
def fs_get_all_xattrs_at(
    dfd: int, path: str, cancellable: Optional[Gio.Cancellable] = None
) -> GLib.Variant: ...
def gpg_error_quark() -> int: ...
def hash_object_name(a: None) -> int: ...
def kernel_args_cleanup(loc: None) -> None: ...
def metadata_variant_type(objtype: ObjectType) -> GLib.VariantType: ...
def object_from_string(str: str) -> Tuple[str, ObjectType]: ...
def object_name_deserialize(variant: GLib.Variant) -> Tuple[str, ObjectType]: ...
def object_name_serialize(checksum: str, objtype: ObjectType) -> GLib.Variant: ...
def object_to_string(checksum: str, objtype: ObjectType) -> str: ...
def object_type_from_string(str: str) -> ObjectType: ...
def object_type_to_string(objtype: ObjectType) -> str: ...
def parse_refspec(refspec: str) -> Tuple[bool, str, str]: ...
def raw_file_to_archive_z2_stream(
    input: Gio.InputStream,
    file_info: Gio.FileInfo,
    xattrs: Optional[GLib.Variant] = None,
    cancellable: Optional[Gio.Cancellable] = None,
) -> Tuple[bool, Gio.InputStream]: ...
def raw_file_to_archive_z2_stream_with_options(
    input: Gio.InputStream,
    file_info: Gio.FileInfo,
    xattrs: Optional[GLib.Variant] = None,
    options: Optional[GLib.Variant] = None,
    cancellable: Optional[Gio.Cancellable] = None,
) -> Tuple[bool, Gio.InputStream]: ...
def raw_file_to_content_stream(
    input: Gio.InputStream,
    file_info: Gio.FileInfo,
    xattrs: Optional[GLib.Variant] = None,
    cancellable: Optional[Gio.Cancellable] = None,
) -> Tuple[bool, Gio.InputStream, int]: ...
def repo_commit_traverse_iter_cleanup(p: None) -> None: ...
def repo_finder_resolve_all_async(
    finders: Sequence[RepoFinder],
    refs: Sequence[CollectionRef],
    parent_repo: Repo,
    cancellable: Optional[Gio.Cancellable] = None,
    callback: Optional[Callable[..., None]] = None,
    *user_data: Any,
) -> None: ...
def repo_finder_resolve_all_finish(
    result: Gio.AsyncResult,
) -> list[RepoFinderResult]: ...
def repo_finder_result_freev(results: Sequence[RepoFinderResult]) -> None: ...
def sign_get_all() -> list[Sign]: ...
def sign_get_by_name(name: str) -> Sign: ...
def validate_checksum_string(sha256: str) -> bool: ...
def validate_collection_id(collection_id: Optional[str] = None) -> bool: ...
def validate_remote_name(remote_name: str) -> bool: ...
def validate_rev(rev: str) -> bool: ...
def validate_structureof_checksum_string(checksum: str) -> bool: ...
def validate_structureof_commit(commit: GLib.Variant) -> bool: ...
def validate_structureof_csum_v(checksum: GLib.Variant) -> bool: ...
def validate_structureof_dirmeta(dirmeta: GLib.Variant) -> bool: ...
def validate_structureof_dirtree(dirtree: GLib.Variant) -> bool: ...
def validate_structureof_file_mode(mode: int) -> bool: ...
def validate_structureof_objtype(objtype: int) -> bool: ...

class AsyncProgress(GObject.Object):
    """
    :Constructors:

    ::

        AsyncProgress(**properties)
        new() -> OSTree.AsyncProgress

    Object OstreeAsyncProgress

    Signals from OstreeAsyncProgress:
      changed ()

    Signals from GObject:
      notify (GParam)
    """

    def copy_state(self, dest: AsyncProgress) -> None: ...
    def do_changed(self, *user_data: Any) -> None: ...
    def finish(self) -> None: ...
    def get_status(self) -> Optional[str]: ...
    def get_uint(self, key: str) -> int: ...
    def get_uint64(self, key: str) -> int: ...
    def get_variant(self, key: str) -> Optional[GLib.Variant]: ...
    @classmethod
    def new(cls) -> AsyncProgress: ...
    def set_status(self, status: Optional[str] = None) -> None: ...
    def set_uint(self, key: str, value: int) -> None: ...
    def set_uint64(self, key: str, value: int) -> None: ...
    def set_variant(self, key: str, value: GLib.Variant) -> None: ...

class AsyncProgressClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AsyncProgressClass()
    """

    parent_class: GObject.ObjectClass = ...
    changed: Callable[..., None] = ...

class BootconfigParser(GObject.Object):
    """
    :Constructors:

    ::

        BootconfigParser(**properties)
        new() -> OSTree.BootconfigParser

    Object OstreeBootconfigParser

    Signals from GObject:
      notify (GParam)
    """

    def clone(self) -> BootconfigParser: ...
    def get(self, key: str) -> Optional[str]: ...
    def get_overlay_initrds(self) -> Optional[list[str]]: ...
    @classmethod
    def new(cls) -> BootconfigParser: ...
    def parse(
        self, path: Gio.File, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def parse_at(
        self, dfd: int, path: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def set(self, key: str, value: str) -> None: ...
    def set_overlay_initrds(self, initrds: Optional[Sequence[str]] = None) -> None: ...
    def write(
        self, output: Gio.File, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def write_at(
        self, dfd: int, path: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...

class CollectionRef(GObject.GBoxed):
    """
    :Constructors:

    ::

        CollectionRef()
        new(collection_id:str=None, ref_name:str) -> OSTree.CollectionRef
    """

    collection_id: str = ...
    ref_name: str = ...
    def dup(self) -> CollectionRef: ...
    @staticmethod
    def dupv(refs: Sequence[CollectionRef]) -> list[CollectionRef]: ...
    def equal(self, ref2: CollectionRef) -> bool: ...
    def free(self) -> None: ...
    @staticmethod
    def freev(refs: Sequence[CollectionRef]) -> None: ...
    def hash(self) -> int: ...
    @classmethod
    def new(cls, collection_id: Optional[str], ref_name: str) -> CollectionRef: ...

class CommitSizesEntry(GObject.GBoxed):
    """
    :Constructors:

    ::

        CommitSizesEntry()
        new(checksum:str, objtype:OSTree.ObjectType, unpacked:int, archived:int) -> OSTree.CommitSizesEntry or None
    """

    checksum: str = ...
    objtype: ObjectType = ...
    unpacked: int = ...
    archived: int = ...
    def copy(self) -> Optional[CommitSizesEntry]: ...
    def free(self) -> None: ...
    @classmethod
    def new(
        cls, checksum: str, objtype: ObjectType, unpacked: int, archived: int
    ) -> Optional[CommitSizesEntry]: ...

class ContentWriter(Gio.OutputStream):
    """
    :Constructors:

    ::

        ContentWriter(**properties)

    Object OstreeContentWriter

    Signals from GObject:
      notify (GParam)
    """

    def finish(self, cancellable: Optional[Gio.Cancellable] = None) -> str: ...

class ContentWriterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContentWriterClass()
    """

    parent_class: Gio.OutputStreamClass = ...

class Deployment(GObject.Object):
    """
    :Constructors:

    ::

        Deployment(**properties)
        new(index:int, osname:str, csum:str, deployserial:int, bootcsum:str=None, bootserial:int) -> OSTree.Deployment

    Object OstreeDeployment

    Signals from GObject:
      notify (GParam)
    """

    def clone(self) -> Deployment: ...
    def equal(self, bp: Deployment) -> bool: ...
    def get_bootconfig(self) -> Optional[BootconfigParser]: ...
    def get_bootcsum(self) -> str: ...
    def get_bootserial(self) -> int: ...
    def get_csum(self) -> str: ...
    def get_deployserial(self) -> int: ...
    def get_index(self) -> int: ...
    def get_origin(self) -> Optional[GLib.KeyFile]: ...
    def get_origin_relpath(self) -> str: ...
    def get_osname(self) -> str: ...
    def get_unlocked(self) -> DeploymentUnlockedState: ...
    def hash(self) -> int: ...
    def is_pinned(self) -> bool: ...
    def is_staged(self) -> bool: ...
    @classmethod
    def new(
        cls,
        index: int,
        osname: str,
        csum: str,
        deployserial: int,
        bootcsum: Optional[str],
        bootserial: int,
    ) -> Deployment: ...
    @staticmethod
    def origin_remove_transient_state(origin: GLib.KeyFile) -> None: ...
    def set_bootconfig(self, bootconfig: Optional[BootconfigParser] = None) -> None: ...
    def set_bootserial(self, index: int) -> None: ...
    def set_index(self, index: int) -> None: ...
    def set_origin(self, origin: Optional[GLib.KeyFile] = None) -> None: ...
    @staticmethod
    def unlocked_state_to_string(state: DeploymentUnlockedState) -> str: ...

class DiffDirsOptions(GObject.GPointer):
    """
    :Constructors:

    ::

        DiffDirsOptions()
    """

    owner_uid: int = ...
    owner_gid: int = ...
    devino_to_csum_cache: RepoDevInoCache = ...
    unused_bools: list[bool] = ...
    unused_ints: list[int] = ...
    unused_ptrs: list[None] = ...

class DiffItem(GObject.GBoxed):
    """
    :Constructors:

    ::

        DiffItem()
    """

    refcount: int = ...
    src: Gio.File = ...
    target: Gio.File = ...
    src_info: Gio.FileInfo = ...
    target_info: Gio.FileInfo = ...
    src_checksum: str = ...
    target_checksum: str = ...
    def ref(self) -> DiffItem: ...
    def unref(self) -> None: ...

class GpgVerifyResult(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        GpgVerifyResult(**properties)

    Object OstreeGpgVerifyResult

    Signals from GObject:
      notify (GParam)
    """

    def count_all(self) -> int: ...
    def count_valid(self) -> int: ...
    def describe(
        self,
        signature_index: int,
        output_buffer: GLib.String,
        line_prefix: Optional[str],
        flags: GpgSignatureFormatFlags,
    ) -> None: ...
    @staticmethod
    def describe_variant(
        variant: GLib.Variant,
        output_buffer: GLib.String,
        line_prefix: Optional[str],
        flags: GpgSignatureFormatFlags,
    ) -> None: ...
    def get(
        self, signature_index: int, attrs: Sequence[GpgSignatureAttr]
    ) -> GLib.Variant: ...
    def get_all(self, signature_index: int) -> GLib.Variant: ...
    def lookup(self, key_id: str) -> Tuple[bool, int]: ...
    def require_valid_signature(self) -> bool: ...

class KernelArgs(GObject.GPointer):
    def append(self, arg: str) -> None: ...
    def append_argv(self, argv: Sequence[str]) -> None: ...
    def append_argv_filtered(
        self, argv: Sequence[str], prefixes: Sequence[str]
    ) -> None: ...
    def append_if_missing(self, arg: str) -> None: ...
    def append_proc_cmdline(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    @staticmethod
    def cleanup(loc: None) -> None: ...
    def contains(self, arg: str) -> bool: ...
    def delete(self, arg: str) -> bool: ...
    def delete_if_present(self, arg: str) -> bool: ...
    def delete_key_entry(self, key: str) -> bool: ...
    def free(self) -> None: ...
    def get_last_value(self, key: str) -> Optional[str]: ...
    def new_replace(self, arg: str) -> bool: ...
    def parse_append(self, options: str) -> None: ...
    def replace(self, arg: str) -> None: ...
    def replace_argv(self, argv: str) -> None: ...
    def replace_take(self, arg: str) -> None: ...
    def to_string(self) -> str: ...
    def to_strv(self) -> list[str]: ...

class KernelArgsEntry(GObject.GPointer): ...

class MutableTree(GObject.Object):
    """
    :Constructors:

    ::

        MutableTree(**properties)
        new() -> OSTree.MutableTree
        new_from_checksum(repo:OSTree.Repo, contents_checksum:str, metadata_checksum:str) -> OSTree.MutableTree
        new_from_commit(repo:OSTree.Repo, rev:str) -> OSTree.MutableTree

    Object OstreeMutableTree

    Signals from GObject:
      notify (GParam)
    """

    def check_error(self) -> bool: ...
    def ensure_dir(self, name: str) -> Tuple[bool, MutableTree]: ...
    def ensure_parent_dirs(
        self, split_path: Sequence[str], metadata_checksum: str
    ) -> Tuple[bool, MutableTree]: ...
    def fill_empty_from_dirtree(
        self, repo: Repo, contents_checksum: str, metadata_checksum: str
    ) -> bool: ...
    def get_contents_checksum(self) -> str: ...
    def get_files(self) -> dict[str, str]: ...
    def get_metadata_checksum(self) -> str: ...
    def get_subdirs(self) -> dict[str, MutableTree]: ...
    def lookup(self, name: str) -> Tuple[bool, str, MutableTree]: ...
    @classmethod
    def new(cls) -> MutableTree: ...
    @classmethod
    def new_from_checksum(
        cls, repo: Repo, contents_checksum: str, metadata_checksum: str
    ) -> MutableTree: ...
    @classmethod
    def new_from_commit(cls, repo: Repo, rev: str) -> MutableTree: ...
    def remove(self, name: str, allow_noent: bool) -> bool: ...
    def replace_file(self, name: str, checksum: str) -> bool: ...
    def set_contents_checksum(self, checksum: str) -> None: ...
    def set_metadata_checksum(self, checksum: str) -> None: ...
    def walk(
        self, split_path: Sequence[str], start: int
    ) -> Tuple[bool, MutableTree]: ...

class MutableTreeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MutableTreeClass()
    """

    parent_class: GObject.ObjectClass = ...

class MutableTreeIter(GObject.GPointer):
    """
    :Constructors:

    ::

        MutableTreeIter()
    """

    in_files: bool = ...
    iter: dict[None, None] = ...

class Remote(GObject.GBoxed):
    def get_name(self) -> str: ...
    def get_url(self) -> Optional[str]: ...
    def ref(self) -> Remote: ...
    def unref(self) -> None: ...

class Repo(GObject.Object):
    """
    :Constructors:

    ::

        Repo(**properties)
        new(path:Gio.File) -> OSTree.Repo
        new_default() -> OSTree.Repo
        new_for_sysroot_path(repo_path:Gio.File, sysroot_path:Gio.File) -> OSTree.Repo

    Object OstreeRepo

    Signals from OstreeRepo:
      gpg-verify-result (gchararray, OstreeGpgVerifyResult)

    Properties from OstreeRepo:
      path -> GFile: Path
        Path
      remotes-config-dir -> gchararray:

      sysroot-path -> GFile:


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        path: Gio.File
        remotes_config_dir: str
        sysroot_path: Gio.File
    props: Props = ...
    def __init__(
        self,
        path: Gio.File = ...,
        remotes_config_dir: str = ...,
        sysroot_path: Gio.File = ...,
    ): ...
    def abort_transaction(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def add_gpg_signature_summary(
        self,
        key_id: Sequence[str],
        homedir: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def append_gpg_signature(
        self,
        commit_checksum: str,
        signature_bytes: GLib.Bytes,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def checkout_at(
        self,
        options: Optional[RepoCheckoutAtOptions],
        destination_dfd: int,
        destination_path: str,
        commit: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def checkout_gc(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def checkout_tree(
        self,
        mode: RepoCheckoutMode,
        overwrite_mode: RepoCheckoutOverwriteMode,
        destination: Gio.File,
        source: RepoFile,
        source_info: Gio.FileInfo,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def commit_add_composefs_metadata(
        self,
        format_version: int,
        dict: GLib.VariantDict,
        repo_root: RepoFile,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def commit_transaction(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, RepoTransactionStats]: ...
    def copy_config(self) -> GLib.KeyFile: ...
    def create(
        self, mode: RepoMode, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    @staticmethod
    def create_at(
        dfd: int,
        path: str,
        mode: RepoMode,
        options: Optional[GLib.Variant] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Repo: ...
    def delete_object(
        self,
        objtype: ObjectType,
        sha256: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def equal(self, b: Repo) -> bool: ...
    def find_remotes_async(
        self,
        refs: Sequence[CollectionRef],
        options: Optional[GLib.Variant],
        finders: Sequence[RepoFinder],
        progress: Optional[AsyncProgress] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def find_remotes_finish(
        self, result: Gio.AsyncResult
    ) -> list[RepoFinderResult]: ...
    def fsck_object(
        self,
        objtype: ObjectType,
        sha256: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def get_bootloader(self) -> str: ...
    def get_collection_id(self) -> Optional[str]: ...
    def get_config(self) -> GLib.KeyFile: ...
    def get_default_repo_finders(self) -> list[str]: ...
    def get_dfd(self) -> int: ...
    def get_disable_fsync(self) -> bool: ...
    def get_min_free_space_bytes(self) -> Tuple[bool, int]: ...
    def get_mode(self) -> RepoMode: ...
    def get_parent(self) -> Optional[Repo]: ...
    def get_path(self) -> Gio.File: ...
    def get_remote_boolean_option(
        self, remote_name: str, option_name: str, default_value: bool
    ) -> Tuple[bool, bool]: ...
    def get_remote_list_option(
        self, remote_name: str, option_name: str
    ) -> Tuple[bool, list[str]]: ...
    def get_remote_option(
        self, remote_name: str, option_name: str, default_value: Optional[str] = None
    ) -> Tuple[bool, str]: ...
    def gpg_sign_data(
        self,
        data: GLib.Bytes,
        old_signatures: Optional[GLib.Bytes],
        key_id: Sequence[str],
        homedir: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, GLib.Bytes]: ...
    def gpg_verify_data(
        self,
        remote_name: Optional[str],
        data: GLib.Bytes,
        signatures: GLib.Bytes,
        keyringdir: Optional[Gio.File] = None,
        extra_keyring: Optional[Gio.File] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> GpgVerifyResult: ...
    def has_object(
        self,
        objtype: ObjectType,
        checksum: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, bool]: ...
    def hash(self) -> int: ...
    def import_object_from(
        self,
        source: Repo,
        objtype: ObjectType,
        checksum: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def import_object_from_with_trust(
        self,
        source: Repo,
        objtype: ObjectType,
        checksum: str,
        trusted: bool,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def is_system(self) -> bool: ...
    def is_writable(self) -> bool: ...
    def list_collection_refs(
        self,
        match_collection_id: Optional[str],
        flags: RepoListRefsExtFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, dict[CollectionRef, str]]: ...
    def list_commit_objects_starting_with(
        self, start: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, dict[GLib.Variant, GLib.Variant]]: ...
    def list_objects(
        self, flags: RepoListObjectsFlags, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, dict[GLib.Variant, GLib.Variant]]: ...
    def list_refs(
        self,
        refspec_prefix: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, dict[str, str]]: ...
    def list_refs_ext(
        self,
        refspec_prefix: Optional[str],
        flags: RepoListRefsExtFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, dict[str, str]]: ...
    def list_static_delta_indexes(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, list[str]]: ...
    def list_static_delta_names(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, list[str]]: ...
    def load_commit(
        self, checksum: str
    ) -> Tuple[bool, GLib.Variant, RepoCommitState]: ...
    def load_file(
        self, checksum: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, Gio.InputStream, Gio.FileInfo, GLib.Variant]: ...
    def load_object_stream(
        self,
        objtype: ObjectType,
        checksum: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, Gio.InputStream, int]: ...
    def load_variant(
        self, objtype: ObjectType, sha256: str
    ) -> Tuple[bool, GLib.Variant]: ...
    def load_variant_if_exists(
        self, objtype: ObjectType, sha256: str
    ) -> Tuple[bool, GLib.Variant]: ...
    def lock_pop(
        self, lock_type: RepoLockType, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def lock_push(
        self, lock_type: RepoLockType, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def mark_commit_partial(self, checksum: str, is_partial: bool) -> bool: ...
    def mark_commit_partial_reason(
        self, checksum: str, is_partial: bool, in_state: RepoCommitState
    ) -> bool: ...
    @staticmethod
    def mode_from_string(mode: str) -> Tuple[bool, RepoMode]: ...
    @classmethod
    def new(cls, path: Gio.File) -> Repo: ...
    @classmethod
    def new_default(cls) -> Repo: ...
    @classmethod
    def new_for_sysroot_path(
        cls, repo_path: Gio.File, sysroot_path: Gio.File
    ) -> Repo: ...
    def open(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    @staticmethod
    def open_at(
        dfd: int, path: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> Repo: ...
    def prepare_transaction(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, bool]: ...
    def prune(
        self,
        flags: RepoPruneFlags,
        depth: int,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, int, int, int]: ...
    def prune_from_reachable(
        self, options: RepoPruneOptions, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, int, int, int]: ...
    def prune_static_deltas(
        self,
        commit: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def pull(
        self,
        remote_name: str,
        refs_to_fetch: Optional[Sequence[str]],
        flags: RepoPullFlags,
        progress: Optional[AsyncProgress] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    @staticmethod
    def pull_default_console_progress_changed(
        progress: AsyncProgress, user_data: None
    ) -> None: ...
    def pull_from_remotes_async(
        self,
        results: Sequence[RepoFinderResult],
        options: Optional[GLib.Variant] = None,
        progress: Optional[AsyncProgress] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def pull_from_remotes_finish(self, result: Gio.AsyncResult) -> bool: ...
    def pull_one_dir(
        self,
        remote_name: str,
        dir_to_pull: str,
        refs_to_fetch: Optional[Sequence[str]],
        flags: RepoPullFlags,
        progress: Optional[AsyncProgress] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def pull_with_options(
        self,
        remote_name_or_baseurl: str,
        options: GLib.Variant,
        progress: Optional[AsyncProgress] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def query_object_storage_size(
        self,
        objtype: ObjectType,
        sha256: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, int]: ...
    def read_commit(
        self, ref: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, Gio.File, str]: ...
    def read_commit_detached_metadata(
        self, checksum: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, GLib.Variant]: ...
    def regenerate_metadata(
        self,
        additional_metadata: Optional[GLib.Variant] = None,
        options: Optional[GLib.Variant] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def regenerate_summary(
        self,
        additional_metadata: Optional[GLib.Variant] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def reload_config(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def remote_add(
        self,
        name: str,
        url: Optional[str] = None,
        options: Optional[GLib.Variant] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def remote_change(
        self,
        sysroot: Optional[Gio.File],
        changeop: RepoRemoteChange,
        name: str,
        url: Optional[str] = None,
        options: Optional[GLib.Variant] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def remote_delete(
        self, name: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def remote_fetch_summary(
        self, name: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, GLib.Bytes, GLib.Bytes]: ...
    def remote_fetch_summary_with_options(
        self,
        name: str,
        options: Optional[GLib.Variant] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, GLib.Bytes, GLib.Bytes]: ...
    def remote_get_gpg_keys(
        self,
        name: Optional[str] = None,
        key_ids: Optional[Sequence[str]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, list[GLib.Variant]]: ...
    def remote_get_gpg_verify(self, name: str) -> Tuple[bool, bool]: ...
    def remote_get_gpg_verify_summary(self, name: str) -> Tuple[bool, bool]: ...
    def remote_get_url(self, name: str) -> Tuple[bool, str]: ...
    def remote_gpg_import(
        self,
        name: str,
        source_stream: Optional[Gio.InputStream] = None,
        key_ids: Optional[Sequence[str]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, int]: ...
    def remote_list(self) -> list[str]: ...
    def remote_list_collection_refs(
        self, remote_name: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, dict[CollectionRef, str]]: ...
    def remote_list_refs(
        self, remote_name: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, dict[str, str]]: ...
    def resolve_collection_ref(
        self,
        ref: CollectionRef,
        allow_noent: bool,
        flags: RepoResolveRevExtFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, str]: ...
    def resolve_keyring_for_collection(
        self, collection_id: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> Remote: ...
    def resolve_rev(self, refspec: str, allow_noent: bool) -> Tuple[bool, str]: ...
    def resolve_rev_ext(
        self, refspec: str, allow_noent: bool, flags: RepoResolveRevExtFlags
    ) -> Tuple[bool, str]: ...
    def scan_hardlinks(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def set_alias_ref_immediate(
        self,
        remote: Optional[str],
        ref: str,
        target: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def set_cache_dir(
        self, dfd: int, path: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def set_collection_id(self, collection_id: Optional[str] = None) -> bool: ...
    def set_collection_ref_immediate(
        self,
        ref: CollectionRef,
        checksum: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def set_disable_fsync(self, disable_fsync: bool) -> None: ...
    def set_ref_immediate(
        self,
        remote: Optional[str],
        ref: str,
        checksum: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def sign_commit(
        self,
        commit_checksum: str,
        key_id: str,
        homedir: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def sign_delta(
        self,
        from_commit: str,
        to_commit: str,
        key_id: str,
        homedir: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def signature_verify_commit_data(
        self,
        remote_name: str,
        commit_data: GLib.Bytes,
        commit_metadata: GLib.Bytes,
        flags: RepoVerifyFlags,
    ) -> Tuple[bool, str]: ...
    def static_delta_execute_offline(
        self,
        dir_or_file: Gio.File,
        skip_validation: bool,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def static_delta_execute_offline_with_signature(
        self,
        dir_or_file: Gio.File,
        sign: Sign,
        skip_validation: bool,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def static_delta_generate(
        self,
        opt: StaticDeltaGenerateOpt,
        from_: Optional[str],
        to: str,
        metadata: Optional[GLib.Variant] = None,
        params: Optional[GLib.Variant] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def static_delta_reindex(
        self,
        flags: StaticDeltaIndexFlags,
        opt_to_commit: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def static_delta_verify_signature(
        self, delta_id: str, sign: Sign
    ) -> Tuple[bool, str]: ...
    def transaction_set_collection_ref(
        self, ref: CollectionRef, checksum: Optional[str] = None
    ) -> None: ...
    def transaction_set_ref(
        self, remote: Optional[str], ref: str, checksum: Optional[str] = None
    ) -> None: ...
    def transaction_set_refspec(
        self, refspec: str, checksum: Optional[str] = None
    ) -> None: ...
    def traverse_commit(
        self,
        commit_checksum: str,
        maxdepth: int,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, dict[GLib.Variant, GLib.Variant]]: ...
    @staticmethod
    def traverse_new_parents() -> dict[GLib.Variant, GLib.Variant]: ...
    @staticmethod
    def traverse_new_reachable() -> dict[GLib.Variant, GLib.Variant]: ...
    @staticmethod
    def traverse_parents_get_commits(
        parents: dict[None, None], object: GLib.Variant
    ) -> list[str]: ...
    def traverse_reachable_refs(
        self,
        depth: int,
        reachable: dict[GLib.Variant, GLib.Variant],
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def verify_commit(
        self,
        commit_checksum: str,
        keyringdir: Optional[Gio.File] = None,
        extra_keyring: Optional[Gio.File] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def verify_commit_ext(
        self,
        commit_checksum: str,
        keyringdir: Optional[Gio.File] = None,
        extra_keyring: Optional[Gio.File] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> GpgVerifyResult: ...
    def verify_commit_for_remote(
        self,
        commit_checksum: str,
        remote_name: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> GpgVerifyResult: ...
    def verify_summary(
        self,
        remote_name: str,
        summary: GLib.Bytes,
        signatures: GLib.Bytes,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> GpgVerifyResult: ...
    def write_archive_to_mtree(
        self,
        archive: Gio.File,
        mtree: MutableTree,
        modifier: Optional[RepoCommitModifier],
        autocreate_parents: bool,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def write_archive_to_mtree_from_fd(
        self,
        fd: int,
        mtree: MutableTree,
        modifier: Optional[RepoCommitModifier],
        autocreate_parents: bool,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def write_commit(
        self,
        parent: Optional[str],
        subject: Optional[str],
        body: Optional[str],
        metadata: Optional[GLib.Variant],
        root: RepoFile,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, str]: ...
    def write_commit_detached_metadata(
        self,
        checksum: str,
        metadata: Optional[GLib.Variant] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def write_commit_with_time(
        self,
        parent: Optional[str],
        subject: Optional[str],
        body: Optional[str],
        metadata: Optional[GLib.Variant],
        root: RepoFile,
        time: int,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, str]: ...
    def write_config(self, new_config: GLib.KeyFile) -> bool: ...
    def write_content(
        self,
        expected_checksum: Optional[str],
        object_input: Gio.InputStream,
        length: int,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, bytes]: ...
    def write_content_async(
        self,
        expected_checksum: Optional[str],
        object: Gio.InputStream,
        length: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def write_content_finish(self, result: Gio.AsyncResult) -> Tuple[bool, int]: ...
    def write_content_trusted(
        self,
        checksum: str,
        object_input: Gio.InputStream,
        length: int,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def write_dfd_to_mtree(
        self,
        dfd: int,
        path: str,
        mtree: MutableTree,
        modifier: Optional[RepoCommitModifier] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def write_directory_to_mtree(
        self,
        dir: Gio.File,
        mtree: MutableTree,
        modifier: Optional[RepoCommitModifier] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def write_metadata(
        self,
        objtype: ObjectType,
        expected_checksum: Optional[str],
        object: GLib.Variant,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, bytes]: ...
    def write_metadata_async(
        self,
        objtype: ObjectType,
        expected_checksum: Optional[str],
        object: GLib.Variant,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def write_metadata_finish(self, result: Gio.AsyncResult) -> Tuple[bool, bytes]: ...
    def write_metadata_stream_trusted(
        self,
        objtype: ObjectType,
        checksum: str,
        object_input: Gio.InputStream,
        length: int,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def write_metadata_trusted(
        self,
        objtype: ObjectType,
        checksum: str,
        variant: GLib.Variant,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def write_mtree(
        self, mtree: MutableTree, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, Gio.File]: ...
    def write_regfile(
        self,
        expected_checksum: Optional[str],
        uid: int,
        gid: int,
        mode: int,
        content_len: int,
        xattrs: Optional[GLib.Variant] = None,
    ) -> ContentWriter: ...
    def write_regfile_inline(
        self,
        expected_checksum: Optional[str],
        uid: int,
        gid: int,
        mode: int,
        xattrs: Optional[GLib.Variant],
        buf: Sequence[int],
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> str: ...
    def write_symlink(
        self,
        expected_checksum: Optional[str],
        uid: int,
        gid: int,
        xattrs: Optional[GLib.Variant],
        symlink_target: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> str: ...

class RepoCheckoutAtOptions(GObject.GPointer):
    """
    :Constructors:

    ::

        RepoCheckoutAtOptions()
    """

    mode: RepoCheckoutMode = ...
    overwrite_mode: RepoCheckoutOverwriteMode = ...
    enable_uncompressed_cache: bool = ...
    enable_fsync: bool = ...
    process_whiteouts: bool = ...
    no_copy_fallback: bool = ...
    force_copy: bool = ...
    bareuseronly_dirs: bool = ...
    force_copy_zerosized: bool = ...
    process_passthrough_whiteouts: bool = ...
    unused_bools: list[bool] = ...
    subpath: str = ...
    devino_to_csum_cache: RepoDevInoCache = ...
    unused_ints: list[int] = ...
    unused_ptrs: list[None] = ...
    filter: Callable[..., RepoCheckoutFilterResult] = ...
    filter_user_data: None = ...
    sepolicy: SePolicy = ...
    sepolicy_prefix: str = ...
    def set_devino(self, cache: Optional[RepoDevInoCache] = None) -> None: ...

class RepoCommitModifier(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(flags:OSTree.RepoCommitModifierFlags, commit_filter:OSTree.RepoCommitFilter=None, user_data=None) -> OSTree.RepoCommitModifier
    """

    @classmethod
    def new(
        cls,
        flags: RepoCommitModifierFlags,
        commit_filter: Optional[Callable[..., RepoCommitFilterResult]] = None,
        *user_data: Any,
    ) -> RepoCommitModifier: ...
    def ref(self) -> RepoCommitModifier: ...
    def set_devino_cache(self, cache: RepoDevInoCache) -> None: ...
    def set_sepolicy(self, sepolicy: Optional[SePolicy] = None) -> None: ...
    def set_sepolicy_from_commit(
        self, repo: Repo, rev: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def set_xattr_callback(
        self, callback: Callable[..., GLib.Variant], *user_data: Any
    ) -> None: ...
    def unref(self) -> None: ...

class RepoCommitTraverseIter(GObject.GPointer):
    """
    :Constructors:

    ::

        RepoCommitTraverseIter()
    """

    initialized: bool = ...
    dummy: list[None] = ...
    dummy_checksum_data: list[int] = ...
    @staticmethod
    def cleanup(p: None) -> None: ...
    def clear(self) -> None: ...
    def get_dir(self) -> Tuple[str, str, str]: ...
    def get_file(self) -> Tuple[str, str]: ...
    def init_commit(
        self, repo: Repo, commit: GLib.Variant, flags: RepoCommitTraverseFlags
    ) -> bool: ...
    def init_dirtree(
        self, repo: Repo, dirtree: GLib.Variant, flags: RepoCommitTraverseFlags
    ) -> bool: ...
    def next(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> RepoCommitIterResult: ...

class RepoDevInoCache(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> OSTree.RepoDevInoCache
    """

    @classmethod
    def new(cls) -> RepoDevInoCache: ...
    def ref(self) -> RepoDevInoCache: ...
    def unref(self) -> None: ...

class RepoFile(GObject.Object, Gio.File):
    """
    :Constructors:

    ::

        RepoFile(**properties)

    Object OstreeRepoFile

    Signals from GObject:
      notify (GParam)
    """

    def ensure_resolved(self) -> bool: ...
    def get_checksum(self) -> str: ...
    def get_repo(self) -> Repo: ...
    def get_root(self) -> RepoFile: ...
    def get_xattrs(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, GLib.Variant]: ...
    def tree_find_child(self, name: str) -> Tuple[int, bool, GLib.Variant]: ...
    def tree_get_contents(self) -> Optional[GLib.Variant]: ...
    def tree_get_contents_checksum(self) -> Optional[str]: ...
    def tree_get_metadata(self) -> Optional[GLib.Variant]: ...
    def tree_get_metadata_checksum(self) -> Optional[str]: ...
    def tree_query_child(
        self,
        n: int,
        attributes: str,
        flags: Gio.FileQueryInfoFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, Gio.FileInfo]: ...
    def tree_set_metadata(self, checksum: str, metadata: GLib.Variant) -> None: ...

class RepoFileClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RepoFileClass()
    """

    parent_class: GObject.ObjectClass = ...

class RepoFinder(GObject.GInterface):
    """
    Interface OstreeRepoFinder

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def resolve_all_async(
        finders: Sequence[RepoFinder],
        refs: Sequence[CollectionRef],
        parent_repo: Repo,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def resolve_all_finish(result: Gio.AsyncResult) -> list[RepoFinderResult]: ...
    def resolve_async(
        self,
        refs: Sequence[CollectionRef],
        parent_repo: Repo,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def resolve_finish(self, result: Gio.AsyncResult) -> list[RepoFinderResult]: ...

class RepoFinderAvahi(GObject.Object, RepoFinder):
    """
    :Constructors:

    ::

        RepoFinderAvahi(**properties)
        new(context:GLib.MainContext=None) -> OSTree.RepoFinderAvahi

    Object OstreeRepoFinderAvahi

    Signals from GObject:
      notify (GParam)
    """

    @classmethod
    def new(cls, context: Optional[GLib.MainContext] = None) -> RepoFinderAvahi: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class RepoFinderAvahiClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RepoFinderAvahiClass()
    """

    parent_class: GObject.ObjectClass = ...

class RepoFinderConfig(GObject.Object, RepoFinder):
    """
    :Constructors:

    ::

        RepoFinderConfig(**properties)
        new() -> OSTree.RepoFinderConfig

    Object OstreeRepoFinderConfig

    Signals from GObject:
      notify (GParam)
    """

    @classmethod
    def new(cls) -> RepoFinderConfig: ...

class RepoFinderConfigClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RepoFinderConfigClass()
    """

    parent_class: GObject.ObjectClass = ...

class RepoFinderInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        RepoFinderInterface()
    """

    g_iface: GObject.TypeInterface = ...
    resolve_async: Callable[..., None] = ...
    resolve_finish: Callable[
        [RepoFinder, Gio.AsyncResult], list[RepoFinderResult]
    ] = ...

class RepoFinderMount(GObject.Object, RepoFinder):
    """
    :Constructors:

    ::

        RepoFinderMount(**properties)
        new(monitor:Gio.VolumeMonitor=None) -> OSTree.RepoFinderMount

    Object OstreeRepoFinderMount

    Properties from OstreeRepoFinderMount:
      monitor -> GVolumeMonitor: Volume Monitor
        Volume monitor to use to look up mounted volumes when queried.

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        monitor: Gio.VolumeMonitor
    props: Props = ...
    def __init__(self, monitor: Gio.VolumeMonitor = ...): ...
    @classmethod
    def new(cls, monitor: Optional[Gio.VolumeMonitor] = None) -> RepoFinderMount: ...

class RepoFinderMountClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RepoFinderMountClass()
    """

    parent_class: GObject.ObjectClass = ...

class RepoFinderOverride(GObject.Object, RepoFinder):
    """
    :Constructors:

    ::

        RepoFinderOverride(**properties)
        new() -> OSTree.RepoFinderOverride

    Object OstreeRepoFinderOverride

    Signals from GObject:
      notify (GParam)
    """

    def add_uri(self, uri: str) -> None: ...
    @classmethod
    def new(cls) -> RepoFinderOverride: ...

class RepoFinderOverrideClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RepoFinderOverrideClass()
    """

    parent_class: GObject.ObjectClass = ...

class RepoFinderResult(GObject.GBoxed):
    """
    :Constructors:

    ::

        RepoFinderResult()
        new(remote:OSTree.Remote, finder:OSTree.RepoFinder, priority:int, ref_to_checksum:dict, ref_to_timestamp:dict=None, summary_last_modified:int) -> OSTree.RepoFinderResult
    """

    remote: Remote = ...
    finder: RepoFinder = ...
    priority: int = ...
    ref_to_checksum: dict[CollectionRef, str] = ...
    summary_last_modified: int = ...
    ref_to_timestamp: dict[CollectionRef, int] = ...
    padding: list[None] = ...
    def compare(self, b: RepoFinderResult) -> int: ...
    def dup(self) -> RepoFinderResult: ...
    def free(self) -> None: ...
    @staticmethod
    def freev(results: Sequence[RepoFinderResult]) -> None: ...
    @classmethod
    def new(
        cls,
        remote: Remote,
        finder: RepoFinder,
        priority: int,
        ref_to_checksum: dict[CollectionRef, str],
        ref_to_timestamp: Optional[dict[CollectionRef, int]],
        summary_last_modified: int,
    ) -> RepoFinderResult: ...

class RepoPruneOptions(GObject.GPointer):
    """
    :Constructors:

    ::

        RepoPruneOptions()
    """

    flags: RepoPruneFlags = ...
    reachable: dict[None, None] = ...
    unused_bools: list[bool] = ...
    unused_ints: list[int] = ...
    unused_ptrs: list[None] = ...

class RepoTransactionStats(GObject.GBoxed):
    """
    :Constructors:

    ::

        RepoTransactionStats()
    """

    metadata_objects_total: int = ...
    metadata_objects_written: int = ...
    content_objects_total: int = ...
    content_objects_written: int = ...
    content_bytes_written: int = ...
    devino_cache_hits: int = ...
    padding1: int = ...
    padding2: int = ...
    padding3: int = ...
    padding4: int = ...

class SePolicy(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        SePolicy(**properties)
        new(path:Gio.File, cancellable:Gio.Cancellable=None) -> OSTree.SePolicy
        new_at(rootfs_dfd:int, cancellable:Gio.Cancellable=None) -> OSTree.SePolicy
        new_from_commit(repo:OSTree.Repo, rev:str, cancellable:Gio.Cancellable=None) -> OSTree.SePolicy

    Object OstreeSePolicy

    Properties from OstreeSePolicy:
      path -> GFile:

      rootfs-dfd -> gint:


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        path: Optional[Gio.File]
        rootfs_dfd: int
    props: Props = ...
    def __init__(self, path: Gio.File = ..., rootfs_dfd: int = ...): ...
    @staticmethod
    def fscreatecon_cleanup(unused: None) -> None: ...
    def get_csum(self) -> Optional[str]: ...
    def get_label(
        self,
        relpath: str,
        unix_mode: int,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, str]: ...
    def get_name(self) -> str: ...
    def get_path(self) -> Optional[Gio.File]: ...
    @classmethod
    def new(
        cls, path: Gio.File, cancellable: Optional[Gio.Cancellable] = None
    ) -> SePolicy: ...
    @classmethod
    def new_at(
        cls, rootfs_dfd: int, cancellable: Optional[Gio.Cancellable] = None
    ) -> SePolicy: ...
    @classmethod
    def new_from_commit(
        cls, repo: Repo, rev: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> SePolicy: ...
    def restorecon(
        self,
        path: str,
        info: Optional[Gio.FileInfo],
        target: Gio.File,
        flags: SePolicyRestoreconFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, str]: ...
    def setfscreatecon(self, path: str, mode: int) -> bool: ...

class Sign(GObject.GInterface):
    """
    Interface OstreeSign

    Signals from GObject:
      notify (GParam)
    """

    def add_pk(self, public_key: GLib.Variant) -> bool: ...
    def clear_keys(self) -> bool: ...
    def commit(
        self,
        repo: Repo,
        commit_checksum: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def commit_verify(
        self,
        repo: Repo,
        commit_checksum: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, str]: ...
    def data(
        self, data: GLib.Bytes, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, GLib.Bytes]: ...
    def data_verify(
        self, data: GLib.Bytes, signatures: GLib.Variant
    ) -> Tuple[bool, str]: ...
    def ed25519_add_pk(self, public_key: GLib.Variant) -> bool: ...
    def ed25519_clear_keys(self) -> bool: ...
    def ed25519_data(
        self,
        data: GLib.Bytes,
        signature: GLib.Bytes,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def ed25519_data_verify(
        self, data: GLib.Bytes, signatures: GLib.Variant, out_success_message: str
    ) -> bool: ...
    def ed25519_get_name(self) -> str: ...
    def ed25519_load_pk(self, options: GLib.Variant) -> bool: ...
    def ed25519_metadata_format(self) -> str: ...
    def ed25519_metadata_key(self) -> str: ...
    def ed25519_set_pk(self, public_key: GLib.Variant) -> bool: ...
    def ed25519_set_sk(self, secret_key: GLib.Variant) -> bool: ...
    @staticmethod
    def get_all() -> list[Sign]: ...
    @staticmethod
    def get_by_name(name: str) -> Sign: ...
    def get_name(self) -> str: ...
    def load_pk(self, options: GLib.Variant) -> bool: ...
    def metadata_format(self) -> str: ...
    def metadata_key(self) -> str: ...
    def set_pk(self, public_key: GLib.Variant) -> bool: ...
    def set_sk(self, secret_key: GLib.Variant) -> bool: ...
    def summary(
        self,
        repo: Repo,
        keys: GLib.Variant,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...

class SignEd25519(GObject.GPointer): ...

class SignEd25519Class(GObject.GPointer):
    """
    :Constructors:

    ::

        SignEd25519Class()
    """

    parent_class: GObject.ObjectClass = ...

class SignInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        SignInterface()
    """

    g_iface: GObject.TypeInterface = ...
    get_name: Callable[[Sign], str] = ...
    data: Callable[
        [Sign, GLib.Bytes, Optional[Gio.Cancellable]], Tuple[bool, GLib.Bytes]
    ] = ...
    data_verify: Callable[[Sign, GLib.Bytes, GLib.Variant], Tuple[bool, str]] = ...
    metadata_key: Callable[[Sign], str] = ...
    metadata_format: Callable[[Sign], str] = ...
    clear_keys: Callable[[Sign], bool] = ...
    set_sk: Callable[[Sign, GLib.Variant], bool] = ...
    set_pk: Callable[[Sign, GLib.Variant], bool] = ...
    add_pk: Callable[[Sign, GLib.Variant], bool] = ...
    load_pk: Callable[[Sign, GLib.Variant], bool] = ...

class Sysroot(GObject.Object):
    """
    :Constructors:

    ::

        Sysroot(**properties)
        new(path:Gio.File=None) -> OSTree.Sysroot
        new_default() -> OSTree.Sysroot

    Object OstreeSysroot

    Signals from OstreeSysroot:
      journal-msg (gchararray)

    Properties from OstreeSysroot:
      path -> GFile:


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        path: Gio.File
    props: Props = ...
    def __init__(self, path: Gio.File = ...): ...
    def cleanup(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def cleanup_prune_repo(
        self, options: RepoPruneOptions, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, int, int, int]: ...
    def deploy_tree(
        self,
        osname: Optional[str],
        revision: str,
        origin: Optional[GLib.KeyFile] = None,
        provided_merge_deployment: Optional[Deployment] = None,
        override_kernel_argv: Optional[Sequence[str]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, Deployment]: ...
    def deploy_tree_with_options(
        self,
        osname: Optional[str],
        revision: str,
        origin: Optional[GLib.KeyFile] = None,
        provided_merge_deployment: Optional[Deployment] = None,
        opts: Optional[SysrootDeployTreeOpts] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, Deployment]: ...
    def deployment_set_kargs(
        self,
        deployment: Deployment,
        new_kargs: Sequence[str],
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def deployment_set_kargs_in_place(
        self,
        deployment: Deployment,
        kargs_str: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def deployment_set_mutable(
        self,
        deployment: Deployment,
        is_mutable: bool,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def deployment_set_pinned(
        self, deployment: Deployment, is_pinned: bool
    ) -> bool: ...
    def deployment_unlock(
        self,
        deployment: Deployment,
        unlocked_state: DeploymentUnlockedState,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def ensure_initialized(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def get_booted_deployment(self) -> Optional[Deployment]: ...
    def get_bootversion(self) -> int: ...
    def get_deployment_directory(self, deployment: Deployment) -> Gio.File: ...
    def get_deployment_dirpath(self, deployment: Deployment) -> str: ...
    @staticmethod
    def get_deployment_origin_path(deployment_path: Gio.File) -> Gio.File: ...
    def get_deployments(self) -> list[Deployment]: ...
    def get_fd(self) -> int: ...
    def get_merge_deployment(
        self, osname: Optional[str] = None
    ) -> Optional[Deployment]: ...
    def get_path(self) -> Gio.File: ...
    def get_repo(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, Repo]: ...
    def get_staged_deployment(self) -> Optional[Deployment]: ...
    def get_subbootversion(self) -> int: ...
    def init_osname(
        self, osname: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def initialize(self) -> bool: ...
    def initialize_with_mount_namespace(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def is_booted(self) -> bool: ...
    def load(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def load_if_changed(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, bool]: ...
    def lock(self) -> bool: ...
    def lock_async(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def lock_finish(self, result: Gio.AsyncResult) -> bool: ...
    @classmethod
    def new(cls, path: Optional[Gio.File] = None) -> Sysroot: ...
    @classmethod
    def new_default(cls) -> Sysroot: ...
    def origin_new_from_refspec(self, refspec: str) -> GLib.KeyFile: ...
    def prepare_cleanup(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def query_deployments_for(
        self, osname: Optional[str] = None
    ) -> Tuple[Deployment, Deployment]: ...
    def repo(self) -> Repo: ...
    def require_booted_deployment(self) -> Deployment: ...
    def set_mount_namespace_in_use(self) -> None: ...
    def simple_write_deployment(
        self,
        osname: Optional[str],
        new_deployment: Deployment,
        merge_deployment: Optional[Deployment],
        flags: SysrootSimpleWriteDeploymentFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def stage_overlay_initrd(
        self, fd: int, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, str]: ...
    def stage_tree(
        self,
        osname: Optional[str],
        revision: str,
        origin: Optional[GLib.KeyFile] = None,
        merge_deployment: Optional[Deployment] = None,
        override_kernel_argv: Optional[Sequence[str]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, Deployment]: ...
    def stage_tree_with_options(
        self,
        osname: Optional[str],
        revision: str,
        origin: Optional[GLib.KeyFile],
        merge_deployment: Optional[Deployment],
        opts: SysrootDeployTreeOpts,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, Deployment]: ...
    def try_lock(self) -> Tuple[bool, bool]: ...
    def unload(self) -> None: ...
    def unlock(self) -> None: ...
    def write_deployments(
        self,
        new_deployments: Sequence[Deployment],
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def write_deployments_with_options(
        self,
        new_deployments: Sequence[Deployment],
        opts: SysrootWriteDeploymentsOpts,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def write_origin_file(
        self,
        deployment: Deployment,
        new_origin: Optional[GLib.KeyFile] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...

class SysrootDeployTreeOpts(GObject.GPointer):
    """
    :Constructors:

    ::

        SysrootDeployTreeOpts()
    """

    unused_bools: list[bool] = ...
    unused_ints: list[int] = ...
    override_kernel_argv: str = ...
    overlay_initrds: str = ...
    unused_ptrs: list[None] = ...

class SysrootUpgrader(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        SysrootUpgrader(**properties)
        new(sysroot:OSTree.Sysroot, cancellable:Gio.Cancellable=None) -> OSTree.SysrootUpgrader
        new_for_os(sysroot:OSTree.Sysroot, osname:str=None, cancellable:Gio.Cancellable=None) -> OSTree.SysrootUpgrader
        new_for_os_with_flags(sysroot:OSTree.Sysroot, osname:str=None, flags:OSTree.SysrootUpgraderFlags, cancellable:Gio.Cancellable=None) -> OSTree.SysrootUpgrader

    Object OstreeSysrootUpgrader

    Properties from OstreeSysrootUpgrader:
      sysroot -> OstreeSysroot:

      osname -> gchararray:

      flags -> OstreeSysrootUpgraderFlags:


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        flags: SysrootUpgraderFlags
        osname: str
        sysroot: Sysroot
    props: Props = ...
    def __init__(
        self,
        flags: SysrootUpgraderFlags = ...,
        osname: str = ...,
        sysroot: Sysroot = ...,
    ): ...
    @staticmethod
    def check_timestamps(repo: Repo, from_rev: str, to_rev: str) -> bool: ...
    def deploy(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def dup_origin(self) -> Optional[GLib.KeyFile]: ...
    def get_origin(self) -> Optional[GLib.KeyFile]: ...
    def get_origin_description(self) -> Optional[str]: ...
    @classmethod
    def new(
        cls, sysroot: Sysroot, cancellable: Optional[Gio.Cancellable] = None
    ) -> SysrootUpgrader: ...
    @classmethod
    def new_for_os(
        cls,
        sysroot: Sysroot,
        osname: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> SysrootUpgrader: ...
    @classmethod
    def new_for_os_with_flags(
        cls,
        sysroot: Sysroot,
        osname: Optional[str],
        flags: SysrootUpgraderFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> SysrootUpgrader: ...
    def pull(
        self,
        flags: RepoPullFlags,
        upgrader_flags: SysrootUpgraderPullFlags,
        progress: Optional[AsyncProgress] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, bool]: ...
    def pull_one_dir(
        self,
        dir_to_pull: str,
        flags: RepoPullFlags,
        upgrader_flags: SysrootUpgraderPullFlags,
        progress: Optional[AsyncProgress] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, bool]: ...
    def set_origin(
        self,
        origin: Optional[GLib.KeyFile] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...

class SysrootWriteDeploymentsOpts(GObject.GPointer):
    """
    :Constructors:

    ::

        SysrootWriteDeploymentsOpts()
    """

    do_postclean: bool = ...
    disable_auto_early_prune: bool = ...
    unused_bools: list[bool] = ...
    unused_ints: list[int] = ...
    unused_ptrs: list[None] = ...

class ChecksumFlags(GObject.GFlags):
    CANONICAL_PERMISSIONS = 2
    IGNORE_XATTRS = 1
    NONE = 0

class DiffFlags(GObject.GFlags):
    IGNORE_XATTRS = 1
    NONE = 0

class GpgSignatureFormatFlags(GObject.GFlags):
    GPG_SIGNATURE_FORMAT_DEFAULT = 0

class RepoCommitModifierFlags(GObject.GFlags):
    CANONICAL_PERMISSIONS = 4
    CONSUME = 16
    DEVINO_CANONICAL = 32
    ERROR_ON_UNLABELED = 8
    GENERATE_SIZES = 2
    NONE = 0
    SKIP_XATTRS = 1

class RepoCommitState(GObject.GFlags):
    FSCK_PARTIAL = 2
    NORMAL = 0
    PARTIAL = 1

class RepoCommitTraverseFlags(GObject.GFlags):
    COMMIT_ONLY = 2
    NONE = 1

class RepoListObjectsFlags(GObject.GFlags):
    ALL = 4
    LOOSE = 1
    NO_PARENTS = 8
    PACKED = 2

class RepoListRefsExtFlags(GObject.GFlags):
    ALIASES = 1
    EXCLUDE_MIRRORS = 4
    EXCLUDE_REMOTES = 2
    NONE = 0

class RepoPruneFlags(GObject.GFlags):
    COMMIT_ONLY = 4
    NONE = 0
    NO_PRUNE = 1
    REFS_ONLY = 2

class RepoPullFlags(GObject.GFlags):
    BAREUSERONLY_FILES = 8
    COMMIT_ONLY = 2
    MIRROR = 1
    NONE = 0
    TRUSTED_HTTP = 16
    UNTRUSTED = 4

class RepoResolveRevExtFlags(GObject.GFlags):
    LOCAL_ONLY = 1
    NONE = 0

class RepoVerifyFlags(GObject.GFlags):
    NONE = 0
    NO_GPG = 1
    NO_SIGNAPI = 2

class SePolicyRestoreconFlags(GObject.GFlags):
    ALLOW_NOLABEL = 1
    KEEP_EXISTING = 2
    NONE = 0

class SysrootSimpleWriteDeploymentFlags(GObject.GFlags):
    NONE = 0
    NOT_DEFAULT = 2
    NO_CLEAN = 4
    RETAIN = 1
    RETAIN_PENDING = 8
    RETAIN_ROLLBACK = 16

class SysrootUpgraderFlags(GObject.GFlags):
    IGNORE_UNCONFIGURED = 2
    STAGE = 4

class SysrootUpgraderPullFlags(GObject.GFlags):
    ALLOW_OLDER = 1
    NONE = 0
    SYNTHETIC = 2

class DeploymentUnlockedState(GObject.GEnum):
    DEVELOPMENT = 1
    HOTFIX = 2
    NONE = 0
    TRANSIENT = 3

class GpgError(GObject.GEnum):
    EXPIRED_KEY = 4
    EXPIRED_SIGNATURE = 3
    INVALID_SIGNATURE = 1
    MISSING_KEY = 2
    NO_SIGNATURE = 0
    REVOKED_KEY = 5

class GpgSignatureAttr(GObject.GEnum):
    EXP_TIMESTAMP = 7
    FINGERPRINT = 5
    FINGERPRINT_PRIMARY = 12
    HASH_ALGO_NAME = 9
    KEY_EXPIRED = 2
    KEY_EXP_TIMESTAMP = 13
    KEY_EXP_TIMESTAMP_PRIMARY = 14
    KEY_MISSING = 4
    KEY_REVOKED = 3
    PUBKEY_ALGO_NAME = 8
    SIG_EXPIRED = 1
    TIMESTAMP = 6
    USER_EMAIL = 11
    USER_NAME = 10
    VALID = 0

class ObjectType(GObject.GEnum):
    COMMIT = 4
    COMMIT_META = 6
    DIR_META = 3
    DIR_TREE = 2
    FILE = 1
    FILE_XATTRS = 8
    FILE_XATTRS_LINK = 9
    PAYLOAD_LINK = 7
    TOMBSTONE_COMMIT = 5

class RepoCheckoutFilterResult(GObject.GEnum):
    ALLOW = 0
    SKIP = 1

class RepoCheckoutMode(GObject.GEnum):
    NONE = 0
    USER = 1

class RepoCheckoutOverwriteMode(GObject.GEnum):
    ADD_FILES = 2
    NONE = 0
    UNION_FILES = 1
    UNION_IDENTICAL = 3

class RepoCommitFilterResult(GObject.GEnum):
    ALLOW = 0
    SKIP = 1

class RepoCommitIterResult(GObject.GEnum):
    DIR = 3
    END = 1
    ERROR = 0
    FILE = 2

class RepoLockType(GObject.GEnum):
    EXCLUSIVE = 1
    SHARED = 0

class RepoMode(GObject.GEnum):
    ARCHIVE = 1
    ARCHIVE_Z2 = 1
    BARE = 0
    BARE_SPLIT_XATTRS = 4
    BARE_USER = 2
    BARE_USER_ONLY = 3

class RepoRemoteChange(GObject.GEnum):
    ADD = 0
    ADD_IF_NOT_EXISTS = 1
    DELETE = 2
    DELETE_IF_EXISTS = 3
    REPLACE = 4

class StaticDeltaGenerateOpt(GObject.GEnum):
    LOWLATENCY = 0
    MAJOR = 1

class StaticDeltaIndexFlags(GObject.GEnum):
    STATIC_DELTA_INDEX_FLAGS_NONE = 0
