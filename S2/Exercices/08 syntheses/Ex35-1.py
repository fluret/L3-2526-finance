from Ex35 import liste_vals
from Test import test


def alternat(c1, c2):
    return [element for conteneur in zip(c1, c2) for element in conteneur]


test(alternat, liste_vals)
