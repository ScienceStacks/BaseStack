'''Codes for creating a basic scientific statck on a linux VM'''


from contextlib import contextmanager
from fabric_solo import (apt_get, chmod, chown, cp, exists, lcd, ln,
    mkdir, mv, rm, runall, sed, wget)

def setup(git_email="jlheller@uw.edu", 
    git_username="Joseph Hellerstein",
    print_only="F"):
  # Invokes all setups to do
  print_only = (print_only == 'T')
  install_tools(print_only=print_only)
  setup_env(git_email, git_username, print_only=print_only)
  setup_apache(print_only=print_only)

DEFAULT_ENGINE = "django.db.backends.sqlite3"
DEFAULT_NAME = "db.sqlite3"
def setup_django(engine=DEFAULT_ENGINE,
                 name=DEFAULT_NAME, 
                 print_only=False,
                 **kwargs):
  DJANGO_DIR = "$HOME/mysite/mysite"
  apt_get("", "sqlite", isSudo=True, **kwargs)
  runall(["pip install django"], isSudo=True, **kwargs)
  if not exists("/usr/local/bin/django-admin", **kwargs):
    runall(["django-admin startproject mysite"], isSudo=False, **kwargs)
  # Modify settings to select the engine and name
  # Modify the settings file
  path = "%s/settings.py" % DJANGO_DIR
  sed(path, DEFAULT_ENGINE, engine, **kwargs)
  sed(path, DEFAULT_NAME, name, **kwargs)
  # Set up the database
  with lcd('$HOME/mysite', print_only=print_only):
    runall(["python manage.py migrate"], isSudo=False, **kwargs)
  
## BUG. print_only becomes false in solo.exists 
def setup_apache(**kwargs):
  apt_get("",  "apache2", isSudo=True, **kwargs)
  if not exists("/vagrant", **kwargs):
    mkdir("$HOME/apache_home", isSudo=False, **kwargs)
    mkdir("$HOME/apache_home/html", isSudo=False, **kwargs)
    command = 'echo "Hello ubuntu World!" > '
    command += '$HOME/apache_home/html/index.html'
    runall([command], isSudo=False, **kwargs)
    ln("s", "$HOME/apache_home", "/vagrant", isSudo=True, **kwargs)
  runall(["rm -rf /var/www"], isSudo=True, **kwargs)
  runall(["ln -fs /vagrant /var/www"], isSudo=True, **kwargs)

def copy_file_in_bin_to_HOME(filename, **kwargs):
  cp('$HOME/BaseStack/bin/%s' % filename, '$HOME', isSudo=True, **kwargs)
  chmod('+x', filename, isSudo=True, **kwargs)
  chown(filename, **kwargs)

def setup_env(git_email, git_username, **kwargs):
  copy_file_in_bin_to_HOME(".bashrc", **kwargs)
  copy_file_in_bin_to_HOME(".vimrc", **kwargs)
  # Git configuration
  commands = '''
    git config --global user.email "%s"
    git config --global user.name "%s"
  ''' % (git_email, git_username)
  runall(commands.split('\n'), isSudo=False, **kwargs)

def install_chef(**kwargs):
  with lcd('$HOME', print_only=kwargs['print_only']):
    commands = '''
       curl -L https://www.opscode.com/chef/install.sh | bash
       wget http://github.com/opscode/chef-repo/tarball/master
       tar -zxf master
       mv chef-chef-repo* chef-repo
       chown -R ubuntu ubuntu chef-repo
       rm master
    '''
    runall(commands.split('\n'), IsSudo=True, **kwargs)
    if exists('BaseStack/cookbooks', **kwargs):
      command = 'cp -r BaseStack/cookbooks/* chef-repo/cookbooks/'
      runall([command], isSudo=False, **kwargs)

def install_tools(**kwargs):
  apt_get("", "python-pip python-dev build-essential", isSudo=True, **kwargs)
  commands = '''
    pip install --upgrade pip 
    pip install --upgrade virtualenv 
  '''
  runall(commands.split('\n'), isSudo=True, **kwargs)
  apt_get("", "curl", isSudo=True, **kwargs)
  apt_get("", "vim", isSudo=True, **kwargs)
