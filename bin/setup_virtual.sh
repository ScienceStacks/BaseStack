#!/bin/bash
# Setup the virtual environment
DIR=$1
python3 -m venv ${DIR}
source ${DIR}/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
