numbers = [-2, -1, 0, 1, 2]

# Using a lambda function
positive_numbers = filter(lambda n: n > 0, numbers)
print(positive_numbers)
print(list(positive_numbers))

# Using a user-defined function
def is_positive(n):
    return n > 0

print(list(filter(is_positive, numbers)))