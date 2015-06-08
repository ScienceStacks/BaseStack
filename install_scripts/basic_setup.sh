#!/bin/bash
sudo apt-get install vim
cp $HOME/BaseStack/bin/.bashrc $HOME
cp $HOME/BaseStack/bin/.vimrc $HOME
chmod +x $HOME/.vimrc
chmod +x $HOME/.bashrc
#sudo ln -s /mnt/hgfs/josephhellerstein /host
