matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],]


flat = []
for row in matrix:
    for number in row:
        flat.append(number)

print(flat)