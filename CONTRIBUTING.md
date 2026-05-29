# Contributing

Thanks for your interest! This repo is a deliberately small, opinionated
deployment baseline that mirrors the guides on
[flask-deployment.com](https://flask-deployment.com). Improvements that keep it
minimal and production-honest are welcome.

## Development setup

```bash
make install                       # creates .venv with runtime deps
pip install -r requirements-dev.txt  # adds pytest + ruff
make test                          # run the tests
make lint                          # run ruff
```

## Guidelines

- Keep it minimal — this is a starter, not a framework. New runtime
  dependencies need a clear justification.
- If you change a config file, keep it consistent with the matching guide on
  the site (and update the guide link if the topic moves).
- Run `make lint` and `make test` before opening a PR; CI runs both plus a
  Docker image build.

## Reporting issues

Use GitHub issues for bugs and suggestions. For security reports, see
[SECURITY.md](SECURITY.md).
