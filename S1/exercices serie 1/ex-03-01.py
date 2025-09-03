age = int(input("Quel est l'âge du joueur ?"))
texte = "Le joueur est dans le groupe U"
if 8 <= age < 10:
    print(f'{texte}8')
elif 10 <= age < 12:
    print(f'{texte}10')
elif 12 <= age < 14:
    print(f'{texte}12')
elif 14 <= age < 16:
    print(f'{texte}14')
else:
    print("Age hors catégorie")
