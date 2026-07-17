from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Vulpilot",
    version="0.1.0",
)

app.include_router(router)