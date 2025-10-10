# Créer une variable age contenant la valeur 81
age = 81
print(f'Adresse mémoire de age {id(age)}')

# Créer un tuple nommé personne
personne = ("Dupont", "Maurice", age, 25, 59000)

# Accéder à la première valeur du tuple personne
premiere_valeur = personne[0]
print(f"La première valeur du tuple personne est : {premiere_valeur}")

# Effectuer l'instruction personne[2]
valeur_age = personne[2]
print(f'Adresse mémoire de personne[2] {id(personne[2])}')

print(f"La valeur de personne[2] est : {valeur_age}")

# Modifier la valeur de la variable age
age = 82
print(f'Adresse mémoire de age {id(age)}')

# Effectuer à nouveau l'instruction personne[2]
valeur_age_modifiee = personne[2]
print(f'Adresse mémoire de personne[2] {id(personne[2])}')
print(f"Après modification de la variable age, la valeur de personne[2] est toujours : {valeur_age_modifiee}")