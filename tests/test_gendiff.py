from gendiff.scripts.gendiff_entry import generate_diff
from tests.fixtures.right import RIGHT_PLAIN, RIGHT_NESTED, RIGHT_SIMPLE


def test_simple():
    assert RIGHT_SIMPLE == generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.json", 'stylish'
    )
    assert RIGHT_SIMPLE == generate_diff(
        "tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml", 'stylish'
    )

def test_nested():
    assert RIGHT_NESTED == generate_diff(
        "tests/fixtures/file3.json", "tests/fixtures/file4.json", 'stylish'
    )
    assert RIGHT_NESTED == generate_diff(
        "tests/fixtures/file3.yaml", "tests/fixtures/file4.yaml", 'stylish'
    )

def test_plain():
    assert RIGHT_PLAIN == generate_diff(
        "tests/fixtures/file3.json", "tests/fixtures/file4.json", 'plain'
    )
    assert RIGHT_PLAIN == generate_diff(
        "tests/fixtures/file3.yaml", "tests/fixtures/file4.yaml", 'plain'
    )