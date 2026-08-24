"""In-memory TAT repository."""

from uuid import UUID

from app.application.dto.tat_result import TATCalculationResult
from app.application.ports.tat_repository import TATRepository


class InMemoryTATRepository(TATRepository):
    """Temporary persistence adapter for v1.0 integration."""

    def __init__(self) -> None:
        self._records: dict[UUID, TATCalculationResult] = {}

    def save(self, result: TATCalculationResult) -> None:
        """Store a TAT result."""
        self._records[result.request_id] = result

    def get(self, request_id: UUID) -> TATCalculationResult | None:
        """Retrieve a TAT result."""
        return self._records.get(request_id)
