"""FastAPI application boundary."""

from fastapi import FastAPI

from app.interface.api.tat import calculate_tat
from app.interface.schemas.tat import CalculateTATRequest, CalculateTATResponse

app = FastAPI(
    title="ALIP QMS TAT API",
    version="1.0.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Return API health status."""
    return {"status": "ok"}


@app.post("/tat/calculate", response_model=CalculateTATResponse)
def calculate_tat_endpoint(request: CalculateTATRequest) -> CalculateTATResponse:
    """Calculate laboratory turnaround time."""
    return calculate_tat(request)
