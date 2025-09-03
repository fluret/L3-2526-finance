from Ex9 import liste
from Test import test


def carre(ligne):
    ligne = ligne.replace(' ', '').replace('\t', '')
    entiers = [int(b) for b in ligne.split(";") if b]
    return ":".join([str(entier**2) for entier in entiers])


test(liste, carre)
