x = 'global'

def f():

    def g():
        print(x)

    g()


f()