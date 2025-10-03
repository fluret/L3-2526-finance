age = input("Quel âge as-tu ? ")
age = int(age)

if age >= 8 and age < 10:
    groupe = "U8"
elif age >= 10 and age < 12:
    groupe = "U10"
elif age >= 12 and age < 14:
    groupe = "U12"
elif age >= 14 and age < 16:
    groupe = "U14"

print(f'Tu fais partie du groupe {groupe}.')