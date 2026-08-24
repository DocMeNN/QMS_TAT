"""Health API integration tests."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.interface.api.health import router


def test_health_endpoint() -> None:
    """Verify the operational health endpoint."""
    application = FastAPI()
    application.include_router(router)

    client = TestClient(application)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "version": "1.0.0",
        "ready": True,
    }
