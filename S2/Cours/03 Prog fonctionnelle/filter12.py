def is_palindrome(word):
    reversed_word = "".join(reversed(word))
    return word.lower() == reversed_word.lower()

print(is_palindrome("Racecar"))
print(is_palindrome("Python"))