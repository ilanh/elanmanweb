#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# elanmanweb documentation build configuration file, created by
# sphinx-quickstart on Thu Nov 30 12:32:09 2017.
#
import os
import sys
import django
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'elanmanweb.docsettings'

django.setup()

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.imgmath',
              'sphinx.ext.githubpages']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = 'elanmanweb'
copyright = '2017, Ilan Harel'
author = 'Ilan Harel'

version = '0.1'
release = '0.1'

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

# todo_include_todos = True
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_logo = 'img/logo.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

htmlhelp_basename = 'elanmanwebdoc'

intersphinx_mapping = {'https://docs.python.org/3.6': None}

autodoc_member_order = 'bysource'
autodoc_default_flags = ['members', 'undoc-members', 'show-inheritance']
autosummary_generate = True