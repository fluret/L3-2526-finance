def est_pangramme(phrase):
    phrase = phrase.lower()
    lettres = ''
    for car in phrase:
        if car == ' ':
            continue
        if car not in lettres:
            lettres += car
    return len(lettres) == 26


print(est_pangramme("Portez ce vieux whisky au juge blond qui fume"))
