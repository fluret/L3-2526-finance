def trouve(tup, element):
    """Renvoie la position de l'élément dans le tuple, ou -1 si l'élément n'est pas trouvé."""
    for index, value in enumerate(tup):
        if value == element:
            return index
    return -1


# Exemple d'utilisation
exemple_tuple = (1, 2, 3, 4, 5)

ELEMENT_A_TROUVER = 3
position = trouve(exemple_tuple, ELEMENT_A_TROUVER)
print(f"La position de l'élément {ELEMENT_A_TROUVER} dans le tuple est : {position}")

ELEMENT_A_TROUVER = 6
position = trouve(exemple_tuple, ELEMENT_A_TROUVER)
print(f"La position de l'élément {ELEMENT_A_TROUVER} dans le tuple est : {position}")
print(exemple_tuple.index(3))
print(exemple_tuple.index(6))
