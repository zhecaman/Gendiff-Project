from gendiff.diffmaker import make_diff
from gendiff.formatters.formatter import format
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.gendiff import generate_diff


__all__ = (
    make_plain,
    make_diff,
    make_stylish,
    format,
    generate_diff,
)
