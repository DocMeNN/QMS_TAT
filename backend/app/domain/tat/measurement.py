"""Laboratory turnaround-time measurement domain model."""

from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum


class TATStatus(Enum):
    """Classification of laboratory turnaround time."""

    WITHIN_TARGET = "within_target"
    AT_RISK = "at_risk"
    BREACHED = "breached"
    NOT_MEASURABLE = "not_measurable"


@dataclass(frozen=True, slots=True)
class TATMeasurement:
    """Measure laboratory turnaround time."""

    start: datetime
    end: datetime
    target: timedelta

    @property
    def duration(self) -> timedelta:
        """Return the elapsed turnaround time."""

        return self.end - self.start

    @property
    def elapsed(self) -> timedelta:
        """Return the elapsed turnaround time."""
        return self.end - self.start

    @property
    def duration_minutes(self) -> int:
        """Return elapsed turnaround time in whole minutes."""

        return int(self.duration.total_seconds() // 60)

    @property
    def status(self) -> TATStatus:
        """Return the TAT classification."""

        if self.duration.total_seconds() < 0:
            return TATStatus.NOT_MEASURABLE

        if self.duration > self.target:
            return TATStatus.BREACHED

        if self.duration >= self.target * 0.75:
            return TATStatus.AT_RISK

        return TATStatus.WITHIN_TARGET
