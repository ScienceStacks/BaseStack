#!/bin/bash
if [ "x" = "x$1" ]; then
    echo "***ERROR: Must specify the virtualization directory"
else
    source $1/bin/activate
fi
