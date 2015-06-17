#!/bin/bash
# Assumes that git is installed and have cloned the BaseStack repo
# Install fabric
FILE_OUT="/tmp/base_stack.txt"

function apt_get {
# Arg 1: package
  echo "***apt-get build-dep $1" &>> $FILE_OUT
  sudo apt-get build-dep $1 &>> $FILE_OUT
  echo "***apt-get install $1" &>> $FILE_OUT
  sudo apt-get install $1 & $FILE_OUT
}

# Do the installs
apt_get fabric
apt_get ssh

cd $HOME/BaseStack/fabric_files
#fab setup
