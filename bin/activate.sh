#!/bin/bash
if [ "x" = "x$1" ]; then
    echo "***ERROR: Must specify the virtualization directory"
else
    source $1/bin/activate
fi
# Setup the python path
FILE="`pwd`/setup_run.sh"
if [ -f "$FILE" ]; then
    source $FILE
else
    PYTHONPATH=`pwd`
    export $PYTHONPATH
fi
