# a sphinx extension for handling Fabric specific types
import sys
from loguru import logger
from docutils import nodes
from docutils.utils import unescape
from sphinx.application import Sphinx
from sphinx.util.inspect import signature
from sphinx.domains.python import PyAttribute
from sphinx.ext.autodoc import AttributeDocumenter


class FixedText(nodes.Text):
    def astext(self):
        return str(unescape(self, respect_whitespace=True))


class SignalDocumenter(AttributeDocumenter):
    priority = 11
    objtype = "signal"
    directivetype = "signal"

    @classmethod
    def can_document_member(
        cls, member: object, member_name: str, is_attr: bool, parent: object
    ):
        import fabric.core.service

        return isinstance(member, fabric.core.service.SignalWrapper)

    def add_directive_header(self, sig):
        super().add_directive_header(sig)

    def format_signature(self):
        logger.debug(
            f"[Ext][FabricDoc] formatting signal's signature with name {self.name}"
        )
        try:
            sig = signature(self.object.func)
            return str(sig)
        except Exception:
            return "<Error Documenting Signal (Report this!)>"

    def should_suppress_value_header(self) -> bool:
        return True  # no thanks

    def document_members(self, all_members: bool = False) -> None:
        return None


class SignalDirective(PyAttribute):
    allow_nesting = True

    def needs_arglist(self) -> bool:
        return True

    def get_signature_prefix(self, sig: str) -> list[FixedText]:
        logger.debug(f"[Ext][FabricDoc] adding signature prefix for the signal {sig}")
        return [FixedText("signal"), FixedText(" ")]

    def get_index_text(self, modname: str, name_cls: str) -> str:
        return "signal"


def initialize_fabric():
    if "fabric" in sys.modules:
        del sys.modules["fabric"]
    if "gi" in sys.modules:
        del sys.modules["gi"]

    # PyGObject adds unwanted docstrings for types with deprecated construtors for some reason
    # get rid of those so they won't appear in the output docs
    import gi.overrides

    old_init_wrapper = gi.overrides.deprecated_init

    def new_init_wrapper(*args, **kwargs):
        func = old_init_wrapper(*args, **kwargs)
        setattr(func, "__doc__", None)
        delattr(func, "__doc__")
        return func

    gi.overrides.deprecated_init = new_init_wrapper

    import fabric.core.service

    fabric.core.service.gi.overrides = new_init_wrapper

    # fix the displayment of some fabric types

    # fabric.core.service.Service = object
    fabric.core.service.Property = lambda *_, **__: property
    # fabric.core.service.Property.__doc__ = "    :meta private:"
    # fabric.core.service.Signal = lambda *_, **__: None
    # fabric.core.service.SignalWrapper.__repr__ = (
    #     lambda self: f"Signal{signature(self.func)}"  # type: ignore
    # )


def skip_internals(
    app: Sphinx,
    what: str,
    name: str,
    obj: object,
    skip: bool,
    options: dict[str, object],
):
    # TODO: use an annotation instead (or a decorator for hiding internals)
    if name.startswith(("on_", "do_")):
        logger.debug(f"[Ext][FabricDoc] skipping internal method with name {name}")
        return True  # "skip me"
    if getattr(obj, "__module__", None) == "builtins":
        return True
    return None  # "do whatever you see right"


def setup(app: Sphinx):
    initialize_fabric()

    app.add_autodocumenter(SignalDocumenter)
    app.add_directive_to_domain("py", "signal", SignalDirective)

    app.connect("autodoc-skip-member", skip_internals)
