#!/bin/bash
# Set-up for miniconda and installs
#rm -rf $HOME/miniconda2
CONDA=$HOME/miniconda3/bin/conda
#wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
#bash Miniconda-latest-Linux-x86_64.sh
#rm Miniconda-latest-Linux-x86_64.sh
$CONDA update -n base -c defaults conda
$CONDA install numpy
$CONDA install pandas
$CONDA install jupyter notebook
