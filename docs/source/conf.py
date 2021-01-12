# -*- coding: utf-8 -*-
import os
import sys
from datetime import date
from sphinx.util import logging
import recommonmark
from recommonmark.transform import AutoStructify	

logger = logging.getLogger(__name__)
sys.path.insert(0, os.path.abspath('.'))
# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.


extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.extlinks',
#   'sphinx.ext.autosectionlabel',
    'sphinx_sitemap',
    'sphinx_scylladb_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_multiversion',
    'recommonmark'
    
]


# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# Add Markdown support
# https://www.sphinx-doc.org/en/master/usage/markdown.html
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Scylla'
copyright = str(date.today().year) + ', ScyllaDB. All rights reserved.'
author = u'Scylla Project Contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.3'
# The full version, including alpha/beta/rc tags.
release = u'1.3.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path

exclude_patterns = ['_build', 'cloud.rst', 'core_graph.rst', 'geo_types.rst', 'graph.rst', 'graph_fluent.rst']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Setup Sphinx
def setup(sphinx):
    sphinx.add_config_value('recommonmark_config', {
        'enable_eval_rst': True,
        'enable_auto_toc_tree': False,
    }, True)
    sphinx.add_transform(AutoStructify)

# substitutions and variables - these are global to the entire Monitoring docs project.
# Adds version variables for monitoring and manager versions when used in inline text
# version should be set to the latest monitoring version
rst_prolog = """
.. |version| replace:: 3.5.3
"""

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_scylladb_theme'

html_style = ''

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'header_links': [
    ('Scylla Monitor', 'https://scylladb.github.io/scylla-monitoring/'),
    ('Scylla Cloud', 'https://docs.scylladb.com/scylla-cloud/'),
    ('Scylla University', 'https://university.scylladb.com/'),
    ('ScyllaDB Home', 'https://www.scylladb.com/')],
    'github_issues_repository': 'scylladb/scylla-monitoring',
    'show_sidebar_index': True,
}

extlinks = {
    'manager': ('/operating-scylla/manager/%s/',''),
    'manager_lst': ('/operating-scylla/manager/2.0/%s/',''),
    'monitor': ('/operating-scylla/monitoring/%s/',''),
    'monitor_lst': ('/operating-scylla/monitoring/3.3/%s/','')
}

sitemap_url_scheme = "{link}"

html_extra_path = ['robots.txt']

# Add ExpertRec Search
html_js_files = ['expertrec.js']

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
html_last_updated_fmt = '%d %B %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
html_sidebars = {'**': ['side-nav.html']}

# If false, no index is generated.
#
html_use_index = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'ScyllaMonitorDocumentationdoc'

# URL which points to the root of the HTML documentation. 
html_baseurl = 'https://scylladb.github.io/scylla-monitoring/'

# Dictionary of values to pass into the template engine’s context for all pages
html_context = {'html_baseurl': html_baseurl}

# -- Options for not found extension -------------------------------------------

# Template used to render the 404.html generated by this extension.
notfound_template =  '404.html'

# Prefix added to all the URLs generated in the 404 page.
notfound_urls_prefix = ''

# -- Options for redirect extension ---------------------------------------

# Read a YAML dictionary of redirections and generate an HTML file for each
redirects_file = "_utils/redirections.yaml"

# -- Options for multiversion --------------------------------------------

# Whitelist pattern for tags (set to None to ignore all tags)
# smv_tag_whitelist = r'^.*$'
smv_tag_whitelist = r'\b(scylla-monitoring-3\.4\.2|scylla-monitoring-3\.5|scylla-monitoring-3\.5\.\d+)\b(?!\S)'
# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = "None"
# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = r"^origin$"
# Pattern for released versions
smv_released_pattern = r'^tags/.*$'
# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
     #
     # 'papersize': 'letterpaper',

     # The font size ('10pt', '11pt' or '12pt').
     #
     # 'pointsize': '10pt',

     # Additional stuff for the LaTeX preamble.
     #
     # 'preamble': '',

     # Latex figure (float) alignment
     #
     # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ScyllaDocumentation.tex', u'Scylla Documentation Documentation',
     u'Scylla Project Contributors', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'scylladocumentation', u'Scylla Documentation Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ScyllaMonitorDocumentation', u'Scylla Monitor Documentation',
     author, 'ScyllaMonitorDocumentation', 'Documentation for Scylla Monitor.',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

