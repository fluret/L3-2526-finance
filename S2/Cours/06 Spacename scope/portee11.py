# This area is the global or module scope
number = 100
def outer_func():
    # This block is the local scope of outer_func()
    # It's also the enclosing scope of inner_func()
    def inner_func():
        # This block is the local scope of inner_func()
        print(number)

    inner_func()

outer_func()