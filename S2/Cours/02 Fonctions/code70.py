def f(x, y, z):
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'z = {z}')

f(1, 2, 3)
print('****')
t = ('foo', 'bar', 'baz')
f(*t)