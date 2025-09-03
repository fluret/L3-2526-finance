def f(*args):
    for i in args:
        print(i)

a = [1, 2, 3]
t = (4, 5, 6)
s = {7, 8, 9}

f(*a, *t, *s)