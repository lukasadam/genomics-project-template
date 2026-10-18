# Genomics project template

Copier template for reproducible genomics data science projects using Pixi,
pytest, Ruff, notebooks, and the reusable `genomics_toolkit` package.

Generate a project with:

```bash
copier copy /path/to/local/genomics-project-template /path/to/new-project
```

Update an existing generated project with:

```bash
copier update --trust
```

The generated project keeps project-specific code separate from the shared
toolkit and provides Pixi, Git, and toolkit installation cheatsheets.
