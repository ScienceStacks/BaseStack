#!/bin/bash
# Assumes that git is installed and have cloned the BaseStack repo
chmod +x $HOME/BaseStack/bin/*.sh
chmod +x $HOME/BaseStack/install_scripts/*.sh
# Install curl
sudo apt-get install curl
# Do other basic setups
bash install_scripts/basic_setup.sh
