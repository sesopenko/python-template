# Development Tasks

This project uses [Invoke](https://www.pyinvoke.org/) to provide a set of common development tasks via `tasks.py`.

With your virtual environment activated and dependencies installed, you can list available tasks:

```bash
invoke help
```

Below is an overview of the tasks defined in `tasks.py`.

> Convention  
> After the initial setup (creating/activating `.venv` and installing `pip-tools` and `invoke`),
> all project-specific commands should be exposed as `invoke` tasks rather than ad-hoc shell
> commands. This keeps the workflow consistent and makes it easy to change commands in one
> place (`tasks.py`) instead of updating multiple docs and scripts. When you find yourself
> documenting or repeatedly running a shell command, prefer adding or updating an `invoke`
> task instead.

## Installation and environment management

### `invoke install`

Install production and development dependencies from `requirements.txt` using `pip-sync`:

```bash
invoke install
```

This ensures your environment matches the locked dependencies exactly.

### `invoke dev`

Install the project in editable mode:

```bash
invoke dev
```

Use this after cloning the repo or after running `invoke sync` / `invoke upgrade`.

### `invoke sync`

Sync the virtual environment with `requirements.txt` using `pip-sync`:

```bash
invoke sync
```

This removes any packages not listed in `requirements.txt` and installs any missing ones.

### `invoke compile`

Compile `requirements.txt` from `requirements.in` using `pip-compile`:

```bash
invoke compile
```

This resolves and pins all transitive dependencies.

### `invoke upgrade`

Upgrade all dependencies to their latest allowed versions and sync:

```bash
invoke upgrade
```

Internally, this runs:

- `pip-compile --upgrade requirements.in`
- `pip-sync requirements.txt`

After upgrading, you should typically run:

```bash
invoke dev
```

to reinstall your project in editable mode.

## Code quality

### `invoke format`

Format code with [Black](https://black.readthedocs.io/) and [isort](https://pycqa.github.io/isort/):

```bash
invoke format
```

This runs:

- `black .`
- `isort .`

### `invoke lint`

Lint the codebase with [Ruff](https://docs.astral.sh/ruff/):

```bash
invoke lint
```

This runs:

- `ruff check .`

### `invoke type-check`

Run static type checks with [mypy](https://mypy-lang.org/):

```bash
invoke type-check
```

This runs:

- `mypy .`

### `invoke validate`

Run all validation checks (formatting check, linting, tests, and type-checking) against the full codebase, similar to the CI pipeline:

```bash
invoke validate
```

This runs, in order:

- `invoke format-check`
- `invoke lint`
- `invoke test`
- `invoke type-check`

Use this before pushing or opening a pull request to mirror what CI will do.

## Testing

### `invoke test`

Run tests with [pytest](https://docs.pytest.org/):

```bash
invoke test
```

By default, pytest is configured via `pyproject.toml` to discover tests under `tests/`.

## Cleaning

### `invoke clean`

Remove build artifacts, caches, and coverage files in a cross-platform way:

```bash
invoke clean
```

This removes:

- `build/`, `dist/`, `*.egg-info`
- `.pytest_cache`, `.ruff_cache`, `.mypy_cache`
- `htmlcov/`
- `.coverage`
- All `__pycache__` directories

## Recommended workflow

A typical development loop might look like:

1. Sync and install:

   ```bash
   invoke compile   # only when dependencies change
   invoke install
   invoke dev
   ```

2. Make code changes.

3. Before committing (or via pre-commit hooks):

   ```bash
   invoke format
   invoke validate   # or run the individual tasks:
                     # invoke lint
                     # invoke type-check
                     # invoke test
   ```

4. Occasionally upgrade dependencies:

   ```bash
   invoke upgrade
   invoke dev
   ```

If you have `pre-commit` installed and have run `invoke pre-commit`, many of these checks (formatting, linting, type-checking, and tests) will run automatically before each commit, helping keep the codebase consistent and healthy.
