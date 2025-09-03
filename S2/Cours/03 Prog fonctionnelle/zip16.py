letters = ["b", "a", "d", "c"]
numbers = [2, 4, 3, 1]
data1 = list(zip(letters, numbers))
print(data1)

data1.sort()  # Sort by letters
print(data1)

data2 = list(zip(numbers, letters))
print(data2)

data2.sort()  # Sort by numbers
print(data2)