"""Observability service."""

from app.observability.health import HealthStatus


class ObservabilityService:
    """Provide operational health information."""

    def __init__(self, version: str = "1.0.0") -> None:
        self._version = version

    def health(self) -> HealthStatus:
        """Return the current service health."""
        return HealthStatus(
            status="healthy",
            version=self._version,
            ready=True,
        )
