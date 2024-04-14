#!/bin/bash
# Creates symbolic links to a random subset of files
#  to the destination path
#   Arg1: dest path
#   Arg2: number of files
DESTPATH=$1
NUMFILE=$2
# Remove existing directory
if [ -d "$DESTPATH" ]; then
  rm -rf ${DESTPATH}
fi
#
mkdir ${DESTPATH}
for f in `ls | shuf -n ${NUMFILE}`
  do
    ln -s $f ${DESTPATH}/$f
  done
