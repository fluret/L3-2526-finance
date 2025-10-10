# Définir la chaîne de commandes de petits pains
COMMANDES = """Amandine 6;Amélie 9;Cécile 5;Camille 10;Roland 6;
            Sebastien 3;David 9;Robin 20;Cédric 1;Kevin 10;Tim 1"""

# Diviser la chaîne en une liste de commandes individuelles
commandes_list = COMMANDES.split(";")
print(commandes_list)
for num_commande, commande in enumerate(commandes_list):
    commandes_list[num_commande] = commande.split()
print("Liste des commandes :", commandes_list)
# Calculer le nombre total de petits pains commandés
TOTAL_PAINS = 0

for commande in commandes_list:
    TOTAL_PAINS += int(commande[1])

# Afficher la liste de listes et le nombre total de petits pains commandés
print("Nombre total de petits pains commandés :", TOTAL_PAINS)
