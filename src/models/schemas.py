"""Performance Review Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class PerformanceReview(BaseModel):
    """PerformanceReview for Performance Review Agent."""
    employee_id: str
    period: str
    overall_rating: str
    strengths: list[str]
    development_areas: list[str]
    narrative: str


class ImprovementPlan(BaseModel):
    """ImprovementPlan for Performance Review Agent."""
    employee_id: str
    gaps: list[dict]
    targets: list[dict]
    timeline_days: int
    check_in_dates: list[str]

