"""API definition."""
from fastapi import APIRouter

from .routers.health import health_router


api_router = APIRouter()
api_router.include_router(health_router, prefix="/health", tags=["health"])

