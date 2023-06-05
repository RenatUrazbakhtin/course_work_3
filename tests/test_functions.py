import pytest
from src.functions import read_json, check_executed
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
