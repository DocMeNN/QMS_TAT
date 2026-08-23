"""Tests for the TAT application service."""

from datetime import datetime, timezone
from uuid import uuid4

from app.application.commands.calculate_tat import CalculateTATCommand
from app.application.services.calculate_tat import CalculateTATService
from app.domain.tat.measurement import TATStatus


def test_calculate_tat_service_within_target() -> None:
    request_id = uuid4()

    command = CalculateTATCommand(
        request_id=request_id,
        started_at=datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc),
        completed_at=datetime(2026, 8, 23, 9, 0, tzinfo=timezone.utc),
        target_minutes=120,
    )

    result = CalculateTATService().execute(command)

    assert result.request_id == request_id
    assert result.duration_minutes == 60
    assert result.target_minutes == 120
    assert result.status is TATStatus.WITHIN_TARGET


def test_calculate_tat_service_at_risk() -> None:
    command = CalculateTATCommand(
        request_id=uuid4(),
        started_at=datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc),
        completed_at=datetime(2026, 8, 23, 9, 30, tzinfo=timezone.utc),
        target_minutes=120,
    )

    result = CalculateTATService().execute(command)

    assert result.duration_minutes == 90
    assert result.status is TATStatus.AT_RISK


def test_calculate_tat_service_breached() -> None:
    command = CalculateTATCommand(
        request_id=uuid4(),
        started_at=datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc),
        completed_at=datetime(2026, 8, 23, 11, 0, tzinfo=timezone.utc),
        target_minutes=120,
    )

    result = CalculateTATService().execute(command)

    assert result.duration_minutes == 180
    assert result.status is TATStatus.BREACHED


def test_calculate_tat_service_preserves_request_identity() -> None:
    request_id = uuid4()

    command = CalculateTATCommand(
        request_id=request_id,
        started_at=datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc),
        completed_at=datetime(2026, 8, 23, 8, 30, tzinfo=timezone.utc),
        target_minutes=60,
    )

    result = CalculateTATService().execute(command)

    assert result.request_id == request_id
