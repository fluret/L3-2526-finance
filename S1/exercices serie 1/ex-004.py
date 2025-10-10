# Demander le nom de l'utilisateur
nom = input("Entrez votre nom : ")

# Demander le sexe de l'utilisateur
sexe = input("Entrez votre sexe (M ou F) : ")

# Vérifier le sexe et afficher le message approprié
if sexe.upper() == 'M':
    print(f"Cher Monsieur {nom}")
elif sexe.upper() == 'F':
    print(f"Chère Madame {nom}")
else:
    print("Sexe non reconnu. Veuillez entrer M ou F.")