def f(my_list=[]):
    print(id(my_list))
    my_list.append('###')
    return my_list

f()
f()
f()
