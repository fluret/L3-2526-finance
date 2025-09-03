from fct import cherche_ville
from data import MESSAGE, pays

while True:
    nom_ville = input(MESSAGE)
    if nom_ville:
        print(cherche_ville(nom_ville, pays))
    else:
        break
