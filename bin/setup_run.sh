#!/bin/bash
# Setup paths to run codes
FILE="`pwd`/common_python"
#
if test -d "$FILE"; then
    PYTHONPATH=$FILE:$PYTHONPATH
fi
PYTHONPATH=`pwd`:$PYTHONPATH
export PYTHONPATH
