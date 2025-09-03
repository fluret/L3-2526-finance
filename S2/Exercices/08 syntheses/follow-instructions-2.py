def follow(instructions):
    c = instructions.count
    return c('r') - c('l'), c('f') - c('b')

#**********

follow = lambda i: [i.count(x)-i.count(y) for x, y in ('rl', 'fb')]

#**********

from collections import Counter
from typing import Tuple


def follow(instructions: str) -> Tuple[int]:
    count = Counter(instructions)
    return (count['r'] - count['l'], count['f'] - count['b'])
