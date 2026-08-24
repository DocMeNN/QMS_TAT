"""Persistence port for TAT records."""

from abc import ABC, abstractmethod
from uuid import UUID

from app.application.dto.tat_result import TATCalculationResult


class TATRepository(ABC):
    """Application persistence boundary."""

    @abstractmethod
    def save(self, result: TATCalculationResult) -> None:
        """Persist a TAT calculation result."""
        raise NotImplementedError

    @abstractmethod
    def get(self, request_id: UUID) -> TATCalculationResult | None:
        """Retrieve a TAT calculation result."""
        raise NotImplementedError
