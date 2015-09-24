#!/bin/bash
# Does a jslint
# Inputs: files to lint
#         if none, then all *.js files a linted
OK="0"

if [ "$#" -eq 0 ]
then
  FILES=`ls *.js`
else
  FILES=$@
fi

# Iterate across all the files to check
for ff in $FILES; do
  clear
  LINES=`jslint.sh $ff | grep "is OK." | wc | awk '{print $1}'`
  if [ $LINES -ne "1" ]
  then
    OK="1"
    jslint.sh $ff | more
    read -p "Press [Enter] to continue ..."
  fi
done

if [ $OK -eq "0" ]
then
  echo "No errors found."
else
  echo "Errors founds."
fi
