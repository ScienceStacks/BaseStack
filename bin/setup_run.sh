#!/bin/bash
deactivate
# Generic setup paths to run codes
FILE="`pwd`/common_python"
#
if test -d "$FILE"; then
    PYTHONPATH=`pwd`:$FILE
else
    PYTHONPATH=`pwd`
fi
export PYTHONPATH
