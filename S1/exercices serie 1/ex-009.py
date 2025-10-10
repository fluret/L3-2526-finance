# Demander à l'utilisateur de saisir un entier
n = int(input("Entrez un entier pour calculer sa factorielle : "))

# Calculer la factorielle de n
if n == 0:
    resultat = 1
else:
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i

# Afficher la factorielle de n
print(f"La factorielle de {n} est {resultat}")