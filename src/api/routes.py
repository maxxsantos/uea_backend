from fastapi import APIRouter
from src.api.endpoints import home, temperature

routes = APIRouter()

version = "v1"

routes.include_router(
    home.router,
    prefix=f"/{version}/home",
    tags=["home"]
)

routes.include_router(
    temperature.router,
    prefix=f"/{version}/temperatures",
    tags=["temperature"]
)