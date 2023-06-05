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

def check_executed(data:list[dict]):
    """
    Проверка словарей по статусу выполнения executed
    :param data:
    :return: список словарей со статусом executed
    """
    executed_list = []
    for item in data:
        if "state" in item.keys():
            if item["state"] == "EXECUTED":
                executed_list.append(item)
        else:
            continue
    return executed_list
