import os

from flask import Flask

from .config import CONFIG_MAP


def create_app(config_name=None):
    """Application factory.

    The active configuration is selected with the ``FLASK_CONFIG`` environment
    variable (``development`` | ``production`` | ``testing``), defaulting to
    ``production``. ``FLASK_DEBUG`` toggles debug mode and is handled by Flask.

    Guide: https://flask-deployment.com/reference/flask-config-environments-dev-vs-staging-vs-production
    """
    config_name = config_name or os.environ.get("FLASK_CONFIG", "production")
    app = Flask(__name__)
    app.config.from_object(CONFIG_MAP.get(config_name, CONFIG_MAP["production"]))

    from .routes import bp

    app.register_blueprint(bp)

    return app
