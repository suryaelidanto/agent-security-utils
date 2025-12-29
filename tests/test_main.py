from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_fuzzy_match():
    payload = {"input_text": "Apple Inc.", "target_text": "Apple"}
    response = client.post("/fuzzy-match", json=payload)
    assert response.status_code == 200
    assert response.json()["score"] > 80
    assert response.json()["input"] == "Apple Inc."
