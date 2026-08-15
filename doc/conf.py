# -*- coding: utf-8 -*-
#
# xlcalcnet documentation build configuration file
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default value; values that are commented out
# serve to show the default value.

import sys

from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter

class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\footnotesize"

PygmentsBridge.latex_formatter = CustomLatexFormatter

#def setup(app):
#    app.add_stylesheet('my_theme.css')

# If your extensions are in another directory, add it here.
sys.path.insert(0, '../..')

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
                'sphinx.ext.autodoc', 
                'sphinx.ext.intersphinx',
                'sphinx.ext.coverage',
                'sphinx.ext.viewcode',
                'sphinx.ext.mathjax', 
                'sphinx.ext.todo', 
                'sphinxcontrib.bibtex',
                'sphinx_copybutton',
             ]

[extensions]
todo_include_todos=True

#copybutton_exclude = '.linenos, .gp,  .go, '

copybutton_prompt_text = ">>> "

bibtex_bibliography_header = ".. rubric:: Footnotes"

bibtex_bibfiles = ['refs.bib']
#bibtex_bibfiles = ['../../refs.bib']


bibtex_reference_style = 'label'
#bibtex_reference_style = 'author_year'

#bibtex_default_style = 'alpha'
bibtex_default_style = 'plain'
#bibtex_default_style = 'unsrt'
#bibtex_default_style = 'unsrtalpha'

exclude_patterns = ["_build"]



# MathJax file, which is free to use.  See http://www.mathjax.org/docs/2.0/start.html
# mathjax_path = 'http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML-full'

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General substitutions.
project = 'XlCalcNet'
author = 'Dietrich Hadler'
copyright = '2026, Dietrich Hadler. '

# The default replacements for |version| and |release|, also used in various
# other places throughout the built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0.0'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. method::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# Options for HTML output
# -----------------------

# The "theme" that the HTML output should use.



html_theme = "sphinx_book_theme"

html_theme_options = {
    # "icon_links": [
    #    {
    #        "name": "GitHub",
    #        "url": "https://github.com/pydata/pydata-sphinx-theme",
    #        "icon": "fa-brands fa-github",
    #    },
    #    {
    #        "name": "PyPI",
    #        "url": "https://pypi.org/project/pydata-sphinx-theme",
    #        "icon": "fa-custom fa-pypi",
    #    },
    #],
     "logo": {
        "text": "XlCalcNet Documentation",
    },
    "show_nav_level": 2,
    "show_toc_level": 2,
    "navigation_depth": 2,
    "collapse_navigation" : True,
    "primary_sidebar_end": ["indices.html", "sidebar-ethical-ads.html"],
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#html_logo = "_static/KuenOrange.jpg"

html_css_files = ['css/custom.css',]

html_js_files = ["custom-icon.js"]



# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Content template for the index page.
#html_index = ''

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If true, the reST sources are included in the HTML build as _sources/<name>.
#html_copy_source = True

# Output file base name for HTML help builder.
htmlhelp_basename = 'XlCalcNet'





# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).

latex_documents = [(master_doc, 'xlcalcnet.tex', 'XlCalcNet Documentation',
                    r'Dietrich Hadler', 'manual')]

# Additional stuff for the LaTeX preamble.
#latex_preamble = r'\usepackage{amsfonts}'


#latex_preamble = r"""
#\usepackage{amsmath,amssymb}
#\setcounter{tocdepth}{2}
#"""


# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/KuenOrange.jpg"

#latex_engine = 'xelatex'

latex_toplevel_sectioning = 'part'

# latex_elements = {'extraclassoptions': 'openany'}



# latex_elements = {
#     'extraclassoptions': 'openany',
#     'sphinxsetup': 'hmargin={0.6in,0.6in}, vmargin={1.0in,1.0in}, marginpar=0.75in',
#     'preamble': r'''
#         \usepackage{amsmath,amsfonts,amssymb,amsthm}
#         \usepackage{setspace}
#         \usepackage{fontspec}
#         \setmonofont{Source Code Pro}
#         \tolerance=1
#         \emergencystretch=\maxdimen
#         \hyphenpenalty=10000
#         \hbadness=10000
#     '''
# }


latex_elements = {
    'extraclassoptions': 'openany',
    'sphinxsetup': 'hmargin={0.6in,0.6in}, vmargin={1.0in,1.0in}, marginpar=0.75in',
    'preamble': r'''
        \usepackage{amsmath,amsfonts,amssymb,amsthm}
        \usepackage{setspace}
        \usepackage{tocloft}
        \setlength{\cftsecnumwidth}{2.8em}        
        \cftsetindents{subsection}{4.3em}{4em}        
        \renewcommand{\sphinxtableofcontentshook}{}% else it will overwrite tocloft!
    '''
}



#\setmonofont{DejaVu Sans Mono}


# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True


latex_table_style = []


default_role = 'math'
pngmath_dvipng_args = ['-gamma 1.5', '-D 110']
