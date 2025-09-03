sentence = (
    "The rocket, who was named Ted, came back "
    "from Mars because he missed his friends."
)


def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels


print([char for char in sentence if is_consonant(char)])

vowels = "aeiou"
print([char for char in sentence if char.isalpha() and char.lower() not in vowels])