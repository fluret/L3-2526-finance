var = 100  # A global variable
def func():
  print(var)  # Reference the global variable, var
  var = 200   # Define a new local variable using the same name, var

func()