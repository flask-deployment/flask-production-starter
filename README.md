# Flask Production Starter

[![CI](https://github.com/flask-deployment/flask-production-starter/actions/workflows/ci.yml/badge.svg)](https://github.com/flask-deployment/flask-production-starter/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A minimal, production-shaped Flask app wired up the way it's actually deployed:
**Gunicorn + Nginx + systemd**, plus a **Docker Compose** path. Every config
file mirrors a step-by-step guide on **[flask-deployment.com](https://flask-deployment.com)**,
so you get a working baseline here and the *why* behind each piece there.

> 📖 **Full guides:** [flask-deployment.com](https://flask-deployment.com) — deployment, fixes, optimization, and production checklists for Flask.

## What's inside

```
app/                 Application factory + environment-based config
wsgi.py              WSGI entrypoint (gunicorn wsgi:app)
gunicorn.conf.py     Gunicorn workers, timeouts, logging, graceful reload
deploy/
  flaskapp.service   systemd unit for Gunicorn
  nginx.conf         Nginx reverse proxy (static + TLS-ready) for a VPS
  flaskapp.env.example  EnvironmentFile template for systemd
docker/
  nginx.conf         Nginx config for the Compose stack (proxies to web:8000)
Dockerfile           Slim, non-root production image
docker-compose.yml   Flask (Gunicorn) behind Nginx, optional Postgres
Makefile             install / dev / run / docker-up helpers
.env.example         Local environment variables
```

Configuration follows the `FLASK_CONFIG` (environment selector) + `FLASK_DEBUG`
(debug toggle) convention — never the deprecated `FLASK_ENV`.

## Quickstart

### Local (dev server)

```bash
make install
make dev          # http://127.0.0.1:5000  (FLASK_CONFIG=development, FLASK_DEBUG=1)
```

### Local (Gunicorn, production-like)

```bash
make install
cp .env.example .env      # set a real SECRET_KEY
make run                  # gunicorn on 127.0.0.1:8000
curl -I http://127.0.0.1:8000/healthz
```

### Docker Compose (Flask + Nginx)

```bash
cp .env.example .env      # set a real SECRET_KEY
make docker-up            # http://localhost
curl -I http://localhost/healthz
```

### VPS (systemd + Nginx)

1. Deploy the code to `/var/www/flaskapp`, create a venv, install requirements.
2. Install `deploy/flaskapp.env.example` to `/etc/flaskapp/flaskapp.env` (chmod 600).
3. Install `deploy/flaskapp.service` to `/etc/systemd/system/`, then
   `sudo systemctl enable --now flaskapp`.
4. Install `deploy/nginx.conf` to `/etc/nginx/sites-available/flaskapp`, symlink
   it into `sites-enabled`, `sudo nginx -t && sudo systemctl reload nginx`.
5. Add HTTPS once HTTP works.

Full walkthrough: **[Deploy Flask on an Ubuntu VPS](https://flask-deployment.com/deploy/deploy-flask-on-ubuntu-vps-step-by-step)**.

## Each file, explained

| File | Guide |
| --- | --- |
| `app/config.py` | [Flask production config basics](https://flask-deployment.com/deploy/flask-production-config-basics) · [Config environments](https://flask-deployment.com/reference/flask-config-environments-dev-vs-staging-vs-production) |
| `gunicorn.conf.py` | [Gunicorn performance tuning](https://flask-deployment.com/optimize/flask-gunicorn-performance-tuning-guide) |
| `deploy/flaskapp.service` | [systemd + Gunicorn service setup](https://flask-deployment.com/deploy/flask-systemd-plus-gunicorn-service-setup) |
| `deploy/nginx.conf` | [Nginx + Gunicorn deploy](https://flask-deployment.com/deploy/deploy-flask-with-nginx-plus-gunicorn-step-by-step-guide) · [HTTPS with Let's Encrypt](https://flask-deployment.com/deploy/how-to-set-up-https-for-flask-nginx-plus-lets-encrypt) |
| `deploy/flaskapp.env.example` | [Environment variables & secrets](https://flask-deployment.com/deploy/flask-environment-variables-and-secrets-setup) |
| `Dockerfile` | [Flask + Docker production setup](https://flask-deployment.com/deploy/flask-plus-docker-production-setup-complete-guide) |
| `docker-compose.yml` · `docker/nginx.conf` | [Flask + Docker Compose](https://flask-deployment.com/deploy/flask-plus-docker-compose-production-setup) |
| static handling in `nginx.conf` | [Static & media files in production](https://flask-deployment.com/deploy/flask-static-and-media-files-production-setup) |
| optional Postgres in `docker-compose.yml` | [Flask + PostgreSQL production setup](https://flask-deployment.com/deploy/flask-plus-postgresql-production-setup) |

**Going live?** Run through the
[Flask production checklist](https://flask-deployment.com/checklist/flask-production-checklist-everything-you-must-do).
Hitting an error? See the [fixes](https://flask-deployment.com/fix-issues/fix-flask-502-bad-gateway-step-by-step-guide).

## License

MIT — see [LICENSE](LICENSE).
