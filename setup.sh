#!/bin/bash
# Assumes that git is installed and have cloned the BaseStack repo
# Install fabric

function apt_get {
# Arg 1: package
  echo "***apt-get build-dep $1" 
  sudo apt-get build-dep $1 
  echo "***apt-get install $1" 
  sudo apt-get install $1 
}

# Do the installs
apt_get fabric
apt_get ssh

cd $HOME/BaseStack/fabric_files
fab setup
cd $HOME/BaseStack
bash setup_miniconda.sh
