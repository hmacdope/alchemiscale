# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "alchemiscale"
copyright = '2022, "OpenFE and OpenFF developers"'
author = '"OpenFE and OpenFF developers"'

import sys
import os
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath("."))

os.environ['SPHINX'] = 'True'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autodoc_mock_imports = [
        "async_lru",
        "boto3",
        "click",
        "fastapi",
        "gufe",
        "httpx",
        "jose",
        "networkx",
        "numpy",
        "passlib",
        "py2neo",
        "pydantic",
        "starlette",
        "yaml",
        ]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# We are not using this currently
#html_static_path = ["_static"]
