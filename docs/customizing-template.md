# Customizing the Template for Your Project

This template uses `project_name` as a placeholder. When you fork or copy this repository to start a new project, you should replace it with your actual project/package name.

## 1. Choose a project/package name

Pick a valid Python package name:

- All lowercase.
- Use underscores (`_`) instead of spaces or hyphens.
- Start with a letter.

Example good names:

- `my_app`
- `awesome_tool`
- `data_pipeline`

You will use this name in:

- `pyproject.toml` → `[project] name`
- Your package directory → `src/<your_project_name>/`

## 2. Replace `project_name` in configuration

At minimum, update:

### `pyproject.toml`

In the `[project]` section:

```toml
[project]
name = "project_name"
```

Change to:

```toml
[project]
name = "your_actual_project_name"
```

You can also update:

- `description`
- `authors`
- `readme`
- `license`
- Any other metadata that should reflect your project.

## 3. Create your source package

This template assumes a `src/`-based layout, which keeps your import paths clean and avoids some common pitfalls.

From the repository root:

```bash
mkdir -p src/your_actual_project_name
```

Create `src/your_actual_project_name/__init__.py` with minimal content:

```python
"""
Top-level package for your_actual_project_name.
"""

__all__ = ["hello"]


def hello(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"
```

Replace `your_actual_project_name` with your chosen name.

## 4. (Optional) Add a main module

If you want a simple entry point, create `src/your_actual_project_name/main.py`:

```python
"""Command-line entry point for your_actual_project_name."""

from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    """Run the main CLI for the project."""
    if argv is None:
        argv = sys.argv[1:]

    name = argv[0] if argv else "world"
    print(f"Hello, {name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## 5. (Optional) Add a console script entry point

If you want a CLI command (e.g. `your-app`), you can add this to `pyproject.toml`:

```toml
[project.scripts]
your-app = "your_actual_project_name.main:main"
```

After running `invoke dev` again, you’ll be able to run:

```bash
your-app
```

## 6. Reinstall in editable mode

After creating or renaming your package, reinstall in editable mode so imports work:

```bash
invoke dev
```

Now you can import your package in Python:

```python
>>> import your_actual_project_name
>>> your_actual_project_name.hello("world")
'Hello, world!'
```

## 7. Update tests

Create or update tests under `tests/` to match your new package name. For example:

```python
from your_actual_project_name import hello


def test_hello_returns_expected_greeting() -> None:
    assert hello("world") == "Hello, world!"
```

Run the tests:

```bash
invoke test
```

You now have a customized project based on this template.
