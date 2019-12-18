#!/bin/bash
# Set-up for miniconda and installs
function setup_conda {
# Arg 1: python level either 2 or 3
  PY=$1
  CONDA=$HOME/miniconda${PY}/bin/conda
  rm -rf $HOME/miniconda${PY}
  wget https://repo.continuum.io/miniconda/Miniconda${PY}-latest-Linux-x86_64.sh
  bash Miniconda${PY}-latest-Linux-x86_64.sh
  rm Miniconda${PY}-latest-Linux-x86_64.sh
  
  $CONDA update -n base conda
  $CONDA install python=3.6.4  # Latest release for Tellurium
  $CONDA install numpy
  $CONDA install pandas
  $CONDA install matplotlib
  $CONDA install jupyter notebook
  $CONDA install scikit-learn
  $HOME/miniconda${PY}/bin/pip install tellurium
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
# Git initialization
git config --global user.email "jlheller@uw.edu"
git config --global user.name "Joseph Hellerstein"
git_credentials.sh
#
echo "Done!"
