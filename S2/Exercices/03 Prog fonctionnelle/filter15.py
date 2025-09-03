numbers = [1, 3, 10, 45, 6, 50]

def is_even(number):
    return number % 2 == 0

def square(n):
    return n ** 2

even_numbers = list(filter(is_even, numbers))
print(even_numbers)
print(list(map(square, even_numbers)))
print(list(map(square, filter(is_even, numbers))))