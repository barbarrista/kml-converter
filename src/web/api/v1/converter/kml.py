from io import StringIO
from typing import Annotated
from uuid import uuid4

from fastapi import APIRouter, File
from starlette.responses import StreamingResponse

from src.core.converter import ReportType
from src.core.converter.kml.service import KMLConvertationService

router = APIRouter(tags=["kml_converter"], prefix="/kml")


@router.post("/build")
def build(report_type: ReportType, file: Annotated[bytes, File()]) -> StreamingResponse:
    filename = f"{uuid4()}.{report_type.name}"
    result = KMLConvertationService.convert(report_type=report_type, file=file)
    return StreamingResponse(
        iter([result.getvalue()]),
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
