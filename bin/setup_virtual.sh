#!/bin/bash
# Setup the virtual environment
DIR=$1
python3 -m venv ${DIR}
source ${DIR}/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
deactivate
