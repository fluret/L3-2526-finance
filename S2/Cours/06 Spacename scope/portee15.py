print(abs(-15))  # Standard use of a built-in function
abs = 20  # Redefine a built-in name in the global scope
print(abs(-15))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
