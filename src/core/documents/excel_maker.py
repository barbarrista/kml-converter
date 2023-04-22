from io import BytesIO

import openpyxl
from openpyxl.styles import Font

from src.core.dto import TableDataDTO


def make_excel(data: TableDataDTO) -> BytesIO:
    """Making .xlsx file as in memory object"""

    in_memory_file = BytesIO()
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(data.header)
    for row in data.rows:
        sheet.append(row)

    for rows in sheet.iter_rows(min_row=1, max_row=1):
        for cell in rows:
            cell.font = Font(bold=True)
    workbook.save(in_memory_file)
    in_memory_file.seek(0)
    return in_memory_file
