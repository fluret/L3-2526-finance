def f(fx):
    print('fx =', fx, '/ id(fx) = ', id(fx))
    fx = 10
    print('fx =', fx, '/ id(fx) = ', id(fx))

x = 5
print('x =', x, '/ id(x) = ', id(x))
f(x)
print('x =', x, '/ id(x) = ', id(x))
