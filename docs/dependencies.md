# Dependency Management

This project uses [`pip-tools`](https://github.com/jazzband/pip-tools) and [`invoke`](https://www.pyinvoke.org/) to manage dependencies in a reproducible way.

## Files involved

- `requirements.in` – Direct (top-level) dependencies you specify.
- `requirements.txt` – Fully pinned dependencies generated from `requirements.in`.
- `tasks.py` – Invoke tasks that wrap `pip-compile` and `pip-sync`.

## Adding a new dependency

1. Add the package name (and optionally a version specifier) to `requirements.in`. Example:

   ```text
   requests>=2.31
   ```

2. Re‑compile the lock file:

   ```bash
   invoke compile
   ```

   This runs `pip-compile requirements.in` and updates `requirements.txt`.

3. Sync your environment:

   ```bash
   invoke sync
   ```

   This runs `pip-sync requirements.txt`, installing new packages and removing any that are no longer needed.

4. Reinstall your project in editable mode (if needed):

   ```bash
   invoke dev
   ```

## Upgrading all dependencies

To upgrade every package to the latest versions allowed by your specifiers:

```bash
invoke upgrade
invoke dev  # re-install editable project after pip-sync
```

This is equivalent to:

```bash
pip-compile --upgrade requirements.in
pip-sync requirements.txt
pip install -e .
```

## Development-only dependencies

All core development tools (e.g., `pytest`, `black`, `ruff`, `mypy`, `invoke`, `pip-tools`) are declared in `requirements.in` and managed via `pip-compile` / `pip-sync`.

If you prefer to manage additional development-only dependencies via `pip-tools`, you can create a `requirements-dev.in` file and adjust `tasks.py` to handle it. A common pattern is:

- `requirements.in` – runtime dependencies.
- `requirements-dev.in` – development-only dependencies (including `-r requirements.in`).

For example, `requirements-dev.in`:

```text
-r requirements.in
pytest>=9.0
black>=25.0
ruff>=0.14
mypy>=1.19
invoke>=2.0
pip-tools>=7.0
```

You would then update your tasks to compile and sync both files. This template currently assumes a single `requirements.in` / `requirements.txt` pair, but it can be extended as needed.

## Using `pip-sync` safely

`pip-sync` removes any packages that are not listed in the provided requirements file(s). This is great for reproducibility, but keep in mind:

- If you install packages manually with `pip install ...`, they may be removed the next time you run `invoke sync` or `invoke upgrade`.
- After syncing, re-run `invoke dev` to ensure your project is still installed in editable mode.

## Optional: Using `uv` instead of `pip-tools`

You can replace `pip-tools` with [`uv`](https://github.com/astral-sh/uv) for faster dependency resolution and installation. `uv` provides compatible `pip-compile` and `pip-sync` commands.

For example:

```bash
uv pip compile requirements.in -o requirements.txt
uv pip sync requirements.txt
```

You can update `tasks.py` to call `uv pip compile` / `uv pip sync` instead of `pip-compile` / `pip-sync` if you prefer.
