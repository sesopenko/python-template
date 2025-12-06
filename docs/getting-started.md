# Getting Started

This guide walks you through setting up a development environment for this template and verifying that everything works.

> This project requires **Python 3.13 or later**. Earlier Python 3 versions
> (3.12 and below) are no longer in active support and are not supported.

## 1. Create a virtual environment

It is recommended to create a virtual environment inside the project directory:

```bash
python -m venv .venv
```

### Activate the virtual environment

- On **Linux/macOS**:

  ```bash
  source .venv/bin/activate
  ```

- On **Windows (PowerShell)**:

  ```powershell
  .venv\Scripts\Activate.ps1
  ```

- On **Windows (Command Prompt)**:

  ```cmd
  .venv\Scripts\activate.bat
  ```

Once activated, the `python` and `pip` commands will refer to the environment inside `.venv`.

## 2. Install core tools

Install `pip-tools` and `invoke`, which are used for dependency management and common development tasks:

```bash
pip install pip-tools invoke
```

If you plan to use the pre-commit framework (recommended), also install `pre-commit`:

```bash
pip install pre-commit
```

> After this initial setup (creating/activating `.venv` and installing `pip-tools` and `invoke`),
> all project-specific commands should be exposed as `invoke` tasks rather than ad-hoc shell
> commands. This keeps the workflow consistent and makes it easy to change commands in one
> place (`tasks.py`) instead of updating multiple docs and scripts.

## 3. Compile and install dependencies

Dependencies are declared in `requirements.in` and compiled into a fully pinned `requirements.txt`.

1. **Compile `requirements.txt` from `requirements.in`:**

   ```bash
   invoke compile
   ```

   This generates (or updates) a locked `requirements.txt` with all transitive dependencies pinned.

2. **Install the exact dependencies:**

   ```bash
   invoke install
   ```

   This uses `pip-sync` under the hood to ensure your virtual environment matches the lock file exactly, removing any extra packages.

## 4. Install the project in editable mode

Install your project in editable mode so local changes are immediately reflected without reinstalling:

```bash
invoke dev
```

If you later run `invoke sync` or `invoke upgrade` (both use `pip-sync`), you should re-run `invoke dev` afterward, because `pip-sync` removes anything not listed in `requirements.txt`.

## 5. Enable pre-commit hooks (optional but recommended)

To automatically run formatting, linting, type checks, and tests before each commit, enable the pre-commit hooks defined in `.pre-commit-config.yaml`:

```bash
invoke pre-commit
```

You can also run all hooks manually on the entire codebase:

```bash
pre-commit run --all-files
```

## 6. Verify the setup

Run the test suite to confirm everything is working:

```bash
invoke test
```

You should see pytest discover and run the tests under `tests/`.

## 7. Next steps

Once your environment is set up:

- Learn how to customize this template for your own project in
  [customizing-template.md](customizing-template.md).
- Explore the available development tasks in
  [development-tasks.md](development-tasks.md).
- Read more about dependency management in
  [dependencies.md](dependencies.md).
