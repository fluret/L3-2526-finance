def f():
    s = 'foo'
    loc = locals()
    print(loc)

    x = 20
    print(loc)

    loc['s'] = 'bar'
    print(s)


f()