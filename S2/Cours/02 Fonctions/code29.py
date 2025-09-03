def f(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append('###')
    return my_list


f()
f()
f()
f(['foo', 'bar', 'baz'])
f([1, 2, 3, 4, 5])
