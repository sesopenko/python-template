.PHONY: help install dev install-dev sync format lint test type-check clean

help:
	@echo "Available commands:"
	@echo "  install       Install production dependencies (from requirements.txt)"
	@echo "  dev           Install dev dependencies (from pyproject.toml optional)"
	@echo "  sync          Sync virtual environment with requirements.txt (pip-sync)"
	@echo "  format        Format code with black and isort"
	@echo "  lint          Lint with ruff"
	@echo "  test          Run pytest"
	@echo "  type-check    Run mypy"
	@echo "  clean         Remove build artifacts, caches, etc."

install:
	pip-sync requirements.txt

dev:
	pip install -e .[dev]

sync:
	pip-sync requirements.txt

format:
	black .
	isort .

lint:
	ruff check .

test:
	pytest

type-check:
	mypy .

clean:
	rm -rf build dist *.egg-info .pytest_cache .ruff_cache .mypy_cache .coverage htmlcov
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
