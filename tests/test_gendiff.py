import pytest
from gendiff.gendiff import generate_diff


SIMPLE1_JSON = "tests/fixtures/simple1.json"
SIMPLE2_JSON = "tests/fixtures/simple2.json"
SIMPLE1_YAML = "tests/fixtures/simple1.yaml"
SIMPLE2_YAML = "tests/fixtures/simple2.yaml"
NESTED1_JSON = "tests/fixtures/nested1.json"
NESTED2_JSON = "tests/fixtures/nested2.json"
NESTED1_YAML = "tests/fixtures/nested1.yaml"
NESTED2_YAML = "tests/fixtures/nested2.yaml"
ANSWER_JSON_SIMPLE = "tests/fixtures/answer_simple_json"
ANSWER_PLAIN_SIMPLE = "tests/fixtures/answer_simple_plain"
ANSWER_STYLISH_SIMPLE = "tests/fixtures/answer_simple_stylish"
ANSWER_JSON_NESTED = "tests/fixtures/answer_nested_json"
ANSWER_PLAIN_NESTED = "tests/fixtures/answer_nested_plain"
ANSWER_STYLISH_NESTED = "tests/fixtures/answer_nested_stylish"


def read_answer(filepath):
    with open(filepath) as file:
        return file.read()


@pytest.mark.parametrize(
    ("filepath1, filepath2, formatter, expected"),
    [
        (SIMPLE1_JSON, SIMPLE2_JSON, "json", ANSWER_JSON_SIMPLE),
        (SIMPLE1_YAML, SIMPLE2_YAML, "json", ANSWER_JSON_SIMPLE),
        (SIMPLE1_JSON, SIMPLE2_JSON, "stylish", ANSWER_STYLISH_SIMPLE),
        (SIMPLE1_JSON, SIMPLE2_JSON, "plain", ANSWER_PLAIN_SIMPLE),
        (SIMPLE1_YAML, SIMPLE2_YAML, "stylish", ANSWER_STYLISH_SIMPLE),
        (NESTED1_YAML, NESTED2_YAML, "plain", ANSWER_PLAIN_NESTED),
        (NESTED1_YAML, NESTED2_YAML, "stylish", ANSWER_STYLISH_NESTED),
        (NESTED1_YAML, NESTED2_YAML, "json", ANSWER_JSON_NESTED),
        (NESTED1_JSON, NESTED2_JSON, "json", ANSWER_JSON_NESTED),
        (NESTED1_JSON, NESTED2_JSON, "stylish", ANSWER_STYLISH_NESTED),
        (NESTED1_JSON, NESTED2_JSON, "plain", ANSWER_PLAIN_NESTED),
    ],
)
def test_gendiff(filepath1, filepath2, formatter, expected):
    answer = read_answer(expected)
    assert generate_diff(filepath1, filepath2, formatter) == answer
