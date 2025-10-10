# Définir la liste initiale
ma_liste = ["T", "O", "A", "p", "t", "p", "l", "o", 
            "e", "s", "t", "t", "r", "s", "t", "t", 
            "t", "u", "m", "m", "p"]

# Supprimer les éléments d'indice impair
nouvelle_liste = []
for index, val in enumerate(ma_liste):
    if index % 2 != 0:
        nouvelle_liste.append(val)
ma_liste = nouvelle_liste
print("Liste après suppression des éléments d'indice impair :", ma_liste)

# Supprimer toutes les lettres "t" restantes
nouvelle_liste = []
for val in ma_liste:
    if val != 't':
        nouvelle_liste.append(val)
ma_liste = nouvelle_liste
print("Liste après suppression de toutes les lettres 't' restantes :", ma_liste)
