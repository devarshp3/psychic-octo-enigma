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

## CLI

After installing the package (editable or normal) the project exposes a small CLI `psychic-calculator`:

Examples:

```bash
# using the installed CLI (after `pip install -e .`)
psychic-calculator add 1 2
psychic-calculator div 6 3

# or run the module directly
python -m psychic_calculator.cli add 1 2
```

## Deploy to Azure App Service

This repository includes a small FastAPI web app in `app/main.py` that exposes the calculator as HTTP endpoints.

1. Create an Azure App Service (Linux) and a Resource Group (choose Python 3.12 runtime if available).
2. In the Azure portal, open your Web App -> Get publish profile -> Download. Copy the contents.
3. In your GitHub repository, go to Settings → Secrets → Actions and add two secrets:
	- `AZURE_WEBAPP_NAME`: the App Service name
	- `AZURE_WEBAPP_PUBLISH_PROFILE`: the contents of the publish profile XML file
4. Push to `main`. The workflow `.github/workflows/azure-deploy.yml` will run tests and deploy automatically.

Recommended startup command (if needed in App Service configuration):
```
gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:{PORT:-8000}
```

Note: Azure App Service may restrict supported Python versions; if 3.12 isn't available, pick a supported runtime (e.g., 3.11) and update the workflow and package settings accordingly.
# psychic-octo-enigma
