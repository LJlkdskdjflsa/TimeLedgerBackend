from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"msg": "pong"}
