#!/bin/bash

rm manuscript-latex.zip
zip --symlinks -r manuscript-latex_sources.zip \
    build_latex.sh \
    images/ \
    latexmkrc \
    main_text.pdf \
    supplementary_information.pdf \
    manuscript.tex

