from datetime import datetime, timedelta
from enum import Enum
from uuid import UUID


class TATStatus(Enum):
    WITHIN_TARGET = "within_target"
    AT_RISK = "at_risk"
    BREACHED = "breached"
    NOT_MEASURABLE = "not_measurable"


class TATMeasurement:
    def __init__(
        self,
        start: datetime,
        end: datetime,
        target: timedelta,
        request_id: UUID | None = None,
    ) -> None:
        self.request_id = request_id
        self.start = start
        self.end = end
        self.target = target

    @property
    def elapsed(self) -> timedelta:
        """Return the elapsed turnaround time."""
        return self.end - self.start

    @property
    def duration(self) -> timedelta:
        """Return the elapsed turnaround time."""
        return self.elapsed

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
