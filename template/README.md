# {{ project_name }}

Reusable, reproducible genomics data science project managed with Pixi.

## Setup

```bash
pixi install
pixi run -e dev pre-commit install
pixi run -e dev test
```

The project uses the local editable `genomics_toolkit` package configured in
`pixi.toml`. Adjust `genomics_toolkit_path` when generating the template.

## Structure

- `src/{{ package_name }}/`: project-specific reusable code
- `notebooks/`: analysis notebooks copied or adapted from toolkit templates
- `data/`: raw, interim, processed, and external data (usually gitignored)
- `results/`: figures, tables, and exported outputs
- `tests/`: automated tests
- `docs/`: Pixi, Git, and project notes

Keep dataset-specific logic here; move broadly reusable functions to
`genomics_toolkit`.

See `docs/PIXI_CHEATSHEET.md`, `docs/GIT_CHEATSHEET.md`, and
`docs/GENOMICS_TOOLKIT.md`.
