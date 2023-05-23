"""Health check."""
from fastapi import APIRouter
from starlette.responses import JSONResponse, Response


health_router = APIRouter()


@health_router.get("/", status_code=204)
async def health():
    """GET Request health endpoint."""
    return Response(status_code=204)


@health_router.get("/info", status_code=200)
async def health_():
    """GET Request info endpoint."""
    return JSONResponse({"status": "ok"}, status_code=200)
