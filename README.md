# Python Project Template

A minimal, best-practice template for Python projects with tooling for
formatting, linting, testing, type-checking, and dependency management.

> This template targets **Python 3.13 or later**. Earlier Python 3 versions
> (3.12 and below) are no longer in active support and are not supported here.

## Quick Start

1. **Create a virtual environment** (recommended inside the project):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   ```

   > For Windows and more detailed instructions, see
   > [docs/getting-started.md](docs/getting-started.md).

2. **Install `pip-tools` and `invoke`** (for dependency management and tasks):

   ```bash
   pip install pip-tools invoke
   ```

3. **Compile and install dependencies, then install the project in editable mode**:

   ```bash
   invoke install
   invoke dev
   ```

4. **Run tests to verify everything works**:

   ```bash
   invoke test
   ```

For a more detailed walkthrough of the setup process, see
[docs/getting-started.md](docs/getting-started.md).

## Project Structure

A typical Python project layout for this template looks like:

```text
├── src/                       # Package source code
│   └── your_actual_project_name/
│       ├── __init__.py
│       └── ...
├── tests/                     # Test suite
├── docs/                      # Additional documentation
├── .venv/                     # Virtual environment (excluded from git)
├── .gitignore
├── .aider.conf.yml            # Aider configuration (if used)
├── .pre-commit-config.yaml    # pre-commit hooks configuration
├── requirements.in            # Direct dependencies
├── requirements.txt           # Locked dependencies (generated)
├── tasks.py                   # Invoke tasks
├── README.md                  # This file
└── pyproject.toml             # Build backend and tool configuration
```

See [docs/project-structure.md](docs/project-structure.md) for more details.

## Continuous Integration (GitHub Actions)

This project includes a GitHub Actions workflow at `.github/workflows/ci.yml`.

The CI workflow runs on:

- All pull requests.
- Pushes to the `main` branch.

For each run, it will:

1. Set up Python 3.13.
2. Install dependencies via `invoke install`.
3. Install the project in editable mode via `invoke dev`.
4. Check formatting via `invoke format-check`.
5. Lint the code via `invoke lint`.
6. Run tests via `invoke test`.
7. Run type checks via `invoke type-check`.

If any of these steps fail, the workflow fails and the pull request will show a failing status check.  
To avoid CI failures, run the same commands locally before pushing:

```bash
invoke format
invoke format-check
invoke lint
invoke type-check
invoke test
```

If you have pre-commit hooks enabled (`invoke pre-commit`), many of these checks will also run automatically before each commit.

## Documentation

Additional documentation is available in the `docs/` directory:

- [Getting Started](docs/getting-started.md)
- [Customizing the Template](docs/customizing-template.md)
- [Development Tasks (invoke)](docs/development-tasks.md)
- [Dependency Management](docs/dependencies.md)
- [Project Structure](docs/project-structure.md)
- [Tips & Tricks](docs/tips-and-tricks.md)

## License

MIT – see [LICENSE.TXT](LICENSE.txt) for details.

## Template Attribution

This project was created from the Python template at <https://github.com/sesopenko/python-template>, created and maintained by [Sean Esopenko](https://github.com/sesopenko)
