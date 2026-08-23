"""Tests for the TAT infrastructure adapter."""

from datetime import datetime, timezone
from uuid import uuid4

from app.application.dto.tat_result import TATCalculationResult
from app.application.ports.tat_calculator import TATCalculator
from app.domain.tat.measurement import TATStatus
from app.infrastructure.adapters.tat_calculator import TATCalculatorAdapter


def test_tat_adapter_implements_port() -> None:
    calculator: TATCalculator = TATCalculatorAdapter()
    request_id = uuid4()
    started_at = datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc)
    completed_at = datetime(2026, 8, 23, 9, 0, tzinfo=timezone.utc)
    result = calculator.calculate(request_id, started_at, completed_at, 120)
    assert isinstance(result, TATCalculationResult)
    assert result.request_id == request_id
    assert result.duration_minutes == 60
    assert result.target_minutes == 120
    assert result.status is TATStatus.WITHIN_TARGET


def test_tat_adapter_breached() -> None:
    adapter = TATCalculatorAdapter()
    result = adapter.calculate(
        uuid4(),
        datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc),
        datetime(2026, 8, 23, 13, 0, tzinfo=timezone.utc),
        240,
    )
    assert result.duration_minutes == 300
    assert result.status is TATStatus.BREACHED
