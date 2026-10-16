from app.app import greet, app


def test_greet():
    assert greet("DevOps") == "Hello DevOps"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from DevSecOps" in response.data
