from gendiff.diffmaker import make_diff
from gendiff.formatters.formatter import format
from gendiff.parser import read_file


def generate_diff(path1, path2, formatter="stylish"):
    file1 = read_file(path1)
    file2 = read_file(path2)
    diff = make_diff(file1, file2)
    return format(diff, formatter)
