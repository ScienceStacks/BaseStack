#!/bin/bash
# Move list of files to temp
for f in $@; do
  if test -f ${f}; then
    mv -f ${f} /tmp
  fi;
done
