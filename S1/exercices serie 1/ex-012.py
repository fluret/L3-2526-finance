# Demander à l'utilisateur de saisir un entier pour la taille du damier
n = int(input("Entrez la taille du damier : "))

# Demander à l'utilisateur de saisir un entier pour la taille des cases
c = int(input("Entrez la taille des cases : "))

# Générer et afficher le damier
for i in range(n):
    for k in range(c):  # Répéter chaque ligne c fois pour la hauteur des cases
        ligne = ""
        for j in range(n):
            if (i + j) % 2 == 0:
                ligne += "X" * c  # Répéter le caractère c fois pour la largeur des cases
            else:
                ligne += "O" * c
        print(ligne)
