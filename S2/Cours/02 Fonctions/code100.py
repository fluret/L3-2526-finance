# This is Python 3.8
def f(x, y, /, z, w, *, a, b):
    print(x, y, z, w, a, b)

f(1, 2, z=3, w=4, a=5, b=6)
f(1, 2, 3, w=4, a=5, b=6)