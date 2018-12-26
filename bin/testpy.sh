#!/bin/bash
# Runs tests for all test_py files in the directory
FILE=`ls | grep "test_.*.py"`
COUNT=`echo ${FILE} | wc -w`
#
#clear
if [ $COUNT \= 0 ]; then
    echo "No test_*.py file found!"
    exit -1
fi
for f in ${FILE}; do
  echo ""
  echo "***$f"
  python $f
done
