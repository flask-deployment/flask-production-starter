from flask import Blueprint, current_app, jsonify

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return f"Flask production starter is running ({current_app.config.get('ENV_NAME')})."


@bp.route("/healthz")
def healthz():
    """Lightweight health check for load balancers and uptime monitors."""
    return jsonify(status="ok"), 200
