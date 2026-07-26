# main.py

from pathlib import Path

from config import PROJECT_NAME, CREATE_EMPTY_FILES, OVERWRITE_EXISTING
from project_files import FILES
from templates import TEMPLATES


def create_project():
    root = Path(PROJECT_NAME)

    created = 0
    skipped = 0

    for file in FILES:
        path = root / file

        # Create parent folders
        path.parent.mkdir(parents=True, exist_ok=True)

        # Skip existing files if overwrite is disabled
        if path.exists() and not OVERWRITE_EXISTING:
            skipped += 1
            continue

        # Get template content (or empty)
        content = TEMPLATES.get(file, "")

        if content or CREATE_EMPTY_FILES:
            path.write_text(content, encoding="utf-8")
            created += 1

    print("=" * 50)
    print(f"Project : {PROJECT_NAME}")
    print(f"Created : {created} files")
    print(f"Skipped : {skipped} files")
    print("Done!")
    print("=" * 50)


if __name__ == "__main__":
    create_project()