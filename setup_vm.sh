#!/usr/bin/env bash
# In case there is a problem with apt-get (e.g., "must have source URI"),
# can regenerate sources.list using https://repogen.simplylinux.ch/.
# The file is in /etc/apt.

function apt_get {
# Arg 1: package
  echo "apt-get build-dep $1"
  sudo apt-get build-dep $1 
  echo "apt-get install $1"
  sudo apt-get install $1 
}

# Update the local repository
sudo apt-get update

# Install git
apt_get git

# Get the base repo
git clone https://github.com/ScienceStacks/BaseStack.git
cd $HOME/BaseStack
git config credential.helper store  # Avoid repeated entry of creds
git config --global push.default simple
git config --global core.editor "vim"
git config --global color.ui "auto"
echo "Success. Now run setup.sh or setup_minimal.sh"
