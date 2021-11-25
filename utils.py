from dicttoxml import dicttoxml


def csv_string_from_dict(data: dict) -> str:
    keys = [*data]
    values = [str(v) for v in data.values()]
    output_str = ','.join(keys)
    output_str += '\n'
    output_str += ','.join(values)
    return output_str


def text_from_dict(data: dict) -> str:
    pass


def xml_from_dict(data: dict) -> str:
    pass
