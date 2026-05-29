# Security Policy

This is a starter template, not a hosted service. Most real-world risk comes
from how it is deployed, so review the production hardening guides at
[flask-deployment.com](https://flask-deployment.com/checklist/flask-security-checklist)
before going live.

## Using it safely

- Never commit a real `.env` or `SECRET_KEY`. Generate a strong key:
  `python -c "import secrets; print(secrets.token_hex(32))"`.
- Keep `FLASK_DEBUG=0` and `FLASK_CONFIG=production` in production.
- Serve behind HTTPS and run Gunicorn as a non-root user (the systemd unit and
  Dockerfile already do this).

## Reporting a vulnerability

Please report security issues in this template **privately** via GitHub's
[private vulnerability reporting](https://github.com/flask-deployment/flask-production-starter/security/advisories/new)
rather than opening a public issue. We aim to respond within a few days.
