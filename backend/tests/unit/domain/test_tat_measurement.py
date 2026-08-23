"""Tests for TAT domain measurements."""

from datetime import datetime, timedelta, timezone

from app.domain.tat.measurement import TATMeasurement, TATStatus

UTC = timezone.utc


def test_tat_within_target() -> None:
    start = datetime(2026, 8, 23, 8, 0, tzinfo=UTC)
    end = datetime(2026, 8, 23, 10, 0, tzinfo=UTC)

    measurement = TATMeasurement(
        start=start,
        end=end,
        target=timedelta(hours=4),
    )

    assert measurement.elapsed == timedelta(hours=2)
    assert measurement.status == TATStatus.WITHIN_TARGET


def test_tat_breached() -> None:
    start = datetime(2026, 8, 23, 8, 0, tzinfo=UTC)
    end = datetime(2026, 8, 23, 13, 0, tzinfo=UTC)

    measurement = TATMeasurement(
        start=start,
        end=end,
        target=timedelta(hours=4),
    )

    assert measurement.elapsed == timedelta(hours=5)
    assert measurement.status == TATStatus.BREACHED


def test_tat_invalid_sequence() -> None:
    start = datetime(2026, 8, 23, 13, 0, tzinfo=UTC)
    end = datetime(2026, 8, 23, 8, 0, tzinfo=UTC)

    measurement = TATMeasurement(
        start=start,
        end=end,
        target=timedelta(hours=4),
    )

    assert measurement.status == TATStatus.NOT_MEASURABLE
