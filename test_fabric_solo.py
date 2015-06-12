# Need to have a way to save command output, like in a file
# Need to write, clear, and read the contents

import fabric_solo as fs

command_list = []

def dummy_runall(commands, isSudo=False):
  command_list.extend(commands)

fs.runall = dummy_runall
  

def test_sed():
  command_list = []
  fs.sed("t.x", "aaa", "bbb")
  import pdb; pdb.set_trace()
  assert command_list == "sed"

test_sed()

  
