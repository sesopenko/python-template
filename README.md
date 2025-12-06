# Python Project Template

This repository provides a template for Python projects with best-practice tooling and workflows.

## Quick Start

**Create a virtual environment** (recommended inside the project):

   ```bash
   python -m venv .venv
   ```

**Activate the virtual environment**:

   - On Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows (PowerShell):
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - On Windows (Command Prompt):
     ```cmd
     .venv\Scripts\activate.bat
     ```

**Install `pip-tools` and `invoke`** (for dependency management and tasks):

   ```bash
   pip install pip-tools invoke
   ```

**Compile `requirements.txt` from `requirements.in`**:

   ```bash
   invoke compile
   ```

   This generates (or updates) a locked `requirements.txt` with all transitive dependencies pinned.

**Install the exact dependencies**:

   ```bash
   invoke install
   ```

   This ensures your virtual environment matches the lock file exactly, removing any extra packages.

**Install your project in editable mode**:

   ```bash
   invoke dev
   ```

   This installs your project in editable mode so local changes are immediately reflected without reinstalling.  
   Note: if you later run `invoke sync` or `invoke upgrade` (both use `pip-sync` under the hood), you should re-run `invoke dev` afterward, because `pip-sync` removes anything not listed in `requirements.txt`.

After completing the Quick Start, you can use `invoke` for all common development tasks.

## Customizing This Template for Your Project

When you fork this repository to start a new project, you should:

1. **Choose your project/package name** (e.g. `awesome_app`, `my_library`).
2. **Replace the placeholder `project_name`** in the relevant files.
3. **Create your first package** under `src/<your_project_name>/`.

### 1. Pick a project/package name

Pick a valid Python package name:

- All lowercase.
- Use underscores (`_`) instead of spaces or hyphens.
- Start with a letter.
- Example good names: `my_app`, `awesome_tool`, `data_pipeline`.

You will use this name in:

- `pyproject.toml` → `[project] name`
- Your package directory → `src/<your_project_name>/`

### 2. Where to replace `project_name`

This template uses `project_name` as a placeholder. When you fork it, search for `project_name` and replace it with your actual project name.

At minimum, you should update:

1. **`pyproject.toml`**

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

2. **Source package layout**

   The recommended layout is:

   ```text
   src/
       your_actual_project_name/
           __init__.py
           ...
   ```

   The placeholder `project_name` in the README’s examples refers to this directory name. When you see `src/project_name/` in the docs, substitute your own name, e.g.:

   ```text
   src/my_cool_app/
   ```

If you add more tooling or configuration later (e.g. CI workflows, docs configs), you may also want to replace `project_name` in those files.

### 3. Creating your first package

This template assumes a `src/`-based layout, which keeps your import paths clean and avoids some common pitfalls.

Follow these steps to create your first package:

1. **Create the `src/` directory (if it doesn’t exist yet)**

   From the repository root:

   ```bash
   mkdir -p src/your_actual_project_name
   ```

2. **Add `__init__.py`**

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

3. **(Optional) Add a main module**

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

4. **Install in editable mode**

   After creating your package, reinstall in editable mode so imports work:

   ```bash
   invoke dev
   ```

   Now you can import your package in Python:

   ```python
   >>> import your_actual_project_name
   >>> your_actual_project_name.hello("world")
   'Hello, world!'
   ```

5. **(Optional) Add a console script entry point**

   If you want a CLI command (e.g. `your-app`), you can add this to `pyproject.toml`:

   ```toml
   [project.scripts]
   your-app = "your_actual_project_name.main:main"
   ```

   After running `invoke dev` again, you’ll be able to run:

   ```bash
   your-app
   ```

### 4. Creating your first tests

To follow the template’s testing guidance:

1. **Create the tests directory**

   ```bash
   mkdir -p tests
   ```

2. **Add a simple test file**

   Create `tests/test_hello.py`:

   ```python
   from your_actual_project_name import hello


   def test_hello_returns_expected_greeting() -> None:
       assert hello("world") == "Hello, world!"
   ```

3. **Run tests**

   ```bash
   invoke test
   ```

   This should discover and run your test using pytest.

## Managing Dependencies

### Adding a new dependency

1. Add the package name (and optionally a version specifier) to `requirements.in`. Example:
   ```text
   requests>=2.31
   ```

2. Re‑compile the lock file:
   ```bash
   invoke compile
   ```

3. Sync your environment:
   ```bash
   invoke sync
   ```

4. Reinstall your project in editable mode (if needed):
   ```bash
   invoke dev
   ```

### Upgrading all dependencies

To upgrade every package to the latest versions allowed by your specifiers:

```bash
invoke upgrade
invoke dev  # re-install editable project after pip-sync
```

### Development dependencies

All core development tools (e.g., `pytest`, `black`, `ruff`, `mypy`, `invoke`, `pip-tools`) are declared in `requirements.in` and managed via `pip-compile` / `pip-sync`.

If you prefer to manage additional development-only dependencies via `pip-tools`, you can still create a `requirements-dev.in` file and compile it with:

```bash
invoke compile  # after adjusting tasks.py to handle requirements-dev.in
```

Then install both production and development dependencies with:

```bash
invoke install  # after adjusting tasks.py to sync multiple requirement files
invoke dev
```

(For now, this template assumes a single `requirements.in` / `requirements.txt` pair.)

## Using the Virtual Environment

- To activate the environment again in a new shell, repeat the **Activate** step above.
- The `python` and `pip` commands inside the activated environment are isolated to the project.
- The `.venv` directory is already ignored by `.gitignore`.

## Development Tasks

With the dependencies installed via `requirements.in` / `requirements.txt` and your project installed in editable mode, you can run common tasks via `invoke`:

- **List available tasks**:
  ```bash
  invoke help
  ```

- **Run tests**:
  ```bash
  invoke test
  ```

- **Format code with Black and isort**:
  ```bash
  invoke format
  ```

- **Lint with Ruff**:
  ```bash
  invoke lint
  ```

- **Type checking with mypy**:
  ```bash
  invoke type-check
  ```

- **Clean build artifacts and caches**:
  ```bash
  invoke clean
  ```

## Project Structure

A typical Python project layout might look like:

```
├── .venv/                     # Virtual environment (excluded from git)
├── src/                       # Package source code
│   └── your_actual_project_name/
│       ├── __init__.py
│       └── ...
├── tests/                     # Test suite
├── .gitignore
├── .aider.conf.yml            # Aider configuration (if used)
├── requirements.in            *Direct dependencies*
├── requirements.txt           *Locked dependencies (generated)*
├── tasks.py                   # Invoke tasks
├── README.md                  *This file*
└── pyproject.toml             # Build backend and tool configuration
```

## Additional Tips

- You can replace `pip-tools` with [`uv`](https://github.com/astral-sh/uv) for faster dependency resolution and installation. `uv` provides compatible `pip-compile` and `pip-sync` commands.
- Use `tasks.py` with [Invoke](https://www.pyinvoke.org/) to encapsulate frequent commands (e.g., `invoke install`, `invoke test`).
- Keep `requirements.txt` under version control to guarantee reproducible environments across machines.

## Need Help?

Consult the official documentation of the tools mentioned:

- [pip‑tools](https://github.com/jazzband/pip-tools)
- [venv](https://docs.python.org/3/library/venv.html)
- [Python Packaging User Guide](https://packaging.python.org)

Happy coding!
