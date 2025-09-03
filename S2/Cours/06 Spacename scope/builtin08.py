import sys
print(vars(sys)) # With a module object
print(vars(sys) is sys.__dict__)
class MyClass:
    def __init__(self, var):
        self.var = var

obj = MyClass(100)
print(vars(obj))  # With a user-defined object
print(vars(MyClass))  # With a class