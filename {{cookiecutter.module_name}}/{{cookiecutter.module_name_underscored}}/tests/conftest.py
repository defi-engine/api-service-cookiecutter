import asyncio
from typing import  Generator, List

import pytest
from httpx import AsyncClient
from loguru import logger
from tortoise import Tortoise

from {{cookiecutter.module_name_underscored}}.app.core.config import settings
from {{cookiecutter.module_name_underscored}}.app.main import create_app


app = create_app()


async def init_db(db_url, create_db: bool = False, schemas: bool = False) -> None:
    """Establish the initial database connection."""
    db_url = f"{db_url}_test"
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["{{cookiecutter.module_name_underscored}}.app.models"]},
        _create_db=create_db,
    )
    if create_db:
        logger.debug(f"Database created! {db_url = }")
    if schemas:
        await Tortoise.generate_schemas()
        logger.debug("Schemas generated successfully")


async def init():
    db_url = settings.TORTOISE_DATABASE_URI  # type: ignore
    await init_db(db_url, True, True)


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        logger.debug("Client is ready")
        yield client


@pytest.fixture(scope="class", autouse=True)
async def initialize_tests():
    await init()
    yield
    await Tortoise._drop_databases()


@pytest.fixture(scope="session")  # type: ignore
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

