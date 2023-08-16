from gendiff.diffmaker import make_diff
from gendiff.formatters.formatter import format
from gendiff.parser import parse_file


def generate_diff(path1, path2, formatter="stylish"):
    f1 = parse_file(path1)
    f2 = parse_file(path2)
    diff = make_diff(f1, f2)
    return format(diff, formatter)
