from typing import Iterable


def compress(items: list) -> Iterable:
    result = []
    for val in items:
        if result:
            if val != result[-1]:
                result.append(val)
        else:
            result.append(val)
    return result


if __name__ == '__main__':
    assert list(compress([
        5, 5, 5,        4, 5, 6,
        6, 5, 5,        7, 8, 0,  0]
    )) == [5, 4, 5, 6, 5, 7, 8, 0]
    assert list(compress([1, 1, 1, 1, 2, 2,
                          2, 1, 1, 1]
                         )) == [1, 2, 1]
    assert list(compress([7, 7])) == [7]
    assert list(compress([])) == []
    assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
    assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
