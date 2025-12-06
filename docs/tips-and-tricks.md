# Tips & Tricks

This document collects additional tips and optional enhancements for working with this template.

## Using `uv` for faster dependency management

[`uv`](https://github.com/astral-sh/uv) is a fast Python package manager that can act as a drop-in replacement for `pip-compile` and `pip-sync`.

If you install `uv`, you can:

- Replace `pip-compile` with `uv pip compile`.
- Replace `pip-sync` with `uv pip sync`.

Example:

```bash
uv pip compile requirements.in -o requirements.txt
uv pip sync requirements.txt
```

You can update `tasks.py` to call these commands instead of the `pip-tools` equivalents if you prefer.

## IDE integration

Some general tips for IDEs/editors:

- Point your IDE’s Python interpreter to the `.venv` environment.
- Configure format-on-save with Black and import sorting with isort, or rely on `invoke format`.
- Enable mypy and Ruff integrations if your IDE supports them, or run them via `invoke type-check` and `invoke lint`.

## Continuous Integration (CI)

When setting up CI (e.g., GitHub Actions, GitLab CI, etc.), a typical workflow might:

1. Check out the code.
2. Set up Python and a virtual environment.
3. Install `pip-tools` and `invoke`.
4. Run:

   ```bash
   invoke compile
   invoke install
   invoke dev
   invoke format
   invoke lint
   invoke type-check
   invoke test
   ```

You can adjust which steps are required for your project (for example, you might skip `invoke format` in CI and only run it locally).

## Keeping the environment clean

- Use `invoke clean` to remove build artifacts, caches, and coverage files.
- Periodically run `invoke upgrade` to keep dependencies up to date, especially for development tools.

## Further customization

As your project grows, you might:

- Add more Invoke tasks (e.g., `invoke docs`, `invoke release`).
- Introduce additional configuration files (e.g., for Sphinx or MkDocs).
- Split tests into subdirectories under `tests/` to mirror complex package structures.

This template is intentionally minimal but is designed to be extended as your needs evolve.
