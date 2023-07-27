from .parser import parse


def generate_diff(f1, f2):
    """Generate difference between two files

    Args:
        filepath1 (str): path to file 1
        filepath2 (str): path to file 2
    """

    keys = sorted(f1.keys() | f2.keys())
    result = dict()
    
    for key in keys:
        if key not in f2:
            result[key] = {
                'type' : 'deleted',
                'value' : f1[key],
                'children' : None,
            }
            
        elif key not in f1:
            result[key] = {
                'type' : 'added',
                'value' : f2[key],
                'children' : None,
            }
            
        elif f1[key] == f2[key]:
            result[key] = {
                'type' : 'unchanged',
                'value' : f1[key],
                'children' : None,
            }
                
        elif isinstance(f1[key], dict) and isinstance(f2[key], dict):
            result[key] = {
                    'type' : 'dict',
                    'value' : None,
                    'children' : generate_diff(f1[key], f2[key]),
                }
        else: 
            result[key] = {
                    'type' : 'changed',
                    'value' : {
                        'old' : f1[key],
                        'new' : f2[key],
                    },
                    'children' : None,
                }
    return result
