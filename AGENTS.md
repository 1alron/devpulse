# Agent and Contributor Guide

## Project

DevPulse is an early-stage Python backend project for GitHub repository
engineering insights. The project follows a modular-monolith direction.

Only describe features as implemented when they exist in the codebase. The
roadmap in `README.md` is aspirational.

## Stack and project structure

- Python 3.12
- FastAPI
- `uv` for dependency management, lockfile, and virtual environment
- Ruff for linting and formatting
- mypy for static type checking
- pytest for tests
- Application package: `src/devpulse/`
- Tests: `tests/`

Keep application code under `src/devpulse/`. Add runtime dependencies with
`uv add <package>` and development dependencies with `uv add --dev <package>`.
Do not edit `uv.lock` manually.

## Development commands

Run these commands from the repository root:

```bash
uv sync
uv run uvicorn devpulse.main:app --app-dir src --reload
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy src/devpulse
```

Use `uv run` so commands run in the project environment.

## Change guidelines

- Keep changes focused and consistent with the modular-monolith direction.
- Add or update tests when behavior changes.
- Do not commit secrets or local `.env` files. Use `.env.example` for
  placeholder configuration.
- Do not add infrastructure or dependencies before they are needed.
- Use Conventional Commit messages, for example:
  `feat: add repository endpoint`,
  `fix: handle missing repository`,
  `docs: clarify local setup`,
  `test: cover health endpoint`,
  `chore: configure tooling`.
- Do not commit or push unless explicitly asked.
