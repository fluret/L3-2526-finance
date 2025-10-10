def separe(nombres):
    """Renvoie un tuple contenant deux tuples : les entiers pairs et les entiers impairs."""
    pairs = []
    impairs = []
    for val in nombres:
        if val % 2 == 0:
            pairs.append(val)
        else:
            impairs.append(val)
    return (tuple(pairs), tuple(impairs))

# Exemple d'utilisation
exemple_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
resultat = separe(exemple_tuple)
print(f"Tuple de départ : {exemple_tuple}")
print(f"Tuple des entiers pairs : {resultat[0]}")
print(f"Tuple des entiers impairs : {resultat[1]}")