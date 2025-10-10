def searchL(element, liste):
    for index, value in enumerate(liste):
        if value == element:
            return index
    return False

# Exemple d'utilisation
ma_liste = [10, 20, 30, 40, 50]
element_a_trouver = 30
resultat = searchL(element_a_trouver, ma_liste)
print(f"L'indice de l'élément {element_a_trouver} dans la liste est : {resultat}")

element_a_trouver = 60
resultat = searchL(element_a_trouver, ma_liste)
print(f"L'indice de l'élément {element_a_trouver} dans la liste est : {resultat}")