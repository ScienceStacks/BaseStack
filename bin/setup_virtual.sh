#!/bin/bash
# Setup the virtual environment.
# Musts:
#   - in the directory where the environment is to be set up
#   - requirements.txt exists
# Arg 1 - name of virtual environment directory
if [ "x" = "x$1" ]; then
    echo "***ERROR: Must specify the virtualization directory"
    exit -1
fi
DIR=$1
#
python3 -m venv ${DIR}
source ${DIR}/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
