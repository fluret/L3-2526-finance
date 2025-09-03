lst = [1, 2, 3]
ex = None
try:
    lst[4]
except IndexError as err:
    ex = err
    print(err)

print('************')
print(ex)