from texte import TEXTE
from functools import reduce

def count_words(d, word):
    d[word] = d.get(word, 0) + 1
    return d

word_counts = reduce(count_words, TEXTE.split(), {})
print(word_counts)