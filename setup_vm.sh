#!/usr/bin/env bash

apt-get update

# Install git
sudo apt-get install git

# Get the base repo
git clone https://github.com/ScienceStacks/BaseStack.git
cd $HOME/BaseStack
bash setup.sh
echo "Success!"
