from fastapi import APIRouter

from . import converter

router = APIRouter(prefix="/v1")

router.include_router(converter.router)
