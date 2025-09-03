list1 = [1, 2, 3]
list2 = [4, 5, 6]
even_odd_sum_tuples = (tuple((x, y, x + y) for x in list1 for y in list2 if (x + y) % 2 == 0),tuple((x, y, x + y) for x in list1 for y in list2 if (x + y) % 2 != 0))
print(list1)
print(list2)
print(even_odd_sum_tuples)