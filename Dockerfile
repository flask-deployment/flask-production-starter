# Production image for the Flask starter.
# Guide: https://flask-deployment.com/deploy/flask-plus-docker-production-setup-complete-guide
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # Containers must listen on all interfaces so Nginx can reach Gunicorn.
    GUNICORN_BIND=0.0.0.0:8000

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run as a non-root user.
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]
