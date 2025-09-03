def f(*args):
    print(type(args), args)

a = ['foo', 'bar', 'baz', 'qux']
f(*a)