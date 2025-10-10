# Tableau des jours de la semaine
jours_semaine = ["Lundi", "Mardi", "Mercredi",
    "Jeudi", "Vendredi", "Samedi", "Dimanche",]

# Tableau des mois de l'année
mois_annee = ["Janvier", "Février", "Mars", "Avril",
    "Mai", "Juin", "Juillet", "Août", "Septembre",
    "Octobre", "Novembre", "Décembre",]

# Tableau du nombre de jours dans chaque mois (année bissextile)
jours_par_mois = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Le 1er janvier 2020 est un mercredi (indice 2 dans la liste des jours)
jour_index = 2

# Parcours de chaque mois
for i in range(12):
    mois = mois_annee[i]
    jours_dans_ce_mois = jours_par_mois[i]

    # Parcours des jours du mois
    for jour in range(1, jours_dans_ce_mois + 1):
        # Affichage de la date
        print(f"{jours_semaine[jour_index]} {jour} {mois} 2020")

        # Incrémentation du jour de la semaine
        jour_index = (jour_index + 1) % 7
