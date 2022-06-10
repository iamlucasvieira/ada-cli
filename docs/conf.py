"""Sphinx configuration."""
project = "Ada CLI"
author = "Lucas Vieira dos Santos"
copyright = "2022, Lucas Vieira dos Santos"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
