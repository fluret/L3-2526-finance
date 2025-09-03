global_counter = 0  # A global name
def update_counter(counter):
    return counter + 1  # Rely on a local name

global_counter = update_counter(global_counter)
print(global_counter)
global_counter = update_counter(global_counter)
print(global_counter)
global_counter = update_counter(global_counter)
print(global_counter)