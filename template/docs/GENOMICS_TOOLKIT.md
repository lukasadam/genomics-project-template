# Using `genomics_toolkit`

The template installs the local toolkit in editable mode:

```toml
genomics-toolkit = { path = "../genomics-toolkit", editable = true }
```

Use it from notebooks or project code:

```python
from genomics_toolkit import qc
from genomics_toolkit.io import load_cellbender
```

Changes made in the toolkit checkout are available after restarting the
notebook kernel. Pin a Git tag or commit for reproducible projects once the
analysis is stable.
