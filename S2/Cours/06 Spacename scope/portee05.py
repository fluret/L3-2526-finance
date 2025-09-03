def outer_func():
  var = 100
  def inner_func():
      print(f"Printing var from inner_func(): {var}")
      print(f"Printing another_var from inner_func(): {another_var}")
  inner_func()
  another_var = 200  # This is defined after calling inner_func()
  print(f"Printing var from outer_func(): {var}")

outer_func()