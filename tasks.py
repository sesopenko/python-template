"""
Invoke task runner for cross-platform project automation.

Equivalent to the previous Makefile targets:
- help
- install
- dev
- sync
- format
- lint
- test
- type-check
- clean
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import Callable

from invoke import Context, Result, task


def _run(c: Context, cmd: str) -> Result | None:
    """Run a command with a PTY on POSIX for nicer output; fail fast on errors."""
    # invoke's c.run will raise UnexpectedExit on non-zero status by default,
    # which causes the task (and thus pre-commit/CI) to exit non-zero.
    return c.run(cmd, pty=os.name != "nt", warn=False)


@task
def help(c: Context) -> None:  # noqa: ARG001 - required by invoke
    """Show available commands."""
    print("Available commands:")
    print("  install       Install production dependencies (from requirements.txt)")
    print("  dev           Install project in editable mode")
    print("  sync          Sync virtual environment with requirements.txt (pip-sync)")
    print("  compile       Compile requirements.txt from requirements.in (pip-compile)")
    print("  upgrade       Upgrade all dependencies (pip-compile --upgrade + pip-sync)")
    print("  format        Format code with black and isort")
    print("  format-check  Check formatting with black --check and ruff format --check")
    print("  lint          Lint with ruff")
    print("  test          Run pytest")
    print("  type-check    Run mypy")
    print("  clean         Remove build artifacts, caches, etc.")
    print("  pre-commit    Install pre-commit git hooks")


@task
def install(c: Context) -> None:
    """Install production and development dependencies from requirements.txt using pip-sync."""
    _run(c, "pip-sync requirements.txt")


@task
def dev(c: Context) -> None:
    """Install project in editable mode."""
    _run(c, "pip install -e .")


@task
def sync(c: Context) -> None:
    """Sync virtual environment with requirements.txt using pip-sync."""
    _run(c, "pip-sync requirements.txt")


@task
def compile(c: Context) -> None:
    """Compile requirements.txt from requirements.in using pip-compile."""
    _run(c, "pip-compile requirements.in")


@task
def upgrade(c: Context) -> None:
    """Upgrade all dependencies to their latest allowed versions and sync."""
    _run(c, "pip-compile --upgrade requirements.in")
    _run(c, "pip-sync requirements.txt")


@task(name="format")
def format_(c: Context) -> None:
    """Format code with Black and isort."""
    _run(c, "black .")
    _run(c, "isort .")


@task(name="format-check")
def format_check(c: Context) -> None:
    """Check formatting with Black and Ruff without modifying files."""
    _run(c, "black --check .")
    _run(c, "ruff format --check .")


@task
def lint(c: Context) -> None:
    """Lint the codebase with Ruff."""
    _run(c, "ruff check .")


@task
def test(c: Context) -> None:
    """Run tests with pytest."""
    _run(c, "pytest")


@task(name="type-check")
def type_check(c: Context) -> None:
    """Run static type checks with mypy."""
    _run(c, "mypy .")


@task
def clean(c: Context) -> None:  # noqa: ARG001 - required by invoke
    """Remove build artifacts, caches, and coverage files in a cross-platform way."""
    root = Path(".")

    # Top-level files/directories to remove (non-recursive patterns)
    patterns = [
        "build",
        "dist",
        "*.egg-info",
        ".pytest_cache",
        ".ruff_cache",
        ".mypy_cache",
        "htmlcov",
    ]

    def _remove_path(p: Path) -> None:
        try:
            if p.is_symlink() or p.is_file():
                p.unlink()
            elif p.is_dir():
                shutil.rmtree(p, ignore_errors=True)
        except FileNotFoundError:
            pass

    # Remove top-level patterns
    for pattern in patterns:
        for p in root.glob(pattern):
            _remove_path(p)

    # Remove the coverage database file at repo root, if present
    _remove_path(root / ".coverage")

    # Remove all __pycache__ directories recursively
    for p in root.rglob("__pycache__"):
        _remove_path(p)


@task(name="pre-commit")
def pre_commit(c: Context) -> None:
    """Install pre-commit git hooks."""
    _run(c, "pre-commit install")
