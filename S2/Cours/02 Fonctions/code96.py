def oper(x, y, *, op='+'):
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
print('****')
print(oper(3, 4, "I don't belong here"))
print('****')
print(oper(3, 4, '+'))