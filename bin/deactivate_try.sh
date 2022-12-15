#!/bin/bash
OUT=`which.py deactivate`
SUB='None'
echo $SUB
if [[ "$OUT" == "$SUB" ]]; then
    echo ""
else
    echo "h"
    source deactivate
fi
