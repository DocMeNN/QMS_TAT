"""Application result DTOs."""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.domain.tat.measurement import TATStatus


@dataclass(frozen=True, slots=True)
class TATCalculationResult:
    """Application-level representation of a TAT calculation."""

    request_id: UUID
    started_at: datetime
    completed_at: datetime
    duration_minutes: int
    target_minutes: int
    status: TATStatus
