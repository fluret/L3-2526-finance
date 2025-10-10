import math

def calculer_hypotenuse(a, b):
    """Calcule la longueur de l'hypoténuse d'un triangle rectangle."""
    return math.sqrt(a**2 + b**2)

def calculer_perimetre(a, b, hypotenuse):
    """Calcule le périmètre d'un triangle rectangle."""
    return a + b + hypotenuse

# Demander à l'utilisateur de saisir les longueurs des deux côtés adjacents
a = float(input("Entrez la longueur du premier côté adjacent à l'angle droit : "))
b = float(input("Entrez la longueur du deuxième côté adjacent à l'angle droit : "))

# Calculer l'hypoténuse et le périmètre
hypotenuse = calculer_hypotenuse(a, b)
perimetre = calculer_perimetre(a, b, hypotenuse)

# Afficher les résultats
print(f"La longueur de l'hypoténuse est {hypotenuse}")
print(f"Le périmètre du triangle est {perimetre}")