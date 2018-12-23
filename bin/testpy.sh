#!/bin/bash
# Runs tests for all test_py files in the directory
FILE="test_*.py"
#
clear
if [ ! -f ${FILE} ]; then
    echo "No test_*.py file found!"
    exit -1
fi
for f in ${FILE}; do
  echo ""
  echo "***$f"
  python $f
done
