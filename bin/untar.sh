#! /bin/bash
# Handles tar.gz and tar.bz2 files
if ( echo $1 | grep -q ".tar.gz$" )
then
  tar -xvzf $1
fi
if ( echo $1 | grep -q ".tgz$" )
then
  tar -xvzf $1
fi
if ( echo $1 | grep -q ".tar.bz2$" )
then
  tar -vxjf $1
fi
