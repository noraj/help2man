"""Configure the Sphinx documentation builder.

https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
import os
from datetime import datetime

from help2man import __version__ as version  # type: ignore

try:
    import tomllib  # type: ignore
except ImportError:
    import tomli as tomllib

scriptdir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "scripts")
os.environ["PATH"] = scriptdir + os.path.pathsep + os.getenv("PATH", "")

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# -- Project information -----------------------------------------------------
language = "en"
copyright = "2022-" + str(datetime.now().year)

PROJECT_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "pyproject.toml"
)

with open(PROJECT_FILE, "rb") as f:
    data = tomllib.load(f)["project"]
    author = data["authors"][0]["name"]
    project = data["name"]

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinxcontrib.autofile",
    "sphinxcontrib.eval",
    "sphinxcontrib.requirements_txt",
]

myst_heading_anchors = 3
myst_title_to_header = True
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]
