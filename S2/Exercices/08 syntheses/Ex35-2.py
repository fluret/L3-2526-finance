from Ex35 import liste_vals
from Test import test
from aplatir import aplatir


def alternat(c1, c2):
    return aplatir(zip(c1, c2))


test(alternat, liste_vals)
