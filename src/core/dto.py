from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TableDataDTO:
    header: list[str]
    rows: Sequence[Sequence[str]]
