def power_factory(exp):
    def power(base):
        return base ** exp
    return power

square = power_factory(2)
print(square(10))
cube = power_factory(3)
print(cube(10))
print(cube(5))
print(square(15))