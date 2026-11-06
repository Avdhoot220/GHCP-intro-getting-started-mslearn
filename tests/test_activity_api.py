from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_unregister_participant_removes_email():
    original = activities["Chess Club"]["participants"][:]
    try:
        response = client.delete(
            "/activities/Chess Club/unregister",
            params={"email": "daniel@mergington.edu"},
        )

        assert response.status_code == 200
        assert "daniel@mergington.edu" not in activities["Chess Club"]["participants"]
        assert response.json()["message"] == "Unregistered daniel@mergington.edu from Chess Club"
    finally:
        activities["Chess Club"]["participants"] = original
