import string
from Ex37 import liste_vals
from Test import test

UPPER_TO_LOWER = ord('a') - ord('A')


def cesar(clear, key, encode=True):
    if clear not in string.ascii_letters:
        return clear
    okey = ord(key)
    if key.isupper():
        okey += UPPER_TO_LOWER
    offset = (okey - ord('a') + 1)
    if not encode:
        offset = -offset
    bottom = ord('A') if clear.isupper() else ord('a')
    return chr(bottom + (ord(clear) - bottom + offset) % 26)


test(cesar, liste_vals)
