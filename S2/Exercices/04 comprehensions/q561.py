numbers = [10, 15, 20, 25]
prime_factors = tuple(factor for num in numbers for factor in range(2, num+1) if num % factor == 0 and all(factor % divisor != 0 for divisor in range(2, factor)))
print(numbers)
print(prime_factors)