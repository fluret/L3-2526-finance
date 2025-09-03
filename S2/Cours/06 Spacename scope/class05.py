class A:
    def __init__(self, var):
        self.var = var  # Create a new instance attribute
        self.var *= 2  # Update the instance attribute

obj = A(100)
print(obj.__dict__)
print(obj.var)