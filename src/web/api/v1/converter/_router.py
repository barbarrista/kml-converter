from fastapi import APIRouter

from . import gpx, kml

router = APIRouter(tags=["converter"], prefix="/converter")


router.include_router(kml.router)
router.include_router(gpx.router)
