n = int(input('Entrez un entier : '))
if n == 0:
    resultat = 1
else:
    resultat = 1
    for i in range(1, n+1):
        resultat *= i
print(f'La factorielle de {n} est {resultat}.')