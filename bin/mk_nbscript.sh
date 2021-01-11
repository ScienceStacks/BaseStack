#!/bin/bash
# Converts and an ipython notebook to a script
# Notes: (1) File should not contain spaces
FILE="$1"
cp "$1.ipynb" ${FILE}.ipynb
NOTEBOOK="${FILE}.ipynb"
PYTHON="${FILE}.py"
TMP1="/tmp/run_nb1.py"
if test -f "${NOTEBOOK}"; then
    echo "Creating ${PYTHON}$"
else
    echo "**Error. Cannot find ${NOTEBOOK}"
    exit -1
fi
#
jupyter nbconvert --to script "${NOTEBOOK}"
sed 's/^# In\[.*$/print("&")/' < ${PYTHON}  >  ${TMP1}
sed 's/^get_ipython().run/#&/' < ${TMP1}  > ${PYTHON}
#
echo "***Success. Result is ${PYTHON}"
