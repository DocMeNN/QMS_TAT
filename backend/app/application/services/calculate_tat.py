from app.application.commands.calculate_tat import CalculateTATCommand
from app.application.dto.tat_result import TATCalculationResult
from app.application.ports.tat_calculator import TATCalculator
from app.infrastructure.adapters.tat_calculator import TATCalculatorAdapter


class CalculateTATService:
    """Application service for TAT calculation."""

    def __init__(self, calculator: TATCalculator | None = None) -> None:
        self._calculator = calculator or TATCalculatorAdapter()

    def execute(self, command: CalculateTATCommand) -> TATCalculationResult:
        """Calculate TAT from an application command."""
        return self._calculator.calculate(
            command.request_id,
            command.started_at,
            command.completed_at,
            command.target_minutes,
        )


def calculate_tat(
    command: CalculateTATCommand,
    calculator: TATCalculator,
) -> TATCalculationResult:
    """Calculate TAT using the application service."""
    return CalculateTATService(calculator).execute(command)
