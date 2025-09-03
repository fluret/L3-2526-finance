from itertools import chain
import string
from Ex37 import liste_vals
from Test import test


ENCODED_LOWER_LOWER = {
    (c, k): chr((ord(c) - 97 + ord(k) - 96) % 26 + 97)
    for c in string.ascii_lowercase
    for k in string.ascii_lowercase
}

ENCODED_LOWER_UPPER = {
    (c, k): ENCODED_LOWER_LOWER[(c, k.lower())]
    for c in string.ascii_lowercase
    for k in string.ascii_uppercase
}

ENCODED_UPPER = {
    (c.upper(), k): value.upper()
    for (c, k), value in chain(ENCODED_LOWER_LOWER.items(),
                               ENCODED_LOWER_UPPER.items())
}

ENCODE_LOOKUP = {}
ENCODE_LOOKUP.update(ENCODED_LOWER_LOWER)
ENCODE_LOOKUP.update(ENCODED_LOWER_UPPER)
ENCODE_LOOKUP.update(ENCODED_UPPER)

DECODE_LOOKUP = {
    (encoded, key): clear for (clear, key), encoded
    in ENCODE_LOOKUP.items()
}


def cesar(clear, key, encode=True):
    lookup = ENCODE_LOOKUP if encode else DECODE_LOOKUP
    return lookup.get((clear, key), clear)


test(cesar, liste_vals)
