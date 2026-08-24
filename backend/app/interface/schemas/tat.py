"""API schemas for TAT calculation."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class CalculateTATRequest(BaseModel):
    """HTTP request schema for TAT calculation."""

    model_config = ConfigDict(extra="forbid")

    request_id: UUID
    started_at: datetime
    completed_at: datetime
    target_minutes: int = Field(gt=0)


class CalculateTATResponse(BaseModel):
    """HTTP response schema for TAT calculation."""

    model_config = ConfigDict(from_attributes=True)

    request_id: UUID
    started_at: datetime
    completed_at: datetime
    duration_minutes: int
    target_minutes: int
    status: str
