def make_diff(f1, f2):
    keys = sorted(f1.keys() | f2.keys())
    result = dict()

    for key in keys:
        if key not in f2:
            result[key] = {
                "type": "deleted",
                "value": f1[key],
            }

        elif key not in f1:
            result[key] = {
                "type": "added",
                "value": f2[key],
            }

        elif f1[key] == f2[key]:
            result[key] = {
                "type": "unchanged",
                "value": f1[key],
            }

        elif isinstance(f1[key], dict) and isinstance(f2[key], dict):
            result[key] = {
                "type": "dict",
                "value": make_diff(f1[key], f2[key]),
            }
        else:
            result[key] = {
                "type": "changed",
                "value": {
                    "old": f1[key],
                    "new": f2[key],
                },
            }
    return result
