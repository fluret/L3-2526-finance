squares_1 = []
for number in range(10):
    squares_1.append(number * number)
    
# qui peut se traduire par :

squares_2 = [number * number for number in range(10)]

print(squares_1)
print(squares_2)
