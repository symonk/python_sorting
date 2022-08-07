import typing


def selection_sort(items: typing.MutableSequence[int]):
    """Implementation of selection sort.

    Selection sort is an `in-place` sorting algorithm, in that it does not
    copy or create a new instance of the items passed, instead it mutates
    items directly.  Generally it is inefficient on larger data sets.

    Selection sort can be beneficial when memory is of concern and the space
    complexity is typically O(1) due to the in place mutation, however it is
    largely unused as there are much better alternatives.

    Algorithm Summary
    ==================

    The algorithm initially begins by iterating the entire data set.
        For each iteration, find the minimum value left in the unsorted part.
        It knows that anything prior to the min index is already sorted.



    Big-O Break down
    =================

    Time complexity: O(n^2) due to iterating the unsorted selection fully each iteration.
    Space complexity: O(1) constant.
    """
    for i in range(len(items)):
        min_idx = i
        for j in range(i+1, len(items)):
            if items[min_idx] > items[j]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]

