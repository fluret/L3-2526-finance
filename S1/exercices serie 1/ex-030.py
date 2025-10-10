# Lecture de la valeur de n
n = int(input('Indiquer la valeur max de la plage dans laquelle se trouve le nombre à trouver : '))  # Le nombre maximum que peut être le nombre secret

# Initialisation de l'ensemble de tous les nombres possibles
candidats = set(range(1, n + 1))

# Boucle pour traiter les suppositions de Béatrice
while True:
    # Lecture de la supposition ou de la demande d'aide
    entree = input().strip()

    if entree == "AIDE":
        # Béatrice demande de l'aide, on affiche les candidats possibles
        val_restante = []
        for val in sorted(candidats):
            val_restante.append(str(val))
        print(" ".join(val_restante))
        break
    # Béatrice fournit une nouvelle supposition
    supposition = set()
    for val in entree.split():
        supposition.add(int(val))
    # supposition = set(map(int, entree.split()))  # Convertir la supposition en ensemble d'entiers

    # Lecture de la réponse d'Auguste (OUI ou NON)
    reponse = input().strip()

    if reponse == "OUI":
        # Si la réponse est OUI, le nombre secret est dans la supposition
        candidats &= supposition  # On garde seulement les éléments communs
        # candidats.intersection(supposition)  # Alternative pour l'intersection
    elif reponse == "NON":
        # Si la réponse est NON, le nombre secret n'est pas dans la supposition
        candidats -= supposition  # On enlève les éléments de la supposition des candidats
        # candidats.difference(supposition)  # Alternative pour la différence
