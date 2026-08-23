"""Infrastructure adapter implementing the TAT application port."""

from datetime import datetime, timedelta
from uuid import UUID

from app.application.dto.tat_result import TATCalculationResult
from app.domain.tat.measurement import TATMeasurement


class TATCalculatorAdapter:
    """Concrete infrastructure implementation of the TAT calculator port."""

    def calculate(
        self,
        request_id: UUID,
        started_at: datetime,
        completed_at: datetime,
        target_minutes: int,
    ) -> TATCalculationResult:
        """Calculate TAT using the domain model."""
        measurement = TATMeasurement(
            start=started_at,
            end=completed_at,
            target=timedelta(minutes=target_minutes),
        )
        return TATCalculationResult(
            request_id=request_id,
            started_at=started_at,
            completed_at=completed_at,
            duration_minutes=int(measurement.elapsed.total_seconds() / 60),
            target_minutes=target_minutes,
            status=measurement.status,
        )
