from pydantic import BaseSettings


class ApiSettings(BaseSettings):
    """
    General configs
    """
    API_URL: str = "/api/v1/user"
    API_PORT: int = 8000
    API_VERSION = "0.0.1"
    API_DESCRIPTION = "API FOR STUDY PURPOSE (FASTAPI AND MONGODB)"
    API_TITLE = "FASTAPI-MONGODB"
    DB_PORT: int = 27017


api_settings = ApiSettings()
