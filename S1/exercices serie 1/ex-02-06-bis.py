n = int(input('Entrez la taille du damier : '))

damier = []
for i in range(n):
    ligne = []
    for j in range(n):
        if (i+j) % 2 == 0:
            ligne.append('X')
        else:
            ligne.append('O')
    damier.append(ligne)


