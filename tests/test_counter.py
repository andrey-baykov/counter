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


def test_counter():
    for key in params:
        assert counter.counter(key[0]) == key[1]


def test_get_count():
    for key in params:
        assert counter.get_count(key[0]) == key[1]


def test_archive():
    for key in params:
        counter.get_count(key[0])
    assert counter.archive == {'': 0, ' ': 1, 'aaa': 0, 'abb': 1, 'asd  f': 4, 'wweqqrt': 3, 'zzx sdf': 5}
