"""Tests for the record TAT application service."""

from datetime import datetime, timezone
from uuid import uuid4

from app.application.commands.calculate_tat import CalculateTATCommand
from app.application.services.record_tat import RecordTATService
from app.infrastructure.persistence.in_memory_tat_repository import (
    InMemoryTATRepository,
)


def make_command() -> CalculateTATCommand:
    """Create a deterministic TAT command."""
    return CalculateTATCommand(
        request_id=uuid4(),
        started_at=datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc),
        completed_at=datetime(2026, 8, 23, 10, 0, tzinfo=timezone.utc),
        target_minutes=240,
    )


def test_record_tat_calculates_and_persists() -> None:
    """Verify calculation and persistence."""
    repository = InMemoryTATRepository()
    service = RecordTATService(repository)
    command = make_command()

    result = service.execute(command)

    assert result.duration_minutes == 120
    assert repository.get(command.request_id) == result


def test_record_tat_returns_persisted_result() -> None:
    """Verify the persisted result is retrievable."""
    repository = InMemoryTATRepository()
    service = RecordTATService(repository)
    command = make_command()

    result = service.execute(command)
    stored = repository.get(command.request_id)

    assert stored is not None
    assert stored.request_id == result.request_id
    assert stored.status == result.status
