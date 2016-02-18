#!/bin/bash
pep8 $1 $2 $3 $4 | grep -v "indentation is not a multiple of four"
