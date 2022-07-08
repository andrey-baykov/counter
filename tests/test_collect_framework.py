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

input_params = [(None, None, 0),
                ('Hello', None, 3),
                (None, '../test_1.txt', 5),
                ('Hello', '../test_2.txt', 7)]


@pytest.mark.parametrize("test_input, expected", params)
def test_counter(test_input, expected):
    assert collect_framework.counter(test_input) == expected


@pytest.mark.parametrize("string, file", parser_params)
def test_read_from_command_line(string, file):
    parser = collect_framework.create_parser()
    parsed = parser.parse_args(['--string', string, '--file', file])
    assert parsed.string == string and parsed.file == file


@pytest.mark.parametrize("string, file_path, expected", input_params)
def test_main_all(string, file_path, expected):
    with mock.patch('counter.collect_framework.get_string_from_file') as mock_data:
        mock_data.return_value = expected
        args = argparse.Namespace(string=string, file=file_path)
        assert collect_framework.main(args) == expected
