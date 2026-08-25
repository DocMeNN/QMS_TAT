"""Health API endpoint."""

from app.observability.service import ObservabilityService
from fastapi import APIRouter

router = APIRouter(tags=["health"])

_service = ObservabilityService()


@router.get("/health")
def health() -> dict[str, object]:
    """Return operational health information."""
    result = _service.health()

    return {
        "status": result.status,
        "version": result.version,
        "ready": result.ready,
    }
