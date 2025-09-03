n = int(input('Entrez un entier : '))

produit = 1

for i in range(1, n+1):
    if i % 2 == 0:
        produit *= i
print(f'Le produit des nombres pairs entre 1 et {n} est {produit}.')