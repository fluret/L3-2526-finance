letters = ["a", "b", "c"]
numbers = [0, 1, 2]
operators = ["*", "/", "+"]
for let, num, op in zip(letters, numbers, operators):
    print(f"Letter: {let}")
    print(f"Number: {num}")
    print(f"Operator: {op}")