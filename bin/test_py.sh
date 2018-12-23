#!/bin/bash
# Runs tests for all test_py files in the directory
for f in $(ls test_*.py); do
  echo ""
  echo "***$f"
  python $f
done
