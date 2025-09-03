class A:
  def __init__(self, var):
    self.var = var

  def duplicate_var(self):
    return self.var * 2

obj = A(100)
print(obj.var)
print('************')
print(obj.duplicate_var())
print('************')
print(A.var)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    A.var
AttributeError: type object 'A' has no attribute 'var'
