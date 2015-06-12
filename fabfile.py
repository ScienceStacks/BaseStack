from fabric.context_managers import cd
from fabric_solo import (apt_get, chmod, chown, cp, exists, ln,
    mkdir, mv, rm, runall, sed, wget)

def setup(git_email="jlheller@uw.edu", 
    git_username="Joseph Hellerstein"):
  # Invokes all setups to do
  install_tools()
  setup_env(git_email, git_username)
  setup_py()
  setup_apache()

def setup_django():
  apt_get("sqlite")
  commands = '''
    pip install django
    django-admin startproject mysite
  '''
  runall(commands.splite('\n'), isSudo=True)
  # MOdify settings to select the engine and name

def setup_apache():
  apt_get("-y apache2", isSudo=True)
  if not exists("/vagrant"):
    mkdir("$HOME/apache_home", isSudo=False)
    mkdir("$HOME/apache_home/html", isSudo=False)
    command = 'echo "Hello ubuntu World!" > '
    command += '$HOME/apache_home/html/index.html'
    runall([command], isSudo=False)
    ln("s", "$HOME/apache_home", "/vagrant", isSudo=True)
  runall(["rm -rf /var/www"], isSudo=True)
  runall(["ln -fs /vagrant /var/www"], isSudo=True)

def copy_file_in_bin_to_HOME(filename):
  cp('$HOME/BaseStack/bin/%s' % filename, '$HOME', isSudo=True)
  chmod('+x', filename, isSudo=True)
  chown(filename)

def setup_env(git_email, git_username):
  copy_file_in_bin_to_HOME(".bashrc")
  copy_file_in_bin_to_HOME(".vimrc")
  # Git configuration
  commands = '''
    git config --global user.email "%s"
    git config --global user.name "%s"
  ''' % (git_email, git_username)
  runall(commands.split('\n'), isSudo=False)

def setup_py():
  commands = '''
    easy_install mock
  '''
  runall(commands.split('\n'), isSudo=False)

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
    runall(commands.split('\n'), IsSudo=True)
    if exists('BaseStack/cookbooks'):
      command = 'cp -r BaseStack/cookbooks/* chef-repo/cookbooks/'
      runall([command], isSudo=False)

def install_tools():
  apt_get("python-pip python-dev build-essential", isSudo=True)
  commands = '''
    pip install --upgrade pip 
    pip install --upgrade virtualenv 
  '''
  runall(commands.split('\n'), isSudo=True)
  apt_get("curl", isSudo=True)
  apt_get("vim", isSudo=True)
