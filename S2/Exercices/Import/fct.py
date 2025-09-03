def cherche_ville(ville_a_chercher, dict_pays):
    for pays in dict_pays.keys():
        if ville_a_chercher in dict_pays[pays]:
            return f"{ville_a_chercher} se situe en {pays}"
    return f"{ville_a_chercher} n'est pas dans la liste des villes"