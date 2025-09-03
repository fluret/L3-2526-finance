import re
def remove_punctuation(word):
    return re.sub(r'[!?.:;,"()-]', "", word)

print(remove_punctuation("...Python!"))