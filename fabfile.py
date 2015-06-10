from fabric.context_managers import cd
from fabric_solo import apt_get, chmod, cp, exists, ln
from fabric_solo import mkdir, mv, rm, runall, wget

def setup(git_email="jlheller@uw.edu", git_username="Joseph Hellerstein"):
  # Invokes all setups to do
  install_tools()
  setup_env(git_email, git_username)
  setup_apache()

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
