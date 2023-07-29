from gendiff.scripts.gendiff_entry import generate_diff
from tests.fixtures.right import RIGHT_PLAIN, RIGHT_NESTED


def test_plain():
    assert RIGHT_PLAIN == generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.json"
    )
    assert RIGHT_PLAIN == generate_diff(
        "tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml"
    )

def test_nested():
    assert RIGHT_NESTED == generate_diff(
        "tests/fixtures/file3.json", "tests/fixtures/file4.json"
    )