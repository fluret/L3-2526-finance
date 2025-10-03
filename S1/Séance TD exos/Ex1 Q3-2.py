age = input("Quel âge as-tu ? ")
age = int(age)

message = "Tu fais partie du groupe "

if age < 8:
    message ="Trop jeune"
elif age < 10:
    message = f'{message}U8'
elif age < 12:
    message = f'{message}U10'
elif age < 14:
    message = f'{message}U12'
elif age < 16:
    message = f'{message}U14'
else:
    message = "Trop vieux"

print(message)