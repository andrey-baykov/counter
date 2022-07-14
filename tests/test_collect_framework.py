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
                 ("Hello", None),
                 (None, 'test.txt'),
                 ("Hello", 'test.txt')
                 ]

input_params = [(None, None, 0),
                ('Hello', None, 3),
                (None, 'Hello', 3),
                ('Hello', 'Hello world', 6)]


@pytest.mark.parametrize('test_input, expected', params)
def test_counter(test_input, expected):
    assert collect_framework.counter(test_input) == expected


@pytest.mark.parametrize('test_input, file_path', parser_params)
def test_read_from_command_line(test_input, file_path):
    parser = collect_framework.create_parser(test_input, file_path)
    assert parser.string == test_input and parser.file == file_path


@pytest.mark.parametrize("string, file_data, expected", input_params)
def test_main_all(string, file_data, expected):
    with mock.patch('counter.collect_framework.create_parser') as mock_parser:
        with mock.patch('counter.collect_framework.get_string_from_file') as mock_data:
            mock_data.return_value = expected
            mock_parser.return_value = argparse.Namespace(string=string, file=file_data)
            assert collect_framework.main() == expected
