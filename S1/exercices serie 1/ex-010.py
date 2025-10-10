# Demander à l'utilisateur de saisir un entier
n = int(input("Entrez un entier : "))

# Initialiser le produit des nombres pairs
produit = 1

# Calculer le produit des nombres pairs entre 1 et n
for i in range(1, n + 1):
    if i % 2 == 0:
        produit *= i

# Afficher le produit des nombres pairs
print(f"Le produit des nombres pairs entre 1 et {n} est {produit}")