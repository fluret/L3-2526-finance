# 5. Différence
difference_AB = ensemble_A.difference(ensemble_B)
difference_AB = ensemble_A - ensemble_B
print("Différence de A par rapport à B:", difference_AB)
# 6. création des deux ensembles pour les tets d'inclusion
set_num1 = {1, 5, 6}
set_num2 = {2, 4, 6}

# 7. Test d'inclusion
est_sous_ensemble = set_num1.issubset(ensemble_A)
est_sur_ensemble = ensemble_A.issuperset(set_num2)

print("B est un sous-ensemble de A:", est_sous_ensemble)
print("A est un sur-ensemble de B:", est_sur_ensemble)

# 8. Test d'appartenance

print("6 appartient à A:", 6 in ensemble_A)
print("3 n'appartient pas à A:", 3 not in ensemble_A)
print("3 appartient à B:", 3  in ensemble_B)

# 9. Suppression de doublons dans une liste
liste = [1, 2, 2, 3, 4, 4, 5]
print("Liste avec doublons:", liste)
liste = list(set(liste))

print("Liste sans doublons:", liste)
