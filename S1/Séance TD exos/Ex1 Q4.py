nom = input("Quel est ton nom ? ")
sexe = input("Es-tu masculin ou féminin ? (M/F) ")

if sexe == "M":
    print(f"Cher Monsieur {nom}")
elif sexe == "F":
    print(f"Chère Madame {nom}")
else:
    print("Genre non reconnu")
