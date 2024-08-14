# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import sphinx_rtd_theme
import time

project = 'SunFounder PiCar-X Kit'
copyright = f'{time.localtime().tm_year}, SunFounder'
author = 'www.sunfounder.com'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Link to other projects’ documentation with intersphinx. Use the intersphinx_mapping configuration to indicate the name and link of the projects you want to use

extensions = [
    'sphinx.ext.intersphinx',
]


intersphinx_mapping = {
    'ezblock': ('https://docs.sunfounder.com/projects/ezblock3/en/latest/', None),
}

html_static_path = ['_static']


# SunFounder logo

# html_js_files = [
#     'https://ezblock.cc/readDocFile/custom.js',
# ]
# html_css_files = [
#     'https://ezblock.cc/readDocFile/custom.css',
# ]

#### RTD+

html_js_files = [
    'https://ezblock.cc/readDocFile/custom.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/ace.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/ext-language_tools.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/theme-chrome.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-python.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-sh.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/monokai.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/xterm.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/FitAddon.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/readTheDocIndex.js',
    './lang.js', # new
    'custom.js', #new

]
html_css_files = [
    'https://ezblock.cc/readDocFile/custom.css',
    'https://ezblock.cc/readDocFile/readTheDoc/src/css/index.css',
    'https://ezblock.cc/readDocFile/readTheDoc/src/css/xterm.css',
]



# Multi-language

language = 'en' # Before running make html, set the language.
locale_dirs = ['locale/'] # .po files for other languages are placed in the locale/ folder.

gettext_compact = False # Support for generating the contents of the folders inside source/ into other languages.

# links

rst_epilog = """

.. |link_sf_facebook| raw:: html

    <a href="https://bit.ly/raphaelkit " target="_blank">here</a>

.. |link_robot_hat| raw:: html

    <a href="https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/hardware_introduction.html" target="_blank">SunFounder Robot HAT</a>

.. |link_german_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/picar-x-v20/de/latest/index.html" target="_blank">Deutsch Online-Kurs</a>

.. |link_jp_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/picar-x-v20/ja/latest/" target="_blank">日本語オンライン教材</a>

.. |link_en_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/picar-x-v20/en/latest/" target="_blank">English Online-tutorials</a>

.. |link_PiCar-X_kit| raw:: html

    <a href="https://www.sunfounder.com/products/picar-x?variant=44269165510891" target="_blank">Purchase Link for PiCar-X Kit</a>

.. |link_PiCar_kit| raw:: html

    <a href="https://www.sunfounder.com/products/picar-x?variant=44269165510891" target="_blank">PiCar-X</a>


"""
