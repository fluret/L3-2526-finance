numbers = [1, 3, 10, 45, 6, 50]

def extract_even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:  # Filtering condition
            even_numbers.append(number)
    return even_numbers

print(extract_even(numbers))