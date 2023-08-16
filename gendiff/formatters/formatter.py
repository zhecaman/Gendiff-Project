from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json import make_json


def format(diff, formatter):
    match formatter:
        case "stylish":
            return make_stylish(diff, level=0)
        case "plain":
            return make_plain(diff)
        case "json":
            return make_json(diff)
