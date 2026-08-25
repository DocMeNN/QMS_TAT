from fastapi import APIRouter

"""TAT API boundary."""

from app.application.commands.calculate_tat import CalculateTATCommand
from app.application.dto.tat_result import TATCalculationResult
from app.application.services.calculate_tat import CalculateTATService
from app.interface.schemas.tat import CalculateTATRequest, CalculateTATResponse


def calculate_tat(
    request: CalculateTATRequest,
) -> CalculateTATResponse:
    """Execute the TAT application use case through the API boundary."""

    command = CalculateTATCommand(
        request_id=request.request_id,
        started_at=request.started_at,
        completed_at=request.completed_at,
        target_minutes=request.target_minutes,
    )

    result: TATCalculationResult = CalculateTATService().execute(command)

    return CalculateTATResponse(
        request_id=result.request_id,
        started_at=result.started_at,
        completed_at=result.completed_at,
        duration_minutes=result.duration_minutes,
        target_minutes=result.target_minutes,
        status=result.status.value,
    )


router = APIRouter()
