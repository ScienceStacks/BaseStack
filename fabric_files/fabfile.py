'''
  Codes for creating a basic scientific statck on a linux VM.
  To see the commands that will be issued, use the flag
  print_only=T
'''

from contextlib import contextmanager
from fabric_solo import (apt_get, chmod, chown, cp, exists, lcd,
    ln, mkdir, mv, rm, runall, sed, wget)

# Shared constants
REPO_PATH = "$HOME/BaseStack"
BIN_PATH = "%s/bin" % REPO_PATH
# Constants used for Django
DEFAULT_ENGINE = "django.db.backends.sqlite3"
DEFAULT_NAME = "db.sqlite3"
SITE_NAME = "mysite"
SITE_DIR = "%s/aux_files/%s" % (REPO_PATH, SITE_NAME)
APP_DIR = "%s/%s" % (SITE_DIR, SITE_NAME)
CONF_PATH = "%s/aux_files/000-default.conf" % REPO_PATH
SUDO_PW = "ubuntu"
GIT_EMAIL = "jlheller@uw.edu"
GIT_USERNAME = "Joseph Hellerstein"

def setup(git_email=GIT_EMAIL,
    git_username=GIT_USERNAME,
    print_only="F"):
  # Invokes all setups to do
  print_only = (print_only == 'T')
  install_tools(print_only=print_only)
  setup_env(git_email=git_email, git_username=git_username, 
      print_only=print_only)
  setup_apache(print_only=print_only)

# UNDER DEVELOPMENT
# Need to:
#  1. Show how connect to database
#  2. Allow ubuntu user access
# Setup for the postgress database
USER = 'ubuntu'
def setup_postgres(db=None,
                     print_only=False,
                     **kwargs):
  apt_get("postgresql postgresql-contrib", 
      isSudo=True, print_only=print_only, **kwargs)
  apt_get("pgadmin3",
      isSudo=True, print_only=print_only, **kwargs)
  runall(["createuser -d %s" % USER],
       isSudo=True, print_only=print_only, user="postgres", **kwargs)
  if db is not None:
    runall(["createdb -O %s %s" % (USER, db)],
         isSudo=False, print_only=print_only, **kwargs)
  # Table manipulation from the command line. Lower case are variables
  # that should be substituted. preface these commands with
  # "PSQL db -c"
  # CREATE TABLE table_name (col_name1 data_type2, col_name2 data_type2);
  # INSERT INTO table_name (col_name1, col_name2) VALUES (value1, value2);
  # SELECT * FROM table_name
  

# This setup assumes that setup_apache has already been done
# To install a new site, use
#  1.  Create a conf_file that points to the appropriate directories
#      for the new site.
#  2.  Run fab setup_django:conf_path=NewConfPath,app_dir=NewAppDir
def setup_django(engine=DEFAULT_ENGINE,
                 name=DEFAULT_NAME,
                 conf_path=CONF_PATH,
                 app_dir=APP_DIR, 
                 print_only=False,
                 **kwargs):
  apt_get("sqlite", isSudo=True, print_only=print_only, **kwargs)
  runall(["pip install django"], isSudo=False, 
      print_only=print_only, **kwargs)
  # Modify settings to select the engine and name
  # Modify the settings file
  path = "%s/settings.py" % app_dir
  sed(path, DEFAULT_ENGINE, engine, 
     print_only=print_only, **kwargs)
  sed(path, DEFAULT_NAME, name, 
    print_only=print_only, **kwargs)
  cp(conf_path,
      '/etc/apache2/sites-available/000-default.conf', 
      options="f", isSudo=True, print_only=print_only, **kwargs)
  runall(["bash %s/apache_restart.sh" % BIN_PATH], isSudo=True, 
      print_only=print_only, **kwargs)

  
def setup_apache(**kwargs):
  apt_get( "apache2", isSudo=True, **kwargs)
  # wsgi must be installed separately
  apt_get( "libapache2-mod-wsgi", isSudo=True, **kwargs)
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
  cp("%s/bin/%s" % (REPO_PATH, filename), 
      '$HOME', isSudo=True, **kwargs)
  chmod('+x', filename, isSudo=True, **kwargs)
  chown(filename, **kwargs)

def setup_env(git_email=GIT_EMAIL,
    git_username=GIT_USERNAME, print_only=False, **kwargs):
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
    if exists("%s/cookbooks" % REP_PATH, **kwargs):
      command = "cp -r %s/cookbooks/* chef-repo/cookbooks/" % REPO_PATH
      runall([command], isSudo=False, **kwargs)

def install_tools(**kwargs):
  apt_get("python-pip python-dev build-essential", isSudo=True, **kwargs)
  apt_get("pylint", isSudo=True, **kwargs)
  commands = '''
    pip install --upgrade pip 
    pip install --upgrade virtualenv 
  '''
  runall(commands.split('\n'), isSudo=True, **kwargs)
  commands = '''
    pip install numpy
    pip install bokeh
    pip install xlrd
    pip install openpyxl
  '''
  runall(commands.split('\n'), isSudo=True, **kwargs)
  apt_get("curl", isSudo=True, **kwargs)
  apt_get("vim", isSudo=True, **kwargs)
  # Install jslint
  apt_get("nodejs npm", isSudo=True, **kwargs)
  commands = '''
    cd /usr/share;
    rm -fR jslint;
    npm install jslint;
  '''
  runall(commands.split('\n'), isSudo=True, **kwargs)
  commands = '''
    npm install smash uglify-js slickgrid yui
    npm install uglifycss -g
    ln -sf /usr/bin/nodejs /usr/bin/node
    npm install -g node-qunit-phantomjs
  '''
  runall(commands.split('\n'), isSudo=True, **kwargs)
