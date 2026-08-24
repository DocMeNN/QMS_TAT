"""Application service for recording TAT results."""

from app.application.commands.calculate_tat import CalculateTATCommand
from app.application.dto.tat_result import TATCalculationResult
from app.application.ports.tat_repository import TATRepository
from app.application.services.calculate_tat import CalculateTATService


class RecordTATService:
    """Calculate and persist a TAT result."""

    def __init__(self, repository: TATRepository) -> None:
        self._repository = repository
        self._calculator = CalculateTATService()

    def execute(self, command: CalculateTATCommand) -> TATCalculationResult:
        """Calculate the TAT result and persist it."""
        result = self._calculator.execute(command)
        self._repository.save(result)
        return result
