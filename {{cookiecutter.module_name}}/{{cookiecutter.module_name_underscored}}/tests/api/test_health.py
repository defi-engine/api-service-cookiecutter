import pytest
from httpx import AsyncClient


from {{cookiecutter.module_name_underscored}}.app.core.config import settings



@pytest.mark.anyio  # type: ignore
async def test_health(
    client: AsyncClient,
) -> None:
    r = await client.get(f"{settings.API_STR}/health/", headers={"accept": "application/json"})
    assert r.status_code == 204


@pytest.mark.anyio  # type: ignore
async def test_health_info(
    client: AsyncClient,
) -> None:
    r = await client.get(f"{settings.API_STR}/health/info", headers={"accept": "application/json"})
    assert r.status_code == 200

    resp = r.json()

    assert resp["status"] == "ok"
