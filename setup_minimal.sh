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
  # Install spyder and intellisense
  $HOME/miniconda${PY}/bin/pip install spyder
  $HOME/miniconda${PY}/bin/pip install rope_py3k
}
# Put shell scripts in path
cp bin/.bashrc $HOME

# Install kite command completion
bash -c "$(wget -q -O - https://linux.kite.com/dls/linux/current)"

#
setup_conda 3
#
sudo apt install python-setuptools
#
sudo apt-get install vim
cp vim/scripts.vim $HOME/.vimrc
cp -r vim/dot_vim $HOME/.vim
# Git initialization
git config --global user.email "jlheller@uw.edu"
git config --global user.name "Joseph Hellerstein"
git_credentials.sh
# Modify the network configuration to ensure network access
sudo touch /etc/NetworkManager/conf.d
# Setup access to clipboard
sudo apt-get update -y
sudo apt-get install -y xclip
# Get xclip
sudo apt-get install xclip
#
# Set up compilers
sudo apt update
sudo apt install build-essential
sudo apt-get install manpages-dev:w
sudo apt-get install gfortran
# Install pip requirements
sudo apt install libssl-dev
sudo apt install libncurses5-dev
sudo apt install libsqlite3-dev
sudo apt install libreadline-dev
sudo apt install libtk8.6
sudo apt install libgdm-dev
sudo apt install libdb4o-cil-dev
sudo apt install libpcap-dev

echo "Done!"
