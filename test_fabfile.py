# Nose tests. Run using "nosetests --pdb". Debug by placing an
# unexecuteable statement where pdb should get control (e.g., "xxyy")

from util import static_var, dummy_runall
import fabric_solo as fs
import fabfile as fb


class TestClass:

  def setUp(self):
    fs.runall = dummy_runall
    dummy_runall(None, initialize=True)
    self.def_exists = fs.exists  # Some tests stub fs.exists

  def teatDown(self):
    fs.exists = self.def_exists
 
  def test_setup(self):
    fb.setup()
    xxxyy
    commands = dummy_runall(None, interrogate=True)
    assert(len(commands) > 0)
  
