from typing import Tuple

def follow(instructions: str) -> Tuple[int, int]:
    result = [0,0]
    for car in instructions:
        if car == "f":
            result[1] += 1
        elif car == "b":
            result[1] -= 1
        elif car == "l":
            result[0] -= 1
        else:
            result[0] += 1
    return tuple(result)


if __name__ == '__main__':
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
