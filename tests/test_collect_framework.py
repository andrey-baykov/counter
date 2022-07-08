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

parser_params = [(None, None),
                 ('Hello', None),
                 (None, 'world'),
                 ('Hello', 'world')]


@pytest.mark.parametrize("test_input, expected", params)
def test_counter(test_input, expected):
    assert collect_framework.counter(test_input) == expected


@pytest.mark.parametrize("string, file", parser_params)
def test_read_from_command_line(string, file):
    parser = collect_framework.create_parser()
    parsed = parser.parse_args(['--string', string, '--file', file])
    assert parsed.string == string and parsed.file == file


@mock.patch('counter.collect_framework.get_string_from_file', return_value=7)
def test_main_full(mock_data):
    args = argparse.Namespace(string="hello", file=mock_data)
    assert collect_framework.main(args) == 7


@mock.patch('counter.collect_framework.get_string_from_file', return_value=5)
def test_main_string(mock_data):
    args = argparse.Namespace(string="hello", file=None)
    assert collect_framework.main(args) == 3


@mock.patch('counter.collect_framework.get_string_from_file', return_value=5)
def test_main_file(mock_data):
    args = argparse.Namespace(string=None, file=mock_data)
    assert collect_framework.main(args) == 5


@mock.patch('counter.collect_framework.get_string_from_file', return_value=3)
def test_main_none(mock_data):
    args = argparse.Namespace(string=None, file=None)
    assert collect_framework.main(args) == 0
