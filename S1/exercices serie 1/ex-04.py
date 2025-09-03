nom = input("Quel est votre nom ? ")
sexe = input("Quel est votre sexe ? (H/F) ")
if sexe.upper() == 'H':
    print(f"Cher Monsieur {nom}")
elif sexe.upper() == 'F':
    print(f"Chère Madame {nom}")
else:
    print("Sexe non reconnu")
