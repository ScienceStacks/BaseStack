'''Utility functions'''


def static_var(varname, value):
  # Decorator function to provide static internal variables
  # Usage: referene the variable using "function.varname", where
  #        function is the name of the function
  # Input: varname - string name of the static internal variable
  #        value - value assigned to the variable initially
  def decorate(func):
    setattr(func, varname, value)
    return func
  return decorate
