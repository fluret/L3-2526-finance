from functools import reduce
numbers = [1, 3, 10, 45, 6, 50]

def is_even(number):
    return number % 2 == 0

def somme(a, b):
    return a + b

even_numbers = list(filter(is_even, numbers))
print(reduce(somme, even_numbers))
print(reduce(somme, filter(is_even, numbers)))