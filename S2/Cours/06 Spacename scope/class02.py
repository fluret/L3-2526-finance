class A:
  attr = 100
  print(attr)  # Access class attributes directly

print('************')
print(A.attr)  # Access a class attribute from outside the class
print('************')
print(attr)  # Isn't defined outside A