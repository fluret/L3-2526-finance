import math


def calculer_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


def calculer_perimetre(a, b):
    return a + b + calculer_hypotenuse(a, b)


def calculer_perimetre2(a, b, c):
    return a + b + c


a = float(input('Entrez la longueur du premier côté : '))
b = float(input('Entrez la longueur du deuxième côté : '))
c = calculer_hypotenuse(a, b)
print(f'La longueur de l\'hypoténuse est {c}.')
print(f'Le périmètre du triangle est {calculer_perimetre(a, b)}.')
print(f'Le périmètre du triangle est {calculer_perimetre2(a, b, c)}.')
