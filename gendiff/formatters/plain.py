import json

MESSAGES = {
    "changed": "Property '{path}' was updated. From {old_val} to {new_val}",
    "deleted": "Property '{path}' was removed",
    "added": "Property '{path}' was added with value: {value}",
}


def prepare_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    return json.dumps(value)


def get_path(key, previous_path=""):
    if previous_path:
        return previous_path + f".{key}"
    return key


def format_plain(diff, previous_path):
    messages = []
    for key, types in diff.items():
        path = get_path(key, previous_path)
        state = types.get("type")
        value = types.get("value")
        if state == "dict":
            messages.append(format_plain(value, path))
        elif state == "changed":
            old_val = prepare_value(value.get("old"))
            new_val = prepare_value(value.get("new"))
            message = MESSAGES[state].format(
                path=path, old_val=old_val, new_val=new_val
            )
            messages.append(message)
        elif state == "added":
            value = prepare_value(types.get("value"))
            message = MESSAGES[state].format(path=path, value=value)
            messages.append(message)
        elif state == "deleted":
            message = MESSAGES[state].format(path=path)
            messages.append(message)
    return "\n".join(messages)


def make_plain(diff):
    return format_plain(diff, previous_path="")
