# Nose tests. Run using "nosetests --pdb". Debug by placing an
# unexecuteable statement where pdb should get control (e.g., "xxyy")

from util import (static_var, dummy_runall, dummy_exists_false,
    dummy_exists_true)
import fabfile as fb
import fabric_solo as fs


class TestClass:

  @staticmethod
  def set_runall():
    # Both assignments of dummy_runall are needed
    fb.runall = dummy_runall  
    fs.runall = dummy_runall

  @staticmethod
  def set_exists(value):
    if value:
      fs.exists = dummy_exists_true
      fb.exists = dummy_exists_true
    else:
      fs.exists = dummy_exists_false
      fb.exists = dummy_exists_false

  def setUp(self):
    self.set_runall()
    dummy_runall(None, initialize=True)
 
  def test_setup(self):
    self.set_exists(False)
    fb.setup()
    commands = dummy_runall(None, interrogate=True)
    assert(len(commands) > 0)
  
