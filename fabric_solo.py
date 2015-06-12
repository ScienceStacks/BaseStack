# Functions used when using fabric on a single machine

from fabric.api import env, local, settings, sudo
from fabric.contrib.files import sed
import fabric.contrib.files as fcf
from fabric.context_managers import cd
from random import random

env.user = 'ubuntu'
env.hosts = ['localhost']

print_only = False  # Print commands but do not execute them
TEST_EXISTS_OUTPUT = False  # Value returned by exists

def runall(commands, isSudo=False):
  # Run sudo on a list of commands
  # Input: commands - list of commands
  #        isSudo - command should be run using sudo
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

def cp(from_path, to_path, isSudo=False):
  # Copies one file path to another
  # TBD: Handle errors
  command = "cp %s %s" % (from_path, to_path)
  runall([command], isSudo=True)
  if not isSudo:
    runall([command])

def chown(path, new_owner=env.user):
  # Changes the owner for the file path
  command = 'chown -R %s:%s %s' % (new_owner, new_owner, path)
  runall([command], isSudo=True)

def chmod(mode, path, isSudo=False):
  command = "chmod %s %s" % (mode, path)
  runall([command], isSudo=isSudo)

def ln(options, target, link, isSudo=False):
  if not exists(link):
    command = "ln -%s %s %s" % (options, target, link)
    runall([command], isSudo=isSudo)

def mkdir(path, isSudo=False):
  if not exists(path):
    command = "mkdir %s" % path
    runall([command], isSudo=isSudo)

def rm(path, isSudo=False):
  if exists(path):
    command = "rm %s" % path
    runall([command], isSudo=isSudo)

def mv(from_path, to_path, isSudo=False):
  if exists(from_path):
    command = "mv %s %s" % (from_path, to_path)
    runall([command], isSudo=isSudo)

def apt_get(args, isSudo=False):
  command = "apt-get install %s" % args
  runall([command], isSudo=isSudo)

def random_integer(size):
  return int(10**size*random())

def sed(path, src_string, rpl_string, isSudo=False):
#  with settings(host_string="localhost"):
#    fcf.sed(path, src_string, rpl_string)
  tmp_path = "/tmp/%d" % random_integer(10)
  commands =  '''
    sed 's/%s/%s/' %s > %s
    mv %s %s
  '''  % (src_string, rpl_string, path, tmp_path,
          tmp_path, path)
  runall(commands.split('\n'), isSudo=isSudo)

def wget(url):
  command = "wget '{}'".format(url)
  runall([command], isSudo=isSudo)

def exists(path):
  if not print_only:
    return fcf.exists(path)
  else:
    return TEST_EXISTS_OUTPUT
