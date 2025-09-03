def square(base):
    result = base ** 2
    print(f'The square of {base} is: {result}')

print(square.__code__.co_argcount)
print(square.__code__.co_consts)
print(square.__code__.co_name)
print(square.__code__.co_varnames)