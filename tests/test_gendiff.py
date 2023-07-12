from gendiff import generate_diff
from tests.fixtures.right import RIGHT


def test_plain():
    assert RIGHT == generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.json"
    )
    assert RIGHT == generate_diff(
        "tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml"
    )
