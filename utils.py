from dicttoxml import dicttoxml


def csv_string_from_dict(data: dict) -> str:
    keys = [*data]
    values = [str(v) for v in data.values()]
    output_str = ','.join(keys)
    output_str += '\n'
    output_str += ','.join(values)
    return output_str


def text_from_dict(data: dict) -> str:
    entries_str_list = []
    for key, value in data.items():
        entries_str_list.append(f"{key}: {value}")
    return ', '.join(entries_str_list)


def xml_from_dict(data: dict) -> str:
    return dicttoxml(data, custom_root='string-analyze-statistics', attr_type=False)
