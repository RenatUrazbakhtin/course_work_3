import json


def read_json(filename):
    """
    перевод файла с читаемый для Python формат
    :param filename:
    :return: читаемый файл из Json
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data