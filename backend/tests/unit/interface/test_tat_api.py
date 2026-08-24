"""Tests for the TAT API boundary."""

from datetime import datetime, timezone
from uuid import uuid4

from app.interface.api.tat import calculate_tat
from app.interface.schemas.tat import CalculateTATRequest, CalculateTATResponse


def test_api_calculates_tat() -> None:
    """Verify API request is mapped to the application use case."""
    request_id = uuid4()
    started_at = datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc)
    completed_at = datetime(2026, 8, 23, 10, 0, tzinfo=timezone.utc)

    request = CalculateTATRequest(
        request_id=request_id,
        started_at=started_at,
        completed_at=completed_at,
        target_minutes=240,
    )

    response = calculate_tat(request)

    assert isinstance(response, CalculateTATResponse)
    assert response.request_id == request_id
    assert response.duration_minutes == 120
    assert response.target_minutes == 240
    assert response.status == "within_target"


def test_api_preserves_breached_status() -> None:
    """Verify domain status crosses the API boundary unchanged."""
    request = CalculateTATRequest(
        request_id=uuid4(),
        started_at=datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc),
        completed_at=datetime(2026, 8, 23, 13, 0, tzinfo=timezone.utc),
        target_minutes=240,
    )

    response = calculate_tat(request)

    assert response.duration_minutes == 300
    assert response.status == "breached"


def test_api_rejects_non_positive_target() -> None:
    """Verify API schema rejects invalid target values."""
    request_id = uuid4()

    try:
        CalculateTATRequest(
            request_id=request_id,
            started_at=datetime(2026, 8, 23, 8, 0, tzinfo=timezone.utc),
            completed_at=datetime(2026, 8, 23, 9, 0, tzinfo=timezone.utc),
            target_minutes=0,
        )
    except ValueError:
        return

    raise AssertionError("Expected validation failure for target_minutes=0")
