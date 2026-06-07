#!/bin/bash
# Setup the virtual environment.
# Musts:
#   - in the directory where the environment is to be set up
#   - requirements.txt exists
# Arg 1 - name of virtual environment directory
PYTHON_LEVEL="3.11"
if [ "x" = "x$1" ]; then
    echo "***ERROR: Must specify the virtualization directory"
    exit -1
fi
DIR=$1
#
virtualenv -p /opt/homebrew/bin/python${PYTHON_LEVEL} ${DIR}
source ${DIR}/bin/activate
pip install --upgrade pip
# Check if need to install requirements
if [ -f "requirements.txt" ]; then
    pip install --no-cache-dir -r requirements.txt
else 
    echo "***No requirements.txt found"
fi
deactivate
