# Contributing Guide

Thank you for your interest in contributing!  
This document provides **project-agnostic guidance** for collaborating on a Python codebase.  
It is intentionally generic so it can be included by tools like **aider** for automated context.

---

## 📌 Project Philosophy

- Keep the codebase **clean, modular, and maintainable**.
- Prefer **clarity over cleverness**.
- Follow **established Python standards** so the project remains approachable.
- All contributions should improve **readability**, **testability**, or **reliability**.

---

## 🧱 Repository Structure Expectations

While each project may evolve differently, contributors should generally expect:

- A top-level Python package containing source code.
- A `tests/` directory mirroring the package structure.
- Documentation inside a `docs/` folder or in root files like `README.md`.
- Tooling and configuration files such as:
  - `pyproject.toml`
  - linters/formatters (e.g., Ruff, Black, isort)
  - type checking (e.g., mypy or pyright)

If you add or reorganize files, ensure the layout stays intuitive and consistent.

---

## ✨ Coding Standards

- Follow **PEP 8** and **PEP 257**.
- Use **type hints** throughout new code.
- Prefer **pure functions**, **small modules**, and **single-purpose classes**.
- Write **docstrings** for all public functions, methods, classes, and modules.
- Avoid unnecessary dependencies; be mindful of project footprint.

---

## 🧪 Testing

- All new functionality must include tests.
- Tests should be **deterministic**, **fast**, and **isolated**.
- Use **pytest** conventions unless the project specifies otherwise.
- When fixing a bug, add a test that fails before the fix and passes afterward.

---

## 🧹 Tooling & Automation

If the project includes automatic tooling (linters, formatters, type checkers):

1. Run them before committing.
2. Do not disable rules unless there is a strong justification.
3. Ensure CI passes before opening a pull request.

---

## 📚 Documentation

- Update relevant docs whenever behavior or APIs change.
- Keep `README.md` accurate for end users.
- Include examples that demonstrate correct usage.
- Maintain a consistent tone: clear, concise, and useful.

---

## 🔀 Branching & Pull Requests

- Create feature branches using descriptive names.
- Keep PRs **focused**: small, single-purpose changes are easier to review.
- Include:
  - A summary of the change
  - Rationale and any tradeoffs considered
  - Notes on testing performed
- Be open to feedback; code review is collaborative.

---

## 💬 Working with aider

If aider is being used for development:

- Add or modify files through structured commands rather than ad hoc edits.
- Provide aider with **accurate context** and keep conversations focused.
- When asking aider to edit files, reference them explicitly and be specific.
- Avoid embedding project-specific assumptions in this file; it must remain reusable.

---

## 🤝 Code of Conduct

Be respectful, constructive, and considerate.  
Assume good intentions and help maintain a positive environment for all contributors.

---

Thank you for helping improve this project!
