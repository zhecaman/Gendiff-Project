import json


def generate_diff(filepath1, filepath2):
    """Generate difference between two files

    Args:
        filepath1 (str): path to file 1
        filepath2 (str): path to file 2
    """    

    def decapitalize(string):
        """To convert python boolean to js"""
        if not string:
            return string
        return string[0].lower() + string[1:]

    output = "{\n"

    def make_diff(f1, f2):
        """takes two objects and returns list of formatted strings based on
        files key-value  difference
        """
        result = []

        for key1 in f1.keys():
            if isinstance(f1[key1], bool):
                f1[key1] = decapitalize(str(f1[key1]))

            if key1 in f2.keys() and f1[key1] == f2[key1]:
                formatted = f"  {key1}: {f1[key1]}"
                result.append(formatted)
            elif key1 not in f2.keys():
                formatted = f"- {key1}: {f1[key1]}"
                result.append(formatted)
            elif key1 in f2.keys() and f1[key1] != f2[key1]:
                formatted = f"- {key1}: {f1[key1]}"
                formatted2 = f"+ {key1}: {f2[key1]}"
                result.append(formatted)
                result.append(formatted2)
        for key2 in f2.keys():
            if isinstance(f2[key2], bool):
                f2[key2] = decapitalize(str(f2[key2]))
            if key2 not in f1.keys():
                formatted = f"+ {key2}: {f2[key2]}"
                result.append(formatted)
        return sorted(result, key=lambda x: x[2])

    with open(filepath1) as f1, open(filepath2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
        formatted_data = make_diff(data1, data2)
        output += "\n".join(formatted_data)
    return output + "\n}"
