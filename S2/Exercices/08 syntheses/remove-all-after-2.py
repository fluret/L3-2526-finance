def remove_all_after(items: list, border: int) -> list:
    try:
        return items[: items.index(border) + 1]
    except ValueError:
        return items
#**********

def remove_all_after(items, border):
    return items[:items.index(border) + 1 if border in items else None]

#**********

from typing import Iterable, List


def remove_all_after(items: List, border: int) -> Iterable:
    for item in items:
        yield item
        if item == border:
            return
