def create_lazy_name():
    global lazy  # Create a global name, lazy
    lazy = 100
    return lazy

print(create_lazy_name())
print(lazy)  # The name is now available in the global scope
print(dir())
['__annotations__', '__builtins__',..., 'create_lazy_name', 'lazy']
