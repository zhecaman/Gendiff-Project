from gendiff.gendiff_module import make_diff
from gendiff.formatters.formatter import format
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain


__all__ = (make_plain, make_diff, make_stylish, format,)
