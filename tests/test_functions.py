import pytest
from src.functions import read_json
def test_read_json(data):
  """
  тест для функции чтения файла из json
  :return:
  """
  assert read_json("test_operations.json") == data
