"""Application command for TAT calculation."""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True, slots=True)
class CalculateTATCommand:
    """Request to calculate laboratory turnaround time."""

    request_id: UUID
    started_at: datetime
    completed_at: datetime
    target_minutes: int
