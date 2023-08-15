import json


SYMBOLS = {"deleted": "  - ", "added": "  + ", "unchanged": "    "}
INDENT = "    "


def stringify_value(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    return value


def stringify(data, level):
    if not isinstance(data, dict):
        return stringify_value(data)
    result = ["{"]
    indent = INDENT * level

    for key, value in data.items():
        if isinstance(value, dict):
            string = f"{indent}{INDENT}{key}: " f"{stringify(value, level+1)}"
            result.append(string)
        else:
            string = f"{indent}{INDENT}{key}: {stringify(value, level)}"
            result.append(string)
    result.append(f"{indent}}}")
    return "\n".join(result)


def format_diff(dictionary, level=0):
    diffs = []
    indent = INDENT * level

    for key, value in dictionary.items():
        type = value.get("type")
        values = value.get("value")
        if type == "dict":
            beg_string = (
                f"{indent}{INDENT}{key}: " f"{{\n{format_diff(values, level+1)}"
            )
            end_string = f"{indent}{INDENT}}}"
            diffs.extend([beg_string, end_string])
        elif type == "changed":
            beg_string = (
                f'{indent}{SYMBOLS["deleted"]}{key}: '
                f'{stringify(values.get("old"), level+1)}'
            )
            end_string = (
                f'{indent}{SYMBOLS["added"]}{key}: '
                f'{stringify(values.get("new"), level+1)}'
            )
            diffs.extend([beg_string, end_string])
        else:
            beg_string = (
                f"{indent}{SYMBOLS[type]}{key}: "
                f"{stringify(values, level+1)}"
            )
            diffs.append(beg_string)

    return "\n".join(diffs)


def make_stylish(diff, level=0):
    result = ["{", format_diff(diff, level), "}"]
    return "\n".join(result)
