def searchl3(elements, liste):
    resultat = []
    indexs = []
    for element in elements:
        for index, valeur in enumerate(liste):
            if element == valeur:
                indexs.append(index)
        resultat.append(indexs[:])
        indexs.clear()
    return resultat


liste_avec_doublons = [1, 2, 3, 4, 5, 3, 2, 1, 6, 7, 8, 6, 9, 10, 9]

liste_recherche = [3, 6, 9, 12]

print(searchl3(liste_recherche, liste_avec_doublons))
