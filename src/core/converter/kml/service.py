from io import BytesIO, StringIO

from selectolax.parser import HTMLParser, Node

from src.core.converter import ReportType
from src.core.documents.csv_maker import make_csv
from src.core.documents.excel_maker import make_excel
from src.core.dto import TableDataDTO


class KMLConvertationService:
    @classmethod
    def convert(cls, report_type: ReportType, file: bytes) -> StringIO | BytesIO:
        if report_type is ReportType.csv:
            return cls._to_csv(file=file)
        # ↓ if report_type is ReportType.xlsx ↓
        return cls._to_excel(file=file)

    @classmethod
    def _to_csv(cls, file: bytes) -> StringIO:
        table_data = cls._build_table_data(content=file)
        return make_csv(data=table_data, delimiter="|")

    @classmethod
    def _to_excel(cls, file: bytes) -> BytesIO:
        table_data = cls._build_table_data(content=file)
        return make_excel(data=table_data)

    @classmethod
    def _build_table_data(cls, content: bytes) -> TableDataDTO:
        parser = HTMLParser(content)
        placemark_nodes = parser.css("Placemark")
        rows = [
            cls._get_data_from_node(node=node, number=number)
            for number, node in enumerate(placemark_nodes, start=1)
            if node.css_first("Polygon") is None
        ]
        return TableDataDTO(
            header=["Number", "Longitude", "Latitude", "Name"],
            rows=rows,
        )

    @classmethod
    def _get_data_from_node(cls, node: Node, number: int) -> tuple[str, str, str, str]:
        name_node = node.css_first("name")
        name = name_node.text(strip=True) if name_node else ""
        coordinates_node = node.css_first("coordinates")
        coordinats = coordinates_node.text(strip=True).split(",")
        longitude, latitude = coordinats[0], coordinats[1]
        return (str(number), name, longitude, latitude)
