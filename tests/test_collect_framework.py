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

input_params = [(None, None, 0),
                ('Hello', None, 3),
                (None, 'Hello', 3),
                ('Hello', 'Hello world', 6)]


@pytest.mark.parametrize('test_input, expected', params)
def test_counter(test_input, expected):
    assert collect_framework.counter(test_input) == expected


@mock.patch('counter.collect_framework.argparse')
def test_read_from_command_line(mock_argparse):
    # Создаю мок для функции parse_args и она должна вернуть Namespace
    mock_argparse.parse_args.return_value = argparse.Namespace(string='Hello', file='test.txt')
    # После выполнения create_parser(), мы должны получить наш Namespace, как это
    # происходит при обычном запуске кода.
    # но приходит обьект мок в котором я не могу найти string и file
    parser = collect_framework.create_parser()
    # Получаем ошибку,
    # AssertionError: assert (<MagicMock name='argparse.ArgumentParser().parse_args().parse_args.string' id='4403083776'> == 'Hello'
    assert parser.parse_args.string == "Hello" and parser.file == "test.txt"


@pytest.mark.parametrize("string, file_data, expected", input_params)
def test_main_all(string, file_data, expected):
    with mock.patch('counter.collect_framework.create_parser') as mock_parser:
        with mock.patch('counter.collect_framework.get_string_from_file') as mock_data:
            mock_data.return_value = expected
            mock_parser.return_value = argparse.Namespace(string=string, file=file_data)
            assert collect_framework.main() == expected
