import csv
from io import StringIO
from pathlib import Path

from src.core.dto import TableDataDTO

from .utils import remove_file_extension


def save_data_to_csv(file_path: Path, data: TableDataDTO, delimiter: str) -> None:
    file_path = remove_file_extension(path=file_path)
    with Path.open(Path(f"{file_path}.csv"), "w", newline="", encoding="UTF8") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(data.header)
        writer.writerows(data.rows)


def make_csv(data: TableDataDTO, delimiter: str) -> StringIO:
    """Making .csv file as in memory object"""

    io = StringIO()
    writer = csv.writer(io, delimiter=delimiter, quoting=csv.QUOTE_ALL)
    writer.writerow(data.header)
    writer.writerows(data.rows)
    return io
