
# global_var = 10
# def example_function():
#  local_variable = 10+global_var
#  print(local_variable)

# example_function()
# print(global_var)


x = 10 # Global variable
def outer_function():
  y = 20 # Enclosed variable
  def inner_function():
    z = 30 # Local variable
    print(x, y, z)
  inner_function()

outer_function()
