'''
  Functions used when using fabric on a single machine
  Naming conventions for wrappers
  Functions have the same name as their bash counterpart
  Variables
    kwargs - optional arguments for running the command (isSudo)
    mode - file mode
    options - command line options
    path, from_path, to_path  - a file/directory path
    src_string, rpl_strings - strings in a replacement operation
    url - string for a URL
'''

from fabric.context_managers import lcd
from fabric.api import env, local, sudo
import fabric.contrib.files as fcf
from random import random

DEFAULT_USER = 'ubuntu'
env.user = DEFAULT_USER
env.hosts = ['localhost']

TEST_EXISTS_OUTPUT = False  # Value returned by exists

################################################
# Utility functions
###############################################
def runall(commands, print_only=False, isSudo=False):
  # Run sudo on a list of commands
  # Input: commands - list of commands
  # kwargs:
  #        isSudo - command should be run using sudo
  for cmd in commands:
    if cmd.strip():  # Must be a string with non-blanks
      if isSudo:
        try:
          if not print_only:
            sudo(cmd, pty=True)
          else:
            print "[debug sudo] %s" % cmd
        except Exception as e:
          print e
      else:
        try: 
          if not print_only:
            local(cmd, env.user)
          else:
            print "[debug local] %s" % cmd
        except Exception as e:
          print e

def random_integer(size):
  return int(10**size*random())


################################################
# Bash Wrappers
###############################################

def apt_get(packages, options="", **kwargs):
  commands = '''
    apt-get build-dep %s
    apt-get install -y%s %s
  ''' % (packages, options, packages)
  runall(commands.split("\n"), **kwargs)

def chmod(mode, path, **kwargs):
  command = "chmod %s %s" % (mode, path)
  runall([command], **kwargs)

def chown(path, new_owner=env.user, **kwargs):
  # Changes the owner for the file path
  command = 'chown -R %s:%s %s' % (new_owner, new_owner, path)
  runall([command], isSudo=True, **kwargs)

def cp(from_path, to_path, options="", **kwargs):
  # Copies one file path to another
  # TBD: Handle errors
  if options:
    addendum = "-%s " % options
  else:
    addendum = ""
  command = "cp %s%s %s" % (addendum, from_path, to_path)
  runall([command], **kwargs)

def exists(path, print_only=False):
  if print_only:
    print "[debug local] exists %s" % path
    return TEST_EXISTS_OUTPUT
  else: 
    print "[local] exists %s is: %s" % (path, fcf.exists(path))
    return fcf.exists(path)

def lcd(path, print_only=False):
  if print_only:
    print "[debug local] lcd %s" % path
  else: 
    print "[local] lcd %s" % path
    return fcf.lcd(path)

def ln(options, path, link, print_only=False, **kwargs):
  if not exists(link, print_only=print_only):
    command = "ln -%s %s %s" % (options, path, link)
    runall([command], print_only=print_only, **kwargs)

def mkdir(path, print_only=False, **kwargs):
  if not exists(path, print_only=print_only):
    command = "mkdir %s" % path
    runall([command], print_only=print_only, **kwargs)

def mv(from_path, to_path, print_only=False, **kwargs):
  if exists(from_path, print_only=print_only):
    command = "mv %s %s" % (from_path, to_path)
    runall([command], print_only=print_only, **kwargs)

def rm(path, print_only=False, **kwargs):
  if exists(path, print_only=print_only):
    command = "rm %s" % path
    runall([command], print_only=print_only, **kwargs)

def sed(path, src_string, rpl_string, **kwargs):
  tmp_path = "/tmp/%d" % random_integer(10)
  commands =  '''
    sed 's/%s/%s/' %s > %s
    mv %s %s
  '''  % (src_string, rpl_string, path, tmp_path,
          tmp_path, path)
  runall(commands.split('\n'), **kwargs)

def wget(url, **kwargs):
  command = "wget '{}'".format(url)
  runall([command], **kwargs)
