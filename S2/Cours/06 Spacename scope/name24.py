def f():
    x = 20

    def g():
        global x
        x = 40

    g()
    print(x)


f()
print(x)