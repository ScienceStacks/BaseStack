#!/bin/bash
# Recursively finds the requested text in all files pattern.
# Patterns should be quotes so that the shell doesn't resolve them to a file
#echo $1
grep -nr "$1" . | grep -v Binary
