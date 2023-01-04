#!/bin/bash
REPOPATH=~/home/Technical/repos
FILE=`pwd`/$1
START_MARKER="$2"
END_MARKER="$3"
# Handle defaults
if [ "x${END_MARKER}" = "x" ];
  then
     END_MARKER='end-code-block'
fi
if [ "x${START_MARKER}" = "x" ];
  then
     START_MARKER='code-block'
fi
PGMDIR=${REPOPATH}/BaseStack/python
source ${PGMDIR}/base/bin/activate
python ${PGMDIR}/src/grep_line.py $FILE -s ${START_MARKER} -e ${END_MARKER}
