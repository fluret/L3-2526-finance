def f():
    return 'foo', 'bar', 'baz', 'qux'

print(type(f()))
t = f()
print(t)

a, b, c, d = f()
print(f'a = {a}, b = {b}, c = {c}, d = {d}')

