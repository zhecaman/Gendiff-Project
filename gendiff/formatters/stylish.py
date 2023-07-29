import json


SYMBOLS = {
    'deleted' : '  - ',
    'added' : '  + ',
    'unchanged' : '    '
}

def stringify(data, level=1):
    result = '{\n'
    indent = '    '

    if isinstance(data, str):
        return data
    if isinstance(data, bool):
        return 'true' if data else 'false'
    if isinstance(data, dict):
        for key, value in data.items():
            result += f'{indent*level}{key}: '
            result += f'{stringify(value, level+1)}\n'
        result += f'{indent*(level-1)}}}'
        return result
    else:
        return json.dumps(data)


def make_stylish_view(dictionary, level=1):
    result = '{\n'
    level += 1

    for key, value in dictionary.items():
        indent = '....' * (level-1)
        type = value.get('type')
        values = value.get('value')
        children = value.get('children')

        if type in ('added', 'deleted', 'unchanged'):
            result += f'{indent}{SYMBOLS[type]}{key}: '
            result += f'{stringify(values, level+1)}\n'
        elif type == 'changed':
            result += f'{indent}{SYMBOLS["deleted"]}{key}: '
            result += f'{stringify(values.get("old"), level+1)}\n'
            result += f'{indent}{SYMBOLS["added"]}{key}: '
            result += f'{stringify(values.get("new"), level+1)}\n'
        elif type == 'dict':
            result += f'{indent*2}{key}: '
            result += f'{make_stylish_view(children, level)}\n'
    return result





