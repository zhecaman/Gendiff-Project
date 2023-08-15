from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain


def format(diff, formatter):
    match formatter:
        case "stylish":
            return make_stylish(diff, level=0)
        case "plain":
            return make_plain(diff)
