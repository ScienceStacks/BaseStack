# Nose tests. Run using "nosetests --pdb". Debug by placing an
# unexecuteable statement where pdb should get control (e.g., "xxyy")

from util import (static_var, dummy_runall, dummy_exists_true,
    dummy_exists_false)
import fabric_solo as fs


class TestClass:

  def setUp(self):
    fs.runall = dummy_runall
    dummy_runall(None, initialize=True)
    self.def_exists = fs.exists  # Some tests stub fs.exists

  def teatDown(self):
    fs.exists = self.def_exists

  def test_dummy_runall(self):
    COMMANDS_ONE = ["first"]
    COMMANDS_TWO = ["second", "third"]
    dummy_runall(None, initialize=True)
    dummy_runall(COMMANDS_ONE)
    dummy_runall(COMMANDS_TWO)
    commands = dummy_runall(None, interrogate=True)
    result = COMMANDS_ONE; result.extend(COMMANDS_TWO)
    assert commands == result
    dummy_runall(None, initialize=True)
    dummy_runall(COMMANDS_ONE)
    commands = dummy_runall(None, interrogate=True)
    assert commands == COMMANDS_ONE

  def test_apt_get(self):
    PACKAGE = "dummy"
    fs.apt_get("", PACKAGE)
    commands = dummy_runall(None, interrogate=True)
    expected_result = "apt-get install -y %s" % PACKAGE
    assert(commands[1].index(expected_result) >= 0)

  def test_chown(self):
    PATH = "/home/me"
    NEW_OWNER = "me_me"
    fs.chown(PATH, NEW_OWNER)
    commands = dummy_runall(None, interrogate=True)
    expected_result = "chown -R %s:%s %s" % (
        NEW_OWNER, NEW_OWNER, PATH)
    assert(commands[0].index(expected_result) >= 0)

  def test_chmod(self):
    MODE = "q"
    PATH = "/home/me"
    fs.chmod(MODE, PATH)
    commands = dummy_runall(None, interrogate=True)
    expected_result = "chmod %s %s" % (MODE, PATH)
    assert(commands[0].index(expected_result) >= 0)

  def test_cp(self):
    PATH1 = "t.x"
    PATH2 = "t.y"
    fs.cp(PATH1, PATH2)
    commands = dummy_runall(None, interrogate=True)
    expected_result = "cp %s %s" % (PATH1, PATH2)
    assert(commands[0].index(expected_result) >= 0)

# TODO: Have a test that doesn't require user interactions
  def test_exists(self):
    PATH_EXISTS = '/tmp'
    PATH_NOT_EXISTS = '/invalid/path'
    # assert(fs.exists(PATH_EXISTS))
    # assert(not fs.exists(PATH_NOT_EXISTS))

  def test_ln(self):
    fs.exists = dummy_exists_false
    PATH = "t.x"
    LINK = "/link"
    OPTIONS = "fs"
    fs.ln(OPTIONS, PATH, LINK)
    commands = dummy_runall(None, interrogate=True)
    expected_result = "ln -%s %s %s" % (OPTIONS, PATH, LINK)
    assert(commands[0].index(expected_result) >= 0)

  def test_mkdir(self):
    fs.exists = dummy_exists_false
    PATH = "t.x"
    fs.mkdir(PATH, print_only=False)
    commands = dummy_runall(None, interrogate=True)
    expected_result = "mkdir %s" % PATH
    assert(commands[0].index(expected_result) >= 0)

  def test_mv(self):
    fs.exists = dummy_exists_true
    FROM_PATH = "t.x"
    TO_PATH = "t.y"
    fs.mv(FROM_PATH, TO_PATH, print_only=False)
    commands = dummy_runall(None, interrogate=True)
    expected_result = "mv %s %s" % (FROM_PATH, TO_PATH)
    assert(commands[0].index(expected_result) >= 0)

  def test_rm(self):
    fs.exists = dummy_exists_true
    PATH = "t.x"
    fs.rm(PATH, print_only=False)
    commands = dummy_runall(None, interrogate=True)
    expected_result = "rm %s" % PATH
    assert(commands[0].index(expected_result) >= 0)

  def test_sed(self):
    FILE = "t.x"
    STRING1 = "aaa"
    STRING2 = "bbb"
    fs.sed(FILE, STRING1, STRING2)
    commands = dummy_runall(None, interrogate=True)
    expected_result0 = "sed 's/%s/%s/' %s > /tmp" % (
        STRING1, STRING2, FILE)
    expected_result1 = "mv /tmp"
    assert(commands[0].index(expected_result0) >= 0)
    assert(commands[1].index(expected_result1) >= 0)

  def test_wget(self):
    URL = "http://some/url"
    fs.wget(URL)
    commands = dummy_runall(None, interrogate=True)
    expected_result = "wget '%s'" % URL
    assert(commands[0].index(expected_result) >= 0)

