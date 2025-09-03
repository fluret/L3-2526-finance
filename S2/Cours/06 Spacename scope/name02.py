b = 30
print(globals())
def f():
    print('Start f()')
    b = 20
    print(locals())
    def g():
        print(locals())
        print('Start g()')
        print('End g()')
        return

    g()

    print('End f()')
    return
print(globals())

f()