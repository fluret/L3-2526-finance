# 1. Créer un ensemble vide
ensemble_vide = set()
print(ensemble_vide)

# 2. Créer les ensembles
ensemble_A = {1, 2, 3, 4, 5}
ensemble_B = set([4, 5, 6, 7, 8])

print("Ensemble A:", ensemble_A)
print("Ensemble B:", ensemble_B)

# 3. Ajouter et supprimer des éléments
ensemble_A.add(6)
print("A après ajout de 6:", ensemble_A)

ensemble_A.remove(3)
print("A après suppression de 3:", ensemble_A)

# 4. Union et intersection
union_AB = ensemble_A.union(ensemble_B)
intersection_AB = ensemble_A.intersection(ensemble_B)

print("Union de A et B:", union_AB)
print("Intersection de A et B:", intersection_AB)

union_AB = ensemble_A | ensemble_B
intersection_AB = ensemble_A & ensemble_B

print("Union de A et B:", union_AB)
print("Intersection de A et B:", intersection_AB)
