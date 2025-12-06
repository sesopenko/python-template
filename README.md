# Python Project Template

A minimal, best-practice template for Python projects with tooling for
formatting, linting, testing, type-checking, and dependency management.

> This template targets **Python 3.13 or later**. Earlier Python 3 versions
> (3.12 and below) are no longer in active support and are not supported here.

## Quick Start

1. **Create a virtual environment** (recommended inside the project):

   ```bash
   python -m venv .venv
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
   invoke compile
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

## Documentation

Additional documentation is available in the `docs/` directory:

- [Getting Started](docs/getting-started.md)
- [Customizing the Template](docs/customizing-template.md)
- [Development Tasks (invoke)](docs/development-tasks.md)
- [Dependency Management](docs/dependencies.md)
- [Project Structure](docs/project-structure.md)
- [Tips & Tricks](docs/tips-and-tricks.md)

## License

MIT – see `LICENSE` for details.
