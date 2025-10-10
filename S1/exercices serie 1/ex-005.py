# Demander les deux entiers A et B
A = int(input("Entrez l'entier A : "))
B = int(input("Entrez l'entier B : "))

# Calculer le quotient et le reste de la division euclidienne
quotient = A // B
reste = A % B

# Afficher le quotient et le reste
print(f"Le quotient de la division de {A} par {B} est {quotient}")
print(f"Le reste de la division de {A} par {B} est {reste}")