def synthese_familles(**kwargs):
    # On commence par créer un dictionnaire pour ranger les résultats
    synthese = {}
    # On traite chaque compte
    for c in kwargs.values():
        # Si le nom de famille n'a pas encore été trouvé
        if c["nom"] not in synthese:
            # On le crée dans le dictionnaire des résultats
            synthese[c["nom"]] = 0
        # Si l'épargne est présente dans le compte...
        if "epargne" in c:
            # On peut alors la rajouter au résultat
            synthese[c["nom"]] += c["epargne"]
    # Trouver le plus pauvre et le plus riche
    pauvre = min(synthese, key=synthese.get)
    riche = max(synthese, key=synthese.get)

    # On retourne les informations récupérées
    return (pauvre, synthese[pauvre]), (riche, synthese[riche])

# Test de la fonction
comptes = {
    "cpt1": {"nom": "Boismoneau", "prenom": "stephane", "epargne": 2500},
    "cpt2": {"nom": "Jambon", "prenom": "fred", "epargne": 5000},
    "cpt3": {"nom": "Durois", "prenom": "nicolas", "epargne": 10000},
    "cpt4": {"nom": "Gueux", "prenom": "phillipe", "epargne": 1250},
    "cpt5": {"nom": "Duchan", "prenom": "alice", "epargne": 4530},
    "cpt6": {"nom": "Lepenou", "prenom": "amed", "epargne": 2200},
    "cpt7": {"nom": "Gueux", "prenom": "bernard"},
    "cpt8": {"nom": "Jambon", "prenom": "steven", "epargne": 1670},
    "cpt9": {"nom": "Gueux", "prenom": "sylvie", "epargne": 3},
    "cpt10": {"nom": "Durois", "prenom": "berbard", "epargne": 300000},
}
print(synthese_familles(**comptes))
