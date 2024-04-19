# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Birth outcomes'
copyright = '2024, Amy Heather'
author = 'Amy Heather'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinxcontrib.mermaid',  # To render mermaid diagrams
    'myst_nb',  # Parse .ipynb files
    'sphinxcontrib.bibtex', # Insert BibTeX citations
    'sphinx_copybutton', # Adds a copy button next to code blocks
    'sphinx_togglebutton', # Allows you to make admonitions toggle-able
    'sphinx_design'  # Allows grides, cards, dropdowns, tabs, badges, etc.
]

myst_enable_extensions = [
    'colon_fence'  # To use sphinx-desin alongside myst_parser
]

# File types for documentation
source_suffix = ['.md', '.ipynb']

# Files to ignore
exclude_patterns = [
    '**.ipynb_checkpoints',
    '.DS_Store',
    'Thumbs.db',
    '_build',
    'README.md'
]

# Notebook execution
nb_execution_allow_errors = False
nb_execution_cache_path = ''
nb_execution_excludepatterns = []
nb_execution_in_temp = False
nb_execution_mode = 'off'
nb_execution_timeout = 30

# Bibliography
bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'unsrt'
bibtex_reference_style = 'super'

# -- Options for HTML output -------------------------------------------------

html_theme = 'pydata_sphinx_theme'