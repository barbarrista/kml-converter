from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

from src.core.converter import ReportType

router = APIRouter(prefix="/converter")

templates = Jinja2Templates(directory="src/web/frontend/templates")


@router.get("", response_class=HTMLResponse)
def get_converter_page(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse("index.html", context={
        "request": request,
        "report_types": [type_.name for type_ in ReportType],
    })
