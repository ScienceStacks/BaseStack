from fabric.api import env, local, sudo
from fabric.contrib.files import exists
from fabric.context_managers import cd
env.user = 'ubuntu'
env.hosts = ['localhost']

env.chef_executable = '/var/lib/gems/1.8/bin/chef-solo'

def old_install_chef():
    sudo('apt-get update', pty=True)
    sudo('apt-get install -y git-core rubygems ruby ruby-dev', pty=True)
    sudo('gem install chef', pty=True)

def also_old_install_chef():
    with cd('$HOME'):
      sudo('curl -L https://www.opscode.com/chef/install.sh | bash', 
          pty=True)
      sudo('wget http://github.com/opscode/chef-repo/tarball/master', 
          pty=True)
      sudo('tar -zxf master', pty=True)
      sudo('mv chef-chef-repo* chef-repo', pty=True)
      sudo('rm master', pty=True)
      if exists('BaseStack/cookbooks'):
        command = 'cp -r BaseStack/cookbooks/* chef-repo/cookbooks/'
        try:
          sudo(command, pty=True)
        except Exception as e:
          print e

def install_chef():
    with cd('$HOME'):
      commands = '''
         curl -L https://www.opscode.com/chef/install.sh | bash
         wget http://github.com/opscode/chef-repo/tarball/master
         tar -zxf master
         mv chef-chef-repo* chef-repo
         rm master
      '''
      do_sudo(commands.split('\n'))
      if exists('BaseStack/cookbooks'):
        command = 'cp -r BaseStack/cookbooks/* chef-repo/cookbooks/'
        do_sudo([command])

def do_sudo(commands):
  # Run sudo a a list of commands
  # Input: commands - list of commands
  for cmd in commands:
    print "cmd = %s" % cmd
    if cmd.strip():  # Must be a string with non-blanks
      try:
        sudo(cmd, pty=True)
      except Exception as e:
        print e


def sync_config():
    local('rsync -av . %s@%s:/etc/chef' % (env.user, env.hosts[0]))

def update():
    sync_config()
    sudo('cd /etc/chef && %s' % env.chef_executable, pty=True)
