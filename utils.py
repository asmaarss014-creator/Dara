# utils.py

from pathlib import Path
from typing import Iterable


def ensure_directory(path: Path) -> None:
    """Create a directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)


def write_file(path: Path, content: str, overwrite: bool = False) -> bool:
    """
    Write content to a file.
    Returns True if the file was written.
    Returns False if it was skipped.
    """
    if path.exists() and not overwrite:
        return False

    ensure_directory(path.parent)
    path.write_text(content, encoding="utf-8")
    return True


def create_empty_file(path: Path, overwrite: bool = False) -> bool:
    """Create an empty file."""
    return write_file(path, "", overwrite)


def count_directories(files: Iterable[str]) -> int:
    """Count unique directories from a list of file paths."""
    directories = {str(Path(f).parent) for f in files}
    return len(directories)


def project_statistics(files: Iterable[str]) -> dict:
    """Return project statistics."""
    return {
        "files": len(list(files)),
        "directories": count_directories(files),
    }


def print_banner(title: str) -> None:
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)


def print_success(message: str) -> None:
    print(f"[OK] {message}")


def print_warning(message: str) -> None:
    print(f"[WARNING] {message}")


def print_error(message: str) -> None:
    print(f"[ERROR] {message}")