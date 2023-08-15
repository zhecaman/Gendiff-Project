from gendiff.parser import parse_args, parse_file
from gendiff.gendiff_module import make_diff
from gendiff.formatters.formatter import format


def generate_diff(path1, path2, formatter="stylish"):
    f1 = parse_file(path1)
    f2 = parse_file(path2)
    diff = make_diff(f1, f2)
    return format(diff, formatter)


def main():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
