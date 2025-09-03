x = 'global'

def f():
    x = 'enclosing'

    def g():
        print(x)

    g()


f()