"""TAT domain value objects and rules."""

from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import StrEnum


class TATStatus(StrEnum):
    """Operational status of a TAT measurement."""

    WITHIN_TARGET = "WITHIN_TARGET"
    AT_RISK = "AT_RISK"
    BREACHED = "BREACHED"
    NOT_MEASURABLE = "NOT_MEASURABLE"


@dataclass(frozen=True)
class WorkflowEvent:
    """A timestamped laboratory workflow event."""

    event_type: str
    occurred_at: datetime


@dataclass(frozen=True)
class TATMeasurement:
    """Calculated turnaround time."""

    start: datetime
    end: datetime
    target: timedelta

    @property
    def elapsed(self) -> timedelta:
        """Return elapsed turnaround time."""
        return self.end - self.start

    @property
    def status(self) -> TATStatus:
        """Determine TAT status against the target."""
        if self.end < self.start:
            return TATStatus.NOT_MEASURABLE

        if self.elapsed > self.target:
            return TATStatus.BREACHED

        return TATStatus.WITHIN_TARGET
