import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('../src'))

project = 'Matt Muszynski Resume'
copyright = f'{datetime.now().year}, Matt Muszynski'
author = 'Matt Muszynski'

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx_simplepdf',  # The pure-Python CSS-based PDF builder
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

html_theme = 'sphinx_rtd_theme' 
html_static_path = ['_static']

# -- Options for SimplePDF ---------------------------------------------------

simplepdf_vars = {
    'primary': '#000000',
    'links': '#0000ee',
    # Adjust your page margins here!
    'page-margin-top': '0.5in',
    'page-margin-bottom': '0.5in',
    'page-margin-left': '0.5in',
    'page-margin-right': '0.5in',
}

# Tell it to use a custom CSS file to override Sphinx defaults
simplepdf_custom_css = '_static/resume_style.css'