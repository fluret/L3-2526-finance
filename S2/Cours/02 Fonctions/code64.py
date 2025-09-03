def avg(a):
    total = 0
    for v in a:
        total += v
    return total / len(a)

print(avg([1, 2, 3]))
print(avg([1, 2, 3, 4, 5]))