# BaseStack
This repo creates a basic software stack on a clean VM. The stack
includes:
  vim, git, pip, curl, apache
There is also a capability to install chef (although some configuration
is still required).

## Usage

1. copy setup_vm.sh from this repo to the home directory of a user on
a clean VM.

2.  In a terminal session, enter: "bash setup_vm.sh".
You will have to enter "y" multiple times, and possibly the root password.

3. In Ubuntu 18, it was necessary to update the Ubuntu network configuration by adding the file /etc/NetworkManager/conf.d/10-globally-managed-devices.conf

## Windows
1. Add c:\Users\windows\Util to path (via env application)
2. Installed python 3.8
3. pip install nose
4. Created .bat files to Util: python.bat, pip.bat, nosetests.bat
5. Created environment variable SCRIPTS that points to my pip install
