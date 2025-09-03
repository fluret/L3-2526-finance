numbers = [1, 3, 10, 45, 6, 50]

def is_even(number):
    return number % 2 == 0  # Filtering condition

print(list(filter(is_even, numbers)))