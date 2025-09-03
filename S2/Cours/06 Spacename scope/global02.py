counter = 0  # A global name
def update_counter():
    global counter  # Declare counter as global
    counter = counter + 1  # Successfully update the counter

update_counter()
print(counter)
update_counter()
print(counter)
update_counter()
print(counter)