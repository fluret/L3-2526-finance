def words_order(text, words):
    text_words = {w for w in text.split() if w in words}
    return list(sorted(text_words, key=text.index)) == words

#**********

def words_order(text, words):
    return words == [w for w in text.split() if w in words and words.count(w) < 2]

#**********

def words_order(text, words):
    text_words = {w for w in text.split() if w in words}
    return sorted(text_words, key=text.index) == words

#**********

import re

def words_order(text, words):
    return len(set(words)) == len(words) and \
        not not re.search(r'\b' + r'\b.*\b'.join(words) + r'\b', text)
        
