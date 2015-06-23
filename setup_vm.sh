#!/usr/bin/env bash

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
bash setup.sh
echo "Success!"
