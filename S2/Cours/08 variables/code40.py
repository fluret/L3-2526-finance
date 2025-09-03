from copy import deepcopy
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = deepcopy(matrix)
matrix[0].append(100)
print(matrix)
print(new_matrix)