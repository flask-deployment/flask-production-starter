.PHONY: help install dev run docker-up docker-down

help:
	@echo "make install      Create .venv and install dependencies"
	@echo "make dev          Run the Flask dev server (FLASK_DEBUG=1)"
	@echo "make run          Run Gunicorn locally with gunicorn.conf.py"
	@echo "make docker-up    Build and start the Docker Compose stack"
	@echo "make docker-down  Stop the Docker Compose stack"

install:
	python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

dev:
	FLASK_CONFIG=development FLASK_DEBUG=1 .venv/bin/flask --app wsgi run --debug

run:
	.venv/bin/gunicorn --config gunicorn.conf.py wsgi:app

docker-up:
	docker compose up --build -d

docker-down:
	docker compose down
