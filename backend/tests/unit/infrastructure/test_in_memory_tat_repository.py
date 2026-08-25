"""Tests for the in-memory TAT repository."""

from datetime import datetime, timezone
from uuid import uuid4

from app.application.dto.tat_result import TATCalculationResult
from app.domain.tat.measurement import TATStatus
from app.infrastructure.persistence.in_memory_tat_repository import \
    InMemoryTATRepository


def make_result() -> TATCalculationResult:
    """Create a deterministic TAT result."""
    request_id = uuid4()
    started_at = datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc)
    completed_at = datetime(2026, 8, 23, 10, 0, tzinfo=timezone.utc)

    return TATCalculationResult(
        request_id=request_id,
        started_at=started_at,
        completed_at=completed_at,
        duration_minutes=120,
        target_minutes=240,
        status=TATStatus.WITHIN_TARGET,
    )


def test_repository_saves_and_retrieves() -> None:
    """Verify a saved record can be retrieved."""
    repository = InMemoryTATRepository()
    result = make_result()

    repository.save(result)

    assert repository.get(result.request_id) == result


def test_repository_returns_none_for_unknown_request() -> None:
    """Verify unknown records return None."""
    repository = InMemoryTATRepository()

    assert repository.get(uuid4()) is None
