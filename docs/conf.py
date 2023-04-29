# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OreSat Software Intern Onboarding Guide'
copyright = f'{datetime.now().year}, Portland State Aerospace Society'
author = 'PSAS'
release = '1.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.mermaid',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc'
]

templates_path = []
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_domain_indices = True
#html_static_path = ['static']
#html_css_files = ['custom.css']


# -- Others Options ----------------------------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
# To add links to stand python type definitions.
intersphinx_mapping = {'python': ('https://docs.python.org/3/', None)}

def setup(app):
    app.add_js_file('zoom.js')
