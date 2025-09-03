from itertools import zip_longest
numbers = [1, 2, 3]
letters = ["a", "b", "c"]
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue="?")
print(list(zipped))