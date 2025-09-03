def f():
    return dict(foo=1, bar=2, baz=3)


print(f())
print(f()['baz'])