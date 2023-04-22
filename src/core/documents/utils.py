from pathlib import Path


def remove_file_extension(path: Path) -> Path:
    return Path(str(path).replace(path.suffix, ""))
