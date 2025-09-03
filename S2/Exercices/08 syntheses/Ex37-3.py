def test(fonction, liste):
    """_summary_

    Args:
        fonction (_type_): _description_
        liste (_type_): _description_
    """
    for l in liste:
        if len(l) == 2:
            a, b = l
            print(f"La fonction cesar({a}, {b}) renvoie : {fonction(a, b)}")
        else:
            a, b, c = l
            if type(c) == dict:
                [(d, e)] = c.items()
                print(
                    f"La fonction cesar({a}, {b}, {d}={e}) renvoie : {fonction(a, b, **c)}")
            else:
                print(
                    f"La fonction cesar({a}, {b}, {c}) renvoie : {fonction(a, b, c)}")
