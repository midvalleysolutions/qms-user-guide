# Quality Management System for Odoo — User guide

The user guide of the **Quality Management System** apps for Odoo 20.0 (the free core, the free bridges and
**QMS Advanced**), published at https://midvalleysolutions.github.io/qms-user-guide/.

The pages are written in reStructuredText and built with [Sphinx](https://www.sphinx-doc.org/):

```bash
pip install -r requirements.txt
sphinx-build -b html . _build/html
```

Every push to `main` rebuilds and republishes the site (see `.github/workflows/pages.yml`).

## Licence

The text and images of this guide are licensed under the
[Creative Commons Attribution-ShareAlike 4.0 International licence](https://creativecommons.org/licenses/by-sa/4.0/)
(CC BY-SA 4.0). The apps themselves are licensed separately (the free core under LGPL-3, QMS Advanced under OPL-1).
