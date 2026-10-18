# Pixi cheatsheet

```bash
pixi install                 # create/synchronize environments
pixi run -e dev test         # run tests
pixi run -e dev lint         # lint
pixi run -e dev format       # format
pixi add numpy               # add a conda dependency
pixi add --pypi scanpy       # add a PyPI dependency
pixi update                  # update the lockfile
pixi list                    # inspect installed packages
pixi shell -e dev            # enter the development shell
```

Commit `pixi.toml` and `pixi.lock`. Do not commit `.pixi/`.
