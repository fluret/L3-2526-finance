words = ['apple', 'banana', 'cherry', 'dog', 'ct']
vowel_counts = {word: sum(1 for char in word if char.lower() in 'aeiou') for word in words if
                any(char.lower() in 'aeiou' for char in word)}
print(words)
print(vowel_counts)