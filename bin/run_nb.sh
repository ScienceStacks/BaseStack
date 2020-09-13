#!/bin/csh
# Converts and executes an ipython notebook
# Notes: (1) File should not contain spaces
NB="$1.ipynb"
OUT="$1.py"
TMP1="/tmp/run_nb1.py"
if test -f "${NB}"; then
    echo "Creating ${OUT}$"
else
    echo "**Error. Cannot find ${NB}"
    exit -1
fi
#
jupyter nbconvert --to script "${NB}"
sed 's/^# In\[.*$/print("&")/' < ${OUT}  >  ${TMP1}
sed 's/^get_ipython().run/#&/' < ${TMP1}  > ${OUT}
