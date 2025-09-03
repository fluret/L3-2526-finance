list1 = [3, 6, 9]
list2 = [5, 10, 15]
abs_diff_dict = {(x, y): abs(x - y) for x in list1 for y in list2}
print(list1)
print(list2)
print(abs_diff_dict)