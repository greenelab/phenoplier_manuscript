#!/bin/bash
set -e

latexmk -shell-escape

# split
pdftk manuscript.pdf cat 1-26 output main_text.pdf
pdftk manuscript.pdf cat 27-end output supplementary_information.pdf

rm manuscript.pdf

