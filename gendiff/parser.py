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


def parse_file(path):
    reader = get_reader(path)
    with open(path) as file:
        return reader(file)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        choices=[
            "stylish",
            "plain",
            "json",
        ],
        help="set format of output",
        default="stylish",
    )
    args = parser.parse_args()
    return args
