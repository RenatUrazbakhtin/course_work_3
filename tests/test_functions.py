import pytest
from src.functions import read_json, check_executed, mask_from
def test_read_json(data):
  """
  тест для функции чтения файла из json
  :return:
  """
  assert read_json("test_operations.json") == data

def test_check_executed(data, executed_expected):
  """
  тест для проверки статуса операции
  :param data:
  :return:
  """
  assert check_executed(data) == executed_expected

def test_mask_from():
  """
  тест для проверки функции mask_from
  :return:
  """
  assert mask_from("Счет 12189246980267075758") == "Счет 1218 92** **** **** 5758"
  assert mask_from("МИР 4878656375033856") == "МИР 4878 65** **** 3856"
  assert mask_from("Visa Platinum 8990850370884895") == "Visa Platinum 8990 85** **** 4895"
  assert mask_from("Visa Gold 3654412434951162") == "Visa Gold 3654 41** **** 1162"
