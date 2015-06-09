#!/bin/bash
sudo apt-get install vim
cp $HOME/BaseStack/bin/.bashrc $HOME
cp $HOME/BaseStack/bin/.vimrc $HOME
chmod +x $HOME/.vimrc
chmod +x $HOME/.bashrc
#sudo ln -s /mnt/hgfs/josephhellerstein /host
# Install pip and related tools
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 
# Fabric and related
sudo apt-get install fabric
# Get and setup an ssh server for fabric
sudo apt-get install ssh
# sudo service ssh start
