def check_numbers(seq):
    seen_numbers = set()
    check_results = []

    for number in seq:
        if number in seen_numbers:
            check_results.append((number, "OUI"))
        else:
            check_results.append((number, "NON"))
            seen_numbers.add(number)

    return check_results


# Example usage
sequence = [1, 2, 3, 2, 4, 1, 5]
results = check_numbers(sequence)
for val, result in results:
    print(f'La valeur {val} a déjà été vue: {result}')
