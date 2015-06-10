#!/bin/bash
# Assumes that git is installed and have cloned the BaseStack repo
# Install fabric
sudo apt-get install fabric
sudo apt-get install ssh
cd $HOME/BaseStack/install_scripts
fab install_tools
fab setup_env  # After tools install to make sure get correct runfiles
