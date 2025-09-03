def test(text, words):
    liste = [text.split().index(word) if text.split().count(word) >= 1 else -1 for word in words ]
    print(text)
    print(words)
    print(f'liste = {liste}')
    print(f'sorted(liste) = {sorted(liste)}')
    print(f'set(liste) = {set(liste)}')
    print(f'len(set(liste)) = {len(set(liste))}')
    print(f'-1 not in liste = {-1 not in liste}')
    print(f'len(words) = {len(words)}')
    print(f'(len(set(liste)) > 1 and len(words) > 1) = {(len(set(liste)) > 1 and len(words) > 1)}')
    print(f'text.split() = {text.split()}')
    print(f'words in text.split() = {words in text.split()}')
    
    print(f'liste == sorted(liste) if (len(set(liste)) > 1 and len(words) > 1 or len(words) == 1) and -1 not in liste and (liste in list(text.split())) else False = {liste == sorted(liste) if (len(set(liste)) > 1 and len(words) > 1 or len(words) == 1) and -1 not in liste else False}')


text = "hi world im here"
words = ["world", "here"]
test(text, words)
print('********************************')

words = ["here", "world"]
liste = [text.find(word) for word in words]
test(text, words)
print('********************************')
words = ["world"]
liste = [text.find(word) for word in words]
test(text, words)
print('********************************')

words = ["world", "world"]
liste = [text.find(word) for word in words]
test(text, words)
print('********************************')
words = ["wo", "rld"]
liste = [text.find(word) for word in words]
test(text, words)
print('********************************')

