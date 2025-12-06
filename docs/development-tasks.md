# Development Tasks

This project uses [Invoke](https://www.pyinvoke.org/) to provide a set of common development tasks via `tasks.py`.

With your virtual environment activated and dependencies installed, you can list available tasks:

```bash
invoke help
```

Below is an overview of the tasks defined in `tasks.py`.

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

3. Before committing:

   ```bash
   invoke format
   invoke lint
   invoke type-check
   invoke test
   ```

4. Occasionally upgrade dependencies:

   ```bash
   invoke upgrade
   invoke dev
   ```
