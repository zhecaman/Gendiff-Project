import json
import yaml
from pathlib import Path
import argparse


def get_reader(filepath):
    return {".json": json.load,
            ".yml": yaml.safe_load,
            ".yaml": yaml.safe_load}.get(
        Path(filepath).suffix
    )


def read_file(path):
    reader = get_reader(path)
    with open(path) as file:
        return reader(file)
