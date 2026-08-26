from __future__ import annotations

from app.application.commands.calculate_tat import CalculateTATCommand
from app.application.dto.tat_result import TATCalculationResult
from app.application.ports.tat_calculator import TATCalculator
from app.application.ports.tat_repository import TATRepository
from app.application.services.calculate_tat import CalculateTATService
from app.infrastructure.adapters.tat_calculator import TATCalculatorAdapter


class RecordTATService:
    """Application service for calculating and persisting TAT results."""

    def __init__(
        self,
        repository: TATRepository,
        calculator: TATCalculator | None = None,
    ) -> None:
        self._repository = repository
        self._calculator = calculator or TATCalculatorAdapter()

    def execute(self, command: CalculateTATCommand) -> TATCalculationResult:
        """Calculate the TAT result and persist it."""
        service = CalculateTATService(self._calculator)
        result = service.execute(command)
        self._repository.save(result)
        return result
