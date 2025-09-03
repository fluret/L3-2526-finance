annee = int(input("Entrez une année : "))

if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
    print(f"L'année {annee} est bissextile.")
else:
    print(f"L'année {annee} n'est pas bissextile.")