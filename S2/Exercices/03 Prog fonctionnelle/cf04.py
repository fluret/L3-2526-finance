from functools import reduce

numbers = ['1', '2', '3', '4', '5']

integers = map(int, numbers)
print(integers)
total = reduce(lambda x, y: x + y, integers)
#total = reduce(lambda x, y: x + y, map(int, numbers))
print(total)