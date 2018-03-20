#!/bin/bash
# Set-up for miniconda and installs
rm -rf $HOME/miniconda3
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh
$HOME/miniconda3/bin/conda install numpy
$HOME/miniconda3/bin/conda install pandas
$HOME/miniconda3/bin/conda install jupyter-notebook
#
sudo apt-get install vim
cp vim/scripts.vim $HOME/.vimrc
