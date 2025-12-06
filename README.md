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
│   └── your_package/
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
