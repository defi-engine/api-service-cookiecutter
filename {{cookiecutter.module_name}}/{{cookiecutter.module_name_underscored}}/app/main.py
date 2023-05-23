"""Main app."""
import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from {{cookiecutter.module_name_underscored}}.app.api.api import api_router
from {{cookiecutter.module_name_underscored}}.app.core.config import settings


def create_app() -> FastAPI:
    """Create FastAPI app."""
    app_fastapi = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url="/openapi.json",
        docs_url="/",
    )

    app_fastapi.include_router(api_router, prefix=settings.API_STR)
    return app_fastapi


app = create_app()


register_tortoise(
    app=app,
    db_url=settings.TORTOISE_DATABASE_URI,
    modules={"models": ["{{cookiecutter.module_name_underscored}}.app.models"]},
    add_exception_handlers=True,
)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.UVICORN_ADDRESS_MAIN, port=settings.UVICORN_PORT_MAIN)


def start():
    """Start uvicorn service."""
    uvicorn.run(app, host=settings.UVICORN_ADDRESS_MAIN, port=settings.UVICORN_PORT_MAIN)
