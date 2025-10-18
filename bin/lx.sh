#!/bin/bash
pdflatex $1.tex
bibtex $1
pdflatex $1.tex
#latex $1.tex
#dvipdft $1.dvi
open $1.pdf
