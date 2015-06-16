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

#####################################
# Test utilities
#####################################
@static_var("command_list", [])
def dummy_runall(commands, isSudo=False, print_only=False,
    initialize=False, interrogate=False):
  # Fake for runall
  # Input: commands - list of commands (as in runall)
  #        isSudo - as in runall
  #        initialize - initializes the list of commands
  #        interrogate - returns the value of the list of commands
  if initialize:
    dummy_runall.command_list = []
    return
  elif interrogate:
    return dummy_runall.command_list
  else:
    for cmd in commands:
      if cmd.strip():  # Has non-blanks
        dummy_runall.command_list.append(cmd.lstrip())
    return

def dummy_exists_true(path, **kwargs):
  return True

def dummy_exists_false(path, **kwargs):
  return False
