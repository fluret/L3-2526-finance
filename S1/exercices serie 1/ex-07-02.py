annees_a_traiter = [2000, 2013, 2100]

for annee in annees_a_traiter:
    if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
        print(f"L'année {annee} est bissextile.")
    else:
        print(f"L'année {annee} n'est pas bissextile.")
