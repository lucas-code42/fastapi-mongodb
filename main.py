from fastapi import FastAPI
from api.api_settings import api_settings
from api.api_router import user_endpoints

app = FastAPI(
    title=api_settings.API_TITLE,
    version=api_settings.API_VERSION,
    description=api_settings.API_DESCRIPTION
)
app.include_router(user_endpoints, prefix=api_settings.API_URL)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=api_settings.API_PORT, log_level="info")
