import random

from algorithms import selection_sort


def test_selection_sort():
    expected = list(range(10_000))
    actual = expected.copy()
    random.shuffle(actual)
    selection_sort(actual)
    assert actual == expected
