# Customizing the Template for Your Project

This template uses `project_name` as a placeholder. When you fork or copy this repository to start a new project, you should replace it with your actual project/package name and your preferred license.

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

## 2. Choose and apply a license

This template ships with MIT as a default, but you should pick the license that matches your goals (e.g. MIT, Apache-2.0, GPL-3.0, proprietary, etc.).

### 2.1 Pick a license

Some common options:

- **MIT** – very permissive, simple, widely used.
- **Apache-2.0** – permissive, with explicit patent grant and some additional conditions.
- **GPL-3.0** – strong copyleft; derivative works must also be GPL-compatible.
- **Proprietary / closed source** – you keep most rights; others have limited or no reuse rights.

Resources to help you choose:

- <https://choosealicense.com/>
- <https://www.gnu.org/licenses/license-list.html>

If you are unsure, MIT or Apache-2.0 are common defaults for open source libraries.

### 2.2 Update license files and metadata

Once you’ve chosen a license:

1. **Top-level license file**

   - Edit `LICENSE` or `LICENSE.txt` at the repository root.
   - Replace its contents with the full text of your chosen license (for example, copy from <https://choosealicense.com/licenses/>).
   - Update any placeholders (e.g. year, your name or organization).

2. **Project metadata (`pyproject.toml`)**

   In the `[project]` section, update the `license` field to match your choice. For example, the template starts with:

   ```toml
   [project]
   name = "project_name"
   license = {text = "MIT"}
   ```

   You might change this to:

   ```toml
   [project]
   name = "your_actual_project_name"
   license = {text = "Apache-2.0"}
   ```

   or, if you prefer to reference a file:

   ```toml
   [project]
   name = "your_actual_project_name"
   license = {file = "LICENSE.txt"}
   ```

   Make sure this matches how you’ve set up the `LICENSE`/`LICENSE.txt` file.

3. **README**

   Update the “License” section in `README.md` so it accurately reflects your chosen license. For example:

   ```markdown
   ## License

   MIT – see `LICENSE` for details.
   ```

   might become:

   ```markdown
   ## License

   Apache-2.0 – see `LICENSE.txt` for details.
   ```

4. **Source file headers (optional)**

   If you want per-file license headers, add or update them in your source files under `src/` to reference your chosen license and copyright holder.

## 3. Replace `project_name` in configuration

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
- `license` (see section 2)
- Any other metadata that should reflect your project.

## 4. Create your source package

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

## 5. (Optional) Add a main module

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

## 6. (Optional) Add a console script entry point

If you want a CLI command (e.g. `your-app`), you can add this to `pyproject.toml`:

```toml
[project.scripts]
your-app = "your_actual_project_name.main:main"
```

After running `invoke dev` again, you’ll be able to run:

```bash
your-app
```

## 7. Reinstall in editable mode

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

## 8. Update tests

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

You now have a customized project based on this template, with your own package name and license.
