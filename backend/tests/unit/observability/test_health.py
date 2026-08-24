"""Observability unit tests."""

from app.observability.health import HealthStatus
from app.observability.service import ObservabilityService


def test_health_status_contract() -> None:
    """Verify operational health information."""
    result = ObservabilityService(version="1.0.0").health()

    assert isinstance(result, HealthStatus)
    assert result.status == "healthy"
    assert result.version == "1.0.0"
    assert result.ready is True


def test_default_version() -> None:
    """Verify the default application version."""
    result = ObservabilityService().health()

    assert result.version == "1.0.0"
