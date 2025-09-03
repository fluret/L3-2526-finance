class A:
    var = 100
    def __init__(self):
        self.var = 200

    def access_attr(self):
        # Use dot notation to access class and instance attributes
        print(f'The instance attribute is: {self.var}')
        print(f'The class attribute is: {A.var}')

obj = A()
obj.access_attr()
print(A.var)  # Access class attributes
print(A().var) # Access instance attributes
print(A.__dict__.keys())
print(A().__dict__.keys())