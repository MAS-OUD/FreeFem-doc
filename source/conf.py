# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.abspath('sphinx-extensions'))

import requests
r = requests.get('https://api.github.com/repos/FreeFem/FreeFem-sources/releases/latest')
GitHubVersion = r.json()

# -- Project information -----------------------------------------------------

project = 'FreeFEM'
copyright = '2019, FreeFEM'
author = 'Frederic Hecht'

# The short X.Y version
version = '4.2.1' # GitHubVersion['tag_name']
# The full version, including alpha/beta/rc tags
release = '4.1.2' #GitHubVersion['tag_name']

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'sphinxcontrib.inlinesyntaxhighlight',
    'sphinx_sitemap',
    'subfig'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

html_extra_path = ['html']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
highlight_language = 'freefem'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'default'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_baseurl = 'https://doc.freefem.org/'

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
htmlhelp_basename = 'FreeFEM-doc'

html_add_permalinks = ' '


# -- Options for LaTeX output ------------------------------------------------

latex_additional_files = ['_static/img/logo_ANR.png', '_static/img/logo_CNRS.png', '_static/img/logo_INRIA.png', '_static/img/logo_LJLL.png', '_static/img/logo_Sorbonne.png', '_static/img/logo_UPMC.png']

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': """
\\usepackage[margin=8pt]{subcaption}
\\captionsetup{labelfont=bf}
\\def\\R{{\\mathbb{R}}}
\\def\\C{{\\mathbb{C}}}
\\def\\P{{\\mathbb{P}}}
\\def\\p{{\\partial}}
\\def\\n{{\\nabla}}
\\def\\boldx{{\\mathbf{x}}}
\\def\\boldxi{{\\boldsymbol{\\xi}}}
\\def\\arccosh{{\\text{arccosh}}}
\\def\\arcsinh{{\\text{arcsinh}}}
\\def\\arctanh{{\\text{arctanh}}}
\\def\\vecttwo#1#2{\\left|\\begin{smallmatrix} #1 \\\\ #2 \\end{smallmatrix}\\right.}
\\def\\vectthree#1#2#3{\\left|\\begin{smallmatrix} #1 \\\\ #2 \\\\ #3\\end{smallmatrix}\\right.}
\\def\\bR{{\\bf R}}
\\def\\bP{{\\bf P}}
\\def\\bZ{{\\bf Z}}
\\def\\bC{{\\bf C}}
\\def\\VS{\\bR^2}
\\def\\SVS{\\underline V}
\\def\\SO{{\\bf SO}}
\\def\\Sym{{\\bf Sym}}
\\def\\qi{{\\bf i}}
\\def\\qj{{\\bf j}}
\\def\\qk{{\\bf k}}
\\def\\ec{\\hat{\\bf e}}
\\def\\xc{\\hat{\\bf x}}
\\def\\bdr{\\partial}
\\def\\PD{\\partial_}
\\def\\strain{\\underline \\epsilon}
\\def\\stress{\\underline \\sigma}
\\def\\strainrate{\\underline \\epsilon^.}
\\def\\stressrate{\\underline \\sigma^.}
\\def\\stiff{\\; \\underline{\\underline C}\\;}
\\def\\comply{\\underline{\\underline \\kappa}\\;}
\\def\\Id{{\\bf I}}
\\def\\Div{\\nabla \\cdot}
\\def\\Grad{\\mathbf{\\nabla}}
\\def\\rot{\\nabla \\times}
\\def\\lap{\\triangle}
\\def\\tr{{\\bf tr}\\;}
\\def\\udH{\\underline H}
\\def\\refX{\\mathbf X}
\\def\\Jac{\\overline{J}}
\\def\\spatx{\\mathbf x}
\\def\\ani{\\overline a}
\\def\\mat{\\left[\\begin{array}}
\\def\\tam{\\end{array}\\right]}
\\def\\arr{\\left.\\begin{array}}
\\def\\rra{\\end{array}\\right\\}}
\\def\\arl{\\left\\{\\begin{array}}
\\def\\lra{\\end{array}\\right.}
\\def\\ar{\\begin{array}}
\\def\\ra{\\end{array}}
\\def\\const{\\mbox{ const.}}
\\def\\eps{\\; \\epsilon}
\\def\\sig{\\; \\sigma}
\\def\\th{\\theta}
\\def\\sgn{\\mbox{sgn}}
\\def\\qed{\\; Q.E.D.\\\\}
\\def\\ranqe{\\end{eqnarray}}
\\def\\ol{\\overline}
\\def\\ul{\\underline}
\\def\\bB{{\\bf B}}
\\def\\bC{{\\bf C}}
\\def\\bD{{\\bf D}}
\\def\\bE{{\\bf E}}
\\def\\bF{{\\bf F}}
\\def\\bK{{\\bf K}}
\\def\\bP{{\\bf P}}
\\def\\bS{{\\bf S}}
\\def\\bT{{\\bf T}}
\\def\\bsig{{\\bf \\sigma}}
\\def\\T{{\mathbb{T}}}
\\def\\d{{text{d}}}
    """,

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'maketitle': r'''
        \sphinxmaketitle
        \clearpage
        In collaboration with:
        \vfill
        \begin{minipage}{.49\linewidth}
            \centering
            \sphinxincludegraphics[width=.8\linewidth]{logo_LJLL.png}
        \end{minipage}
        \hfill
        \begin{minipage}{.49\linewidth}
            \centering
            \sphinxincludegraphics[width=.8\linewidth]{logo_UPMC.png}
        \end{minipage}
        \vfill
        \begin{minipage}{.49\linewidth}
            \centering
            \sphinxincludegraphics[width=.8\linewidth]{logo_Sorbonne.png}
        \end{minipage}
        \hfill
        \begin{minipage}{.49\linewidth}
            \centering
            \sphinxincludegraphics[width=.8\linewidth]{logo_ANR.png}
        \end{minipage}
        \vfill
        \begin{minipage}{.49\linewidth}
            \centering
            \sphinxincludegraphics[width=.8\linewidth]{logo_INRIA.png}
        \end{minipage}
        \hfill
        \begin{minipage}{.49\linewidth}
            \centering
            \sphinxincludegraphics[width=.8\linewidth]{logo_CNRS.png}
        \end{minipage}
    '''
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'FreeFEM.tex', 'FreeFEM Documentation',
     'Frederic Hecht', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'freefem', 'FreeFEM Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'FreeFEM', 'FreeFEM Documentation',
     author, 'FreeFEM', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

numfig = True

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
