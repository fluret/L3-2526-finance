x = 'global'

def f():
    x = 'enclosing'

    def g():
        x = 'local'
        print(x)
        
    g()


f()