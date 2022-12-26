# Recursively finds files satisfying the requested pattern.
# Patterns should be quotes so that the shell doesn't resolve them to a file
#echo $1
#find . -name "$1" -print
find . | grep $1 > /tmp/ff.out
clear
cat /tmp/ff.out
