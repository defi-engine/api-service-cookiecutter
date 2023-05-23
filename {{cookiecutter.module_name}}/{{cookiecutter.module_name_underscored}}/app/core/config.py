"""Config file."""
from typing import Dict

from pydantic import AnyUrl, BaseSettings, validator


class Settings(BaseSettings):
    """Settings."""

    # GENEREAL
    PROJECT_NAME: str
    API_STR: str

    # POSTGRESQL
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    TORTOISE_DATABASE_URI: str | None = None

    # REDIS
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    # UVICORN
    UVICORN_PORT_MAIN: int
    UVICORN_ADDRESS_MAIN: str

    @validator("TORTOISE_DATABASE_URI", pre=True)
    def _assemble_db_connection(cls, v: str | None, values: Dict[str, str]) -> str:
        if isinstance(v, str):
            return v
        return AnyUrl.build(
            scheme="postgres",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB')}",
        )

    class Config:
        """Config class."""

        env_file = ".env.test", ".env"
        case_sensitive = True


settings: Settings = Settings()

# used by pyproject.toml
TORTOISE_ORM = {
    "connections": {"default": settings.TORTOISE_DATABASE_URI},
    "apps": {
        "models": {
            "models": ["{{cookiecutter.module_name_underscored}}.app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
