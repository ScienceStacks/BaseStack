from fabric.api import sudo
from fabric.contrib.files import exists
from fabric.context_managers import cd
from fabric_solo import apt_get, chmod, cp, mkdir, mv, rm, runall, wget

def setup(git_email="jlheller@uw.edu", git_username="Joseph Hellerstein"):
  # Invokes all setups to do
  print "git_email=%s git_username=%s" % (git_email, git_username)
  return
  install_tools()
  setup_env(git_email, git_username)
  setup_apache()

def setup_apache():
  #sudo("apt-get install -y apache2", pty=True)
  if not exists("/vagrant"):
    mkdir("$HOME/apache_home", isSudo=False)
    mkdir("$HOME/apache_home/html", isSudo=False)
    command = 'echo "Hello ubuntu World!" > '
    command += '$HOME/apache_home/html/index.html'
    runall([command], isSudo=False)
    ln("$HOME/apache_home", "/vagrant", "-s", isSudo=False)
  sudo("rm -rf /var/www", pty=True)
  sudo ("ln -fs /vagrant /var/www")

def setup_env(git_email, git_username):
  cp('$HOME/BaseStack/bin/.bashrc', '$HOME', isSudo=False)
  chmod('+x', '.bashrc', isSudo=True)
  cp('$HOME/BaseStack/bin/.vimrc', '$HOME', isSudo=False)
  chmod('+x', '.vimrc', isSudo=True)
  # Git configuration
  commands = '''
    git config --global user.email "%s"
    git config --global user.name "%s"
  ''' % (git_email, git_username)
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
    runall(commands.split('\n'), sudo=True)
    if exists('BaseStack/cookbooks'):
      command = 'cp -r BaseStack/cookbooks/* chef-repo/cookbooks/'
      runall([command], isSudo=False)

def install_tools():
  apt_get("python-pip python-dev build-essential")
  commands = '''
    pip install --upgrade pip 
    pip install --upgrade virtualenv 
  '''
  runall(commands.split('\n'), isSudo=True)
  apt_get(curl)
  apt_get(vim)
