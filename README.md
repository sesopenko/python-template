# Python Project Template

This repository provides a template for Python projects with best-practice tooling and workflows.

## Quick Start

1. **Create a virtual environment** (recommended inside the project):

   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment**:

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

3. **Install `pip-tools`** (for dependency management):

   ```bash
   pip install pip-tools
   ```

4. **Compile `requirements.txt` from `requirements.in`**:

   ```bash
   pip-compile requirements.in
   ```

   This generates (or updates) a locked `requirements.txt` with all transitive dependencies pinned.

5. **Install the exact dependencies**:

   ```bash
   pip-sync requirements.txt
   ```

   This ensures your virtual environment matches the lock file exactly, removing any extra packages.

## Managing Dependencies

### Adding a new dependency

1. Add the package name (and optionally a version specifier) to `requirements.in`. Example:
   ```
   requests>=2.31
   ```

2. Re‑compile the lock file:
   ```bash
   pip-compile requirements.in
   ```

3. Sync your environment:
   ```bash
   pip-sync requirements.txt
   ```

### Upgrading all dependencies

To upgrade every package to the latest versions allowed by your specifiers:

```bash
pip-compile --upgrade requirements.in
pip-sync requirements.txt
```

### Development dependencies

If you have separate development dependencies (e.g., `pytest`, `black`, `mypy`), consider creating a `requirements-dev.in` file. Compile it with:

```bash
pip-compile requirements-dev.in
```

Then install both production and development dependencies with:

```bash
pip-sync requirements.txt requirements-dev.txt
```

## Using the Virtual Environment

- To activate the environment again in a new shell, repeat the **Activate** step above.
- The `python` and `pip` commands inside the activated environment are isolated to the project.
- The `.venv` directory is already ignored by `.gitignore`.

## Development Tasks

If your project includes a `pyproject.toml` with optional tool configurations, you can run common tasks such as:

- **Run tests** (assuming `pytest` is installed):
  ```bash
  pytest
  ```

- **Format code with Black**:
  ```bash
  black .
  ```

- **Sort imports with isort**:
  ```bash
  isort .
  ```

- **Lint with Ruff**:
  ```bash
  ruff check .
  ```

- **Type checking with mypy**:
  ```bash
  mypy .
  ```

## Project Structure

A typical Python project layout might look like:

```
├── .venv/                     # Virtual environment (excluded from git)
├── src/                       # Package source code
│   └── your_package/
│       ├── __init__.py
│       └── ...
├── tests/                     # Test suite
├── .gitignore
├── .aider.conf.yml            # Aider configuration (if used)
├── requirements.in            *Direct dependencies*
├── requirements.txt           *Locked dependencies (generated)*
├── README.md                  *This file*
└── pyproject.toml (optional)  # Build backend and tool configuration
```

## Using tasks.py (Invoke)

For convenience, this project includes a Python task runner via Invoke. You can use:

```bash
invoke help        # List available tasks
invoke install     # Sync the virtual environment with requirements.txt
invoke dev         # Install development dependencies (editable + extras)
invoke format      # Format code with black and isort
invoke lint        # Lint with ruff
invoke test        # Run tests with pytest
invoke type-check  # Run mypy
invoke clean       # Remove temporary files and caches
```

If you don't have Invoke installed, install it with:

```bash
pip install invoke
```

Or install all development dependencies (including Invoke) with:

```bash
pip install -e .[dev]
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
