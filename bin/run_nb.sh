#!/bin/bash
# Converts and executes an ipython notebook
# Notes: (1) File should not contain spaces
PYTHON="$1.py"
bash mk_nbscript.sh $1
python ${PYTHON}
