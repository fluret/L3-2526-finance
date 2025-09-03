def test(fonction, liste):
    for l in liste:
        a, b = l
        print(f"La fonction alternat({a}, {b}) renvoie  -> {fonction(a, b)}")
