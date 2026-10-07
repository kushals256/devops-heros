import os

os.environ["DATABASE_URL"] = "sqlite:///./test.db"

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_health(client):
    assert client.get("/health").json() == {"status": "UP"}


def test_ready(client):
    assert client.get("/ready").json() == {"status": "READY"}


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "TaskBoard API"


def test_create_list_and_stats(client):
    created = client.post(
        "/api/tasks",
        json={"title": "Deploy application", "priority": "HIGH", "assignee": "Kushal S"},
    )
    assert created.status_code == 201
    task_id = created.json()["id"]
    assert created.json()["title"] == "Deploy application"

    listed = client.get("/api/tasks")
    assert listed.status_code == 200
    assert any(item["id"] == task_id for item in listed.json())

    stats = client.get("/api/tasks/stats")
    assert stats.status_code == 200
    assert stats.json()["total"] >= 1


def test_get_update_delete_task(client):
    created = client.post("/api/tasks", json={"title": "Write tests", "assignee": "Kushal S"})
    task_id = created.json()["id"]

    fetched = client.get(f"/api/tasks/{task_id}")
    assert fetched.status_code == 200
    assert fetched.json()["status"] == "TODO"

    updated = client.put(f"/api/tasks/{task_id}", json={"status": "DONE"})
    assert updated.status_code == 200
    assert updated.json()["status"] == "DONE"

    deleted = client.delete(f"/api/tasks/{task_id}")
    assert deleted.status_code == 204
    assert client.get(f"/api/tasks/{task_id}").status_code == 404


def test_create_task_validation(client):
    response = client.post("/api/tasks", json={"title": "", "priority": "HIGH"})
    assert response.status_code == 422
