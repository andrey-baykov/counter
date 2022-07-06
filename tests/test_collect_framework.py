import argparse
from unittest import mock
import pytest
from counter import collect_framework

params = [("aaa", 0),
          ("abb", 1),
          ("wweqqrt", 3),
          ("", 0),
          (" ", 1),
          ("asd  f", 4),
          ("zzx sdf", 5),
          ("aaa", 0),
          ("wweqqrt", 3),
          ("", 0),
          (" ", 1),
          ("asd  f", 4)
          ]


@pytest.mark.parametrize("test_input, expected", params)
def test_counter(test_input, expected):
    assert collect_framework.counter(test_input) == expected


@mock.patch('counter.collect_framework.get_string_from_file', return_value=7)
def test_main_full(file_data):
    args = argparse.Namespace(string="hello", file=file_data)
    assert collect_framework.main(args) == 7


@mock.patch('counter.collect_framework.get_string_from_file', return_value=5)
def test_main_string(file_data):
    args = argparse.Namespace(string="hello", file=None)
    assert collect_framework.main(args) == 3


@mock.patch('counter.collect_framework.get_string_from_file', return_value=5)
def test_main_file(file_data):
    args = argparse.Namespace(string=None, file=file_data)
    assert collect_framework.main(args) == 5


@mock.patch('counter.collect_framework.get_string_from_file', return_value=3)
def test_main_none(file_data):
    args = argparse.Namespace(string=None, file=None)
    assert collect_framework.main(args) == 0
