"""End-to-end TAT workflow integration tests."""

from datetime import datetime, timezone
from uuid import uuid4

from app.application.commands.calculate_tat import CalculateTATCommand
from app.application.services.record_tat import RecordTATService
from app.domain.tat.measurement import TATStatus
from app.infrastructure.persistence.in_memory_tat_repository import (
    InMemoryTATRepository,
)


def test_complete_tat_workflow() -> None:
    """Verify command -> application -> domain -> persistence."""
    repository = InMemoryTATRepository()
    service = RecordTATService(repository)

    request_id = uuid4()

    command = CalculateTATCommand(
        request_id=request_id,
        started_at=datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc),
        completed_at=datetime(2026, 8, 23, 10, 0, tzinfo=timezone.utc),
        target_minutes=240,
    )

    result = service.execute(command)
    stored = repository.get(request_id)

    assert result.request_id == request_id
    assert result.duration_minutes == 120
    assert result.target_minutes == 240
    assert result.status is TATStatus.WITHIN_TARGET
    assert stored == result


def test_complete_breached_tat_workflow() -> None:
    """Verify breached status survives the complete workflow."""
    repository = InMemoryTATRepository()
    service = RecordTATService(repository)

    request_id = uuid4()

    command = CalculateTATCommand(
        request_id=request_id,
        started_at=datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc),
        completed_at=datetime(2026, 8, 23, 13, 0, tzinfo=timezone.utc),
        target_minutes=240,
    )

    result = service.execute(command)
    stored = repository.get(request_id)

    assert result.duration_minutes == 300
    assert result.status is TATStatus.BREACHED
    assert stored is not None
    assert stored.status is TATStatus.BREACHED
