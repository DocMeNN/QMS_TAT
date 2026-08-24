"""FastAPI integration tests."""

from datetime import datetime, timezone
from uuid import uuid4

from fastapi.testclient import TestClient

from app.interface.api.application import app

client = TestClient(app)


def test_health_endpoint() -> None:
    """Verify the API health endpoint."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_calculate_tat_endpoint() -> None:
    """Verify HTTP request reaches the application boundary."""
    response = client.post(
        "/tat/calculate",
        json={
            "request_id": str(uuid4()),
            "started_at": datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc).isoformat(),
            "completed_at": datetime(
                2026, 8, 23, 10, 0, tzinfo=timezone.utc
            ).isoformat(),
            "target_minutes": 240,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["duration_minutes"] == 120
    assert body["target_minutes"] == 240
    assert body["status"] == "within_target"


def test_calculate_tat_rejects_invalid_target() -> None:
    """Verify HTTP validation remains at the interface boundary."""
    response = client.post(
        "/tat/calculate",
        json={
            "request_id": str(uuid4()),
            "started_at": datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc).isoformat(),
            "completed_at": datetime(
                2026, 8, 23, 9, 0, tzinfo=timezone.utc
            ).isoformat(),
            "target_minutes": 0,
        },
    )

    assert response.status_code == 422
