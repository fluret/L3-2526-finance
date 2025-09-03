def remove_employes(liste, *args):
    for employe in args:
        while employe in liste:
            liste.remove(employe)
    return liste

employes_origine = ["Patrick", "Julie", "Simon", "Paul", "Pauline"]

employes_final = remove_employes(employes_origine, "Patrick", "Paul")
print(employes_final)