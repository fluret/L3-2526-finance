def f(x):
    x = 'foo'

for i in (
        40,
        dict(foo=1, bar=2),
        {1, 2, 3},
        'bar',
        ['foo', 'bar', 'baz']):
    f(i)
    print(i)
