# Cette ligne permet d'avoir accès à la fonction randint
# située dans le module random.py
from random import randint

print("Bienvenue sur notre jeu")

while True:
    # On demande un entier aléatoire entre 1 et 100 compris.
    random_value = randint(1, 100)
    # print("Valeur aléatoire choisie :", random_value)
    score = 0
    # Tant que l'entier aléatoire n'a pas été trouvé.
    while True:
        # On demande la saisie d'un entier à partir de la console.
        str_value = input("Veuillez saisir une valeur (1..100) : ")
        if str_value.isdigit():
            value = int(str_value)
            score += 1
        else:
            print("Vous devez saisir un entier !")
            continue
        # On compare l'entier saisi avec la valeur aléatoire.
        if value < random_value:
            print("La valeur à trouver est plus grande !")
        elif value > random_value:
            print("La valeur à trouver est plus petite !")
        else:
            print(f"Gagne en {score} coup(s) !")
            break
    # On demande si l'utilisateur veut une nouvelle partie.
    retry = input("Voulez-vous recommencer (oui, non) : ").lower()
    if retry == "non":
        break
print("Merci à bientôt")
