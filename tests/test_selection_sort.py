import random

from algorithms import selection_sort


def test_selection_sort():
    expected = list(range(1_000_000))
    actual = expected.copy()
    random.shuffle(actual)
    assert selection_sort(actual) == expected
