def f():
    x = 20

    def g():
        x = 40

    g()
    print(x)


f()