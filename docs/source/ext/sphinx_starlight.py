# glue code for exporting MDX files ready to be used with Starlight
# definitely overriding the builder would be a better idea but this is just a PoC

import json
from typing import cast
from loguru import logger
from docutils import nodes
from docutils.utils import unescape
from sphinx.application import Sphinx
from sphinx.addnodes import pending_xref
from docutils.parsers.rst import Directive
from sphinx.domains.python import PythonDomain
from sphinx_markdown_builder.builder import MarkdownBuilder
from sphinx_markdown_builder.translator import MarkdownTranslator
from sphinx.addnodes import (
    desc_signature,
    desc_annotation,
    desc_name,
    desc_parameterlist,
    desc_returns,
)


OUTPUT_TARGET = "starlight"
OUTPUT_FORMAT = "markdown"
STARLIGHT_ASIDE_TYPES = {
    nodes.note: "note",
    nodes.warning: "warning",
    nodes.tip: "tip",
    nodes.hint: "hint",
    nodes.important: "important",
    nodes.danger: "danger",
    nodes.error: "error",
    nodes.admonition: "admonition",
}


class FixedText(nodes.Text):
    def astext(self):
        return str(unescape(self, respect_whitespace=True))


class MDXTranslator(MarkdownTranslator):
    def visit_Text(self, node):
        return self.add(node.astext())


class MDXBuilder(MarkdownBuilder):
    out_suffix = ".mdx"
    default_translator_class = MDXTranslator


class PatchedPythonDomain(PythonDomain):
    # an override for removing cross-refs
    def resolve_xref(
        self,
        env,
        source_doc: str,
        builder,
        type_prefix: str,
        target: str,
        node: pending_xref,
        content: nodes.Element,
    ):
        if OUTPUT_TARGET == "starlight":
            # useless link and it will not work so we remove it
            # TODO: might do something useful about this (e.g. transform for it to work)
            return None
        return super().resolve_xref(
            env, source_doc, builder, type_prefix, target, node, content
        )


class MetaDirective(Directive):
    name = "meta"
    has_content = True

    def run(self):
        docname: str = self.state.document.settings.env.docname
        metadata: dict[str, str] = self.state.document.settings.env.metadata.setdefault(
            docname, {}
        )
        for line in self.content:
            if ":" not in line:
                continue
            key, value = line.lstrip(":").split(":", 1)
            metadata[key.strip()] = value.strip()
        return []  # do not edit the document but leave it for the next handler to edit it


def handle_admonitions(app: Sphinx, doctree: nodes.document, docname: str):
    for node in doctree.traverse(
        lambda n: isinstance(n, tuple(STARLIGHT_ASIDE_TYPES.keys()))
    ):
        logger.debug(
            "[Ext][FabricDoc] preprocessing sphinx admonition into starlight's <aside>"
        )

        admonition_type: str = STARLIGHT_ASIDE_TYPES.get(type(node), "note")  # type: ignore
        text_content = "".join(n.astext() for n in node.traverse(nodes.Text))
        aside_text = (
            f":::{admonition_type}\n{text_content}\n:::"
            or f"<Aside type='{admonition_type}'>{text_content}</Aside>"
        )
        raw_node = nodes.raw(aside_text, aside_text, format=OUTPUT_FORMAT)
        cast(nodes.Element, node).replace_self(raw_node)


def bake_signature_component(
    doctree,
    signature_type: str | None,
    signature_name: str,
    args: str | None,
    return_type: str | None,
):
    stringify = lambda x: f"{{ {json.dumps(x)} }}"
    attributes = [
        f"typeName={stringify(signature_name)}",
        f"typePrefix={stringify(signature_type) if signature_type else "def"}",
    ]
    if args:
        attributes.append(f"typeArgList={stringify(args)}")
    if return_type and signature_type != "class":
        attributes.append(f"returnType={stringify(return_type)}")
    attributes_str = " ".join(attributes)
    # we wrap the type's name so that heading render properly
    tag_content = f"<TypeSignature {attributes_str}> {signature_name} </TypeSignature>"
    return tag_content


def handle_signature_headers(app: Sphinx, doctree: nodes.document, docname: str):
    for node in doctree.traverse(desc_signature):
        annotations = node.traverse(desc_annotation)
        type_prefix_node = annotations[0] if len(annotations) >= 1 else FixedText("def")
        object_name_node = node.next_node(desc_name)
        signature_node = node.next_node(desc_parameterlist)
        return_type_node = node.parent.next_node(desc_returns) or (
            annotations[-1] if len(annotations) >= 2 else None
        )

        object_name = object_name_node.astext().strip()
        type_prefix = type_prefix_node.astext().strip() or None
        args = signature_node.astext().strip() if signature_node else None
        return_type = (
            return_type_node.astext().strip().lstrip("->").lstrip(":").strip()
            if return_type_node
            else None
        )

        # FIXME: this no good
        if type_prefix and type_prefix.startswith("="):
            tag_content = bake_signature_component(
                doctree, "member", object_name, None, type_prefix.lstrip("=").strip()
            )
        elif type_prefix and type_prefix.startswith(":"):
            tag_content = bake_signature_component(
                doctree, "attribute", object_name, None, type_prefix.lstrip(":").strip()
            )
        else:
            tag_content = bake_signature_component(
                doctree, type_prefix, object_name, args, return_type
            )

        raw_node = nodes.raw(tag_content, tag_content)

        node.clear()

        node.append(raw_node)


def bake_page_header(page_title: str = "Unknown", **kwargs):
    kwargs.setdefault("title", page_title) if not kwargs.get("title", None) else None

    header = "---"
    for name, value in kwargs.items():
        header += "\n" + f"{name}: {value}" + "\n"
    header += "---\n"

    header += """

import { Aside } from "@astrojs/starlight/components";
import TypeSignature from "@components/TypeSignature.astro";


"""

    return header


def handle_page_metadata(app: Sphinx, doctree: nodes.document, docname: str):
    metadata = app.env.metadata.get(docname, {})
    page_title = docname.split("/")[-1].replace("_", " ").title()

    header = bake_page_header(page_title, **metadata)

    return doctree.children.insert(0, nodes.raw(header, header))


def setup(app: Sphinx):
    app.config.markdown_uri_doc_suffix = ".mdx"

    app.add_builder(MDXBuilder, override=True)
    app.add_domain(PatchedPythonDomain, override=True)
    app.add_directive("meta", MetaDirective, override=True)

    app.connect("doctree-resolved", handle_admonitions)
    app.connect("doctree-resolved", handle_page_metadata)
    app.connect("doctree-resolved", handle_signature_headers)
