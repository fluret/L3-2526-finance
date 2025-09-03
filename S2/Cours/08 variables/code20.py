from copy import deepcopy
a = [["alex", "beth"]]
b = a.copy()
b[0].append("charlie")
print(b[0])
print(a[0])
print('****')
c = deepcopy(a)
c[0].append("dan")
print(c[0])
print(a[0])