
import json
from pathlib import Path


def save_json(file, data):
    Path(file).write_text(
        json.dumps(data, indent=4)
    )


def load_json(file):
    path = Path(file)

    if not path.exists():
        return {}

    return json.loads(
        path.read_text()
    )
