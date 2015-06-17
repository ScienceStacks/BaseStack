#!/usr/bin/env bash

FILE_OUT="/tmp/base_stack.txt"

function apt_get {
# Arg 1: package
  echo "apt-get build-dep $1" >> $FILE_OUT
  sudo apt-get build-dep $1 &>> $FILE_OUT
  echo "apt-get install $1" >> $FILE_OUT
  sudo apt-get install $1 &>> $FILE_OUT
}

# Update the local repository
sudo apt-get update > $FILE_OUT

# Install git
apt_get git

# Get the base repo
git clone https://github.com/ScienceStacks/BaseStack.git
cd $HOME/BaseStack
bash setup.sh
echo "Success!"
