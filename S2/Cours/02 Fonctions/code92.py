def oper(x, y, op='+'):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '/':
        return x / y
    else:
        return None

print(oper(3, 4))
print(oper(3, 4, '+'))
print(oper(3, 4, '/'))