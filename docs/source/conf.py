from datetime import datetime

import alabaster

project = "FermulerPy"
year = datetime.now().year
copyright = "%d FermulerPy Development Team" % year

version = "v1"
release = "v1.dev0"
highlight_language = "python"
pygments_style = "sphinx"
autoclass_content = "both"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}


def setup(app):
    app.add_js_file('https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.6/require.min.js')

autodoc_member_order = "bysource"

html_theme_options = {
    "badge_branch": "master",
    "codecov_button": True,
    "description": "Number Theory in Python",
    "body_text_align": "left",
    "github_user": "fermulerpy",
    "github_repo": "fermulerpy",
    "show_relbars": True,
    "show_powered_by": False,
    "page_width": "80%",
    "github_banner": True,
    "github_button": True,
}

add_function_parentheses = True

add_module_names = True

needs_sphinx = "3.03"
extensions = [
    "alabaster",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "nbsphinx",
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinx.ext.mathjax", 
    "sphinx.ext.graphviz",  
    "sphinx.ext.viewcode",  
]
templates_path = ["_templates"]

source_suffix = ".rst"

master_doc = "index"

html_theme = "alabaster"

html_theme_path = [alabaster.get_path()]

html_title = "FermulerPy"

html_static_path = ["_static"]

htmlhelp_basename = "fermulerpydoc"

html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "donate.html",
    ]
}