def nom_fonction():
    print("Hello World")


nom_fonction()


def nom_fonction2(a):
    print(f'Bonjour {a} !')


nom_fonction2('Alice')


def traite_nom_age(nom, age):
    age_future = age + 10
    resultat = f'Dans 10 ans, {nom} aura {age_future} ans.'
    return resultat


liste_nom_age = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
for nom, age in liste_nom_age:
    print(traite_nom_age(nom, age))