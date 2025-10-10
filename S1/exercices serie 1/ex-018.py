def multiplie(nombres, n):
    """Renvoie un nouveau tuple obtenu en multipliant chaque élément du tuple par n."""
    retour = []
    for val in nombres:
        retour.append(val * n)
    return tuple(retour)
# Exemple d'utilisation
exemple_tuple = (1, 2, 3, 4, 5)
n = 3
nouveau_tuple = multiplie(exemple_tuple, n)
print(f"Tuple de départ : {exemple_tuple}")
print(f"Le nouveau tuple obtenu en multipliant chaque élément par {n} est : {nouveau_tuple}")