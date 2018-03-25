#!/bin/bash
# Set-up for miniconda and installs
function setup_conda {
# Arg 1: python level either 2 or 3
  PY=$1
  rm -rf $HOME/miniconda${PY}
  wget https://repo.continuum.io/miniconda/Miniconda${PY}-latest-Linux-x86_64.sh
  bash Miniconda${PY}-latest-Linux-x86_64.sh
  rm Miniconda${PY}-latest-Linux-x86_64.sh
  $HOME/miniconda${PY}/bin/conda update -n base conda
  $HOME/miniconda${PY}/bin/conda install numpy
  $HOME/miniconda${PY}/bin/conda install pandas
  $HOME/miniconda${PY}/bin/conda install jupyter notebook
}
# Put shell scripts in path
cp bin/.bashrc $HOME

#
setup_conda 3
#
sudo apt install python-setuptools
#
sudo apt-get install vim
cp vim/scripts.vim $HOME/.vimrc
#
echo "Done!"
