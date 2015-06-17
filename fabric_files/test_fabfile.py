# Nose tests. Run using "nosetests --pdb". Debug by placing an
# unexecuteable statement where pdb should get control (e.g., "xxyy")

from util import (static_var, dummy_runall, dummy_exists_false,
    dummy_exists_true)
import fabfile as fb
import fabric_solo as fs


TRUTH_VALUES = [True, False]

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
    for val in TRUTH_VALUES:
      self.set_exists(val)
      fb.setup()
      commands = dummy_runall(None, interrogate=True)
      assert(len(commands) > 0)
 
  def test_install_tools(self):
    for val in TRUTH_VALUES:
      self.set_exists(val)
      fb.install_tools()
      commands = dummy_runall(None, interrogate=True)
      assert(len(commands) > 0)
 
  def test_setup_env(self):
    EMAIL = "me@there.com"
    NAME = "Mickey Mouse"
    for val in TRUTH_VALUES:
      self.set_exists(val)
      fb.setup_env(EMAIL, NAME)
      commands = dummy_runall(None, interrogate=True)
      assert(len(commands) > 0)
 
  def test_setup_apache(self):
    for val in TRUTH_VALUES:
      self.set_exists(val)
      fb.setup_apache()
      commands = dummy_runall(None, interrogate=True)
      assert(len(commands) > 0)
 
  def test_setup_django(self):
    for val in TRUTH_VALUES:
      self.set_exists(val)
      fb.setup_django()
      commands = dummy_runall(None, interrogate=True)
      assert(len(commands) > 0)
  
