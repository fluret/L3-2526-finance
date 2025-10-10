# Définir la liste initiale
ma_liste = ["T", "O", "A", "p", "t", "p", "l", "o", "e", "s", "t", "t", "r", "s", "t", "t", "t", "u", "m", "m", "p"]

# Supprimer les éléments d'indice pair
ma_liste = [val for index, val in enumerate(ma_liste) if index % 2 != 0]
print("Liste après suppression des éléments d'indice pair :", ma_liste)

# Supprimer toutes les lettres "t" restantes
ma_liste = [val for val in ma_liste if val != 't']
print("Liste après suppression de toutes les lettres 't' restantes :", ma_liste)