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

MAJOR_VERSION: int = 1
MICRO_VERSION: int = 4
MINOR_VERSION: int = 15
_lock = ...  # FIXME Constant
_namespace: str = "Flatpak"
_version: str = "1.0"

def error_quark() -> int: ...
def get_default_arch() -> str: ...
def get_supported_arches() -> list[str]: ...
def get_system_installations(
    cancellable: Optional[Gio.Cancellable] = None,
) -> list[Installation]: ...
def portal_error_quark() -> int: ...
def transaction_operation_type_to_string(kind: TransactionOperationType) -> str: ...

class BundleRef(Ref):
    """
    :Constructors:

    ::

        BundleRef(**properties)
        new(file:Gio.File) -> Flatpak.BundleRef

    Object FlatpakBundleRef

    Properties from FlatpakBundleRef:
      file -> GFile:


    Properties from FlatpakRef:
      name -> gchararray: Name
        The name of the application or runtime
      arch -> gchararray: Architecture
        The architecture of the application or runtime
      branch -> gchararray: Branch
        The branch of the application or runtime
      commit -> gchararray: Commit
        The commit
      kind -> FlatpakRefKind: Kind
        The kind of artifact
      collection-id -> gchararray: Collection ID
        The collection ID

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        file: Gio.File
        arch: str
        branch: str
        collection_id: str
        commit: str
        kind: RefKind
        name: str
    props: Props = ...
    parent: Ref = ...
    def __init__(
        self,
        file: Gio.File = ...,
        arch: str = ...,
        branch: str = ...,
        collection_id: str = ...,
        commit: str = ...,
        kind: RefKind = ...,
        name: str = ...,
    ): ...
    def get_appstream(self) -> GLib.Bytes: ...
    def get_file(self) -> Gio.File: ...
    def get_icon(self, size: int) -> GLib.Bytes: ...
    def get_installed_size(self) -> int: ...
    def get_metadata(self) -> GLib.Bytes: ...
    def get_origin(self) -> str: ...
    def get_runtime_repo_url(self) -> str: ...
    @classmethod
    def new(cls, file: Gio.File) -> BundleRef: ...

class BundleRefClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BundleRefClass()
    """

    parent_class: RefClass = ...

class Installation(GObject.Object):
    """
    :Constructors:

    ::

        Installation(**properties)
        new_for_path(path:Gio.File, user:bool, cancellable:Gio.Cancellable=None) -> Flatpak.Installation
        new_system(cancellable:Gio.Cancellable=None) -> Flatpak.Installation
        new_system_with_id(id:str=None, cancellable:Gio.Cancellable=None) -> Flatpak.Installation
        new_user(cancellable:Gio.Cancellable=None) -> Flatpak.Installation

    Object FlatpakInstallation

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    def add_remote(
        self,
        remote: Remote,
        if_needed: bool,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def cleanup_local_refs_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def create_monitor(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Gio.FileMonitor: ...
    def drop_caches(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def fetch_remote_metadata_sync(
        self, remote_name: str, ref: Ref, cancellable: Optional[Gio.Cancellable] = None
    ) -> GLib.Bytes: ...
    def fetch_remote_ref_sync(
        self,
        remote_name: str,
        kind: RefKind,
        name: str,
        arch: Optional[str] = None,
        branch: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> RemoteRef: ...
    def fetch_remote_ref_sync_full(
        self,
        remote_name: str,
        kind: RefKind,
        name: str,
        arch: Optional[str],
        branch: Optional[str],
        flags: QueryFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> RemoteRef: ...
    def fetch_remote_size_sync(
        self, remote_name: str, ref: Ref, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, int, int]: ...
    def get_config(
        self, key: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> str: ...
    def get_current_installed_app(
        self, name: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> InstalledRef: ...
    def get_default_languages(self) -> list[str]: ...
    def get_default_locales(self) -> list[str]: ...
    def get_display_name(self) -> str: ...
    def get_id(self) -> str: ...
    def get_installed_ref(
        self,
        kind: RefKind,
        name: str,
        arch: Optional[str] = None,
        branch: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> InstalledRef: ...
    def get_is_user(self) -> bool: ...
    def get_min_free_space_bytes(self) -> Tuple[bool, int]: ...
    def get_no_interaction(self) -> bool: ...
    def get_path(self) -> Gio.File: ...
    def get_priority(self) -> int: ...
    def get_remote_by_name(
        self, name: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> Remote: ...
    def get_storage_type(self) -> StorageType: ...
    def install(
        self,
        remote_name: str,
        kind: RefKind,
        name: str,
        arch: Optional[str] = None,
        branch: Optional[str] = None,
        progress: Optional[Callable[..., None]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        *progress_data: Any,
    ) -> InstalledRef: ...
    def install_bundle(
        self,
        file: Gio.File,
        progress: Optional[Callable[..., None]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        *progress_data: Any,
    ) -> InstalledRef: ...
    def install_full(
        self,
        flags: InstallFlags,
        remote_name: str,
        kind: RefKind,
        name: str,
        arch: Optional[str] = None,
        branch: Optional[str] = None,
        subpaths: Optional[Sequence[str]] = None,
        progress: Optional[Callable[..., None]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        *progress_data: Any,
    ) -> InstalledRef: ...
    def install_ref_file(
        self, ref_file_data: GLib.Bytes, cancellable: Optional[Gio.Cancellable] = None
    ) -> RemoteRef: ...
    def launch(
        self,
        name: str,
        arch: Optional[str] = None,
        branch: Optional[str] = None,
        commit: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def launch_full(
        self,
        flags: LaunchFlags,
        name: str,
        arch: Optional[str] = None,
        branch: Optional[str] = None,
        commit: Optional[str] = None,
        instance_out: Optional[Instance] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def list_installed_refs(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> list[InstalledRef]: ...
    def list_installed_refs_by_kind(
        self, kind: RefKind, cancellable: Optional[Gio.Cancellable] = None
    ) -> list[InstalledRef]: ...
    def list_installed_refs_for_update(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> list[InstalledRef]: ...
    def list_installed_related_refs_sync(
        self, remote_name: str, ref: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> list[RelatedRef]: ...
    def list_pinned_refs(
        self, arch: Optional[str] = None, cancellable: Optional[Gio.Cancellable] = None
    ) -> list[InstalledRef]: ...
    def list_remote_refs_sync(
        self, remote_or_uri: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> list[RemoteRef]: ...
    def list_remote_refs_sync_full(
        self,
        remote_or_uri: str,
        flags: QueryFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> list[RemoteRef]: ...
    def list_remote_related_refs_for_installed_sync(
        self, remote_name: str, ref: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> list[RelatedRef]: ...
    def list_remote_related_refs_sync(
        self, remote_name: str, ref: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> list[RelatedRef]: ...
    def list_remotes(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> list[Remote]: ...
    def list_remotes_by_type(
        self, types: Sequence[RemoteType], cancellable: Optional[Gio.Cancellable] = None
    ) -> list[Remote]: ...
    def list_unused_refs(
        self, arch: Optional[str] = None, cancellable: Optional[Gio.Cancellable] = None
    ) -> list[InstalledRef]: ...
    def list_unused_refs_with_options(
        self,
        arch: Optional[str] = None,
        metadata_injection: Optional[dict[None, None]] = None,
        options: Optional[GLib.Variant] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> list[InstalledRef]: ...
    def load_app_overrides(
        self, app_id: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> str: ...
    def modify_remote(
        self, remote: Remote, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    @classmethod
    def new_for_path(
        cls, path: Gio.File, user: bool, cancellable: Optional[Gio.Cancellable] = None
    ) -> Installation: ...
    @classmethod
    def new_system(
        cls, cancellable: Optional[Gio.Cancellable] = None
    ) -> Installation: ...
    @classmethod
    def new_system_with_id(
        cls, id: Optional[str] = None, cancellable: Optional[Gio.Cancellable] = None
    ) -> Installation: ...
    @classmethod
    def new_user(
        cls, cancellable: Optional[Gio.Cancellable] = None
    ) -> Installation: ...
    def prune_local_repo(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def remove_local_ref_sync(
        self, remote_name: str, ref: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def remove_remote(
        self, name: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def run_triggers(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def set_config_sync(
        self, key: str, value: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def set_no_interaction(self, no_interaction: bool) -> None: ...
    def uninstall(
        self,
        kind: RefKind,
        name: str,
        arch: Optional[str] = None,
        branch: Optional[str] = None,
        progress: Optional[Callable[..., None]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        *progress_data: Any,
    ) -> bool: ...
    def uninstall_full(
        self,
        flags: UninstallFlags,
        kind: RefKind,
        name: str,
        arch: Optional[str] = None,
        branch: Optional[str] = None,
        progress: Optional[Callable[..., None]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        *progress_data: Any,
    ) -> bool: ...
    def update(
        self,
        flags: UpdateFlags,
        kind: RefKind,
        name: str,
        arch: Optional[str] = None,
        branch: Optional[str] = None,
        progress: Optional[Callable[..., None]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        *progress_data: Any,
    ) -> InstalledRef: ...
    def update_appstream_full_sync(
        self,
        remote_name: str,
        arch: Optional[str] = None,
        progress: Optional[Callable[..., None]] = None,
        out_changed: Optional[bool] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        *progress_data: Any,
    ) -> bool: ...
    def update_appstream_sync(
        self,
        remote_name: str,
        arch: Optional[str] = None,
        out_changed: Optional[bool] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def update_full(
        self,
        flags: UpdateFlags,
        kind: RefKind,
        name: str,
        arch: Optional[str] = None,
        branch: Optional[str] = None,
        subpaths: Optional[Sequence[str]] = None,
        progress: Optional[Callable[..., None]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        *progress_data: Any,
    ) -> InstalledRef: ...
    def update_remote_sync(
        self, name: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...

class InstallationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InstallationClass()
    """

    parent_class: GObject.ObjectClass = ...

class InstalledRef(Ref):
    """
    :Constructors:

    ::

        InstalledRef(**properties)

    Object FlatpakInstalledRef

    Properties from FlatpakInstalledRef:
      is-current -> gboolean: Is Current
        Whether the application is current
      origin -> gchararray: Origin
        The origin
      latest-commit -> gchararray: Latest Commit
        The latest commit
      deploy-dir -> gchararray: Deploy Dir
        Where the application is installed
      installed-size -> guint64: Installed Size
        The installed size of the application
      subpaths -> GStrv: Subpaths
        The subpaths for a partially installed ref
      end-of-life -> gchararray: End of life
        The reason for the ref to be end of life
      end-of-life-rebase -> gchararray: End of life rebase
        The new ref for the end-of-lifed ref
      appdata-name -> gchararray: Appdata Name
        The localized name field from the appdata
      appdata-summary -> gchararray: Appdata Summary
        The localized summary field from the appdata
      appdata-version -> gchararray: Appdata Version
        The default version field from the appdata
      appdata-license -> gchararray: Appdata License
        The license from the appdata
      appdata-content-rating-type -> gchararray: Appdata Content Rating Type
        The type of the content rating data from the appdata
      appdata-content-rating -> GHashTable: Appdata Content Rating
        The content rating data from the appdata

    Properties from FlatpakRef:
      name -> gchararray: Name
        The name of the application or runtime
      arch -> gchararray: Architecture
        The architecture of the application or runtime
      branch -> gchararray: Branch
        The branch of the application or runtime
      commit -> gchararray: Commit
        The commit
      kind -> FlatpakRefKind: Kind
        The kind of artifact
      collection-id -> gchararray: Collection ID
        The collection ID

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        appdata_content_rating: Optional[dict[None, None]]
        appdata_content_rating_type: Optional[str]
        appdata_license: str
        appdata_name: str
        appdata_summary: str
        appdata_version: str
        deploy_dir: str
        end_of_life: str
        end_of_life_rebase: str
        installed_size: int
        is_current: bool
        latest_commit: Optional[str]
        origin: str
        subpaths: list[str]
        arch: str
        branch: str
        collection_id: str
        commit: str
        kind: RefKind
        name: str
    props: Props = ...
    parent: Ref = ...
    def __init__(
        self,
        appdata_content_rating: dict[None, None] = ...,
        appdata_content_rating_type: str = ...,
        appdata_license: str = ...,
        appdata_name: str = ...,
        appdata_summary: str = ...,
        appdata_version: str = ...,
        deploy_dir: str = ...,
        end_of_life: str = ...,
        end_of_life_rebase: str = ...,
        installed_size: int = ...,
        is_current: bool = ...,
        latest_commit: str = ...,
        origin: str = ...,
        subpaths: Sequence[str] = ...,
        arch: str = ...,
        branch: str = ...,
        collection_id: str = ...,
        commit: str = ...,
        kind: RefKind = ...,
        name: str = ...,
    ): ...
    def get_appdata_content_rating(self) -> Optional[dict[str, str]]: ...
    def get_appdata_content_rating_type(self) -> Optional[str]: ...
    def get_appdata_license(self) -> str: ...
    def get_appdata_name(self) -> str: ...
    def get_appdata_summary(self) -> str: ...
    def get_appdata_version(self) -> str: ...
    def get_deploy_dir(self) -> str: ...
    def get_eol(self) -> str: ...
    def get_eol_rebase(self) -> str: ...
    def get_installed_size(self) -> int: ...
    def get_is_current(self) -> bool: ...
    def get_latest_commit(self) -> Optional[str]: ...
    def get_origin(self) -> str: ...
    def get_subpaths(self) -> list[str]: ...
    def load_appdata(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> GLib.Bytes: ...
    def load_metadata(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> GLib.Bytes: ...

class InstalledRefClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InstalledRefClass()
    """

    parent_class: RefClass = ...

class Instance(GObject.Object):
    """
    :Constructors:

    ::

        Instance(**properties)

    Object FlatpakInstance

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    @staticmethod
    def get_all() -> list[Instance]: ...
    def get_app(self) -> Optional[str]: ...
    def get_arch(self) -> str: ...
    def get_branch(self) -> str: ...
    def get_child_pid(self) -> int: ...
    def get_commit(self) -> str: ...
    def get_id(self) -> str: ...
    def get_info(self) -> GLib.KeyFile: ...
    def get_pid(self) -> int: ...
    def get_runtime(self) -> str: ...
    def get_runtime_commit(self) -> str: ...
    def is_running(self) -> bool: ...

class InstanceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InstanceClass()
    """

    parent_class: GObject.ObjectClass = ...

class Ref(GObject.Object):
    """
    :Constructors:

    ::

        Ref(**properties)

    Object FlatpakRef

    Properties from FlatpakRef:
      name -> gchararray: Name
        The name of the application or runtime
      arch -> gchararray: Architecture
        The architecture of the application or runtime
      branch -> gchararray: Branch
        The branch of the application or runtime
      commit -> gchararray: Commit
        The commit
      kind -> FlatpakRefKind: Kind
        The kind of artifact
      collection-id -> gchararray: Collection ID
        The collection ID

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        arch: str
        branch: str
        collection_id: str
        commit: str
        kind: RefKind
        name: str
    props: Props = ...
    parent: GObject.Object = ...
    def __init__(
        self,
        arch: str = ...,
        branch: str = ...,
        collection_id: str = ...,
        commit: str = ...,
        kind: RefKind = ...,
        name: str = ...,
    ): ...
    def format_ref(self) -> str: ...
    def format_ref_cached(self) -> str: ...
    def get_arch(self) -> str: ...
    def get_branch(self) -> str: ...
    def get_collection_id(self) -> str: ...
    def get_commit(self) -> str: ...
    def get_kind(self) -> RefKind: ...
    def get_name(self) -> str: ...
    @staticmethod
    def parse(ref: str) -> Ref: ...

class RefClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RefClass()
    """

    parent_class: GObject.ObjectClass = ...

class RelatedRef(Ref):
    """
    :Constructors:

    ::

        RelatedRef(**properties)

    Object FlatpakRelatedRef

    Properties from FlatpakRelatedRef:
      subpaths -> GStrv: Subpaths
        The subpaths for a partially installed ref
      should-download -> gboolean: Should download
        Whether to auto-download the ref with the main ref
      should-delete -> gboolean: Should delete
        Whether to auto-delete the ref with the main ref
      should-autoprune -> gboolean: Should autoprune
        Whether to delete when pruning unused refs

    Properties from FlatpakRef:
      name -> gchararray: Name
        The name of the application or runtime
      arch -> gchararray: Architecture
        The architecture of the application or runtime
      branch -> gchararray: Branch
        The branch of the application or runtime
      commit -> gchararray: Commit
        The commit
      kind -> FlatpakRefKind: Kind
        The kind of artifact
      collection-id -> gchararray: Collection ID
        The collection ID

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        should_autoprune: bool
        should_delete: bool
        should_download: bool
        subpaths: list[str]
        arch: str
        branch: str
        collection_id: str
        commit: str
        kind: RefKind
        name: str
    props: Props = ...
    parent: Ref = ...
    def __init__(
        self,
        should_autoprune: bool = ...,
        should_delete: bool = ...,
        should_download: bool = ...,
        subpaths: Sequence[str] = ...,
        arch: str = ...,
        branch: str = ...,
        collection_id: str = ...,
        commit: str = ...,
        kind: RefKind = ...,
        name: str = ...,
    ): ...
    def get_subpaths(self) -> list[str]: ...
    def should_autoprune(self) -> bool: ...
    def should_delete(self) -> bool: ...
    def should_download(self) -> bool: ...

class RelatedRefClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RelatedRefClass()
    """

    parent_class: RefClass = ...

class Remote(GObject.Object):
    """
    :Constructors:

    ::

        Remote(**properties)
        new(name:str) -> Flatpak.Remote
        new_from_file(name:str, data:GLib.Bytes) -> Flatpak.Remote

    Object FlatpakRemote

    Properties from FlatpakRemote:
      name -> gchararray: Name
        The name of the remote
      type -> FlatpakRemoteType: Type
        The type of the remote

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        name: str
        type: RemoteType
    props: Props = ...
    parent: GObject.Object = ...
    def __init__(self, name: str = ..., type: RemoteType = ...): ...
    def get_appstream_dir(self, arch: Optional[str] = None) -> Gio.File: ...
    def get_appstream_timestamp(self, arch: Optional[str] = None) -> Gio.File: ...
    def get_collection_id(self) -> Optional[str]: ...
    def get_comment(self) -> str: ...
    def get_default_branch(self) -> str: ...
    def get_description(self) -> str: ...
    def get_disabled(self) -> bool: ...
    def get_filter(self) -> str: ...
    def get_gpg_verify(self) -> bool: ...
    def get_homepage(self) -> str: ...
    def get_icon(self) -> str: ...
    def get_main_ref(self) -> str: ...
    def get_name(self) -> str: ...
    def get_nodeps(self) -> bool: ...
    def get_noenumerate(self) -> bool: ...
    def get_prio(self) -> int: ...
    def get_remote_type(self) -> RemoteType: ...
    def get_title(self) -> str: ...
    def get_url(self) -> str: ...
    @classmethod
    def new(cls, name: str) -> Remote: ...
    @classmethod
    def new_from_file(cls, name: str, data: GLib.Bytes) -> Remote: ...
    def set_collection_id(self, collection_id: Optional[str] = None) -> None: ...
    def set_comment(self, comment: str) -> None: ...
    def set_default_branch(self, default_branch: str) -> None: ...
    def set_description(self, description: str) -> None: ...
    def set_disabled(self, disabled: bool) -> None: ...
    def set_filter(self, filter_path: str) -> None: ...
    def set_gpg_key(self, gpg_key: GLib.Bytes) -> None: ...
    def set_gpg_verify(self, gpg_verify: bool) -> None: ...
    def set_homepage(self, homepage: str) -> None: ...
    def set_icon(self, icon: str) -> None: ...
    def set_main_ref(self, main_ref: str) -> None: ...
    def set_nodeps(self, nodeps: bool) -> None: ...
    def set_noenumerate(self, noenumerate: bool) -> None: ...
    def set_prio(self, prio: int) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_url(self, url: str) -> None: ...

class RemoteClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RemoteClass()
    """

    parent_class: GObject.ObjectClass = ...

class RemoteRef(Ref):
    """
    :Constructors:

    ::

        RemoteRef(**properties)

    Object FlatpakRemoteRef

    Properties from FlatpakRemoteRef:
      remote-name -> gchararray: Remote Name
        The name of the remote
      installed-size -> guint64: Installed Size
        The installed size of the application
      download-size -> guint64: Download Size
        The download size of the application
      metadata -> GBytes: Metadata
        The metadata info for the application
      end-of-life -> gchararray: End of life
        The reason for the ref to be end of life
      end-of-life-rebase -> gchararray: End of life rebase
        The new ref for the end of lifeed ref

    Properties from FlatpakRef:
      name -> gchararray: Name
        The name of the application or runtime
      arch -> gchararray: Architecture
        The architecture of the application or runtime
      branch -> gchararray: Branch
        The branch of the application or runtime
      commit -> gchararray: Commit
        The commit
      kind -> FlatpakRefKind: Kind
        The kind of artifact
      collection-id -> gchararray: Collection ID
        The collection ID

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        download_size: int
        end_of_life: str
        end_of_life_rebase: str
        installed_size: int
        metadata: Optional[GLib.Bytes]
        remote_name: str
        arch: str
        branch: str
        collection_id: str
        commit: str
        kind: RefKind
        name: str
    props: Props = ...
    parent: Ref = ...
    def __init__(
        self,
        download_size: int = ...,
        end_of_life: str = ...,
        end_of_life_rebase: str = ...,
        installed_size: int = ...,
        metadata: GLib.Bytes = ...,
        remote_name: str = ...,
        arch: str = ...,
        branch: str = ...,
        collection_id: str = ...,
        commit: str = ...,
        kind: RefKind = ...,
        name: str = ...,
    ): ...
    def get_download_size(self) -> int: ...
    def get_eol(self) -> str: ...
    def get_eol_rebase(self) -> str: ...
    def get_installed_size(self) -> int: ...
    def get_metadata(self) -> Optional[GLib.Bytes]: ...
    def get_remote_name(self) -> str: ...

class RemoteRefClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RemoteRefClass()
    """

    parent_class: RefClass = ...

class Transaction(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        Transaction(**properties)
        new_for_installation(installation:Flatpak.Installation, cancellable:Gio.Cancellable=None) -> Flatpak.Transaction

    Object FlatpakTransaction

    Signals from FlatpakTransaction:
      new-operation (FlatpakTransactionOperation, FlatpakTransactionProgress)
      operation-error (FlatpakTransactionOperation, GError, gint) -> gboolean
      operation-done (FlatpakTransactionOperation, gchararray, gint)
      choose-remote-for-ref (gchararray, gchararray, GStrv) -> gint
      end-of-lifed (gchararray, gchararray, gchararray)
      end-of-lifed-with-rebase (gchararray, gchararray, gchararray, gchararray, GStrv) -> gboolean
      ready () -> gboolean
      ready-pre-auth () -> gboolean
      add-new-remote (gint, gchararray, gchararray, gchararray) -> gboolean
      install-authenticator (gchararray, gchararray)
      webflow-start (gchararray, gchararray, GVariant, gint) -> gboolean
      webflow-done (GVariant, gint)
      basic-auth-start (gchararray, gchararray, GVariant, gint) -> gboolean

    Properties from FlatpakTransaction:
      installation -> FlatpakInstallation: Installation
        The installation instance
      no-interaction -> gboolean: No Interaction
        The installation instance

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        installation: Installation
        no_interaction: bool
    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self, installation: Installation = ..., no_interaction: bool = ...
    ): ...
    def abort_webflow(self, id: int) -> None: ...
    def add_default_dependency_sources(self) -> None: ...
    def add_dependency_source(self, installation: Installation) -> None: ...
    def add_install(
        self, remote: str, ref: str, subpaths: Optional[Sequence[str]] = None
    ) -> bool: ...
    def add_install_bundle(
        self, file: Gio.File, gpg_data: Optional[GLib.Bytes] = None
    ) -> bool: ...
    def add_install_flatpakref(self, flatpakref_data: GLib.Bytes) -> bool: ...
    def add_rebase(
        self,
        remote: str,
        ref: str,
        subpaths: Optional[str] = None,
        previous_ids: Optional[Sequence[str]] = None,
    ) -> bool: ...
    def add_sideload_repo(self, path: str) -> None: ...
    def add_uninstall(self, ref: str) -> bool: ...
    def add_update(
        self,
        ref: str,
        subpaths: Optional[Sequence[str]] = None,
        commit: Optional[str] = None,
    ) -> bool: ...
    def complete_basic_auth(
        self, id: int, user: str, password: str, options: GLib.Variant
    ) -> None: ...
    def do_add_new_remote(
        self, reason: TransactionRemoteReason, from_id: str, remote_name: str, url: str
    ) -> bool: ...
    def do_basic_auth_start(
        self, remote: str, realm: str, options: GLib.Variant, id: int
    ) -> bool: ...
    def do_choose_remote_for_ref(
        self, for_ref: str, runtime_ref: str, remotes: str
    ) -> int: ...
    def do_end_of_lifed(self, ref: str, reason: str, rebase: str) -> None: ...
    def do_end_of_lifed_with_rebase(
        self, remote: str, ref: str, reason: str, rebased_to_ref: str, previous_ids: str
    ) -> bool: ...
    def do_install_authenticator(self, remote: str, authenticator_ref: str) -> None: ...
    def do_new_operation(
        self, operation: TransactionOperation, progress: TransactionProgress
    ) -> None: ...
    def do_operation_done(
        self, operation: TransactionOperation, commit: str, details: TransactionResult
    ) -> None: ...
    def do_operation_error(
        self,
        operation: TransactionOperation,
        error: GLib.Error,
        detail: TransactionErrorDetails,
    ) -> bool: ...
    def do_ready(self) -> bool: ...
    def do_ready_pre_auth(self) -> bool: ...
    def do_run(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def do_webflow_done(self, options: GLib.Variant, id: int) -> None: ...
    def do_webflow_start(
        self, remote: str, url: str, options: GLib.Variant, id: int
    ) -> bool: ...
    def get_auto_install_debug(self) -> bool: ...
    def get_auto_install_sdk(self) -> bool: ...
    def get_current_operation(self) -> TransactionOperation: ...
    def get_include_unused_uninstall_ops(self) -> bool: ...
    def get_installation(self) -> Installation: ...
    def get_no_deploy(self) -> bool: ...
    def get_no_interaction(self) -> bool: ...
    def get_no_pull(self) -> bool: ...
    def get_operation_for_ref(
        self, remote: Optional[str], ref: str
    ) -> TransactionOperation: ...
    def get_operations(self) -> list[TransactionOperation]: ...
    def get_parent_window(self) -> str: ...
    def is_empty(self) -> bool: ...
    @classmethod
    def new_for_installation(
        cls, installation: Installation, cancellable: Optional[Gio.Cancellable] = None
    ) -> Transaction: ...
    def run(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def set_auto_install_debug(self, auto_install_debug: bool) -> None: ...
    def set_auto_install_sdk(self, auto_install_sdk: bool) -> None: ...
    def set_default_arch(self, arch: str) -> None: ...
    def set_disable_auto_pin(self, disable_pin: bool) -> None: ...
    def set_disable_dependencies(self, disable_dependencies: bool) -> None: ...
    def set_disable_prune(self, disable_prune: bool) -> None: ...
    def set_disable_related(self, disable_related: bool) -> None: ...
    def set_disable_static_deltas(self, disable_static_deltas: bool) -> None: ...
    def set_force_uninstall(self, force_uninstall: bool) -> None: ...
    def set_include_unused_uninstall_ops(
        self, include_unused_uninstall_ops: bool
    ) -> None: ...
    def set_no_deploy(self, no_deploy: bool) -> None: ...
    def set_no_interaction(self, no_interaction: bool) -> None: ...
    def set_no_pull(self, no_pull: bool) -> None: ...
    def set_parent_window(self, parent_window: str) -> None: ...
    def set_reinstall(self, reinstall: bool) -> None: ...

class TransactionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TransactionClass()
    """

    parent_class: GObject.ObjectClass = ...
    new_operation: Callable[
        [Transaction, TransactionOperation, TransactionProgress], None
    ] = ...
    operation_done: Callable[
        [Transaction, TransactionOperation, str, TransactionResult], None
    ] = ...
    operation_error: Callable[
        [Transaction, TransactionOperation, GLib.Error, TransactionErrorDetails], bool
    ] = ...
    choose_remote_for_ref: Callable[[Transaction, str, str, str], int] = ...
    end_of_lifed: Callable[[Transaction, str, str, str], None] = ...
    ready: Callable[[Transaction], bool] = ...
    add_new_remote: Callable[
        [Transaction, TransactionRemoteReason, str, str, str], bool
    ] = ...
    run: Callable[[Transaction, Optional[Gio.Cancellable]], bool] = ...
    end_of_lifed_with_rebase: Callable[
        [Transaction, str, str, str, str, str], bool
    ] = ...
    webflow_start: Callable[[Transaction, str, str, GLib.Variant, int], bool] = ...
    webflow_done: Callable[[Transaction, GLib.Variant, int], None] = ...
    basic_auth_start: Callable[[Transaction, str, str, GLib.Variant, int], bool] = ...
    install_authenticator: Callable[[Transaction, str, str], None] = ...
    ready_pre_auth: Callable[[Transaction], bool] = ...
    padding: list[None] = ...

class TransactionOperation(GObject.Object):
    """
    :Constructors:

    ::

        TransactionOperation(**properties)

    Object FlatpakTransactionOperation

    Signals from GObject:
      notify (GParam)
    """

    def get_bundle_path(self) -> Gio.File: ...
    def get_commit(self) -> str: ...
    def get_download_size(self) -> int: ...
    def get_installed_size(self) -> int: ...
    def get_is_skipped(self) -> bool: ...
    def get_metadata(self) -> GLib.KeyFile: ...
    def get_old_metadata(self) -> GLib.KeyFile: ...
    def get_operation_type(self) -> TransactionOperationType: ...
    def get_ref(self) -> str: ...
    def get_related_to_ops(self) -> Optional[list[TransactionOperation]]: ...
    def get_remote(self) -> str: ...
    def get_requires_authentication(self) -> bool: ...
    def get_subpaths(self) -> list[str]: ...

class TransactionOperationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TransactionOperationClass()
    """

    parent_class: GObject.ObjectClass = ...

class TransactionProgress(GObject.Object):
    """
    :Constructors:

    ::

        TransactionProgress(**properties)

    Object FlatpakTransactionProgress

    Signals from FlatpakTransactionProgress:
      changed ()

    Signals from GObject:
      notify (GParam)
    """

    def get_bytes_transferred(self) -> int: ...
    def get_is_estimating(self) -> bool: ...
    def get_progress(self) -> int: ...
    def get_start_time(self) -> int: ...
    def get_status(self) -> str: ...
    def set_update_frequency(self, update_interval: int) -> None: ...

class TransactionProgressClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TransactionProgressClass()
    """

    parent_class: GObject.ObjectClass = ...

class InstallFlags(GObject.GFlags):
    NONE = 0
    NO_DEPLOY = 4
    NO_PULL = 8
    NO_STATIC_DELTAS = 1
    NO_TRIGGERS = 16

class LaunchFlags(GObject.GFlags):
    DO_NOT_REAP = 1
    NONE = 0

class QueryFlags(GObject.GFlags):
    ALL_ARCHES = 4
    NONE = 0
    ONLY_CACHED = 1
    ONLY_SIDELOADED = 2

class TransactionErrorDetails(GObject.GFlags):
    FATAL = 1

class TransactionResult(GObject.GFlags):
    CHANGE = 1

class UninstallFlags(GObject.GFlags):
    NONE = 0
    NO_PRUNE = 1
    NO_TRIGGERS = 2

class UpdateFlags(GObject.GFlags):
    NONE = 0
    NO_DEPLOY = 1
    NO_PRUNE = 8
    NO_PULL = 2
    NO_STATIC_DELTAS = 4
    NO_TRIGGERS = 16

class Error(GObject.GEnum):
    ABORTED = 4
    ALREADY_INSTALLED = 0
    AUTHENTICATION_FAILED = 23
    DIFFERENT_REMOTE = 3
    DOWNGRADE = 9
    EXPORT_FAILED = 14
    INVALID_DATA = 11
    INVALID_NAME = 17
    INVALID_REF = 10
    NEED_NEW_FLATPAK = 6
    NOT_AUTHORIZED = 24
    NOT_CACHED = 20
    NOT_INSTALLED = 1
    ONLY_PULLED = 2
    OUT_OF_SPACE = 18
    PERMISSION_DENIED = 22
    REF_NOT_FOUND = 21
    REMOTE_NOT_FOUND = 7
    REMOTE_USED = 15
    RUNTIME_NOT_FOUND = 8
    RUNTIME_USED = 16
    SETUP_FAILED = 13
    SKIPPED = 5
    UNTRUSTED = 12
    WRONG_USER = 19
    @staticmethod
    def quark() -> int: ...

class PortalError(GObject.GEnum):
    CANCELLED = 5
    EXISTS = 3
    FAILED = 0
    INVALID_ARGUMENT = 1
    NOT_ALLOWED = 4
    NOT_FOUND = 2
    WINDOW_DESTROYED = 6
    @staticmethod
    def quark() -> int: ...

class RefKind(GObject.GEnum):
    APP = 0
    RUNTIME = 1

class RemoteType(GObject.GEnum):
    LAN = 2
    STATIC = 0
    USB = 1

class StorageType(GObject.GEnum):
    DEFAULT = 0
    HARD_DISK = 1
    MMC = 3
    NETWORK = 4
    SDCARD = 2

class TransactionOperationType(GObject.GEnum):
    INSTALL = 0
    INSTALL_BUNDLE = 2
    LAST_TYPE = 4
    UNINSTALL = 3
    UPDATE = 1
    @staticmethod
    def to_string(kind: TransactionOperationType) -> str: ...

class TransactionRemoteReason(GObject.GEnum):
    GENERIC_REPO = 0
    RUNTIME_DEPS = 1
