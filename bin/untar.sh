#! /bin/bash
# Handles tar.zip and tar.bz2 files
if ( echo $1 | grep -q ".tar.zip$" )
then
  tar -xvzf $1
fi
if ( echo $1 | grep -q ".tar.bz2$" )
then
  tar -vxjf $1
fi
