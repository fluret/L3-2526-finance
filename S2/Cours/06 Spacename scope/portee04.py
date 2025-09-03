def outer_func():
  # This block is the Local scope of outer_func()
  var = 100  # A nonlocal var
  # It's also the enclosing scope of inner_func()
  def inner_func():
      # This block is the Local scope of inner_func()
      print(f"Printing var from inner_func(): {var}")

  inner_func()
  print(f"Printing var from outer_func(): {var}")

outer_func()
print('*****')
#inner_func()