def oper(x, y, *ignore, op='+'):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '/':
        return x / y
    else:
        return None

print(oper(3, 4, op='+'))
print(oper(3, 4, op='/'))