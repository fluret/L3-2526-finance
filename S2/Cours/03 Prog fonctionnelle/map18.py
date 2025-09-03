def powers(x):
    return x ** 2, x ** 3

numbers = [1, 2, 3, 4]
print(list(map(powers, numbers)))