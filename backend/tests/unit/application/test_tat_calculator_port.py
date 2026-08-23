"""Tests for the TAT application calculator port."""

from datetime import datetime, timezone
from typing import assert_type
from uuid import uuid4

from app.application.dto.tat_result import TATCalculationResult
from app.application.ports.tat_calculator import TATCalculator
from app.domain.tat.measurement import TATStatus


class FakeTATCalculator:
    """Test implementation satisfying the application port."""

    def calculate(
        self,
        request_id,
        started_at,
        completed_at,
        target_minutes,
    ) -> TATCalculationResult:
        """Return a deterministic calculation result."""
        duration_minutes = int((completed_at - started_at).total_seconds() / 60)

        return TATCalculationResult(
            request_id=request_id,
            started_at=started_at,
            completed_at=completed_at,
            duration_minutes=duration_minutes,
            target_minutes=target_minutes,
            status=TATStatus.WITHIN_TARGET,
        )


def test_tat_calculator_port_contract() -> None:
    """Verify the concrete implementation satisfies TATCalculator."""
    calculator: TATCalculator = FakeTATCalculator()

    request_id = uuid4()
    started_at = datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc)
    completed_at = datetime(2026, 8, 23, 9, 0, tzinfo=timezone.utc)

    result = calculator.calculate(
        request_id=request_id,
        started_at=started_at,
        completed_at=completed_at,
        target_minutes=120,
    )

    assert_type(calculator, TATCalculator)
    assert result.request_id == request_id
    assert result.duration_minutes == 60
    assert result.target_minutes == 120
    assert result.status is TATStatus.WITHIN_TARGET
