from fabric.api import env, local, sudo
from fabric.contrib.files import exists
from fabric.context_managers import cd
from fabric.operations import put, run

env.user = 'ubuntu'
env.hosts = ['localhost']

def setup():
  # Invokes all setups to do
  install_tools()
  setup_env()
  setup_apache()

def setup_apache():
  #sudo("apt-get install -y apache2", pty=True)
  if not exists("/vagrant"):
    mkdir_local("$HOME/apache_home", isSudo=False)
    mkdir_local("$HOME/apache_home/html", isSudo=False)
    command = 'echo "Hello ubuntu World!" > '
    command += '$HOME/apache_home/html/index.html'
    do_commands([command], isSudo=False)
    ln_local("-s","$HOME/apache_home", "/vagrant", isSudo=False)
    sudo("ln -s $HOME/apache_home /vagrant")
  sudo("rm -rf /var/www", pty=True)
  sudo ("ln -fs /vagrant /var/www")

def setup_env():
  cp_local('$HOME/BaseStack/bin/.bashrc', '$HOME', isSudo=False)
  chmod_local('+x', '.bashrc', isSudo=True)
  cp_local('$HOME/BaseStack/bin/.vimrc', '$HOME', isSudo=False)
  chmod_local('+x', '.vimrc', isSudo=True)

def install_chef():
  with cd('$HOME'):
    commands = '''
       curl -L https://www.opscode.com/chef/install.sh | bash
       wget http://github.com/opscode/chef-repo/tarball/master
       tar -zxf master
       mv chef-chef-repo* chef-repo
       chown -R ubuntu ubuntu chef-repo
       rm master
    '''
    do_commands(commands.split('\n'), sudo=True)
    if exists('BaseStack/cookbooks'):
      command = 'cp -r BaseStack/cookbooks/* chef-repo/cookbooks/'
      do_commands([command], isSudo=False)

def install_tools():
  commands = '''
    apt-get install python-pip python-dev build-essential 
    pip install --upgrade pip 
    pip install --upgrade virtualenv 
    apt-get install curl
    apt-get install vim
  '''
  do_commands(commands.split('\n'), isSudo=True)


def do_commands(commands, isSudo=False):
  # Run sudo on a list of commands
  # Input: commands - list of commands
  #        isSudo - command should be run using sudo
  for cmd in commands:
    if cmd.strip():  # Must be a string with non-blanks
      if isSudo:
        try: 
          sudo(cmd, pty=True)
        except Exception as e:
          print e
      else:
        try: 
          print "[local] %s" % cmd
          local(cmd)
        except Exception as e:
          print e

def cp_local(from_path, to_path, isSudo=False):
  command = "cp %s %s" % (from_path, to_path)
  do_commands([command], isSudo=True)
  if not isSudo:
    chown_local(to_path, env.user)

def chown_local(path, new_owner):
  command = 'chown -R %s:%s %s' % (new_owner, new_owner, path)
  do_commands([command], isSudo=True)

def chmod_local(mode, path, isSudo=False):
  command = "chmod %s %s" % (mode, path)
  do_commands([command], isSudo=isSudo)

def ln_local(target, link, options, isSudo=False):
  if not exists(link):
    command = "ln -%s %s %s" % (options, target, link)
    do_commands([command], isSudo=isSudo)

def mkdir_local(path, isSudo=False):
  if not exists(path):
    command = "mkdir %s" % path
    do_commands([command], isSudo=isSudo)

def sync_config():
    local('rsync -av . %s@%s:/etc/chef' % (env.user, env.hosts[0]))

def update():
    sync_config()
    sudo('cd /etc/chef && %s' % env.chef_executable, pty=True)
