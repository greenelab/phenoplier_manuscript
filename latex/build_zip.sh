#!/bin/bash
set -e

rm manuscript-latex_sources.zip
zip --symlinks -r manuscript-latex_sources.zip \
    build_latex.sh \
    images/ \
    latexmkrc \
    manuscript-main_text.pdf \
    manuscript-supplementary_information.pdf \
    manuscript.tex

