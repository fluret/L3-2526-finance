def test(liste, ma_fonction):
    for l in liste:
        print(f"Chaine à traiter : |{l}|\n"
              f"donne le résultat : {ma_fonction(l)!r:>50} \n"
              f"{20*'*'}"
              )