# DevPulse

**AI-powered engineering intelligence for GitHub repositories.**

DevPulse is an open-source project in its early development stage. Its goal is to help engineering teams understand repository activity, review pull requests, and surface actionable insights by combining GitHub data, deterministic analysis, and AI-assisted workflows.

> **Project status:** Initial setup. The features described below are planned and are not available yet.

## Planned capabilities

- Connect GitHub repositories and ingest repository events through webhooks.
- Analyze pull requests asynchronously and produce structured code review findings.
- Track repository activity and engineering health metrics.
- Search repository source code and documentation using retrieval-augmented generation (RAG).
- Generate periodic engineering reports from repository activity and analysis results.
- Deliver notifications through integrations such as email or Telegram.

AI-generated findings are intended to support developer decision-making. They should include relevant context and remain reviewable by a human.

## Architecture and technology

The project is planned as a **modular monolith**. This keeps domain boundaries clear while avoiding the operational overhead of microservices during early development.

The initial backend is planned around:

- Python 3.14
- FastAPI and Pydantic
- SQLAlchemy 2.x and PostgreSQL
- Alembic for database migrations
- Redis and Celery for background processing
- HTTPX for asynchronous HTTP clients
- `uv` for Python project and dependency management
- Ruff, mypy, and pytest for code quality and testing
- Docker Compose for local infrastructure

AI, vector search, and observability integrations are planned for later phases. The exact versions and scope will be documented as they are adopted.

## Development roadmap

1. **Foundation:** project tooling, API skeleton, database, migrations, and authentication.
2. **GitHub integration:** repository management, GitHub API client, and verified webhooks.
3. **Asynchronous processing:** background jobs, retries, idempotency, caching, and rate limiting.
4. **AI-assisted analysis:** structured pull request reviews and usage tracking.
5. **Repository search and reports:** embeddings, PostgreSQL vector search, RAG, and engineering reports.
6. **Production readiness:** automated tests, CI, deployment documentation, and observability.

This roadmap is a direction, not a delivery commitment. Features will be marked complete as they are implemented and verified.

## Getting started

The project is being initialized. Setup instructions will be added when the first runnable application is available.

## Contributing

Contributions and feedback will be welcome as the project takes shape. Contribution guidelines, development setup, and code of conduct will be published before the project opens for external contributions.

## License

No license has been selected yet. Until a license file is added, all rights are reserved by the copyright holder.
