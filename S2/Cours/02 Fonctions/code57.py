def double_list(x):
    r = []
    for i in x:
        r.append(i * 2)
    return r

a = [1, 2, 3, 4, 5]
a = double_list(a)
print(a)