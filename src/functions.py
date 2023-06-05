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

def mask_from(input_from_account: str):
    """
    форматирует строку в формат: первые 6 цифр читаемые, последние 4 цифры читаемые, остальные символы "*", разделены по пробелам
    :param input_from_account:
    :return: форматированную строку
    """
    from_account_split = input_from_account.split(" ")
    if len(from_account_split) == 2:
        if len(from_account_split[1]) == 16:
            str = " " + from_account_split[-1][0:4] + " " + from_account_split[-1][4:6] + "** " + "**** " + from_account_split[-1][12:]
        elif len(from_account_split[1]) == 20:
            str = " " + from_account_split[-1][0:4] + " " + from_account_split[-1][4:6] + "** " + "**** " + "**** " + from_account_split[-1][16:]
        else:
            return "Cannot identify account from"
        return from_account_split[0] + str
    if len(from_account_split) == 3:
        if len(from_account_split[2]) == 16:
            str = ' ' + from_account_split[-1][0:4] + ' ' + from_account_split[-1][4:6] + '** ' + '**** ' + from_account_split[-1][12:]
        elif len(from_account_split[2]) == 20:
            str = " " + from_account_split[1][0:4] + " " + from_account_split[1][4:6] + "** " + "**** " + "**** " + from_account_split[1][16:]
        else:
            return "Cannot identify account from"
        return from_account_split[0] + " " + from_account_split[1] + str