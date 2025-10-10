def produit_tableaux(tab1, tab2):
    resultat = []
    for i in range(len(tab1)):
        ligne = []
        for j in range(len(tab2)):
            ligne.append(tab1[i] * tab2[j])
        resultat.append(ligne)
    return resultat

# Exemple d'utilisation
tab1 = [2, 3]
tab2 = [4, 5]

tableau_2d = produit_tableaux(tab1, tab2)
print(tableau_2d)
