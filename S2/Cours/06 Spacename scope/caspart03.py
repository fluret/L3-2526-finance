lst = [1, 2, 3]
try:
    lst[4]
except IndexError as err:
    # The variable err is local to this block
    # Here you can do anything with err
    print(err)
print('************')
print(err) # Is out of scope