#!/bin/bash
set -e

latexmk -shell-escape

# split
pdftk manuscript.pdf cat 1-23 output manuscript-main_text.pdf
pdftk manuscript.pdf cat 24-end output manuscript-supplementary_information.pdf

#rm manuscript.pdf

