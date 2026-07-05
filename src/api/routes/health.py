"""Performance Review Agent - Health Check Routes."""

import time
from fastapi import APIRouter
from src.config import get_settings

router = APIRouter(tags=["Health"])
settings = get_settings()
_start_time = time.time()


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "agent": settings.app_name,
        "version": "1.0.0",
        "uptime_seconds": round(time.time() - _start_time, 2),
        "features": ['review_writing', 'feedback_aggregation', 'calibration_analysis', 'goal_tracking', 'pip_generation'],
    }
