<!--
This file is generated/updated by an AI assistant. Please review and adjust any
project-specific commands or policies to match human expectations.
-->
# Copilot / AI Agent Instructions

**Purpose:** Provide concise, actionable guidance so an AI coding agent can become productive in this repository immediately. The repository currently has no application code; these instructions include a Python-focused scaffold and conventions to follow when creating a Python project here.

**Repository snapshot (discoverable):**
- **Name:** `psychic-octo-enigma`
- **Default branch:** `main` (current branch: `main`)
- **Top-level files:** `README.md` (currently only a title)
- **Dev container:** Ubuntu 24.04.3 LTS
- **Default shell:** `bash`

**Immediate facts an agent can rely on**
- No existing source code, CI config, or language manifests were found.

**Primary goals for the agent (order of priority)**
1. Confirm the user's intent for this repository (language, framework, app vs library).
2. When asked, scaffold a minimal, opinionated Python project (see Python guidance below).
3. Propose options (Node/Go/Python) rather than making high-level design choices without approval.

**How to explore this repo**
- Inspect `README.md` and the repo root to confirm missing content.
- Search for language manifests: `package.json`, `pyproject.toml`, `Pipfile`, `requirements.txt`, `go.mod`, `Cargo.toml`.

**When modifying the repository**
- Make minimal, incremental changes grouped by purpose (scaffold, CI, docs).
- Add a short `README.md` quickstart showing exact commands to set up and run tests.
- Place CI workflows under `.github/workflows/` and include what triggers them (push, PR to `main`, tags).

**Commit & PR guidance**
- Use conventional, short commit messages: `feat: scaffold python`, `chore: add ci`, `fix: tests`.
- PR descriptions must state how to run the project, test commands, and any open questions for maintainers.

**Python-specific guidance**
- Target Python >= 3.12 (confirm if you prefer 3.13+). Use a `pyproject.toml` (PEP 621) as the single source of project metadata.
- Recommended layout:
	- `pyproject.toml` (build system, dependencies, dev-deps)
	- `src/<package_name>/` (application code)
	- `tests/` (pytest test modules)
	- `README.md`, `LICENSE`, `.github/`, `.pre-commit-config.yaml`
- Development tooling (suggested): `pytest`, `mypy`, `black`, `isort`, `ruff` or `flake8`, `pre-commit`.
- Example dev commands:
	- Create venv: `python -m venv .venv`
	- Activate: `source .venv/bin/activate`
	- Install deps: `pip install -U pip` then `pip install -r requirements-dev.txt` or use Poetry/Poetry-compatible `pyproject.toml`.
	- Run tests: `python -m pytest -q`
	- Format: `black . && isort .`
	- Type check: `mypy src tests`
	- Lint: `ruff check .` or `flake8 src tests`

**Python naming & style conventions (project-specific)**
- Modules/packages: lowercase with underscores as needed (e.g., `src/my_package/`).
- Functions & variables: `snake_case`.
- Classes: `PascalCase`.
- Constants: `UPPER_SNAKE_CASE`.
- Tests: files named `tests/test_*.py`, test functions `test_<behavior>()`.

**Unit test best practices (pytest-focused)**
- Prefer small, focused tests with clear names (Arrange-Act-Assert).
- Use fixtures in `tests/conftest.py` for reusable test setup.
- Use `pytest.mark.parametrize` for data-driven cases.
- Use `tmp_path` and `monkeypatch` for filesystem and env isolation.
- Keep tests fast and deterministic; prefer mocks for external services.

**CI and workflows**
- Suggest a GitHub Actions workflow `python-package.yml` using `ubuntu-latest` and `actions/setup-python` with `python-version: '3.12'` (or user-preferred version). Steps: checkout, set up venv, install deps, run `black --check`, `ruff`, `mypy`, `pytest --maxfail=1 --disable-warnings -q`.

**Examples & snippets to include when scaffolding**
- Minimal `pyproject.toml` snippet (PEP 621) and a `tests/test_sample.py` demonstrating pytest, fixtures, and assertions.
- A `Makefile` or `scripts/` dir with common commands (`make test`, `make lint`, `make format`) is helpful for maintainers.

**Safety & scope**
- Do not add secrets, credentials, or external API keys. Ask before integrating external services.

**When you can't proceed**
- Report precisely what's missing (e.g., package name, preferred Python version, CI preferences) and provide 2–3 scaffold options.

**Next steps (recommended minimal workflow for humans/agents)**
1. Ask the user: which language and Python version should we target?
2. Offer 2 scaffolding options (minimal `pyproject.toml` + `src/` layout, or Poetry-managed project) and list files to be created.
3. After approval, implement the chosen scaffold, update `README.md` with run/test commands, add CI workflow, and open a PR.

---
If you want, I can now scaffold a Python project with `src/` layout, `pyproject.toml`, `tests/`, dev tooling, and a GitHub Actions workflow—tell me which Python version and whether to use Poetry or pip + requirements.
 
**Strict Python conventions, coding standards & test patterns**

These are the concrete, repository-level standards an AI agent should follow when creating or editing Python code here. Keep changes minimal and explicit; prefer fixing root causes over band-aid edits.

- **Python Version:** Target Python >= 3.12. Use `from __future__ import annotations` for forward-compatible typing.
- **Project layout:** Use `pyproject.toml` (PEP 621) and the `src/` layout: `src/<package_name>/` for code and `tests/` for tests.
- **Naming conventions:**
	- Packages/modules: `lowercase_with_underscores` (e.g., `src/my_package/utils.py`).
	- Classes: `PascalCase` (e.g., `DataProcessor`).
	- Functions/variables: `snake_case`.
	- Constants: `UPPER_SNAKE_CASE`.
	- Private members: single leading underscore (e.g., `_helper`).

- **Typing & docstrings:**
	- Add type hints to public functions and methods. Prefer explicit signatures over `Any` where feasible.
	- Use the `typing` module and `from __future__ import annotations`.
	- Run `mypy` in CI for new code; aim for `--strict` checks progressively.
	- Write concise docstrings (one-line summary + 1–2 sentence description). Prefer Google-style or NumPy-style consistently across the repo.

- **Formatting & linting:**
	- Use `black` for formatting, `isort` for imports, and `ruff` (or `flake8`) for linting. Enforce via `pre-commit`.
	- Keep line lengths at 88 (black default) unless the user requests otherwise.

- **Logging & prints:**
	- Use `logging.getLogger(__name__)` and structured logs where useful. Avoid `print()` in library code.

- **Error handling:**
	- Catch specific exceptions (no bare `except:`). Attach context when re-raising using `raise ... from ...`.
	- Use small, descriptive custom exception classes for domain errors.

- **Unit tests (pytest-focused):**
	- Test files: `tests/test_*.py`. Test functions: `test_<behavior>()`.
	- Prefer small, focused tests and follow Arrange-Act-Assert structure.
	- Use `tests/conftest.py` for fixtures. Name fixtures clearly (e.g., `db_session`, `temp_dir`).
	- Use `pytest.mark.parametrize` for table-driven tests and `tmp_path` and `monkeypatch` for isolation.
	- Mock external services (HTTP, DB) in unit tests; reserve integration tests for separate workflows with markers (e.g., `@pytest.mark.integration`).

- **Test assertions & patterns:**
	- Use plain `assert` for assertions. Use `with pytest.raises(...)` for exception assertions and inspect messages when needed.

- **CI expectations:**
	- CI should run: `black --check`, `isort --check-only`, `ruff`, `mypy`, and `pytest --maxfail=1 -q`.
	- Keep CI logs concise and include steps to reproduce locally in PR descriptions.

- **Security & secrets:**
	- Never commit secrets. Use environment variables and documented secrets/config placeholders. Ask before adding external integrations.

If you'd like, I can scaffold a minimal Python project that follows these rules (create `pyproject.toml`, `src/<pkg>/__init__.py`, `tests/test_sample.py`, `.github/workflows/python-package.yml`, and a `README.md`). Tell me the package name and whether to use Poetry or pip + requirements, and I'll implement it.
