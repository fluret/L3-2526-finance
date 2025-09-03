def produit_listes(liste1, liste2):
    resultat = []
    for i in liste1:
        ligne = []
        for j in liste2:
            ligne.append(i * j)
        resultat.append(ligne)
    return resultat

liste1 = [1, 2, 3]
liste2 = [4, 5]

print(produit_listes(liste1, liste2))