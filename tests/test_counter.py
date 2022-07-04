import pytest

from counter import counter

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
    assert counter.counter(test_input) == expected
