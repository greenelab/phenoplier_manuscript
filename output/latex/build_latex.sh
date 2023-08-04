#!/bin/bash
set -e

latexmk -shell-escape manuscript.tex

# split pdf
pdftk manuscript.pdf cat 1-24 output manuscript-main_text.pdf
pdftk manuscript.pdf cat 25-end output manuscript-supplementary_information.pdf

#rm manuscript.pdf

# split main text for journal
csplit manuscript.tex /%SUPPLEMENTARY_INFORMATION_STARTS_HERE%/ '{*}'
mv xx00 manuscript-main_text.tex
echo "\end{document}" >> manuscript-main_text.tex

# the supplementary tex file is not compilable, but it is useful to extract a list
# of labels for the supplementary figures and tables
mv xx01 manuscript-supplementary_information.tex
# rm xx01

# replace in main text file references to supplementary information
python3 replace_labels.py manuscript-supplementary_information.tex manuscript-main_text.tex
