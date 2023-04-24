from pydantic import BaseSettings


class ApiSettings(BaseSettings):
    """
    General configs
    """
    API_VERSION = "0.0.1"
    API_TITLE = "FASTAPI-MONGODB"
    API_DESCRIPTION = "API FOR STUDY PURPOSE (FASTAPI AND MONGODB)"
    
    API_URL: str = "/api/v1/user"
    API_PORT: int = 8000
    
    db_port: int = 27017
    db_password: str = "root"
    db_user: str = "root"
    
    DB_HOST: str = f"mongodb://{db_user}:{db_password}@:{db_port}"
   
    


api_settings = ApiSettings()
