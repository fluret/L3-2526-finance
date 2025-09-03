nonlocal my_var  # Try to use nonlocal in the global scope

def func():
  nonlocal var  # Try to use nonlocal in a local scope
  print(var)