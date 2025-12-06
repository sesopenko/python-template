"""
Lightweight task runner for cross-platform project automation.

This file intentionally avoids ALL external dependencies (e.g. `invoke`)
and uses only the Python standard library so it can be executed in a
fresh environment to bootstrap the project (create venv, install tools,
etc.) before any packages are installed.

Equivalent to the previous Invoke-based tasks:
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

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def _run(cmd: str) -> int:
    """Run a shell command, streaming output, and return the exit code."""
    # Use shell=True for convenience since this is a developer tool script.
    # Commands are simple and controlled (pip, pytest, etc.).
    print(f"+ {cmd}")
    return subprocess.call(cmd, shell=True)


def task_help(_: argparse.Namespace) -> int:
    """Show available commands."""
    print("Available commands:")
    print("  help          Show this help message")
    print("  install       Install production dependencies (from requirements.txt)")
    print("  dev           Install dev dependencies (from pyproject.toml optional)")
    print("  sync          Sync virtual environment with requirements.txt (pip-sync)")
    print("  format        Format code with black and isort")
    print("  lint          Lint with ruff")
    print("  test          Run pytest")
    print("  type-check    Run mypy")
    print("  clean         Remove build artifacts, caches, etc.")
    return 0


def task_install(_: argparse.Namespace) -> int:
    """Install production dependencies from requirements.txt using pip-sync."""
    return _run("pip-sync requirements.txt")


def task_dev(_: argparse.Namespace) -> int:
    """Install project in editable mode with development extras."""
    return _run("pip install -e .[dev]")


def task_sync(_: argparse.Namespace) -> int:
    """Sync virtual environment with requirements.txt using pip-sync."""
    return _run("pip-sync requirements.txt")


def task_format(_: argparse.Namespace) -> int:
    """Format code with Black and isort."""
    code = _run("black .")
    if code != 0:
        return code
    return _run("isort .")


def task_lint(_: argparse.Namespace) -> int:
    """Lint the codebase with Ruff."""
    return _run("ruff check .")


def task_test(_: argparse.Namespace) -> int:
    """Run tests with pytest."""
    return _run("pytest")


def task_type_check(_: argparse.Namespace) -> int:
    """Run static type checks with mypy."""
    return _run("mypy .")


def task_clean(_: argparse.Namespace) -> int:
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

    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lightweight task runner (no external dependencies)."
    )
    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")

    # Map command names to handler functions and help text
    commands = {
        "help": (task_help, "Show available commands"),
        "install": (task_install, "Install production dependencies"),
        "dev": (task_dev, "Install dev dependencies"),
        "sync": (task_sync, "Sync environment with requirements.txt"),
        "format": (task_format, "Format code with black and isort"),
        "lint": (task_lint, "Lint with ruff"),
        "test": (task_test, "Run tests with pytest"),
        "type-check": (task_type_check, "Run mypy"),
        "clean": (task_clean, "Remove build artifacts and caches"),
    }

    for name, (_, help_text) in commands.items():
        sp = subparsers.add_parser(name, help=help_text)
        sp.set_defaults(func=commands[name][0])

    return parser


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    parser = _build_parser()
    if not argv:
        # Default to help if no command is provided
        args = parser.parse_args(["help"])
    else:
        args = parser.parse_args(argv)

    func = getattr(args, "func", None)
    if func is None:
        parser.print_help()
        return 1

    return func(args)


if __name__ == "__main__":
    # Ensure script runs with only stdlib available.
    # Example usage:
    #   python tasks.py help
    #   python tasks.py install
    #   python tasks.py test
    sys.exit(main())
