from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
    if items:
        items = items[items.index(border):] if (border in items) else items
    return items

assert remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
assert remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]
assert remove_all_before([1, 1, 2, 4, 2, 3, 4], 2) == [2, 4, 2, 3, 4]
assert remove_all_before([1, 1, 5, 6, 7], 2) == [1, 1, 5, 6, 7]
assert remove_all_before([], 0) == []
assert remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
assert remove_all_before([10, 1, 5, 6, 7, 10], 5) == [5, 6, 7, 10]
assert remove_all_before([1, 2, 6, 7, 1, 2, 4, 6, 7, 8, 3, 5, 2, 3], 6) == [6, 7, 1, 2, 4, 6, 7, 8, 3, 5, 2, 3]

