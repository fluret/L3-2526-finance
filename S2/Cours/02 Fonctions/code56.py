def double_list(x):
    i = 0
    while i < len(x):
            x[i] *= 2
            i += 1

a = [1, 2, 3, 4, 5]
double_list(a)
print(a)