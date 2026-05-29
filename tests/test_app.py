from app import create_app


def test_index_ok():
    app = create_app("testing")
    resp = app.test_client().get("/")
    assert resp.status_code == 200
    assert "running" in resp.get_data(as_text=True)


def test_healthz_ok():
    app = create_app("testing")
    resp = app.test_client().get("/healthz")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_config_selection():
    assert create_app("production").config["ENV_NAME"] == "production"
    assert create_app("development").config["ENV_NAME"] == "development"
    # Unknown names fall back to the production config.
    assert create_app("bogus").config["ENV_NAME"] == "production"
