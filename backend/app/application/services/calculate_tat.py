"""Application service for TAT calculation."""

from datetime import timedelta

from app.application.commands.calculate_tat import CalculateTATCommand
from app.application.dto.tat_result import TATCalculationResult
from app.domain.tat.measurement import TATMeasurement


class CalculateTATService:
    """Coordinate TAT calculation without infrastructure dependencies."""

    def execute(
        self,
        command: CalculateTATCommand,
    ) -> TATCalculationResult:
        """Execute a TAT calculation command."""

        measurement = TATMeasurement(
            start=command.started_at,
            end=command.completed_at,
            target=timedelta(minutes=command.target_minutes),
        )

        return TATCalculationResult(
            request_id=command.request_id,
            started_at=command.started_at,
            completed_at=command.completed_at,
            duration_minutes=measurement.duration_minutes,
            target_minutes=command.target_minutes,
            status=measurement.status,
        )
