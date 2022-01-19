# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

from os.path import abspath, join, dirname

sys.path.insert(0, abspath(join(dirname(__file__))))
# -- Project information -----------------------------------------------------

project = u'openIMIS'
subproject= u'User manual'
copyright = u'2020, openIMIS team'
author = u'openIMIS team'
html_logo = 'img/logo.png'
html_favicon = 'img/favicon.ico'
# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u''

# -- Numbering figures
numfig = True
numfig_format = {'figure': 'Img. %s', 'table': 'Tab. %s', 'code-block': 'Code %s'}
numfig_secnum_depth = (2)
# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions =['sphinx.ext.intersphinx']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [u'_build', u'ar_manual', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#html_context = {

#     }

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'openIMISdoc'


# -- Options for LaTeX output ------------------------------------------------


latex_logo = 'img/logo.png'

latex_engine = 'pdflatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',
    'release':"1.4.1",
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
    # 'fncychap': '\\usepackage[Lenny]{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
    ''',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'extraclassoptions': 'openany'
}
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'openIMIS.tex', u'openIMIS installation and user manual',
     author, 'sphinxmanual'),
]
#latex_documents = [
#    (master_doc, 'openIMIS.tex', u'openIMIS Documentation',
#     u'openIMIS team', 'manual'),
#]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'openimis', u'openIMIS Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'openIMIS', u'openIMIS Documentation',
     author, 'openIMIS', 'openIMIS is a health insurance management solution',
     'Miscellaneous'),
]

# Add custom CSS to resize the tables
def setup(app):
    app.add_css_file('css/theme_overrides.css')

#interlink mapping
# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# This is used for linking and such so we link to the thing we're building
rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
if rtd_version not in ['stable', 'latest']:
    rtd_version = 'stable'
intersphinx_mapping = {
  'user': ('http://openimis.readthedocs.io/en/%s/' % rtd_version, None),
  'install': ('http://openimis-install.readthedocs.io/en/%s/' % rtd_version, None),
}

## Local and internalization

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

## Gen menu
import gensidebar

gensidebar.generate_sidebar(globals(), "openIMIS")
