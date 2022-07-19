import argparse
from unittest import mock
import pytest
from src.counter import collect_framework

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


input_params = [(None, None, 0),
                ('Hello', None, 3),
                (None, 'Hello', 3),
                ('Hello', 'Hello world', 6)]


@pytest.mark.parametrize('test_input, expected', params)
def test_counter(test_input, expected):
    assert collect_framework.counter(test_input) == expected


def test_read_from_command_line():
    parser = collect_framework.create_parser('--string hello --file check.txt'.split())
    assert parser.string == 'hello' and parser.file == 'check.txt'


@pytest.mark.parametrize("string, file_data, expected", input_params)
def test_main_all(string, file_data, expected):
    with mock.patch('src.counter.collect_framework.create_parser') as mock_parser:
        with mock.patch('src.counter.collect_framework.get_string_from_file') as mock_data:
            mock_data.return_value = expected
            mock_parser.return_value = argparse.Namespace(string=string, file=file_data)
            assert collect_framework.pipeline() == expected
