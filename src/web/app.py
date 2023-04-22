from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

from . import frontend
from .api import v1


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(frontend.router)
    _configure_routers(app=app)
    app.mount("/", StaticFiles(directory="src/web/frontend/static"), name="static")
    return app


def _configure_routers(app: FastAPI) -> None:
    api_router = APIRouter(prefix="/api")
    api_router.include_router(v1.router)
    app.include_router(api_router)
