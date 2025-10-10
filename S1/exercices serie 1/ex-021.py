liste = [17, 38, 10, 25, 72]
# 1
liste.sort()
print(f"Liste triée : {liste}")
# 2
liste.append(12)
print(f"Liste après ajout de 12 : {liste}")
# 3
liste.reverse()
print(f"Liste renversée : {liste}")
# 4
indice_17 = liste.index(17)
print(f"Indice de l'élément 17 : {indice_17}")
# 5
liste.remove(38)
print(f"Liste après suppression de 38 : {liste}")
# 6
sous_liste_2_3 = liste[1:3]
print(f"Sous-liste du 2e au 3e élément : {sous_liste_2_3}")
# 7
sous_liste_debut_2 = liste[:2]
print(f"Sous-liste du début au 2e élément : {sous_liste_debut_2}")
# 8
sous_liste_3_fin = liste[2:]
print(f"Sous-liste du 3e élément à la fin : {sous_liste_3_fin}")
# 9
sous_liste_complete = liste[:]
print(f"Sous-liste complète : {sous_liste_complete}")
# 10
dernier_element = liste[-1]
print("Dernier élément : {dernier_element}")