#!/bin/bash
# Sets up Jupyter environment
# Install nodejs and related
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs
# Install labs extensions
jupyter labextension install @jupyterlab/toc
