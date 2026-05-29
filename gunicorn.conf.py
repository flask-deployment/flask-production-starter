"""Gunicorn configuration.

Tune workers, threads, and worker class to your CPU count and workload:
https://flask-deployment.com/optimize/flask-gunicorn-performance-tuning-guide
"""
import multiprocessing
import os

# Loopback bind for the systemd + Nginx setup. The Docker image overrides this
# to 0.0.0.0:8000 (see Dockerfile) so the container is reachable from Nginx.
bind = os.environ.get("GUNICORN_BIND", "127.0.0.1:8000")

workers = int(os.environ.get("WEB_CONCURRENCY", multiprocessing.cpu_count() * 2 + 1))
worker_class = os.environ.get("GUNICORN_WORKER_CLASS", "sync")
threads = int(os.environ.get("GUNICORN_THREADS", "1"))

timeout = int(os.environ.get("GUNICORN_TIMEOUT", "30"))
graceful_timeout = 30
keepalive = 5

# Recycle workers periodically to bound memory growth from leaks.
max_requests = 1000
max_requests_jitter = 100

# Log to stdout/stderr so journald or Docker captures the output.
accesslog = "-"
errorlog = "-"
loglevel = os.environ.get("GUNICORN_LOG_LEVEL", "info")
