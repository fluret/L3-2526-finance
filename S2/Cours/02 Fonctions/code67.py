def avg(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args)

print(avg(1, 2, 3))
print(avg(1, 2, 3, 4, 5))