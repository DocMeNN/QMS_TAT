"""Operational health and readiness models."""

from dataclasses import dataclass


@dataclass(frozen=True)
class HealthStatus:
    """Represent operational health state."""

    status: str
    version: str
    ready: bool
