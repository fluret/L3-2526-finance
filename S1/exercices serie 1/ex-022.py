X = {'a', 'b', 'c', 'd'}
Y = {'s', 'b', 'd'}
# 1
print(f"Ensemble X : {X}")
print(f"Ensemble Y : {Y}")
# 2
appartenance_c_X = 'c' in X
print(f"L'élément 'c' appartient à X : {appartenance_c_X}")
# 3
appartenance_a_Y = 'a' in Y
print(f"L'élément 'a' appartient à Y : {appartenance_a_Y}")
# 4
difference_X_Y = X - Y
difference_Y_X = Y - X
print(f"Ensemble X - Y : {difference_X_Y}")
print(f"Ensemble Y - X : {difference_Y_X}")
# 5
union_X_Y = X | Y
print(f"Union de X et Y : {union_X_Y}")
# 6
intersection_X_Y = X & Y
print(f"Intersection de X et Y : {intersection_X_Y}")