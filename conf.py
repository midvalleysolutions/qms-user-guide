# Sphinx configuration of the Quality user guide, modelled on the Odoo documentation (one page per app, topic pages
# of numbered steps, menu paths as Quality ‣ Configuration ‣ Settings).
#
#   .venv/bin/sphinx-build -b html docs/userguide docs/userguide/_build/html/en
#   .venv/bin/sphinx-build -b html -D language=vi docs/userguide docs/userguide/_build/html/vi
#
# Translations live in locale/<lang>/LC_MESSAGES/*.po (sphinx-intl), English is the source.

project = "Quality Management System"
author = "Midvalley Solutions"
copyright = "2026, Midvalley Solutions. This guide is licensed under CC BY-SA 4.0"
version = release = "20.0"

extensions = []
root_doc = "index"
exclude_patterns = ["_build", "locale", "_shots", "_publish"]

language = "en"
locale_dirs = ["locale/"]
gettext_compact = False

html_theme = "furo"
html_title = "Quality Management System — User guide"
html_baseurl = "https://midvalleysolutions.github.io/qms-user-guide/20.0/en/"
html_static_path = []
html_theme_options = {
    "light_css_variables": {"color-brand-primary": "#714B67", "color-brand-content": "#714B67"},
    "dark_css_variables": {"color-brand-primary": "#C9A5BF", "color-brand-content": "#C9A5BF"},
    "sidebar_hide_name": False,
}
