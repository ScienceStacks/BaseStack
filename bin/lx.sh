#!/bin/bash
pdflatex $1
#latex $1.tex
#dvipdft $1.dvi
open $1.pdf
