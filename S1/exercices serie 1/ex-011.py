# Demander à l'utilisateur de saisir un entier pour la taille du damier
n = int(input("Entrez la taille du damier : "))

# Générer et afficher le damier
for i in range(n):
    ligne = ""
    for j in range(n):
        if (i + j) % 2 == 0:
            ligne += "X"
        else:
            ligne += "O"
    print(ligne)