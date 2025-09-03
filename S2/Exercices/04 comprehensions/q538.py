strings = ["apple", "banana", "cherry"]
vowel_replaced = [''.join(['*' if char.lower() in 'aeiou' else char for char in word]) for word in strings]
print(strings)
print(vowel_replaced)