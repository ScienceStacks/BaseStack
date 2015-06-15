#!/bin/bash
# Assumes that git is installed and have cloned the BaseStack repo
# Install fabric
sudo apt-get build-dep fabric
sudo apt-get install fabric
sudo apt-get build-dep ssh
sudo apt-get install ssh
cd $HOME/BaseStack
fab setup
