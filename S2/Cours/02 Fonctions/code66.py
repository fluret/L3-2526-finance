def f(*args):
    print(args)
    print(type(args), len(args))
    for x in args:
        print(x)

f(1, 2, 3)
print('***')
f('foo', 'bar', 'baz', 'qux', 'quux')