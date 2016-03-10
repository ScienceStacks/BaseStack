#!/bin/bash
# Set-up for miniconda and installs
rm -rf $HOME/miniconda2
wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
bash Miniconda-latest-Linux-x86_64.sh
rm Miniconda-latest-Linux-x86_64.sh
$HOME/miniconda2/bin/conda install numpy
$HOME/miniconda2/bin/conda install ipython-notebook
