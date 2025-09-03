def f(a, b, c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')

d = {'a': 'foo', 'b': 25, 'c': 'qux'}
f(**d)