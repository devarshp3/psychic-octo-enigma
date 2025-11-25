# psychic-octo-enigma — sample Python calculator

This repository contains a small example Python package `psychic_calculator` and unit tests.

Quickstart (local):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-dev.txt
python -m pytest -q
```

Package layout:

- `src/psychic_calculator/` — package code
- `tests/` — pytest tests

If you want a different package name, Python version, or to use Poetry instead of requirements, tell me and I'll update the scaffold.

## Development: pre-commit & formatting

To ensure a consistent code style and catch issues before pushing, we use `pre-commit` hooks (black, isort, ruff).

Local setup:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements-dev.txt

# Install git hooks (run once per clone)
pre-commit install

# Format and lint all files now (safe to run before committing)
pre-commit run --all-files

# Run tests
PYTHONPATH=src python -m pytest -q
```

CI runs formatting and lint checks (`black --check`, `isort --check-only`, `ruff check .`), then `mypy src` and the test suite.

If you prefer to run the package in editable mode instead of using `PYTHONPATH`, run:

```bash
pip install -e .
python -m pytest -q
```
# psychic-octo-enigma
