def f(*args):
    for i in args:
        print(i)

f(*[1, 2, 3], *[4, 5, 6])

def f(**kwargs):
    for k, v in kwargs.items():
        print(k, '->', v)

f(**{'a': 1, 'b': 2}, **{'x': 3, 'y': 4})