import argparse

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

params_input = [("aa1", "../test_1.txt", 3),
                ("aa1", "../test_2.txt", 7),
                ("aa1", "../test_3.txt", 9),
                ("aa1", None, 1),
                ("hello", None, 3),
                ("'hello world!'", None, 7),
                (None, "../test_1.txt", 3),
                (None, "../test_2.txt", 7),
                (None, "../test_3.txt", 9),
                (None, None, 0)
                ]


@pytest.mark.parametrize("test_input, expected", params)
def test_counter(test_input, expected):
    assert collect_framework.counter(test_input) == expected


@pytest.mark.parametrize("test_input_str, test_input_file, expected", params_input)
def test_main(test_input_str, test_input_file, expected):
    args = argparse.Namespace(string=test_input_str, file_path=test_input_file)
    assert collect_framework.main(args) == expected
