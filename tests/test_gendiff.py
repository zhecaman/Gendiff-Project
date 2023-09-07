import pytest
import os
from gendiff.gendiff import generate_diff


NESTED1_JSON = "nested1.json"
NESTED2_JSON = "nested2.json"
NESTED1_YAML = "nested1.yaml"
NESTED2_YAML = "nested2.yaml"
ANSWER_JSON_NESTED = "answer_nested_json"
ANSWER_PLAIN_NESTED = "answer_nested_plain"
ANSWER_STYLISH_NESTED = "answer_nested_stylish"


def get_path_to_fixture(filename):
    return os.path.join('tests/fixtures', filename)


def read_answer(filename):
    filepath = get_path_to_fixture(filename)
    with open(filepath) as file:
        return file.read()


@pytest.mark.parametrize(
    ("filename1, filename2, formatter, expected"),
    [
        (NESTED1_YAML, NESTED2_YAML, "plain", ANSWER_PLAIN_NESTED),
        (NESTED1_YAML, NESTED2_YAML, "stylish", ANSWER_STYLISH_NESTED),
        (NESTED1_YAML, NESTED2_YAML, "json", ANSWER_JSON_NESTED),
        (NESTED1_JSON, NESTED2_JSON, "json", ANSWER_JSON_NESTED),
        (NESTED1_JSON, NESTED2_JSON, "stylish", ANSWER_STYLISH_NESTED),
        (NESTED1_JSON, NESTED2_JSON, "plain", ANSWER_PLAIN_NESTED),
    ],
)
def test_gendiff(filename1, filename2, formatter, expected):
    answer = read_answer(expected)
    filepath1 = get_path_to_fixture(filename1)
    filepath2 = get_path_to_fixture(filename2)
    assert generate_diff(filepath1, filepath2, formatter) == answer
