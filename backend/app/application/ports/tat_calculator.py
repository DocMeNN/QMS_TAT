"""Application ports for TAT operations."""

from datetime import datetime
from typing import Protocol
from uuid import UUID

from app.application.dto.tat_result import TATCalculationResult


class TATCalculator(Protocol):
    """Port for calculating laboratory turnaround time."""

    def calculate(
        self,
        request_id: UUID,
        started_at: datetime,
        completed_at: datetime,
        target_minutes: int,
    ) -> TATCalculationResult:
        """Calculate and evaluate laboratory TAT."""
        ...
