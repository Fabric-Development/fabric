import os
import sys
from recommonmark.parser import CommonMarkParser


project = "fabric"
release = "0.0.2"
author = "Yousef EL-Darsh"
copyright = "2024, Yousef EL-Darsh"

sys.path.insert(0, os.path.abspath("./"))
sys.path.insert(0, os.path.abspath("../../fabric"))

extensions = [
    "sphinx_markdown_builder",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "recommonmark",
    "ext.fabric_types",
    "ext.sphinx_starlight",
    "sphinx_toolbox.more_autodoc.overloads",
]

smartquotes = False
exclude_patterns = []
master_doc = "fabric"
html_permalinks = False
html_show_sourcelink = False
html_theme = "sphinxawesome_theme"
html_permalinks_icon = "<span>#</span>"

source_parsers = {".md": CommonMarkParser}
source_suffix = [".rst", ".md"]
autodoc_member_order = "bysource"

# autodoc_typehints = "description"
# autodoc_class_signature = "separated"
autodoc_typehints_format = "short"
autodoc_preserve_defaults = True
add_module_names = False
default_role = None
autoclass_content = "both"
