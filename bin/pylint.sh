#!/bin/bash
# Does a pylint of one or more files
# Inputs: files to lint. If none, does all *.py files in directory
OK="0"

if [ "$#" -eq 0 ]
then
  FILES=`ls *.py`
else
  FILES=$@
fi

clear
# Iterate across all the files to check
for ff in $FILES; do
  NO_LINES=`pylint --rcfile $HOME/BaseStack/bin/pylint.rcfile $ff \
        | grep ":*,"  \
        | grep -v 'Your code has been rated' \
        | grep -v 'Unable to import' \
        | wc | awk '{print $1}'`
  if [ $NO_LINES -ne "0" ]
  then
    OK="1"
    read -p "Press enter to see errors in $ff:"
    echo ""
    pylint --rcfile $HOME/BaseStack/bin/pylint.rcfile $ff \
        | grep ","  \
        | grep -v 'Your code has been rated' \
        | grep -v 'Unable to import'
  fi
done

if [ $OK -eq "0" ]
then
  echo "No errors found."
