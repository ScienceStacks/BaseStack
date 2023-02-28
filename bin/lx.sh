#!/bin/bash
latex $1.tex
dvipdft $1.dvi
open $1.pdf
