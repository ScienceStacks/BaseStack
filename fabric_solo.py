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

from fabric.api import env, local, sudo
import fabric.contrib.files as fcf
from random import random

DEFAULT_USER = 'ubuntu'
env.user = DEFAULT_USER
env.hosts = ['localhost']

print_only = False  # Print commands but do not execute them
TEST_EXISTS_OUTPUT = False  # Value returned by exists

################################################
# Utility functions
###############################################
def runall(commands, **kwargs):
  # Run sudo on a list of commands
  # Input: commands - list of commands
  # kwargs:
  #        isSudo - command should be run using sudo
  isSudo = False
  for key, value in kwargs.iteritems():
    if key == 'isSudo':
      isSudo = value
  for cmd in commands:
    if cmd.strip():  # Must be a string with non-blanks
      if isSudo:
        try:
          if not print_only:
            sudo(cmd, pty=True)
          else:
            print "[sudo debug] %s" % cmd
        except Exception as e:
          print e
      else:
        try: 
          if not print_only:
            print "[local] %s" % cmd
            local(cmd, env.user)
          else:
            print "[local debug] %s" % cmd
        except Exception as e:
          print e

def random_integer(size):
  return int(10**size*random())


################################################
# Bash Wrappers
###############################################

def apt_get(args, **kwargs):
  command = "apt-get install %s" % args
  runall([command], **kwargs)

def chmod(mode, path, **kwargs):
  command = "chmod %s %s" % (mode, path)
  runall([command], **kwargs)

def chown(path, new_owner=env.user):
  # Changes the owner for the file path
  command = 'chown -R %s:%s %s' % (new_owner, new_owner, path)
  runall([command], isSudo=True)

def cp(from_path, to_path, **kwargs):
  # Copies one file path to another
  # TBD: Handle errors
  command = "cp %s %s" % (from_path, to_path)
  runall([command], **kwargs)

def exists(path):
  if print_only:
    print "[debug local] exists %s" % path
    return TEST_EXISTS_OUTPUT
  else: 
    print "[local] exists %s" % path
    return fcf.exists(path)

def ln(options, path, link, **kwargs):
  if not exists(link):
    command = "ln -%s %s %s" % (options, path, link)
    runall([command], **kwargs)

def mkdir(path, **kwargs):
  if not exists(path):
    command = "mkdir %s" % path
    runall([command], **kwargs)

def mv(from_path, to_path, **kwargs):
  if exists(from_path):
    command = "mv %s %s" % (from_path, to_path)
    runall([command], **kwargs)

def rm(path, **kwargs):
  if exists(path):
    command = "rm %s" % path
    runall([command], **kwargs)

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
