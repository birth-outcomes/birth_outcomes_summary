# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Birth outcomes'
copyright = '2024, Amy Heather'
author = 'Amy Heather'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',  # To use markdown as well as reStructuredText
]

# File types for documentation
source_suffix = ['.md', '.ipynb']

extensions = [
    'sphinx_togglebutton',
    'sphinx_copybutton',
    'myst_nb',
    'jupyter_book',
    'sphinx_thebe',
    'sphinx_comments',
    'sphinx_external_toc',
    'sphinx.ext.intersphinx',
    'sphinx_design',
    'sphinx_book_theme',
    'sphinxcontrib.mermaid',
    'sphinxcontrib.bibtex',
    'sphinx_jupyterbook_latex',
    'sphinx_multitoc_numbering'
]

myst_enable_extensions = [
    'colon_fence',
    'dollarmath',
    'linkify',
    'substitution',
    'tasklist'
]

html_theme_options = {
    'search_bar_text': 'Search this book...',
    'launch_buttons': {
        'notebook_interface': 'classic',
        'binderhub_url': '',
        'jupyterhub_url': '',
        'thebe': False,
        'colab_url': ''},
    'path_to_docs': 'docs',
    'repository_url': 'https://github.com/executablebooks/jupyter-book',
    'repository_branch': 'main',
    'extra_footer': '',
    'home_page_in_toc': True,
    'announcement': '',
    'analytics': {'google_analytics_id': ''},
    'use_repository_button': True,
    'use_edit_page_button': False,
    'use_issues_button': True
}

bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'unsrt'
bibtex_reference_style = 'super'

exclude_patterns = [
    '**.ipynb_checkpoints',
    '.DS_Store',
    'Thumbs.db',
    '_build'
]

html_theme = 'pydata_sphinx_theme'

comments_config = {'hypothesis': False, 'utterances': False}
external_toc_exclude_missing = True
external_toc_path = '_toc.yml'
html_baseurl = ''
html_favicon = ''
html_logo = ''
html_sourcelink_suffix = ''
html_title = 'Birth Outcomes'
latex_engine = 'pdflatex'
myst_url_schemes = ['mailto', 'http', 'https']
nb_execution_allow_errors = False
nb_execution_cache_path = ''
nb_execution_excludepatterns = []
nb_execution_in_temp = False
nb_execution_mode = 'off'
nb_execution_timeout = 30
nb_output_stderr = 'show'
numfig = True
pygments_style = 'sphinx'
suppress_warnings = ['myst.domains']
use_jupyterbook_latex = True
use_multitoc_numbering = True
