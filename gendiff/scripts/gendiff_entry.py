from ..parser import parse_args, parse_file
from ..gendiff_module import make_diff
from ..formatters.stylish import make_stylish_view

def generate_diff(path1, path2):
    f1 = parse_file(path1)
    f2 = parse_file(path2)
    formatted_data = make_diff(f1, f2)
    return make_stylish_view(formatted_data)

def main():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
