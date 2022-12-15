#!/bin/bash
# Arg 1 - addiional path to add at end
deactivate
# Generic setup paths to run codes
FILE="`pwd`/common_python"
PYTHONPATH=`pwd`
#
if test -d "$FILE"; then
    PYTHONPATH=$FILE:${PYTHONPATH}
fi
if [ "x$1" != "x" ]; then
    PYTHONPATH=${PYTHONPATH}:$1
fi
export PYTHONPATH
