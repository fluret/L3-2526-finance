def func():
    var = 100
    locals()['var'] = 200
    print(var)

func()