numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print({number**2 if number % 2 == 0 else number**3 for number in numbers})
