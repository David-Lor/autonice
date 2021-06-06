"""Module with functions for loading configurations"""

import os
import json
from typing import List

from ..entities.process import Process

JSON_LOCATION = os.getenv("AUTONICE_SETTINGS", "settings.json")


def load_json() -> List[Process]:
    with open(JSON_LOCATION, "r") as file:
        file_parsed = json.load(file)

    processes_raw = file_parsed.get("processes", None)
    if not processes_raw:
        raise ValueError("No processes defined")

    return [Process(**data) for data in processes_raw]
