from io import BytesIO, StringIO

from selectolax.parser import HTMLParser, Node

from src.core.converter import ReportType
from src.core.documents.csv_maker import make_csv
from src.core.documents.excel_maker import make_excel
from src.core.dto import TableDataDTO


class GPXConvertationService:
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
        wpt_nodes = parser.css("wpt")
        rows = [
            cls._get_data_from_node(node=node, number=number)
            for number, node in enumerate(wpt_nodes, start=1)
        ]
        return TableDataDTO(
            header=["Number", "Longitude", "Latitude", "Name"],
            rows=rows,
        )

    @staticmethod
    def _get_data_from_node(node: Node, number: int) -> tuple[str, str, str, str]:
        name_node = node.css_first("name")
        name = name_node.text(strip=True) if name_node else ""
        longitude = node.attrs["lon"]
        latitude = node.attrs["lat"]
        return (str(number), name, longitude, latitude)
