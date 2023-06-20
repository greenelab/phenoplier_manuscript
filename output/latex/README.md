# Steps to build latex file

1. Compile with Manubot:
    ```bash
    # conda activate manubot-phenoplier
    BUILD_PDF=false BUILD_DOCX=false BUILD_LATEX=true bash build/build.sh && manubot webpage
    ```

1. Now the latex file is in `output/latex/manuscript.tex`.
Several changes were manually added after generating this file (such as list of authors, affiliations, supplementary figures/tables, etc) that MUST NOT BE overwritten by this next step.

1. Compile with latex:
    ```bash
    cd output/latex
    bash build_latex.sh
    ```

    After compilations, the output files are `main_text.pdf` and `supplementary_information.pdf`.

1. To generate "Supplementary Reference", you can remove all the other files in `content/` and leave the supplementary information only, then compile with Manubot (first step), and copy/paste the generated references.
This will also allow to see which references are actually being used.
Then you'll need to manually change the reference numbers in the tex file.
Remember to remove the supplementary references from the main references.
