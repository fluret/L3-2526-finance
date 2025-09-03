numbers = [10, 15, 20, 25]
divisors = {num: [x for x in range(1, num+1) if num % x == 0] for num in numbers}
print(numbers)
print(divisors)