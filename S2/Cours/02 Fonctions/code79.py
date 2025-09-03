def f(**kwargs):
    for k, v in kwargs.items():
        print(k, '->', v)

d1 = {'a': 1, 'b': 2}
d2 = {'x': 3, 'y': 4}

f(**d1, **d2)