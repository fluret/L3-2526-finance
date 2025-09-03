from math import prod
def checkio(number: int) -> int:
    return prod([int(val) for val in str(number) if val !='0'])




assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1
assert checkio(999999) == 531441
assert checkio(1) == 1
assert checkio(9) == 9
assert checkio(736635) == 11340
assert checkio(375251) == 1050
assert checkio(778241) == 3136
assert checkio(930154) == 540
assert checkio(306026) == 216
assert checkio(194325) == 1080
assert checkio(376087) == 7056
assert checkio(550643) == 1800
assert checkio(90160) == 54
assert checkio(232177) == 588
assert checkio(951216) == 540
assert checkio(273438) == 4032
assert checkio(256991) == 4860
assert checkio(542929) == 6480
assert checkio(399996) == 118098
assert checkio(929806) == 7776
assert checkio(638332) == 2592