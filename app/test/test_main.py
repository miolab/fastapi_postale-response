from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_post_status_dummy_ping():
    response = client.post(
        "/",
        json={"status": "ping"},
    )
    assert response.status_code == 200
    assert response.json() == {"status": "pong"}


def test_post_status_dummy_ok():
    response = client.post(
        "/",
        json={"status": "ok"},
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_post_status_dummy_return():
    response = client.post(
        "/",
        json={"status": "ko"},
    )
    assert response.status_code == 200
    assert response.json() == {"status": "error"}


def test_get_root():
    response = client.get(
        "/"
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, this is GET root."}
