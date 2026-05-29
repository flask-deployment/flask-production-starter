"""Environment-specific configuration.

Keep structure in these classes and inject secrets through environment
variables. ``FLASK_CONFIG`` selects the class; ``FLASK_DEBUG`` (read by Flask
itself) toggles debug mode — never enable it in production.

Guide: https://flask-deployment.com/deploy/flask-production-config-basics
"""
import os


class BaseConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-me")

    # Wire up a database by setting DATABASE_URL. See:
    # https://flask-deployment.com/deploy/flask-plus-postgresql-production-setup
    DATABASE_URL = os.environ.get("DATABASE_URL")


class DevelopmentConfig(BaseConfig):
    ENV_NAME = "development"


class ProductionConfig(BaseConfig):
    ENV_NAME = "production"
    # Secure cookies assume HTTPS termination at Nginx. See:
    # https://flask-deployment.com/deploy/how-to-set-up-https-for-flask-nginx-plus-lets-encrypt
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PREFERRED_URL_SCHEME = "https"


class TestingConfig(BaseConfig):
    ENV_NAME = "testing"
    TESTING = True


CONFIG_MAP = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
