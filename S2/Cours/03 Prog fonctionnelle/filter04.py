def identity(x):
    return x
print(identity(42))
objects = [0, 1, [], 4, 5, "", None, 8]
print(list(filter(identity, objects)))