---
title: Projecting genetic associations through gene expression patterns highlights disease etiology and drug mechanisms
keywords:
- gene co-expression
- MultiPLIER
- PhenomeXcan
- TWAS
lang: en-US
date-meta: '2022-09-08'
author-meta:
- Milton Pividori
- Sumei Lu
- Binglan Li
- Chun Su
- Matthew E. Johnson
- Wei-Qi Wei
- Qiping Feng
- Bahram Namjou
- Krzysztof Kiryluk
- Iftikhar Kullo
- Yuan Luo
- Blair D. Sullivan
- Benjamin F. Voight
- Carsten Skarke
- Marylyn D. Ritchie
- Struan F.A. Grant
- Casey S. Greene
header-includes: |-
  <!--
  Manubot generated metadata rendered from header-includes-template.html.
  Suggest improvements at https://github.com/manubot/manubot/blob/main/manubot/process/header-includes-template.html
  -->
  <meta name="dc.format" content="text/html" />
  <meta name="dc.title" content="Projecting genetic associations through gene expression patterns highlights disease etiology and drug mechanisms" />
  <meta name="citation_title" content="Projecting genetic associations through gene expression patterns highlights disease etiology and drug mechanisms" />
  <meta property="og:title" content="Projecting genetic associations through gene expression patterns highlights disease etiology and drug mechanisms" />
  <meta property="twitter:title" content="Projecting genetic associations through gene expression patterns highlights disease etiology and drug mechanisms" />
  <meta name="dc.date" content="2022-09-08" />
  <meta name="citation_publication_date" content="2022-09-08" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Milton Pividori" />
  <meta name="citation_author_institution" content="Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA" />
  <meta name="citation_author_orcid" content="0000-0002-3035-4403" />
  <meta name="twitter:creator" content="@miltondp" />
  <meta name="citation_author" content="Sumei Lu" />
  <meta name="citation_author_institution" content="Center for Spatial and Functional Genomics, Children&#39;s Hospital of Philadelphia, Philadelphia, PA, 19104, USA" />
  <meta name="citation_author" content="Binglan Li" />
  <meta name="citation_author_institution" content="Department of Biomedical Data Science, Stanford University, Stanford, CA, USA" />
  <meta name="citation_author_orcid" content="0000-0002-0103-6107" />
  <meta name="citation_author" content="Chun Su" />
  <meta name="citation_author_institution" content="Center for Spatial and Functional Genomics, Children&#39;s Hospital of Philadelphia, Philadelphia, PA, 19104, USA" />
  <meta name="citation_author_orcid" content="0000-0001-6388-8666" />
  <meta name="citation_author" content="Matthew E. Johnson" />
  <meta name="citation_author_institution" content="Center for Spatial and Functional Genomics, Children&#39;s Hospital of Philadelphia, Philadelphia, PA, 19104, USA" />
  <meta name="citation_author" content="Wei-Qi Wei" />
  <meta name="citation_author_institution" content="Vanderbilt University Medical Center" />
  <meta name="citation_author" content="Qiping Feng" />
  <meta name="citation_author_institution" content="Vanderbilt University Medical Center" />
  <meta name="citation_author_orcid" content="0000-0002-6213-793X" />
  <meta name="citation_author" content="Bahram Namjou" />
  <meta name="citation_author_institution" content="Cincinnati Children&#39;s Hospital Medical Center" />
  <meta name="citation_author" content="Krzysztof Kiryluk" />
  <meta name="citation_author_institution" content="Department of Medicine, Division of Nephrology, Vagelos College of Physicians &amp; Surgeons, Columbia University, New York, New York" />
  <meta name="citation_author_orcid" content="0000-0002-5047-6715" />
  <meta name="twitter:creator" content="@kirylukk" />
  <meta name="citation_author" content="Iftikhar Kullo" />
  <meta name="citation_author_institution" content="Mayo Clinic" />
  <meta name="citation_author" content="Yuan Luo" />
  <meta name="citation_author_institution" content="Northwestern University" />
  <meta name="citation_author" content="Blair D. Sullivan" />
  <meta name="citation_author_institution" content="School of Computing, University of Utah, Salt Lake City, UT, USA" />
  <meta name="citation_author" content="Benjamin F. Voight" />
  <meta name="citation_author_institution" content="Department of Systems Pharmacology and Translational Therapeutics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA" />
  <meta name="citation_author_institution" content="Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA" />
  <meta name="citation_author_institution" content="Institute for Translational Medicine and Therapeutics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA" />
  <meta name="citation_author_orcid" content="0000-0002-6205-9994" />
  <meta name="twitter:creator" content="@bvoight28" />
  <meta name="citation_author" content="Carsten Skarke" />
  <meta name="citation_author_institution" content="Institute for Translational Medicine and Therapeutics, Department of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA" />
  <meta name="citation_author_orcid" content="0000-0001-5145-3681" />
  <meta name="twitter:creator" content="@CarstenSkarke" />
  <meta name="citation_author" content="Marylyn D. Ritchie" />
  <meta name="citation_author_institution" content="Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA" />
  <meta name="citation_author_orcid" content="0000-0002-1208-1720" />
  <meta name="twitter:creator" content="@MarylynRitchie" />
  <meta name="citation_author" content="Struan F.A. Grant" />
  <meta name="citation_author_institution" content="Center for Spatial and Functional Genomics, Children&#39;s Hospital of Philadelphia, Philadelphia, PA, 19104, USA" />
  <meta name="citation_author_institution" content="Department of Pediatrics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, 19104, USA" />
  <meta name="citation_author_institution" content="Division of Human Genetics, Children&#39;s Hospital of Philadelphia, Philadelphia, PA, 19104, USA" />
  <meta name="citation_author_orcid" content="0000-0003-2025-5302" />
  <meta name="twitter:creator" content="@STRUANGRANT" />
  <meta name="citation_author" content="Casey S. Greene" />
  <meta name="citation_author_institution" content="Center for Health AI, University of Colorado School of Medicine, Aurora, CO 80045, USA" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, University of Colorado School of Medicine, Aurora, CO 80045, USA" />
  <meta name="citation_author_orcid" content="0000-0001-8713-9213" />
  <meta name="twitter:creator" content="@GreeneScientist" />
  <link rel="canonical" href="https://greenelab.github.io/phenoplier_manuscript/" />
  <meta property="og:url" content="https://greenelab.github.io/phenoplier_manuscript/" />
  <meta property="twitter:url" content="https://greenelab.github.io/phenoplier_manuscript/" />
  <meta name="citation_fulltext_html_url" content="https://greenelab.github.io/phenoplier_manuscript/" />
  <meta name="citation_pdf_url" content="https://greenelab.github.io/phenoplier_manuscript/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://greenelab.github.io/phenoplier_manuscript/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://greenelab.github.io/phenoplier_manuscript/v/f467eed0356d9715c502c530b136646a78e6bed7/" />
  <meta name="manubot_html_url_versioned" content="https://greenelab.github.io/phenoplier_manuscript/v/f467eed0356d9715c502c530b136646a78e6bed7/" />
  <meta name="manubot_pdf_url_versioned" content="https://greenelab.github.io/phenoplier_manuscript/v/f467eed0356d9715c502c530b136646a78e6bed7/manuscript.pdf" />
  <meta property="og:type" content="article" />
  <meta property="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />
  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />
  <meta name="theme-color" content="#ad1457" />
  <!-- end Manubot generated metadata -->
bibliography:
- content/manual-references.json
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
manubot-clear-requests-cache: false
...



<!--  -->

<!-- [
<i class="fas fa-info-circle fa-lg"></i> **Draft manuscript**<br>
Text in <span style="color: red">red</span>/<span class="red">red</span> are internal comments
]{.banner .lightblue} -->


<small><em>
This manuscript
([permalink](https://greenelab.github.io/phenoplier_manuscript/v/f467eed0356d9715c502c530b136646a78e6bed7/))
was automatically generated
from [greenelab/phenoplier_manuscript@f467eed](https://github.com/greenelab/phenoplier_manuscript/tree/f467eed0356d9715c502c530b136646a78e6bed7)
on September 8, 2022.
</em></small>

## Authors



+ **Milton Pividori**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-3035-4403](https://orcid.org/0000-0002-3035-4403)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [miltondp](https://github.com/miltondp)
    · ![Twitter icon](images/twitter.svg){.inline_icon width=16 height=16}
    [miltondp](https://twitter.com/miltondp)<br>
  <small>
     Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA
     · Funded by The Gordon and Betty Moore Foundation GBMF 4552; The National Human Genome Research Institute (R01 HG010067); The National Human Genome Research Institute (K99HG011898)
  </small>

+ **Sumei Lu**
  <br><br>
  <small>
     Center for Spatial and Functional Genomics, Children's Hospital of Philadelphia, Philadelphia, PA, 19104, USA
  </small>

+ **Binglan Li**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-0103-6107](https://orcid.org/0000-0002-0103-6107)<br>
  <small>
     Department of Biomedical Data Science, Stanford University, Stanford, CA, USA
  </small>

+ **Chun Su**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0001-6388-8666](https://orcid.org/0000-0001-6388-8666)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [sckinta](https://github.com/sckinta)<br>
  <small>
     Center for Spatial and Functional Genomics, Children's Hospital of Philadelphia, Philadelphia, PA, 19104, USA
  </small>

+ **Matthew E. Johnson**
  <br><br>
  <small>
     Center for Spatial and Functional Genomics, Children's Hospital of Philadelphia, Philadelphia, PA, 19104, USA
  </small>

+ **Wei-Qi Wei**
  <br><br>
  <small>
     Vanderbilt University Medical Center
  </small>

+ **Qiping Feng**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-6213-793X](https://orcid.org/0000-0002-6213-793X)<br>
  <small>
     Vanderbilt University Medical Center
  </small>

+ **Bahram Namjou**
  <br><br>
  <small>
     Cincinnati Children's Hospital Medical Center
  </small>

+ **Krzysztof Kiryluk**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-5047-6715](https://orcid.org/0000-0002-5047-6715)
    · ![Twitter icon](images/twitter.svg){.inline_icon width=16 height=16}
    [kirylukk](https://twitter.com/kirylukk)<br>
  <small>
     Department of Medicine, Division of Nephrology, Vagelos College of Physicians & Surgeons, Columbia University, New York, New York
  </small>

+ **Iftikhar Kullo**
  <br><br>
  <small>
     Mayo Clinic
  </small>

+ **Yuan Luo**
  <br><br>
  <small>
     Northwestern University
  </small>

+ **Blair D. Sullivan**
  <br><br>
  <small>
     School of Computing, University of Utah, Salt Lake City, UT, USA
  </small>

+ **Benjamin F. Voight**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-6205-9994](https://orcid.org/0000-0002-6205-9994)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [bvoight](https://github.com/bvoight)
    · ![Twitter icon](images/twitter.svg){.inline_icon width=16 height=16}
    [bvoight28](https://twitter.com/bvoight28)<br>
  <small>
     Department of Systems Pharmacology and Translational Therapeutics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA; Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA; Institute for Translational Medicine and Therapeutics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA
  </small>

+ **Carsten Skarke**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0001-5145-3681](https://orcid.org/0000-0001-5145-3681)
    · ![Twitter icon](images/twitter.svg){.inline_icon width=16 height=16}
    [CarstenSkarke](https://twitter.com/CarstenSkarke)<br>
  <small>
     Institute for Translational Medicine and Therapeutics, Department of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA
  </small>

+ **Marylyn D. Ritchie**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-1208-1720](https://orcid.org/0000-0002-1208-1720)
    · ![Twitter icon](images/twitter.svg){.inline_icon width=16 height=16}
    [MarylynRitchie](https://twitter.com/MarylynRitchie)<br>
  <small>
     Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA
  </small>

+ **Struan F.A. Grant**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0003-2025-5302](https://orcid.org/0000-0003-2025-5302)
    · ![Twitter icon](images/twitter.svg){.inline_icon width=16 height=16}
    [STRUANGRANT](https://twitter.com/STRUANGRANT)<br>
  <small>
     Center for Spatial and Functional Genomics, Children's Hospital of Philadelphia, Philadelphia, PA, 19104, USA; Department of Pediatrics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, 19104, USA; Division of Human Genetics, Children's Hospital of Philadelphia, Philadelphia, PA, 19104, USA
  </small>

+ **Casey S. Greene**
  ^[✉](#correspondence)^<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0001-8713-9213](https://orcid.org/0000-0001-8713-9213)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [cgreene](https://github.com/cgreene)
    · ![Twitter icon](images/twitter.svg){.inline_icon width=16 height=16}
    [GreeneScientist](https://twitter.com/GreeneScientist)<br>
  <small>
     Center for Health AI, University of Colorado School of Medicine, Aurora, CO 80045, USA; Department of Biomedical Informatics, University of Colorado School of Medicine, Aurora, CO 80045, USA
     · Funded by The Gordon and Betty Moore Foundation (GBMF 4552); The National Human Genome Research Institute (R01 HG010067); The National Cancer Institute (R01 CA237170)
  </small>


::: {#correspondence}
✉ — Correspondence possible via [GitHub Issues](https://github.com/greenelab/phenoplier_manuscript/issues)
or email to
Casey S. Greene \<casey.s.greene@cuanschutz.edu\>.


:::


## Abstract {.page_break_before}

Understanding how dysregulated transcriptional processes result in tissue-specific pathology requires a mechanistic interpretation of expression regulation across different cell types.
It has been shown that this insight is key for the development of new therapies.
These mechanisms can be identified with transcriptome-wide association studies (TWAS), which have represented a significant step forward to test the mediating role of gene expression in GWAS associations.
However, it is hard to disentangle causal cell types using eQTL data alone, and other methods generally do not use the large amounts of publicly available RNA-seq data.
Here we introduce PhenoPLIER, a polygenic approach that maps both gene-trait associations and pharmacological perturbation data into a common latent representation for a joint analysis.
This representation is based on modules of genes with similar expression patterns across the same tissues.
We observed that diseases were significantly associated with gene modules expressed in relevant cell types, and our approach was accurate in predicting known drug-disease pairs and inferring mechanisms of action.
Furthermore, using a CRISPR screen to analyze lipid regulation, we found that functionally important players lacked TWAS associations but were prioritized in phenotype-associated modules by PhenoPLIER.
By incorporating groups of co-expressed genes, PhenoPLIER can contextualize genetic associations and reveal potential targets within associated processes that are missed by single-gene strategies.


## Introduction

Human diseases have tissue-specific etiologies and manifestations [@pmid:20624743; @pmid:14707169; @doi:10.1073/pnas.0810772105].
In this context, determining how genes influence these complex phenotypes requires mechanistically understanding expression regulation across different cell types [@doi:10.1126/science.aaz1776; @doi:10.1038/s41586-020-2559-3; @doi:10.1038/s41576-019-0200-9], which in turn should lead to improved treatments [@doi:10.1038/ng.3314; @doi:10.1371/journal.pgen.1008489].
Previous studies have described regulatory DNA elements, including chromatin-state annotations [@doi:10.1038/nature11247; @doi:10.1038/nature14248], high-resolution enhancers [@doi:10.1038/nature12787; @doi:10.1038/s41586-020-03145-z], DNase I hypersensitivity maps [@doi:10.1038/s41586-020-2559-3], and genetic effects on gene expression across different tissues [@doi:10.1126/science.aaz1776].
Integrating functional genomics data and GWAS data [@doi:10.1016/j.ajhg.2018.04.002] has improved the identification of these transcriptional mechanisms that, when dysregulated, commonly result in tissue- and cell lineage-specific pathology.


Given the availability of gene expression data across several tissues [@doi:10.1038/nbt.3838; @doi:10.1038/s41467-018-03751-6; @doi:10.1126/science.aaz1776; @doi:10.1186/s13040-020-00216-9], a popular approach to identify these biological processes is the transcription-wide association study (TWAS), which integrates expression quantitative trait loci (eQTLs) data to provide a mechanistic interpretation for GWAS findings.
TWAS relies on testing whether perturbations in gene regulatory mechanisms mediate the association between genetic variants and human diseases [@doi:10.1371/journal.pgen.1009482; @doi:10.1038/ng.3506; @doi:10.1371/journal.pgen.1007889; @doi:10.1038/ng.3367].
However, TWAS has not reliably detected tissue-specific effects because eQTLs are commonly shared across tissues [@doi:10.1016/j.ajhg.2017.01.031; @doi:10.1038/s41588-018-0081-4].
This sharing makes it challenging to identify the tissue or tissues that are etiologically relevant.
Existing methods that connect GWAS findings with gene expression data can infer disease-relevant tissues and cell types [@doi:10.1038/s41588-018-0081-4; @doi:10.1016/j.ajhg.2011.09.002; @doi:10.1093/bioinformatics/btu326; @doi:10.1038/ng.3598; @doi:10.1038/ncomms6890; @doi:10.1038/ng.3981], but they generally rely on small sets of expression data compared with the total number of RNA-seq samples that are increasingly available [@doi:10.1038/s41467-018-03751-6; @doi:10.1038/nbt.3838].
Moreover, widespread gene pleiotropy across complex traits reveals the highly interconnected nature of transcriptional networks [@doi:10.1038/s41588-019-0481-0; @doi:10.1038/ng.3570], where potentially all genes expressed in disease-relevant cell types have a non-zero effect [@doi:10.1016/j.cell.2017.05.038; @doi:10.1016/j.cell.2019.04.014].
Consequently, this complicates the interpretation of genetic effects and hampers translational efforts.


We propose PhenoPLIER, a polygenic approach that infers how groups of functionally-related genes influence complex traits, and how pharmacological perturbations affect these genes' activity to exert their effects.
The approach maps both gene-trait associations and drug-induced transcriptional responses into a common representation for a joint analysis.
For this, we integrated more than 4,000 gene-trait associations (using TWAS from PhenomeXcan [@doi:10.1126/sciadv.aba2083]) and transcriptional profiles of drugs (LINCS L1000 [@doi:10.1016/j.cell.2017.10.049]) into a low-dimensional space learned from public gene expression data on tens of thousands of RNA-seq samples (recount2 [@doi:10.1016/j.cels.2019.04.003; @doi:10.1038/nbt.3838]).
We used a latent representation defined by a computational approach [@doi:10.1038/s41592-019-0456-1] that learns recurrent gene co-expression patterns with certain sparsity constraints and preferences for those that align with prior knowledge (pathways).
This low-dimensional space comprised features representing groups of genes (gene modules) with coordinated expression across different tissues and cell types.
When mapping gene-trait associations to this reduced expression space, we observed that diseases were significantly associated with gene modules expressed in relevant cell types, such as hypothyroidism with T cells and thyroid, corneal endothelial cells with keratometry measurements, hematological assays on specific blood cell types, plasma lipids with adipose tissue, and neuropsychiatric disorders with different brain cell types.
Moreover, since we rely on a large and heterogeneous RNA-seq dataset, we were also able to identify modules associated with cell types under specific stimuli or disease states.
We replicated gene module associations with cardiovascular and autoimmune diseases in the Electronic Medical Records and Genomics (eMERGE) network phase III [@doi:10.1038/gim.2013.72; @doi:10.1101/2021.10.21.21265225].
Furthermore, we performed a CRISPR screen to analyze lipid regulation in HepG2 cells and observed more robust trait associations with modules than with individual genes, even when single genes known to be involved in lipid metabolism did not reach genome-wide significance.
<!-- Since our approach incorporates groups of genes associated with a phenotype instead single genes, it was also more robust in finding meaningful gene module-trait associations, even when individual genes involved in lipid metabolism did not reach genome-wide significance in lipid-related traits. -->
Compared to a single-gene approach, our module-based method also better predicted FDA-approved drug-disease links by capturing tissue-specific pathophysiological mechanisms linked with the mechanism of action of drugs (e.g., niacin with cardiovascular traits via a known immune mechanism), suggesting that modules may provide a better means to examine drug-disease relationships than individual genes.
Finally, exploring the phenotype-module space also revealed stable trait clusters associated with relevant tissues, including a complex branch involving lipids with cardiovascular, autoimmune, and neuropsychiatric disorders.
In summary, instead of considering single genes associated with different complex traits, PhenoPLIER incorporates groups of genes that act together to carry out different functions in specific cell types.
This improves robustness to detect and interpret genetic associations, and here we show how it can prioritize alternative and potentially more promising candidate targets when important single gene associations are not detected.
The approach represents a conceptual shift in the interpretation of genetic studies, and has the potential to extract mechanistic insight from statistical associations to enhance the understanding of complex diseases and their therapeutic modalities.


## Results

<!--

Some papers that might be interesting:

https://www.nature.com/articles/s41591-020-01221-5
Air pollution linked to neurodegeneration markers

-->


### PhenoPLIER: an integration framework based on gene co-expression patterns

![
**Schematic of the PhenoPLIER framework.**
**a)** High-level schematic of PhenoPLIER (a gene module-based method) in the context of TWAS (single-gene) and GWAS (genetic variants).
PhenoPLIER integrates groups of genes co-expressed in specific cell types (gene modules) with gene-trait and gene-drug associations.
**b)** The integration consists of projecting gene-trait/gene-drug associations from PhenomeXcan/LINCS L1000 (bottom) to a latent space based on gene modules (represented by latent variables/LVs) from MultiPLIER (top).
The process generates matrix $\mathbf{\hat{M}}$, where each trait/drug is now described by LVs (only traits are shown).
**c)** LV603, termed as a neutrophil signature in the original MultiPLIER study, was associated in PhenoPLIER with neutrophil counts and other white blood cells (bottom, showing the top 10 traits for LV603).
Genes in LV603 were expressed in relevant cell types (top).
PBMC: peripheral blood mononuclear cells;
mDCs: myeloid dendritic cells.
](images/entire_process/entire_process.svg "PhenoPLIER framework"){#fig:entire_process width="100%"}


PhenoPLIER combines TWAS and drug-induced transcriptional responses with gene co-expression patterns by projecting gene-trait and gene-drug associations onto a latent gene expression representation (Figure @fig:entire_process).
We used PhenomeXcan [@doi:10.1126/sciadv.aba2083], a TWAS resource for the UK Biobank [@doi:10.1038/s41586-018-0579-z] and other cohorts with 4,091 different diseases and traits, and the transcriptional responses to small molecule perturbations from LINCS L1000 [@doi:10.1016/j.cell.2017.10.049] comprising 1,170 compounds.
We obtained a latent gene expression representation from MultiPLIER [@doi:10.1016/j.cels.2019.04.003], an unsupervised learning approach applied to recount2 [@doi:10.1038/nbt.3838] -- a uniformly-curated collection of transcript-level gene expression quantified by RNA-seq in a large, diverse set of samples collected across a range of disease state, cell types differentiation stages, and various stimuli (Methods).
MultiPLIER extracted 987 latent variables (LV) by optimizing data reconstruction but also the alignment of LVs with prior knowledge/pathways (Methods).
Each LV or gene module represents a group of weighted genes expressed together in the same tissues and cell types as a functional unit.
Since LVs might represent a functional set of genes regulated by the same transcriptional program [@doi:10.1186/1471-2164-7-187; @doi:10.1186/s13059-019-1835-8], we conjecture that the projection of TWAS and pharmacologic perturbations data into this latent space could provide context for their interpretation.
PhenoPLIER converts gene associations to an LV score:
all genes' standardized effect sizes for a trait (from TWAS) or differential expression values for a drug (from pharmacologic perturbation data) are multiplied by the LV genes' weights and summed, producing a single value.
This process links different traits and drugs to LVs representing cell types and tissues, even at specific developmental stages or under distinct stimuli.
Examining these LVs is possible because the MultiPLIER's models link to samples, which may be annotated for experimental conditions (represented by matrix $\mathbf{B}$ in Figure @fig:entire_process b, top) in which genes in an LV are expressed.
To further analyze LV-trait associations, we adapted the gene-property approach from MAGMA [@doi:10.1371/journal.pcbi.1004219] to compute an LV-trait $p$-value by fitting a regression model with LV weights as predictors of a trait's gene associations.
Thus PhenoPLIER allows the user to address specific questions, namely:
do disease-associated genes belong to modules expressed in specific tissues and cell types?
Are these cell type-specific modules associated with different diseases (thus, potentially representing a "network pleiotropy" example from an omnigenic point of view [@doi:10.1016/j.cell.2017.05.038])?
Is there a subset of module's genes that is closer to the definition of "core" genes (i.e., directly affecting the trait with no mediated regulation of other genes [@doi:10.1016/j.cell.2019.04.014]) and thus represent alternative and potentially better candidate targets?
Are drugs perturbing these transcriptional mechanisms, and if so, can they suggest potential mechanisms of action?


In the original MultiPLIER study, the authors reported that one of the latent variables, identified as LV603, was associated with a known neutrophil pathway and highly correlated with neutrophil count estimates from whole blood RNA-seq profiles [@doi:10.1186/s13059-016-1070-5].
We analyzed LV603 using PhenoPLIER (Figure @fig:entire_process c) and found that
1) neutrophil counts and other white blood cell traits were ranked among the top 10 traits out of 4,091 (Figure @fig:entire_process c, bottom) and significantly associated with this LV (Supplementary Table @tbl:sup:phenomexcan_assocs:lv603) when using the gene-property approach,
and 2) LV603's genes were expressed in highly relevant cell types (Figure @fig:entire_process c, top).
These results suggested that groups of functionally related and co-expressed genes tend to correspond to groups of trait-associated genes.
Thus, the gene expression space (which has no GTEx samples) and the TWAS space (with gene models trained using GTEx v8) contained shared patterns, and the approach can link transcriptional mechanisms from large and diverse dataset collections to complex traits.


### LVs link genes that alter lipid accumulation with relevant traits and tissues

Our first experiment attempted to answer whether genes in a disease-relevant LV could represent potential therapeutic targets.
For this, the first step was to obtain a set of genes strongly associated with a phenotype of interest.
Therefore, we performed a fluorescence-based CRISPR-Cas9 in the HepG2 cell line and identified 462 genes associated with lipid regulation (Methods).
From these, we selected two high-confidence gene-sets that either caused a decrease or increase of lipids:
a lipids-decreasing gene-set with eight genes: *BLCAP*, *FBXW7*, *INSIG2*, *PCYT2*, *PTEN*, *SOX9*, *TCF7L2*, *UBE2J2*;
and a lipids-increasing gene-set with six genes: *ACACA*, *DGAT2*, *HILPDA*, *MBTPS1*, *SCAP*, *SRPR* (Supplementary File 1).


<!-- From these, we selected four gene-sets that either caused a decrease or increase of lipids with varying degrees of confidence:
a median-confidence lipids-decreasing gene-set had 96 genes in total, with a subset of eight high-confidence genes: *BLCAP*, *FBXW7*, *INSIG2*, *PCYT2*, *PTEN*, *SOX9*, *TCF7L2*, *UBE2J2*;
a median-confidence lipids-increasing gene-set had 175 genes in total, with a subset of eight high-confidence genes: *ACACA*, *DGAT2*, *HILPDA*, *MBTPS1*, *SCAP*, *SRPR* (Supplementary File 1). -->
<!-- Using Fast Gene Set Enrichment Analysis (FGSEA) [@doi:10.1101/060012], we found four LVs significantly enriched for the medium-confidence lipid-altering gene-sets (FDR < 0.05) (Supplementary Table @tbl:sup:lipids_crispr:modules_enriched).
Using the gene-property method, we found that three of these LVs were significantly associated with cardiovascular traits both in PhenomeXcan and eMERGE (Supplementary Tables @tbl:sup:phenomexcan_assocs:lv707, @tbl:sup:emerge_assocs:lv707, @tbl:sup:phenomexcan_assocs:lv905, @tbl:sup:emerge_assocs:lv905, @tbl:sup:phenomexcan_assocs:lv915, @tbl:sup:emerge_assocs:lv915). -->


<!-- Next, we analyzed all 987 LVs using Fast Gene Set Enrichment Analysis (FGSEA) [@doi:10.1101/060012], and found 15 LVs nominally enriched (unadjusted *P* < 0.01) with these lipid-altering gene-sets (Supplementary Tables @tbl:sup:lipids_crispr:modules_enriched_increase and @tbl:sup:lipids_crispr:modules_enriched_decrease).
To maximize interpretability, we only considered LVs that were well-aligned with at least one pathway from the MultiPLIER models (FDR < 0.05) and those where reliable sample metadata about tissue/cell type was available. -->
<!-- We found four LVs nominally enriched (unadjusted *P* < 0.01) with the lipids-increasing gene-set (Supplementary Table @tbl:sup:lipids_crispr:modules_enriched_increase) and two LVs nominally enriched with the lipids-decreasing gene-set (Supplementary Table @tbl:sup:lipids_crispr:modules_enriched_decrease).
By applying our adapted gene-property method, we found that `XXX`{.red} of these LVs were significantly associated with `XXX`{.red} traits both in PhenomeXcan and eMERGE (Supplementary Tables @, @, @, @, @, @).
`Talk briefly about the other LVs`{.red} -->
<!--  -->
<!--  -->
<!-- First, for each lipid-altering gene-set, we assessed the genes' effects on all phenotypes by adding their $p$-values (from S-MultiXcan, transformed to $z$-scores, with no direction of effect and standardized to account for large sample sizes) and obtaining a ranked list of traits. -->
<!-- The top associated traits for genes in the decreasing-lipids gene-set were highly relevant to lipid levels, such as hypertension, diastolic and systolic blood pressure, and vascular diseases, also including asthma and lung function (Supplementary Table @tbl:sup:single_genes:lipids_decreasing:top_traits). -->
<!-- We performed the same operation for our LV-based approach by considering 24 LVs nominally enriched (unadjusted $p$-value < 0.05) with the decreasing-lipids gene-set by using Fast Gene Set Enrichment Analysis (FGSEA) [@doi:10.1101/060012]. -->
<!-- In this case, we also found lipid-related traits among the top 25, including hypertension, blood pressure, cardiometabolic diseases like atherosclerosis, and celiac disease (Supplementary Table @tbl:sup:modules:lipids_decreasing:top_traits). -->


![
**Tissues and traits associated with a gene module related to lipid metabolism (LV246).**
<!--  -->
**a)** Top cell types/tissues where LV246's genes are expressed in.
Values in the $y$-axis come from matrix $\mathbf{B}$ in the MultiPLIER models (Figure @fig:entire_process b, see Methods).
In the $x$-axis, cell types/tissues are sorted by the maximum sample value.
<!--  -->
**b)** Gene-trait associations (S-MultiXcan; threshold at -log($p$)=10) and colocalization probability (fastENLOC) for the top traits in LV246.
The top 40 genes in LV246 are shown, sorted by their LV weight (matrix $\mathbf{Z}$), from largest (the top gene *SCD*) to smallest (*FAR2*);
*DGAT2* and *ACACA*, in boldface, are two of the six high-confidence genes in the lipids-increasing gene-set from the CRISPR-screen.
Cardiovascular-related traits are in boldface.
<!--  -->
SGBS: Simpson Golabi Behmel Syndrome;
CH2DB: CH<sub>2</sub> groups to double bonds ratio;
HDL: high-density lipoprotein;
RCP: locus regional colocalization probability.
<!--  -->
](images/lvs_analysis/lv246/lv246.svg "LV246 TWAS plot"){#fig:lv246 width="100%"}


Next, we analyzed all 987 LVs using Fast Gene Set Enrichment Analysis (FGSEA) [@doi:10.1101/060012], and found 15 LVs nominally enriched (unadjusted *P* < 0.01) with these lipid-altering gene-sets (Supplementary Tables @tbl:sup:lipids_crispr:modules_enriched_increase and @tbl:sup:lipids_crispr:modules_enriched_decrease).
<!-- When we considered the increasing-lipids gene-set, genes and LVs were associated with a more diverse set of traits, such as blood count tests, impedance measures, and bone-densitometry (Supplementary Tables @tbl:sup:single_genes:lipids_increasing:top_traits and @tbl:sup:modules:lipids_increasing:top_traits). -->
<!-- FGSEA found 27 LVs nominally enriched for the increasing-lipids gene-set which were associated with the same traits, and additionally to lung function, arterial stiffness, intraocular pressure, handgrip strength, rheumatoid arthritis, and celiac disease. -->
Among those with reliable sample metadata, LV246, the top LV associated with the lipids-increasing gene-set, contained genes mainly co-expressed in adipose tissue (Figure @fig:lv246 a), which plays a key role in coordinating and regulating lipid metabolism.
<!-- Gene-trait associations and colocalization for the top genes in this LV are shown in Figure @fig:lv246 b). -->
Using the gene-property analysis method, we found that gene weights for this LV were predictive of gene associations for plasma lipids and high cholesterol (Supplementary Table @tbl:sup:phenomexcan_assocs:lv246).
Two high-confidence genes from our CRISPR screening, *DGAT2* and *ACACA*, are responsible for encoding enzymes for triglycerides and fatty acid synthesis and were among the highest-weighted genes of LV246 (Figure @fig:lv246 b, in boldface).
However, in contrast to other members of this LV, *DGAT2* and *ACACA* were not strongly associated nor colocalized with any of the cardiovascular-related traits and thus would not have been prioritized by TWAS alone;
other members of LV246, such as *SCD*, *LPL*, *FADS2*, *HMGCR*, and *LDLR*, were instead significantly associated and colocalized with lipid-related traits.
This lack of association/colocalization of two high-confidence genes from our CRISPR-screen might be explained from an omnigenic point of view [@doi:10.1016/j.cell.2019.04.014].
Assuming that the TWAS models for *DGAT2* and *ACACA* capture all common *cis*-eQTLs (the only genetic component of gene expression that TWAS can capture) and there are no rare *cis*-eQTLs, these two genes might represent "core" genes (i.e., they directly affect the trait with no mediated regulation of other genes), and many of the rest in the LV are "peripheral" genes that *trans*-regulate them.
These results suggested that our LV-based approach can contextualize genetic associations and prioritize alternative therapeutic targets, mainly when TWAS cannot detect them or hits are not druggable.


### PhenoPLIER with LVs predicts drug-disease pairs better than single genes

We next determined the extent to which substituting LVs in place of individual genes predicted known treatment-disease relationships.
For this, we used the transcriptional responses to small molecule perturbations profiled in LINCS L1000 [@doi:10.1016/j.cell.2017.10.049], which were further processed and mapped to DrugBank IDs [@doi:10.1093/nar/gkt1068; @doi:10.7554/eLife.26726; @doi:10.5281/zenodo.47223].
Based on an established drug repurposing strategy that matches reversed transcriptome patterns between genes and drug-induced perturbations [@doi:10.1126/scitranslmed.3002648; @doi:10.1126/scitranslmed.3001318], we adopted a previously described framework that uses imputed transcriptomes from TWAS to prioritize drug candidates [@doi:10.1038/nn.4618].
For this, we computed a drug-disease score by calculating the negative dot product between the $z$-scores for a disease (from TWAS) and the $z$-scores for a drug (from LINCS) across sets of genes of different size (see Methods).
Therefore, a large score for a drug-disease pair indicated that a higher (lower) predicted expression of disease-associated genes are down (up)-regulated by the drug, thus predicting a potential treatment.
Similarly, for the LV-based approach, we estimated how pharmacological perturbations affected the gene module activity by projecting expression profiles of drugs into our latent representation (Figure @fig:entire_process b).
We used a manually-curated gold standard set of drug-disease medical indications [@doi:10.7554/eLife.26726; @doi:10.5281/zenodo.47664] for 322 drugs across 53 diseases to evaluate the prediction performance.


![
**Drug-disease prediction performance for gene-based and module-based approaches.**
<!--  -->
The receiver operating characteristic (ROC) (left) and the precision-recall curves (right) for a gene-based and our module-based approach.
<!--  -->
AUC: area under the curve; AP: average precision.
<!--  -->
](images/drug_disease_prediction/roc_pr_curves.svg "ROC-PR curves for drug-disease prediction"){#fig:drug_disease:roc_pr width="80%"}


The gene-trait associations and drug-induced expression profiles projected into the latent space represent a compressed version of the entire set of results.
Despite this information loss, the LV-based method outperformed the gene-based one with an area under the curve of 0.632 and an average precision of 0.858 (Figure @fig:drug_disease:roc_pr).
The prediction results suggested that this low-dimensional space captures biologically meaningful patterns that can link pathophysiological processes with the mechanism of action of drugs.


We examined a specific drug-disease pair to determine whether the LVs driving the prediction were biologically plausible.
Nicotinic acid (niacin) is a B vitamin widely used clinically to treat lipid disorders, although there is controversy on its clinical utility to prevent cardiovascular disease [@pmid:22085343; @pmid:25014686; @pmid:30977858].
Niacin exerts its effects on multiple tissues, although its mechanisms are not well understood [@doi:10.1016/j.amjcard.2008.02.029; @doi:10.1194/jlr.S092007; @pmid:24363242; @pmid:24713591].
This compound can increase high-density lipoprotein (HDL) by inhibiting an HDL catabolism receptor in the liver.
Niacin also inhibits diacylglycerol acyltransferase–2 (DGAT2), which decreases the production of low-density lipoproteins (LDL) by modulating triglyceride synthesis in hepatocytes or by inhibiting adipocyte triglyceride lipolysis [@doi:10.1016/j.amjcard.2008.02.029].
<!--  -->
Niacin was one of the drugs in the gold standard set indicated for atherosclerosis (AT) and coronary artery disease (CAD).
We observed that this compound was predicted by the gene-based and LV-based approach as a medical indication for coronary artery disease (CAD), with scores above the mean (0.51 and 0.96, respectively).
For AT, the LV-based approach predicted niacin as a therapeutic drug with a score of 0.52, whereas the gene-based method assigned a negative score of -0.01 (below the mean).
Since LVs represent interpretable features associated with specific cell types, we analyzed which LVs were positively contributing to these predictions (i.e., with an opposite direction between niacin and the disease).
Notably, LV246 (Figure @fig:lv246), expressed in adipose tissue and liver and associated with plasma lipids and high cholesterol (Supplementary Table @tbl:sup:phenomexcan_assocs:lv246), was the 16th most important module in the prediction of niacin as a therapeutic drug for AT.
Besides the gold standard set, LV246 was among the top modules for other cardiovascular diseases, such as ischaemic heart disease (wide definition, 15th module) and high cholesterol (7th module).

![
**Top cell types/tissues where LV116's genes are expressed in.**
Values in the $y$-axis come from matrix $\mathbf{B}$ in the MultiPLIER models (Figure @fig:entire_process b).
In the $x$-axis, cell types/tissues are sorted by the maximum sample value.
The figure shows a clear immune response with cell types under different stimuli.
<!-- https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP045500 -->
MS: multiple sclerosis;
<!-- https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP045569 -->
<!-- PBMCs: peripheral blood mononuclear cells; -->
HSV: treated with herpes simplex virus;
<!-- https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP015670 -->
WNV: infected with West Nile virus;
<!-- https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP062958 -->
IFNa: treated with interferon-alpha;
<!-- https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP039361 -->
HMDM: human peripheral blood mononuclear cell-derived macrophages;
<!-- IPSDM: human induced pluripotent stem cell-derived macrophages; -->
<!-- https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP056733 -->
Salm: infected with *Salmonella typhimurium*;
Yers: infected with *Yersinia pseudotuberculosis*;
<!-- https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP062966 -->
ISM: Interferon Signature Metric;
SLE: Systemic lupus erythematosus.
](images/lvs_analysis/lv116/lv116-cell_types.svg "LV116 cell types"){#fig:lv116:cell_types width="100%"}



The analysis of other top niacin-contributing LVs across different cardiovascular diseases revealed additional mechanisms of action.
<!--  -->
For example, *GPR109A/HCAR2* encodes a G protein-coupled high-affinity niacin receptor in adipocytes and immune cells, including monocytes, macrophages, neutrophils and dendritic cells [@doi:10.1016/j.tips.2006.05.008; @doi:10.1038/sj.jid.5700586].
It was initially thought that the antiatherogenic effects of niacin were solely due to inhibition of lipolysis in adipose tissue.
However, it has been shown that nicotinic acid can reduce atherosclerosis progression independently of its antidyslipidemic activity through the activation of *GPR109A* in immune cells [@doi:10.1172/JCI41651], thus boosting anti-inflammatory processes [@doi:10.1161/ATVBAHA.108.179283].
In addition, flushing, a common adverse effect of niacin, is also produced by the activation of GPR109A in Langerhans cells (macrophages of the skin).
This alternative mechanism for niacin could have been hypothesized by examining the cell types where the top-contributing modules are expressed:
for instance, LV116 and LV931 (Figure @fig:lv116:cell_types, Supplementary Figure @fig:sup:lv931, and Supplementary Tables @tbl:sup:multiplier_pathways:lv116 and @tbl:sup:multiplier_pathways:lv931) were the top two modules for AT, with a strong signature in monocytes, macrophages, neutrophils, dendritic cells, among others.
In Figure @fig:lv116:cell_types, it can be seen that LV116's genes are expressed as an immune response when these cell types are under different stimuli, such as diarrhea caused by different pathogens [@doi:10.1371/journal.pone.0192082], samples from multiple sclerosis or systemic lupus erythematosus [@doi:10.1371/journal.pone.0109760; @doi:10.1126/science.aac7442], or infected with different viruses (such as herpes simplex [@url:https://www.ncbi.nlm.nih.gov/bioproject/PRJNA258384], West Nile virus [@doi:10.3390/v5071664], *Salmonella typhimurium* [@doi:10.1038/srep16882], among others).
These three LVs (LV246, LV116 and LV931) were among the top 20 modules contributing to the niacin prediction across different cardiovascular traits (Table @tbl:niacin:cardio:top_lvs).
Given the current controversy around this compound and its effect on cardiovascular disease, our approach may help to better understand different pathophysiological mechanisms linked with the mechanism of action of niacin.


<!-- niacin:cardiovascular:top_lvs:start DISABLE NOW, BUT HAS TO BE ADDED THE "end" version just below to update table -->
| LV    | Cell type             | Disease                                      |
|:------|:----------------------|:---------------------------------------------|
| LV116 | Immune cells, skin    | Atherosclerosis (ICD10 I70)                  |
|       |                       | Chronic ischaemic heart disease (ICD10 I25)  |
|       |                       | Heart attack, angina, stroke or hypertension |
|       |                       | Ischaemic heart disease (wide definition)    |
| LV931 | Immune cells          | Atherosclerosis (ICD10 I70)                  |
|       |                       | Heart attack, angina, stroke or hypertension |
|       |                       | Ischaemic heart disease (wide definition)    |
| LV246 | Adipose tissue, liver | Atherosclerosis (ICD10 I70)                  |
|       |                       | High cholesterol (self-reported)             |
|       |                       | Ischaemic heart disease (wide definition)    |

Table: LVs among the top 20 contributors of prediction of niacin for five cardiovascular diseases. "Heart attack, angina, stroke or hypertension" refers to the UK Biobank data-field 6150. GWAS sample size: Atherosclerosis (361,194 in total and 566 cases), Chronic ischaemic heart disease (361,194 in total and 12,769 cases), Heart attack, angina, stroke or hypertension (360,420 in total and 253,565 cases), Ischaemic heart disease/wide definition (361,194 in total and 20,857 cases), High cholesterol/self-reported (361,141 in total and 43,957 cases).  {#tbl:niacin:cardio:top_lvs}


The LV-based method was able to integrate different data types to provide an interpretable approach for drug repositioning research based on genetic studies.
Additionally, our approach could also be helpful to understand better the mechanism of pharmacological effect of known or experimental drugs.
For example, LV66, one of the top LVs affected by niacin (Supplementary Figure @fig:sup:lv66) was mainly expressed in ovarian granulosa cells.
This compound has been very recently considered as a potential therapeutic for ovarian diseases [@doi:10.1159/000495051; @doi:10.1071/RD20306], as it was found to promote follicle growth and inhibit granulosa cell apoptosis in animal models.
Our LV-based approach could be helpful to generate novel hypotheses to evaluate potential mechanisms of action, or even adverse effects, of different drugs.


### LV projections reveal trait clusters with shared transcriptomic properties

![
**Cluster analysis on traits using the latent gene expression representation.**
<!--  -->
**a)** The projection of TWAS results on $n$=3,752 traits into the latent gene expression representation is the input data to the clustering process.
A linear (PCA) and non-linear (UMAP) dimensionality reduction techniques were applied to the input data, and the three data versions were processed by five different clustering algorithms.
These algorithms derive partitions from the data using different sets of parameters (such as the number of clusters), leading to an ensemble of 4,428 partitions.
Then, a distance matrix is derived by counting how many times a pair of traits were grouped in different clusters across the ensemble.
Finally, a consensus function is applied to the distance matrix to generate consolidated partitions with different numbers of clusters (from 2 to $\sqrt{n}\approx$ 60).
These final solutions were represented in the clustering tree (Figure @fig:clustering:tree).
<!--  -->
**b)** The clusters found by the consensus function were used as labels to train a decision tree classifier on the original input data, which detects the LVs that better differentiate groups of traits.
<!--  -->
](images/clustering/clustering_design.svg "Cluster analysis on traits"){#fig:clustering:design width="100%"}


The previous results suggested that the compression into $\hat{\mathbf{M}}$ increases the signal-to-noise ratio.
Thus, we analyzed $\hat{\mathbf{M}}$ to find groups of traits that were affected by the same transcriptional processes.
To identify relationships that were robust to the selection of a specific clustering algorithm (each of which makes particular assumptions about the structure of data), we employed a consensus clustering approach.
Therefore, we applied different methods with varying sets of parameters and later combined these into a consolidated solution (Methods).
Our clustering pipeline generated 15 final consensus clustering solutions with 5 to 29 clusters (Supplementary Figure @fig:sup:consensus_agreement).
Instead of selecting a specific number of clusters, we used a clustering tree [@doi:10.1093/gigascience/giy083] (Figure @fig:clustering:tree) to examine stable groups of traits across multiple resolutions.
To understand which latent variables differentiated the group of traits, we trained a decision tree classifier on the input data $\hat{\mathbf{M}}$ using the clusters found as labels.


![
**Clustering tree using multiple resolutions for clusters of traits.**
<!--  -->
Each row represents a partition/grouping of the traits, and each circle is a cluster from that partition.
The number of clusters goes from 5 to 29.
Arrows indicate how traits in one cluster move across clusters from different partitions.
Most of the clusters are preserved across different resolutions, showing highly stable solutions even with independent runs of the clustering algorithm.
<!--  -->
RDW: red cell (erythrocyte) distribution width;
BMI: body mass index;
WC: waist circumference;
HC: hip circumference;
RA: rheumatoid arthritis;
SLE: systemic lupus erythematosus;
HTN: Hypertension;
IBD: inflammatory bowel disease;
SCZ: Schizophrenia;
CAD: Coronary artery disease;
AD: Alzheimer's disease;
<!--  -->
*Descriptions of traits by cluster ID (from left to right):*
12: also includes lymphocyte count and allergies such as allergic rhinitis or eczema;
4: includes reticulocyte count and percentage, immature reticulocyte fraction, and high light scatter reticulocytes count and percentage;
2: includes mean corpuscular volume, mean corpuscular hemoglobin, mean reticulocyte volume, mean sphered cell volume;
5: includes erythrocyte count, hemoglobin concentration, and hematocrit percentage;
20: also includes weight, waist and hip circumference;
18: also includes body impedance measures and ankle spacing width;
19: also includes basal metabolic rate;
1: includes platelet count, crit, mean volume, and distribution width;
13: diabetes refers to age when diabetes was first diagnosed;
25: also includes vascular problems such as angina, deep vein thrombosis (DVT), intraocular pressure, eye and mouth problems, pulse rate, hand-grip strength, several measurements of physical activity, jobs involving heavy physical work, types of transport used, intake of vitamin/mineral supplements, and various types of body pain and medications for pain relief;
21: also includes attention deficit hyperactivity disorder (ADHD), number of years of schooling completed, bone density, and intracranial volume measurement;
28: includes diabetes, gout, arthrosis, and respiratory diseases (and related medications such as ramipril, allopurinol, and lisinopril), urine assays, female-specific factors (age at menarche, menopause, first/last live birth), and several environmental/behavioral factors such as intake of a range of food/drink items including alcohol, time spent outdoors and watching TV, smoking and sleeping habits, early-life factors (breastfed as a baby, maternal smoking around birth), education attainment, psychological and mental health, and health satisfaction;
11: also includes fasting blood glucose and insulin measurement;
16: lipids include high and low-density lipoprotein (HDL and LDL) cholesterol, triglycerides, and average number of methylene groups per a double bond;
14: includes myocardial infarction, coronary atherosclerosis, ischaemic heart disease (wide definition);
7: includes monocyte count and percentage;
24: includes lymphocyte count and percentage;
9: includes neutrophil count, neutrophil+basophil count, neutrophil+eosinophil count, granulocyte count, leukocyte count, and myeloid cell count;
3: includes eosinophil count, eosinophil percentage, and eosinophil+basophil count.
](images/clustering/clustering_tree.svg "Clustering tree on groups of traits"){#fig:clustering:tree width="100%"}


We found that phenotypes were grouped into five clear branches (Figure @fig:clustering:tree).
These were
0) a "large" branch that includes most of the traits subdivided only starting at $k$=16 (with asthma, subjective well-being traits, and nutrient intake clusters),
1) heel bone-densitometry measurements,
2) hematological assays on red blood cells,
3) physical measures, including spirometry and body impedance, and anthropometric traits with fat-free and fat mass measures in separate sub-branches, and
4) a "complex" branch including keratometry measurements, assays on white blood cells and platelets, skin and hair color traits, autoimmune disorders (type 1 diabetes, psoriasis, hyper/hypothyroidism, rheumatoid arthritis, systemic lupus erythematosus, celiac disease), and cardiovascular diseases (hypertension, coronary artery disease, myocardial infarction, hypercholesterolemia, and other cardiovascular-related traits such hand-grip strength [@pmid:25982160], and environmental/behavioral factors such as physical activity and diet) (See Supplementary Files 2-6 for clustering results).
Within these branches, results were relatively stable.
The same traits were often clustered together across different resolutions, even with the consensus algorithm using random initializations at each level.
Arrows between different clusters show traits moving from one group to another across different resolutions.
This mainly happens between clusters within the "complex" branch, and between clusters from the "large" branch to the "complex" branch.
We would expect that continuing to explore higher dimensionalities would result in further subdivisions of these large groupings.
This behavior was expected since complex diseases are usually associated with shared genetic and environmental factors and are thus hard to categorize into a single cluster.
We would also expect that exploring solutions with a larger number of clusters would result in further subdivisions of these large groupings.


![
**Cluster-specific and general transcriptional processes associated with disease.**
The plot shows a submatrix of $\hat{\mathbf{M}}$ for the main trait clusters at $k$=29, considering only LVs (rows) that are well-aligned with at least one pathway.
Standardized values from -5 (lighter color) to 16 (darker color).
](images/clustering/global_clustermap-plain.svg "Heatmap with gene modules and traits"){#fig:clustering:heatmap width="100%"}


Next, we analyzed which LVs were driving these clusters of traits.
We trained decision tree classifiers on the input data (Figure @fig:clustering:design) using each cluster at $k$=29 (bottom of Figure @fig:clustering:tree) as labels (see Methods).
This yielded for each cluster the top LVs, where several of them were well-aligned to existing pathways (Figure @fig:clustering:heatmap), and others were novel and expressed in relevant tissues (Supplementary Figure @fig:sup:clustering:novel:heatmap).
In Figure @fig:clustering:heatmap, it can be seen that some LVs were highly specific to certain types of traits, while others were associated with a wide range of different phenotypes, thus potentially involved in more general biological functions.
For example, LVs such as LV928 and LV30, which were well-aligned to early progenitors of the erythrocytes lineage [@doi:10.1016/j.cell.2011.01.004] (Supplementary Tables @tbl:sup:multiplier_pathways:lv928 and @tbl:sup:multiplier_pathways:lv30), were predominantly expressed in early differentiation stages of erythropoiesis (Supplementary Figures @fig:sup:lv928 and @fig:sup:lv30) and strongly associated with different assays on red blood cells (FDR < 0.05; Supplementary Tables @tbl:sup:phenomexcan_assocs:lv928, @tbl:sup:emerge_assocs:lv928, and @tbl:sup:emerge_assocs:lv30).
In contrast, other LVs were highly specific, such as LV730, which is expressed in thrombocytes from different cancer samples (Supplementary Figures @fig:sup:lv730 and Supplementary Table @tbl:sup:multiplier_pathways:lv730), and strongly associated with hematological assays on platelets (FDR < 2e-4, Supplementary Table @tbl:sup:phenomexcan_assocs:lv730);
or LV598, whose genes were expressed in corneal endothelial cells (Supplementary Figures @fig:sup:lv598 and Supplementary Table @tbl:sup:multiplier_pathways:lv598) and associated with keratometry measurements (FDR < 4e-05; Supplementary Table @tbl:sup:phenomexcan_assocs:lv598).


The autoimmune diseases sub-branch also had significant LVs associations expressed in relevant cell types.
LV844 was the most strongly associated gene module with autoimmune disorders in both PhenomeXcan (FDR < 7e-16; Supplementary Tables @tbl:sup:phenomexcan_assocs:lv844) and eMERGE (FDR < 2e-6, @tbl:sup:emerge_assocs:lv844), and was expressed in a wide range of cell types, including blood, breast organoids, myeloma cells, lung fibroblasts, and different cell types from the brain (Supplementary Figures @fig:sup:lv844 and Supplementary Table @tbl:sup:multiplier_pathways:lv844).
LV155 was strongly expressed in the thyroid (Supplementary Figures @fig:sup:lv155 and Supplementary Table @tbl:sup:multiplier_pathways:lv155) and significantly associated with hypothyroidism both in PhenomeXcan (FDR < 0.05, Supplementary Table @tbl:sup:phenomexcan_assocs:lv155) and eMERGE (FDR < 0.10, Supplementary Table @tbl:sup:emerge_assocs:lv155).
Other important LVs associated with autoimmunity in both PhenomeXcan and eMERGE were LV57, expressed in T cells (Supplementary Figure @fig:sup:lv57 and Supplementary Tables @tbl:sup:multiplier_pathways:lv57, @tbl:sup:phenomexcan_assocs:lv57, @tbl:sup:emerge_assocs:lv57), and LV54, expressed in different soft tissue tumors, breast, lung, pterygia and epithelial cells (Supplementary Figure @fig:sup:lv54 and Supplementary Tables @tbl:sup:multiplier_pathways:lv54, @tbl:sup:phenomexcan_assocs:lv54, @tbl:sup:emerge_assocs:lv54).


The cardiovascular sub-branch also exhibited significant associations.
LV847 (Supplementary Figure @fig:sup:lv847 and Supplementary Table @tbl:sup:multiplier_pathways:lv847) was strongly associated with hypertension in PhenomeXcan (FDR < 2e-13, Supplementary Tables @tbl:sup:phenomexcan_assocs:lv847) and several cardiovascular diseases, type 1 diabetes, prostate cancer, and others in eMERGE (FDR < 0.05, Supplementary Table @tbl:sup:emerge_assocs:lv847).
LV847 was expressed in CD19 (B cells) (which are related to preeclampsia [@doi:10.1161/HYPERTENSIONAHA.111.188276]), Jurkat cells (T lymphocyte cells), and cervical carcinoma cell lines (the uterus was previously reported to be linked to blood pressure through a potential hormonal pathway [@doi:10.1038/s41467-018-06022-6; @doi:10.1007/s11906-006-0080-1]).
LV136 was aligned with known collagen formation and muscle contraction pathways (Supplementary Table @tbl:sup:multiplier_pathways:lv136), and it was associated with coronary artery disease (FDR < 2e-8), myocardial infarction (FDR < 6e-4) and keratometry measurements (FDR < 1e-7) in PhenomeXcan (Supplementary Tables @tbl:sup:phenomexcan_assocs:lv136), but with no strong associations in eMERGE (FDR < 0.20, Supplementary Table @tbl:sup:emerge_assocs:lv136).
This LV was expressed in a wide range of cell types, including fibroblasts, mesenchymal stem cells, osteoblasts, pancreatic stellate cells, cardiomyocytes, and adipocytes (Supplementary Figure @fig:sup:lv136).
Lipids, clustered with chronotype and Alzheimer's disease, were significantly associated with several modules expressed mainly in brain cell types, including LV93 (Supplementary Figure @fig:sup:lv93 and Supplementary Tables @tbl:sup:multiplier_pathways:lv93, @tbl:sup:phenomexcan_assocs:lv93, @tbl:sup:emerge_assocs:lv93), LV206 (Supplementary Figure @fig:sup:lv206 and Supplementary Tables @tbl:sup:multiplier_pathways:lv206, @tbl:sup:phenomexcan_assocs:lv206, @tbl:sup:emerge_assocs:lv206), and LV260 (Supplementary Figure @fig:sup:lv260 and Supplementary Tables @tbl:sup:multiplier_pathways:lv260, @tbl:sup:phenomexcan_assocs:lv260 and @tbl:sup:emerge_assocs:lv260).
These modules were associated mainly with cardiovascular traits in eMERGE.


Within the cardiovascular sub-branch, we found neuropsychiatric and neurodevelopmental disorders such as Alzheimer's disease, schizophrenia, and attention deficit hyperactivity disorder (ADHD).
These disorders were previously linked to the cardiovascular system [@pmid:12093424; @doi:10.1161/CIRCULATIONAHA.113.002065; @doi:10.1192/bjp.bp.117.202606; @doi:10.1161/CIRCRESAHA.118.313563] and share several risk factors, including hypertension, high cholesterol, obesity, smoking, among others [@doi:10.1186/s12916-014-0206-2; @doi:10.1111/j.1076-7460.2007.06696.x].
In our results, however, these diseases were grouped by potentially shared transcriptional processes expressed in specific tissues/cell types.
Alzheimer's disease, for example, was significantly associated with LV21 in PhenomeXcan (FDR < 2e-19, Supplementary Table @tbl:sup:phenomexcan_assocs:lv21) and with LV5 (FDR < 3e-3, Supplementary Table @tbl:sup:phenomexcan_assocs:lv5).
LV21 was strongly expressed in a variety of soft tissue sarcomas, monocytes/macrophages (including microglia from cortex samples), and aortic valves (Supplementary Figure @fig:sup:lv21 and Supplementary Table @tbl:sup:multiplier_pathways:lv21).
This LV was also associated with lipids: LDL cholesterol (FDR < 1e-4) and triglycerides (FDR < 0.02).
As discussed previously, macrophages play a key role in the reverse cholesterol transport and thus atherogenesis [@doi:10.1093/qjmed/hci136], and lipid metabolism in microglia has been recently identified as an important factor in the development of neurodegenerative diseases [@doi:10.3389/fphys.2020.00393].
On the other hand, LV5 was expressed in breast cancer and brain glioma samples, microglia (cortex), liver, and kidney, among other cell types (Supplementary Figure @fig:sup:lv5 and Supplementary Table @tbl:sup:multiplier_pathways:lv5).
In addition to lipids, LV5 was also associated with depression traits from the UK Biobank (FDR < 0.05, Supplementary Table @tbl:sup:phenomexcan_assocs:lv5).
Since Alzheimer's disease was not present in eMERGE, we could not replicate this association.
ADHD was the only significantly associated trait for LV434 (FDR < 6e-3) (Supplementary Table @tbl:sup:phenomexcan_assocs:lv434), which was expressed in breast cancer and glioma cells, cerebral organoids, and several different cell populations from the brain: fetal neurons (replicating and quiescence), microglia, and astrocytes (Supplementary Figure @fig:sup:lv434 and Supplementary Table @tbl:sup:multiplier_pathways:lv434).
Schizophrenia was not significantly associated (FDR < 0.05) with any gene module tested in our analysis.
None of these LVs were significantly aligned to prior pathways, which might represent potentially novel transcriptional processes affecting the cardiovascular and central nervous systems.


## Discussion

We have introduced a novel computational strategy that integrates statistical associations from TWAS with groups of genes (gene modules) that have similar expression patterns across the same cell types.
Our key innovation is that we project gene-trait associations through a latent representation derived not strictly from measures of normal tissue but also cell types under a variety of stimuli and at various developmental stages.
This improves interpretation by going beyond statistical associations to infer cell type-specific features of complex phenotypes.
We found that our approach can identify disease-relevant cell types from summary statistics, and several disease-associated gene modules were replicated in eMERGE.
Using a CRISPR screen to analyze lipid regulation, we found that our gene module-based approach can prioritize causal genes even when single gene associations are not detected.
We interpret these findings with an omnigenic perspective of "core" and "peripheral" genes, suggesting that the approach can identify genes that directly affect the trait with no mediated regulation of other genes, and thus prioritize alternative and potentially more attractive therapeutic targets.
Using our gene module perspective, we also integrated drug-induced transcriptional profiles, which allowed us to connect diseases, drugs, and cell types.
Furthermore, and beyond statistical prediction, we focused on a particular drug (niacin) and set of traits (cardiovascular diseases) to show that the approach connects disease-relevant transcriptional processes with known mechanisms of action.
This suggests that the conceptual approach may reveal the mechanisms of pharmacological effect of known or experimental drugs.
Finally, we found that the analysis of associations through latent representations provided reasonable groupings of diseases and traits affected by shared and distinct transcriptional mechanisms expressed in highly relevant tissues.


In some cases, the features/LVs linked to phenotypes appear to be associated with specific cell types.
Associations with such cell type marker genes may reveal potentially causal cell types for a phenotype with more precision.
We observed modules expressed primarily in one tissue (such as adipose in LV246, thyroid in LV155, or ovary in LV66).
Others appeared to be expressed in many contexts, and these may capture pathways associated with a set of related complex diseases.
For example, LV136 is associated with cardiovascular disease and measures of corneal biomechanics, and expressed in fibroblasts, osteoblasts, pancreas, liver, and cardiomyocytes, among others.
Another example is LV844, expressed in whole blood samples and strongly associated with a range of autoimmune diseases.
From an omnigenic point of view, these patterns might represent cases of "network pleiotropy," where the same cell types mediate molecularly related traits.
To our knowledge, projection through a representation learned on complementary but distinct datasets is a novel approach to identify cell type and pathway effects on complex phenotypes that is computationally simple to implement.


Our approach rests on the assumption that gene modules with coordinated expression patterns will also manifest coordinated pathological effects.
Our implementation in this work integrates two complementary approaches.
The first is MultiPLIER, which extracts latent variables from large expression datasets, and these LVs could represent either real transcriptional processes or technical factors ("batch effects").
We used a previously published model derived from recount2, which was designed to analyze rare disorders but might not be the optimal latent representation for the wide range of complex diseases considered here.
Also, the underlying factorization method rests on linear combinations of variables, which could miss important and more complex co-expression patterns.
In addition, recount2, the training dataset used, has since been surpassed in size and scale by other resources [@doi:10.1038/s41467-018-03751-6; @doi:10.1101/2021.05.21.445138].
The second approach we used in this study is TWAS, where we are only considering the hypothesis that GWAS loci affect traits via changes in gene expression, and other effects such as coding variants disrupting protein-protein interactions are not captured.
Additionally, TWAS has several limitations that can lead to false positives [@doi:10.1038/s41588-019-0385-z; @doi:10.1016/j.ajhg.2020.11.012].
Like GWAS, which generally detects groups of associated variants in linkage disequilibrium (LD), TWAS usually identifies several genes within the same locus [@doi:10.1038/s41588-018-0092-1; @doi:10.1038/ng.3367].
This is due to sharing of GWAS variants in gene expression models, correlated expression of nearby genes, or even correlation of their predicted expression due to eQTLs in LD, among others [@doi:10.1038/s41588-019-0385-z].
Larger datasets and methods designed to learn representations with this application in mind could further refine the approach and are a promising avenue for future research.


Our findings are concordant with previous studies showing that drugs with genetic support are more likely to succeed through the drug development pipeline [@doi:10.1038/ng.3314; @doi:10.1038/nn.4618].
In this case, projecting association results through latent variables better prioritized disease-treatment pairs than considering single-gene effects alone.
An additional benefit is that the latent variables driving predictions can be examined to infer potential mechanisms of action.
Here we prioritized drugs for diseases with very different tissue etiologies, and a challenge of the approach is to select the most appropriate tissue model from TWAS to find reversed transcriptome patterns between genes and drug-induced perturbations.
We also demonstrated that clustering trees, introduced initially as a means to examine developmental processes in single-cell data, provide a multi-resolution grouping of phenotypes based on latent variable associations.
We employed hard-partitioning algorithms (one trait belongs exclusively to one cluster) where the distance between two traits takes into account all gene modules.
However, it is also plausible for two complex diseases to share only a few biological processes instead of being similar across most of them.
In this portion, we used S-MultiXcan associations, which only provide the association strength between a gene and a trait, but with no direction of effect.
This does mean that traits are grouped based on associated genes, but genes could have opposite effects on traits within the same cluster.
Considering groups of related diseases was previously shown to be more powerful to detect shared genetic etiology [@doi:10.1038/ng.3985; @doi:10.1038/s41588-018-0121-0], and clustering trees provide a way to explore such relationships in the context of latent variables.
Finally, our TWAS results were derived from a large set of GWAS of different sample sizes and qualities.
Although the potential issues derived from this data heterogeneity were addressed before performing cluster analysis of traits, data preprocessing steps are always challenging and might not avoid bias altogether.


Ultimately, the quality of the representations is essential to performance.
Here we used a representation derived from a factorization of bulk RNA-seq data.
Detailed perturbation datasets and single-cell profiling of tissues, with and without perturbagens, and at various stages of development provide an avenue to generate higher quality and more interpretable representations.
On the other hand, the key to interpretability is driven by the annotation of sample metadata.
New approaches to infer and annotate with structured metadata are promising and can be directly applied to existing data [@doi:10.1101/2021.05.10.443525].
Rapid improvements in both areas set the stage for latent variable projections to be widely applied to disentangle the genetic basis of complex human phenotypes.
By providing a new perspective for a mechanistic understanding of statistical associations from TWAS, our method can generate testable hypotheses for the post-GWAS functional characterization of complex diseases, which will likely be an area of great importance in the coming years.


## Methods and materials

PhenoPLIER is a framework that combines different computational approaches to integrate gene-trait associations and drug-induced transcriptional responses with groups of functionally-related genes (referred to as gene modules or latent variables/LVs).
Gene-trait associations are computed using the PrediXcan family of methods, whereas latent variables are inferred by the MultiPLIER models applied on large gene expression compendia.
PhenoPLIER provides
1) a regression model to compute an LV-trait association,
2) a consensus clustering approach applied to the latent space to learn shared and distinct transcriptomic properties between traits, and
3) an interpretable, LV-based drug repurposing framework.
We provide the details of these methods below.


### The PrediXcan family of methods for gene-based associations

We used Summary-PrediXcan (S-PrediXcan) [@doi:10.1038/s41467-018-03621-1] and Summary-MultiXcan (S-MultiXcan) [@doi:10.1371/journal.pgen.1007889] as the gene-based statistical approaches, which belong to the PrediXcan family of methods [@doi:10.1038/ng.3367].
We broadly refer to these approaches as TWAS (transcription-wide association studies).
S-PrediXcan, the summary-based version of PrediXcan, computes the univariate association between a trait and a gene's predicted expression in a single tissue.
In contrast, S-MultiXcan, the summary-based version of MultiXcan, computes the joint association between a gene's predicted expression in all tissues and a trait.
S-PrediXcan and S-MultiXcan only need GWAS summary statistics instead of individual-level genotype and phenotype data.

Here we briefly provide the details about these TWAS methods that are necessary to explain our regression framework later (see the referenced articles for more information).
In the following, we refer to $\mathbf{y}$ as a vector of traits for $n$ individuals that is centered for convenience (so that no intercept is necessary);
$\mathbf{\tilde{t}}_l = \sum_{a \in \mathrm{model}_l} w_{a}^{l} X_{a}$ is the gene's predicted expression for all individuals in tissue $l$, $X_a$ is the genotype of SNP $a$ and $w_{a}$ its weight in the tissue prediction model $l$;
and $\mathbf{t}_l$ is the standardized version of $\mathbf{\tilde{t}}_l$ with mean equal to zero and standard deviation equal to one.

S-PrediXcan [@doi:10.1038/s41467-018-03621-1] is the summary version of PrediXcan [@doi:10.1038/ng.3367].
PrediXcan models the trait as a linear function of the gene's expression on a single tissue using the univariate model

$$
\mathbf{y} = \mathbf{t}_l \gamma_l + \bm{\epsilon}_l,
$$ {#eq:predixcan}

where $\hat{\gamma}_l$ is the estimated effect size or regression coefficient, and $\bm{\epsilon}_l$ are the error terms with variance $\sigma_{\epsilon}^{2}$.
The significance of the association is assessed by computing the $z$-score $\hat{z}_{l}=\hat{\gamma}_l / \mathrm{se}(\hat{\gamma}_l)$ for a gene's tissue model $l$.
<!--  -->
PrediXcan needs individual-level data to fit this model, whereas S-PrediXcan approximates PrediXcan $z$-scores using only GWAS summary statistics with the expression

$$
\hat{z}_{l} \approx \sum_{a \in model_{l}} w_a^l \frac{\hat{\sigma}_a}{\hat{\sigma}_l} \frac{\hat{\beta}_a}{\mathrm{se}(\hat{\beta}_a)},
$$ {#eq:spredixcan}

where $\hat{\sigma}_a$ is the variance of SNP $a$, $\hat{\sigma}_l$ is the variance of the predicted expression of a gene in tissue $l$, and $\hat{\beta}_a$ is the estimated effect size of SNP $a$ from the GWAS.
In these TWAS methods, the genotype variances and covariances are always estimated using the Genotype-Tissue Expression project (GTEx v8) [@doi:10.1126/science.aaz1776] as the reference panel.
<!--  -->
Since S-PrediXcan provides tissue-specific direction of effects (for instance, whether a higher or lower predicted expression of a gene confers more or less disease risk), we used the $z$-scores in our drug repurposing approach (described below).

S-MultiXcan [@doi:10.1371/journal.pgen.1007889], on the other hand, is the summary version of MultiXcan.
MultiXcan is more powerful than PrediXcan in detecting gene-trait associations, although it does not provide the direction of effects.
Its main output is the $p$-value (obtained with an F-test) of the multiple tissue model

$$
\begin{split}
\mathbf{y} & = \sum_{l=1}^{p} \mathbf{t}_l g_l + \mathbf{e} \\
 & = \mathbf{T} \mathbf{g} + \mathbf{e},
\end{split}
$$ {#eq:multixcan}

where $\mathbf{T}$ is a matrix with $p$ columns $\mathbf{t}_l$,
$\hat{g}_l$ is the estimated effect size for the predicted gene expression in tissue $l$ (and thus $\mathbf{\hat{g}}$ is a vector with $p$ estimated effect sizes $\hat{g}_l$),
and $\mathbf{e}$ are the error terms with variance $\sigma_{e}^{2}$.
Given the high correlation between predicted expression values for a gene across different tissues, MultiXcan uses the principal components (PCs) of $\mathbf{T}$ to avoid collinearity issues.
<!--  -->
S-MultiXcan derives the joint regression estimates (effect sizes and their variances) in Equation (@eq:multixcan) using the marginal estimates from S-PrediXcan in Equation (@eq:spredixcan).
Under the null hypothesis of no association, $\mathbf{\hat{g}}^{\top} \frac{\mathbf{T}^{\top}\mathbf{T}}{\sigma_{e}^{2}} \mathbf{\hat{g}} \sim \chi_{p}^{2}$, and therefore the significance of the association in S-MultiXcan is estimated with

$$
\begin{split}
\frac{\mathbf{\hat{g}}^{\top} (\mathbf{T}^{\top}\mathbf{T}) \mathbf{\hat{g}}}{\sigma_{e}^{2}} & \approx \bm{\hat{\gamma}}^{\top} \frac{\sqrt{n-1}}{\sigma_{\epsilon}} \left(\frac{\mathbf{T}^{\top} \mathbf{T}}{n-1}\right)^{-1} \frac{\sqrt{n-1}}{\sigma_{\epsilon}} \bm{\hat{\gamma}} \\
 & = \mathbf{\hat{z}}^{\top} Cor(\mathbf{T})^{-1} \mathbf{\hat{z}},
\end{split}
$$ {#eq:smultixcan}

where $\mathbf{\hat{z}}$ is a vector with $p$ $z$-scores (Equation (@eq:spredixcan)) for each tissue available for the gene,
and $Cor(\mathbf{T})$ is the autocorrelation matrix of $\mathbf{T}$.
Since $\mathbf{T}^{\top}\mathbf{T}$ is singular for many genes, S-MultiXcan computes the pseudo-inverse $Cor(\mathbf{T})^{+}$ using the $k$ top PCs, and thus $\mathbf{\hat{z}}^{\top} Cor(\mathbf{T})^{+} \mathbf{\hat{z}} \sim \chi_k^2$.
<!--  -->
To arrive at this expression, S-MultiXcan uses the conservative approximation $\sigma_{e}^{2} \approx \sigma_{\epsilon}^{2}$, that is, the variance of the error terms in the joint regression is approximately equal to the residual variance of the marginal regressions.
Another important point is that $Cor(\mathbf{T})$ is estimated using a global genotype covariance matrix, whereas marginal $\hat{z}_l$ in Equation (@eq:spredixcan) are approximated using tissue-specific genotype covariances.
Although S-MultiXcan yields highly concordant estimates compared with MultiXcan, results are not perfectly correlated across genes [@doi:10.1371/journal.pgen.1007889].
As we explain later, these differences are important for our LV-based regression model when computing the gene-gene correlation matrix.
We used S-MultiXcan results for our LV-based regression model and our cluster analyses of traits.


### TWAS resources

We used two large TWAS resources from different cohorts for discovery and replication.
<!--  -->
PhenomeXcan [@doi:10.1126/sciadv.aba2083], our discovery cohort, provides results on 4,091 traits across different categories (`add phenotyp_info file with categories like in emerge`{.red}).
PhenomeXcan was built using publicly available GWAS summary statistics to compute gene-based associations with the PrediXcan family of methods described before.
<!--  -->
We refer to the matrix of $z$-scores from S-PrediXcan (Equation (@eq:spredixcan)) across $q$ traits and $m$ genes in tissue $t$ as $\mathbf{M}^{t} \in \mathbb{R}^{q \times m}$.
As explained later, matrices $\mathbf{M}^{t}$ were used in our LV-based drug repurposing framework since they provide direction of effects.
<!--  -->
The S-MultiXcan results (22,515 gene associations across 4,091 traits) were used in our LV-based regression framework and our cluster analyses of traits.
For the cluster analyses, we used the $p$-values converted to $z$-scores: $\mathbf{M}=\Phi^{-1}(1 - p/2)$, where $\Phi^{-1}$ is the probit function.
Higher $z$-scores correspond to stronger associations.

Our discovery cohort was eMERGE [@doi:10.1038/gim.2013.72], where the same TWAS methods were run on 309 phecodes [@doi:10.1101/2021.10.21.21265225] across different categories (more information about traits are available in [@doi:10.1101/2021.10.21.21265225]).
We used these results to replicate the associations found with our LV-based regression framework in PhenomeXcan.


### MultiPLIER and Pathway-level information extractor (PLIER)

MultiPLIER [@doi:10.1016/j.cels.2019.04.003] extracts patterns of co-expressed genes from recount2 [@doi:10.1038/nbt.3838], a large gene expression dataset.
The approach applies the pathway-level information extractor method (PLIER) [@doi:10.1038/s41592-019-0456-1], which performs unsupervised learning using prior knowledge (canonical pathways) to reduce technical noise.
PLIER uses a matrix factorization approach that deconvolutes gene expression data into a set of latent variables (LV), where each LV represents a gene module.
The MultiPLIER models reduced the dimensionality in recount2 to 987 LVs.

Given a gene expression dataset $\mathbf{Y}^{m \times c}$ with $m$ genes and $c$ experimental conditions and a prior knowledge matrix $\mathbf{C} \in \{0,1\}^{m \times p}$ for $p$ MSigDB pathways [@doi:10.1016/j.cels.2015.12.004] (so that $\mathbf{C}_{ij} = 1$ if gene $i$ belongs to pathway $j$), PLIER finds $\mathbf{U}$, $\mathbf{Z}$, and $\mathbf{B}$ minimizing

$$
||\mathbf{Y} - \mathbf{Z}\mathbf{B}||^{2}_{F} + \lambda_1 ||\mathbf{Z} - \mathbf{C}\mathbf{U}||^{2}_{F} + \lambda_2 ||\mathbf{B}||^{2}_{F} + \lambda_3 ||\mathbf{U}||_{L^1}
$$ {#eq:met:plier_func}

subject to $\mathbf{U}>0, \mathbf{Z}>0$;
$\mathbf{Z}^{m \times l}$ are the gene loadings with $l$ latent variables,
$\mathbf{B}^{l \times c}$ is the latent space for $c$ conditions,
$\mathbf{U}^{p \times l}$ specifies which of the $p$ prior-information pathways in $\mathbf{C}$ are represented for each LV,
and $\lambda_i$ are different regularization parameters used in the training step.
<!--  -->
$\mathbf{Z}$ is a low-dimensional representation of the gene space where each LV aligns as much as possible to prior knowledge, and it might represent either a known or novel gene module (i.e., a meaningful biological pattern) or noise.

For our drug repurposing and cluster analyses, we used this model to project gene-trait (from TWAS) and gene-drug associations (from LINCS L1000) into this low-dimensional gene module space.
<!--  -->
For instance, TWAS associations $\mathbf{M}$ (either from S-PrediXcan or S-MultiXcan) were projected using

$$
\hat{\mathbf{M}} = (\mathbf{Z}^{\top} \mathbf{Z} + \lambda_{2} \mathbf{I})^{-1} \mathbf{Z}^{\top} \mathbf{M},
$$ {#eq:proj}

where $\hat{\mathbf{M}}^{l \times q}$ is a matrix where traits are represented by gene modules instead of single genes.
<!--  -->
As explained later, we used the same approach to project drug-induced transcriptional profiles in LINCS L1000 to obtain a representation of drugs using gene modules.


### Regression model for LV-trait associations

We adapted the gene-set analysis framework from MAGMA [@doi:10.1371/journal.pcbi.1004219] to TWAS.
We used a competitive test to predict gene-trait associations from TWAS using gene weights from an LV, testing whether top-weighted genes for an LV are more strongly associated with the phenotype than other genes with relatively small or zero weights.
Thus, we fit the model

$$
\mathbf{m}=\beta_{0} + \mathbf{s} \beta_{s} + \sum_{i} \mathbf{x}_{i} \beta_{i} + \bm{\epsilon},
$$

where $\mathbf{m}$ is a vector of S-MultiXcan gene $p$-values for a trait (with a $-log_{10}$ transformation);
$\mathbf{s}$ is a binary indicator vector with $s_{\ell}=1$ for the top 1% of genes with the largest loadings for LV $\ell$ (from $\mathbf{Z}_{\ell}$) and zero otherwise;
$\mathbf{x}_{i}$ is a gene property used as a covariate;
$\beta$ are effect sizes (with $\beta_{0}$ as the intercept);
and $\bm{\epsilon} \sim \mathrm{MVN}(0, \sigma^{2} \mathbf{R})$ is a vector of error terms with a multivariate normal distribution (MVN) where $\mathbf{R}$ is the matrix of gene correlations.

The model tests the null hypothesis $\beta_{s} = 0$ against the one-sided hypothesis $\beta_{s} > 0$.
Therefore, $\beta_{s}$ reflects the difference in trait associations between genes that are part of LV $\ell$ and genes outside of it.
Following the MAGMA framework, we used two gene properties as covariates:
1) *gene size*, defined as the number of PCs retained in S-MultiXcan,
and 2) *gene density*, defined as the ratio of the number of PCs to the number of tissues available.

Since the error terms $\bm{\epsilon}$ could be correlated, we cannot assume they have independent normal distributions as in a standard linear regression model.
In the PrediXcan family of methods, the predicted expression of a pair of genes could be correlated if they share eQTLs or if these are in LD [@doi:10.1038/s41588-019-0385-z].
Therefore, we used a generalized least squares approach to account for these correlations.
The gene-gene correlation matrix $\mathbf{R}$ was approximated by computing the correlations between the model sum of squares (SSM) for each pair of genes under the null hypothesis of no association.
These correlations are derived from the individual-level MultiXcan model (Equation (@eq:multixcan)), where the predicted expression matrix $\mathbf{T}_{i} \in \mathbb{R}^{n \times p_i}$ of a gene $i$ across $p_i$ tissues is projected into its top $k_i$ PCs, resulting in matrix $\mathbf{P}_{i} \in \mathbb{R}^{n \times k_i}$.
From the MAGMA framework, we know that the SSM for each gene is proportial to $\mathbf{y}^{\top} \mathbf{P}_{i} \mathbf{P}_{i}^{\top} \mathbf{y}$.
Under the null hypothesis of no association, the covariances between the SSM of genes $i$ and $j$ is therefore given by $2 \times \mathrm{Trace}(\mathbf{P}_{i}^{\top} \mathbf{P}_{j} \mathbf{P}_{j}^{\top} \mathbf{P}_{i})$.
The standard deviations of each SSM are given by $\sqrt{2 \times k_{i}} \times (n - 1)$.
Therefore, the correlation between the SSMs for genes $i$ and $j$ can be written as follows:

$$
\begin{split}
\mathbf{R}_{ij} & = \frac{2 \times \mathrm{Tr}(\mathbf{P}_{i}^{\top} \mathbf{P}_{j} \mathbf{P}_{j}^{\top} \mathbf{P}_{i})}{\sqrt{2 \times k_{i}} \times \sqrt{2 \times k_{j}} \times (n - 1)^2} \\
& = \frac{2 \times \mathrm{Tr}(Cor(\mathbf{P}_{i}, \mathbf{P}_{j}) \times Cor(\mathbf{P}_{j}, \mathbf{P}_{i}))}{\sqrt{2 \times k_{i}} \times \sqrt{2 \times k_{j}}},
\end{split}
$$

where columns $\mathbf{P}$ are standardized,
$\mathrm{Tr}$ is the trace of a matrix,
and the cross-correlation matrix between PCs $Cor(\mathbf{P}_{i}, \mathbf{P}_{j}) \in \mathbb{R}^{k_i \times k_j}$ is given by

$$
\begin{split}
Cor(\mathbf{P}_{i}, \mathbf{P}_{j}) & = Cor(\mathbf{T}_{i} \mathbf{V}_{i}^{\top} \mathrm{diag}(\lambda_i)^{-1/2}, \mathbf{T}_{j} \mathbf{V}_{j}^{\top} \mathrm{diag}(\lambda_j)^{-1/2}) \\
& = \mathrm{diag}(\lambda_i)^{-1/2} \mathbf{V}_{i} (\frac{\mathbf{T}_{i}^{\top} \mathbf{T}_{j}}{n-1}) \mathbf{V}_{j}^{\top} \mathrm{diag}(\lambda_j)^{-1/2},
\end{split}
$$

where $\frac{\mathbf{T}_{i}^{\top} \mathbf{T}_{j}}{n-1} \in \mathbb{R}^{p_i \times p_j}$ is the cross-correlation matrix between the predicted expression levels of genes $i$ and $j$,
and columns of $\mathbf{V}_{i}$ and scalars $\lambda_i$ are the eigenvectors and eigenvalues of $\mathbf{T}_{i}$, respectively.
S-MultiXcan keeps only the top eigenvectors using a condition number threshold of $\frac{\max(\lambda_i)}{\lambda_i} < 30$.
To estimate the correlation of predicted expression levels for genes $i$ in tissue $k$ and gene $j$ in tissue $l$, $(\mathbf{t}_k^i, \mathbf{t}_l^j)$ ($\mathbf{t}_k^i$ is the $k$th column of $\mathbf{T}_{i}$), we used [@doi:10.1371/journal.pgen.1007889]

$$
\begin{split}
\frac{(\mathbf{T}_{i}^{\top} \mathbf{T}_{j})_{kl}}{n-1} & = Cor(\mathbf{t}_k^i, \mathbf{t}_l^j) \\
 & = \frac{ Cov(\mathbf{t}_k, \mathbf{t}_l) } { \sqrt{\widehat{\mathrm{var}}(\mathbf{t}_k) \widehat{\mathrm{var}}(\mathbf{t}_l)} } \\
 & = \frac{ Cov(\sum_{a \in \mathrm{model}_k} w_a^k X_a, \sum_{b \in \mathrm{model}_l} w_b^l X_b) }  {\sqrt{\widehat{\mathrm{var}}(\mathbf{t}_k) \widehat{\mathrm{var}}(\mathbf{t}_l)} } \\
 & = \frac{ \sum_{a \in \mathrm{model}_k \\ b \in \mathrm{model}_l} w_a^k w_b^l Cov(X_a, X_b)} {\sqrt{\widehat{\mathrm{var}}(\mathbf{t}_k) \widehat{\mathrm{var}}(\mathbf{t}_l)} } \\
 & = \frac{ \sum_{a \in \mathrm{model}_k \\ b \in \mathrm{model}_l} w_a^k w_b^l \Gamma_{ab}} {\sqrt{\widehat{\mathrm{var}}(\mathbf{t}_k) \widehat{\mathrm{var}}(\mathbf{t}_l)} },
\end{split}
$$

where $X_a$ is the genotype of SNP $a$,
$w_a^k$ is the weight of SNP $a$ for gene expression prediction in the tissue model $k$,
and $\Gamma = \widehat{\mathrm{var}}(\mathbf{X}) = (\mathbf{X} - \mathbf{\bar{X}})^{\top} (\mathbf{X} - \mathbf{\bar{X}}) / (n-1)$ is the genotype covariance matrix using GTEx v8 as the reference panel, which is the same used in all TWAS methods described here.
The variance of the predicted expression values of gene $i$ in tissue $k$ is estimated as [@doi:10.1038/s41467-018-03621-1]:

$$
\begin{split}
\widehat{\mathrm{var}}(\mathbf{t}_k^i) & = (\mathbf{W}^k)^\top \Gamma^k \mathbf{W}^k \\
 & = \sum_{a \in \mathrm{model}_k \\ b \in \mathrm{model}_k} w_a^k w_b^k \Gamma_{ab}^k.
\end{split}
$$

Note that, since we used the MultiXcan regression model (Equation (@eq:multixcan)), $\mathbf{R}$ is only an approximation of gene correlations in S-MultiXcan.
As explained before, S-MultiXcan approximates the joint regression parameters in MultiXcan using the marginal regression estimates from S-PrediXcan in (@eq:spredixcan) with some simplifying assumptions and different genotype covariance matrices.
This complicates the derivation of an S-MultiXcan-specific solution to compute $\mathbf{R}$.
To account for this, we used a submatrix $\mathbf{R}_{\ell}$ corresponding to genes that are part of LV $\ell$ only (top 1% of genes) instead of the entire matrix $\mathbf{R}$.
This simplification is conservative since correlations are accounted for top genes only.
Our simulations (Supplementary Note `XXX`{.red}) show that the model is approximately well-calibrated and can correct for LVs with adjacent and highly correlated genes at the top (Supplementary Figure `YYY`{.red}).
The model can also detect LVs associated with relevant traits (Figure @fig:lv246 and Table @tbl:sup:phenomexcan_assocs:lv246) that are replicated in a different cohort (Table @tbl:sup:emerge_assocs:lv246).

We ran our regression model for all 987 LVs across the 4,091 traits in PhenomeXcan.
For replication, we ran the model in the 309 phecodes in eMERGE.
We adjusted the $p$-values using the Benjamini-Hochberg procedure.


### LV-based drug repurposing approach

For the drug-disease prediction, we derived an LV-based method based on a drug repositioning framework previously used for psychiatry traits [@doi:10.1038/nn.4618], where individual/single genes associated with a trait are anticorrelated with expression profiles for drugs.
We compared our LV-based method with this previously published, single-gene approach.
For the single-gene method, we computed a drug-disease score by multiplying each S-PrediXcan set of results in tissue $t$, $\mathbf{M}^t$, with the transcriptional responses profiled in LINCS L1000 [@doi:10.1016/j.cell.2017.10.049], $\mathbf{L}^{c \times m}$ (for $c$ compounds): $\mathbf{D}^{t,k}=-1 \cdot \mathbf{M}^{t,k} \mathbf{L}^\top$, where $k$ refers to the number of most significant gene associations in $\mathbf{M}^t$ for each trait.
As suggested in [@doi:10.1038/nn.4618], $k$ could be either all genes or the top 50, 100, 250, and 500; then, we averaged score ranks across all $k$ and obtained $\mathbf{D}^t$.
Finally, for each drug-disease pair, we took the maximum prediction score across all tissues: $\mathbf{D}_{ij} = \max \{ \mathbf{D}_{ij}^t \mid \forall t \}$.


The same procedure was used for the LV-based approach, where we projected $\mathbf{M}^{t}$ and $\mathbf{L}$ into the gene module latent space using Equation (@eq:proj), leading to $\hat{\mathbf{M}}^t$ and $\hat{\mathbf{L}}^{l \times c}$, respectively.
<!--  -->
Finally, $\mathbf{D}^{t,k}=-1 \cdot \hat{\mathbf{L}}^{\top} \hat{\mathbf{M}}^{t,k}$, where in this case $k$ could be all LVs or the top 5, 10, 25 and 50 (since we have an order of magnitude less LVs than genes).


Since the gold standard of drug-disease medical indications is described with Disease Ontology IDs (DOID) [@doi:10.1093/nar/gky1032], we mapped PhenomeXcan traits to the Experimental Factor Ontology [@doi:10.1093/bioinformatics/btq099] using [@url:https://github.com/EBISPOT/EFO-UKB-mappings], and then to DOID.


### Consensus clustering of traits

We performed two preprocessing steps on the S-MultiXcan results before the cluster analysis.
First, we combined results in $\mathbf{M}$ (with $p$-values converted to $z$-scores, as described before) for traits that mapped to the same Experimental Factor Ontology (EFO) [@doi:10.1093/bioinformatics/btq099] term using the Stouffer's method: $\sum w_i M_{ij} / \sqrt{\sum w_i^2}$, where $w_i$ is a weight based on the GWAS sample size for trait $i$, and $M_{ij}$ is the $z$-score for gene $j$.
Second, we divided all $z$-scores for each trait $i$ by their sum to reduce the effect of highly polygenic traits: $M_{ij} / \sum M_{ij}$.
Finally, we projected this data matrix using Equation (@eq:proj), obtaining $\hat{\mathbf{M}}$ with $n$=3,752 traits and $l$=987 LVs as the input of our clustering pipeline.


A partitioning of $\hat{\mathbf{M}}$ with $n$ traits into $k$ clusters is represented as a label vector $\pi \in \mathbb{N}^n$.
<!--  -->
Consensus clustering approaches consist of two steps:
1) the generation of an ensemble $\Pi$ with $r$ partitions of the dataset: $\Pi=\{\pi_1, \pi_2, \ldots, \pi_r\}$,
and 2) the combination of the ensemble into a consolidated solution defined as:

$$
\pi^* = \mathrm{arg}\,\underset{\hat{\pi}}{\max} Q(\{ \lvert \mathcal{L}^i \lvert \phi(\hat{\pi}_{\mathcal{L}^i}, \pi_{i \mathcal{L}^i}) \mid i \in \{1,\ldots,r\} \}),
$$ {#eq:consensus:obj_func}

where $\mathcal{L}^i$ is a set of data indices with known cluster labels for partition $i$,
$\phi\colon \mathbb{N}^n \times \mathbb{N}^n \to \mathbb{R}$ is a function that measures the similarity between two partitions,
and $Q$ is a measure of central tendency, such as the mean or median.
We used the adjusted Rand index (ARI) [@doi:10.1007/BF01908075] for $\phi$ and the median for $Q$.
<!--  -->
To obtain $\pi^*$, we define a consensus function $\Gamma\colon \mathbb{N}^{n \times r} \to \mathbb{N}^n$ with $\Pi$ as the input.
We used consensus functions based on the evidence accumulation clustering (EAC) paradigm [@doi:10.1109/TPAMI.2005.113], where $\Pi$ is first transformed into a distance matrix
<!--  -->
<!-- $\mathbf{D}_{ij} = \frac{d_{ij}}{r}$, -->
$\mathbf{D}_{ij} = d_{ij} / r$,
<!--  -->
where $d_{ij}$ is the number of times traits $i$ and $j$ were grouped in different clusters across all $r$ partitions in $\Pi$.
Then, $\Gamma$ can be any similarity-based clustering algorithm, which is applied on $\mathbf{D}$ to derive the final partition $\pi^*$.


For the ensemble generation step, we used different algorithms to create a highly diverse set of partitions (see Figure @fig:clustering:design) since diversity is an important property for ensembles [@doi:10.1016/j.ins.2016.04.027; @doi:10.1109/TPAMI.2011.84; @doi:10.1016/j.patcog.2014.04.005].
We used three data representations: the raw dataset, its projection into the top 50 principal components, and the embedding learned by UMAP [@arxiv:1802.03426] using 50 components.
<!--  -->
For each of these, we applied five clustering algorithms covering a wide range of different assumptions on the data structure: $k$-means [@Arthur2007], spectral clustering [@Ng2001], a Gaussian mixture model (GMM), hierarchical clustering, and DBSCAN [@Ester1996].
<!--  -->
For $k$-means, spectral clustering and GMM, we specified a range of $k$ between 2 and $\sqrt{n} \approx 60$, and for each $k$ we generated five partitions using random seeds.
<!--  -->
For hierarchical clustering, for each $k$, we generated four partitions using common linkage criteria: ward, complete, average and single.
<!--  -->
For DBSCAN, we combined different ranges for parameters $\epsilon$ (the maximum distance between two data points to be considered part of the same neighborhood) and *minPts* (the minimum number of data points in a neighborhood for a data point to be considered a core point), based on the procedure in [@doi:10.1088/1755-1315/31/1/012012].
Specifically, we used *minPts* values from 2 to 125.
For each data representation (raw, PCA and UMAP), we determined a plausible range of $\epsilon$ values by observing the distribution of the mean distance of the *minPts*-nearest neighbors across all data points.
Since some combinations of *minPts* and $\epsilon$ might not produce a meaningful partition (for instance, when all points are detected as noisy or only one cluster is found), we resampled partitions generated by DBSCAN to ensure an equal representation of this algorithm in the ensemble.
<!--  -->
This procedure generated a final ensemble of 4,428 partitions of 3,752 traits.


Finally, we used spectral clustering on $\mathbf{D}$ to derive the final consensus partitions.
$\mathbf{D}$ was first transformed into a similarity matrix by applying an RBF kernel $\mathrm{exp}(-\gamma \mathbf{D}^2)$ using four different values for $\gamma$ that we empirically determined to work best.
Therefore, for each $k$ between 2 and 60, we derived four consensus partitions and selected the one that maximized Equation (@eq:consensus:obj_func).
<!--  -->
We further filtered this set of 59 solutions to keep only those with an ensemble agreement larger than the 75th percentile, leaving a total of 15 final consensus partitions shown in Figure @fig:clustering:tree.

<!-- Clustering interpretation -->
The input data in our clustering pipeline undergoes several linear and nonlinear transformations, including PCA, UMAP and the ensemble transformation using the EAC paradigm (distance matrix $\mathbf{D}$).
Although consensus clustering has clear advantages for biological data [@pmid:27303057], this set of data transformations complicates the interpretation of results.
<!--  -->
To circumvent this, we used a supervised learning approach to detect which gene modules/LVs are the most important for each cluster of traits (Figure @fig:clustering:design b).
`To address reviewer comment:`{.red} Note that we did not use this supervised model for prediction but only to learn which features (LVs) were most discriminative for each cluster.
For this, we used the highest resolution partition ($k$=29, although any could be used) to train a decision tree model using each of the clusters as labels and the projected data $\hat{\mathbf{M}}$ as the training samples.
For each $k$, we built a set of binary labels with the current cluster's traits as the positive class and the rest of the traits as the negative class.
Then, we selected the LV in the root node of the trained model only if its threshold was positive and larger than one standard deviation.
Next, we removed this LV from $\hat{\mathbf{M}}$ (regardless of being previously selected or not) and trained the model again.
We repeated this procedure 20 times to extract the top 20 LVs that better discriminate traits in a cluster from the rest.


### CRISPR-Cas9 screening

**Cell culture.**
HepG2 cells were obtained from ATCC (ATCC® HB-8065™), and maintained in Eagle's Minimum Essential Medium with L-Glutamine (EMEM, Cat. 112-018-101, Quality Biology) supplemented with 10% Fetal Bovine Serum (FBS, Gibco, Cat.16000-044), and 1% Pen/Strep (Gibco, Cat.15140-122).
Cells were kept at 37oC in a humidity-controlled incubator with 5% CO2, and were maintained at a density not exceeding more than 80% confluency.

**Genome-wide lentiviral pooled CRISPR-Cas9 library.**
3rd lentiviral generation, Broad GPP genome-wide Human Brunello CRISPR knockout Pooled library was provided by David Root and John Doench from Addgene (Cat. 73179-LV), and was used for HepG2 cell transduction.
It consists of 76,441 sgRNAs, and targets 19,114 genes in the human genome with an average of 4 sgRNAs per gene.
Each 20nt sgRNA cassette was inserted into the lentiCRIS-PRv2 backbone between U6 promoter and gRNA scaffold.
Through cell transduction, the lentiviral vectors which encode Cas9 were used to deliver the sgRNA cassette containing plasmids into cells during cell replication. 
Unsuccessful transduced cells were excluded through puromycin selection.

**Lentiviral titer determination.**
No-spin lentiviral transduction was utilized for the screen.
In a Collagen-I coated 6-wells plate, approximate 2.5 M cells were seeded each well in the presence of 8ug/ml polybrene (Millipore Sigma, Cat. TR-1003 G), and a different titrated virus volume (e.g., 0, 50, 100, 200, 250, and 400ul) was assigned to each well.
EMEM complete media was added to make the final volume of 1.24ml. 16-18hrs post-transduction, virus/polybrene-containing media was removed from each well.
Cells were washed twice with 1x DPBS and replaced with fresh EMEM.
At 24h, cells in each well were trypsinized, diluted (e.g.,1:10), and seeded in pairs of wells of 6-well plates. At 60hr post-transduction, cell media in each well was replaced with fresh EMEM. 2ug/ml of puromycin (Gibco, Cat. A1113803) was added to one well out of the pair. 2-5 days after puromycin selection, or the 0 virus well treated with puromycin had no survival of cells, cells in both wells with/without puromycin were collected and counted for viability.
Percentage of Infection (PI%) was obtained by comparing the cell numbers with/without puromycin selection within each pair.
By means of Poisson's distribution theory, when transduction efficiency (PI%) is between 30-50%, which corresponds to an MOI (Multiplicity of Infection) of ~0.35-0.70. At MOI equal to or close to 0.3, around 95% of infected cells are predicted to have only one copy of the virus.
Therefore, a volume of virus (120ul) yielding 30-40% of transduction efficiency was chosen for further large-scale viral transduction.

**Lentiviral Transduction in HepG2 Using Brunello CRISPR Knockout Pooled Library.**
In order to achieve a coverage (representation) of at least 500 cells per sgRNA, and at an MOI between 0.3-0.4 to ensure 95% of infected cells get only one viral particle per cell, ~200M cells were initiated for the screen.
Transduction was carried out in a similar fashion as described above.
Briefly, 2.5M cells were seeded in each well of 14 6-well plates, along with 8ug/ml of polybrene.
A volume of 120ul of the virus was added to each experimental well. 18hrs post-transduction, virus/PB mix medium was removed, and cells in each well were collected, counted, and pooled into T175 flasks.
At 60hr post-transduction, 2ug/ml of puromycin was added to each flask.
Mediums were changed every two days with fresh EMEM, topped with 2ug/ml puromycin.
Seven days after puromycin selection, cells were collected, pooled, counted, and replated.

**Fluorescent dye staining.** 9 days after puromycin selection, cells were assigned to 2 groups. 20-30M cells were collected as Unsorted Control.
The cell pellet was spun down at 500 x g for 5min at 4oC.
The dry pellet was kept at -80oC for further genomic DNA isolation.
The rest of the cells (approximately 200M) were kept in 100mm dishes and stained with a fluorescent dye (LipidSpotTM 488, Biotium, Cat. 70065-T).
In Brief, LipidSpot 488 was diluted to 1:100 with DPBS.
4ml of staining solution was used for each dish and incubated at 37oC for 30min.
Cell images were captured through fluorescent microscope EVOS for GFP signal detection (Supplementary Figure @fig:sup:crispr:fig1).

**Fluorescence-activated cell sorting (FACS).**
Cells were immediately collected into 50ml tubes (From this point on, keep cells cold), and spun at 500 x g for 5min at 4oC.
After DPBS wash, cell pellets were resuspended with FACS Sorting Buffer (1x DPBS without Ca2+/Mg2+, 2.5mM EDTA, 25mM HEPES, 1% BSA.
The solution was filter sterilized, and kept at 4oC), pi-pet gently to make single cells.
The cell solution was then filtered through a cell strainer (Falcon, Cat. 352235) and was kept on ice, protected from light.
Collected cells were sorted on FACSJazz. 100um nozzle was used for sorting. ~20% of each GFP-High and GFP-Low (Supplementary Figure @fig:sup:crispr:fig2) were collected into 15ml tubes.
After sorting, cells were immediately spun down.
Pellets were kept at -80oC for further genomic DNA isolation.

**Genomic DNA isolation and verification.**
Three conditions of Genomic DNA (Un-Sorted Control, lentiV2 GFP-High, and lentiV2 GFP-Low) were extracted using QIAamp DNA Blood Mini Kit (Qiagen, Cat.51104), followed by UV Spectroscopy (Nanodrop) to access the quality and quantity of the gDNA.
A total of 80-160ug of gDNA was isolated for each condition.
sgRNA cassette and lentiviral specific transgene in isolated gDNA were verified through PCR (Supplementary Figure @fig:sup:crispr:fig3).

**Illumina libraries generation and sequencing.**
The fragment containing sgRNA cassette was amplified using P5 /P7 primers, as indicated in [@pmid:26780180], and primer sequences were adapted from Broad Institute protocol (Supplementary Figure @fig:sup:crispr:table1).
Stagger sequence (0-8nt) was included in P5 and 8bp uniquely barcoded sequence in P7.
Primers were synthesized through Integrated DNA Technologies (IDT), and each primer was PAGE purified. 32 PCR reactions were set up for each condition.
Each 100ul PCR reaction consists of roughly 5ug of gDNA, 5ul of each 10uM P5 and P7. ExTaq DNA Polymerase (TaKaRa, Cat. RR001A) was used to amplify the amplicon.
PCR Thermal Cycler Parameters set as Initial at 95oC for 1min; followed by 24 cycles of Denaturation at 94oC for 30 seconds, Annealing at 52.5oC for 30 seconds, Extension at 72oC for 30 seconds.
A final Elongation at 72oC for 10 minutes. 285bp-293bp PCR products were expected (Supplementary Figure @fig:sup:crispr:fig4 A).
PCR products within the same condition were pooled and purified using SPRIselect beads (Beckman Coulter, Cat. B23318).
Purified Illumina libraries were quantitated on Qubit, and the quality of the library was analyzed on Bio-analyzer using High Sensitivity DNA Chip.
A single approximate 285bp peak was expected. (Supplementary Figure @fig:sup:crispr:fig4 B).
Final Illumina library samples were sequenced on Nova-seq 6000.
Samples were pooled and loaded on an SP flow cell, along with a 20% PhiX control v3 library spike-in.


### Code and data availability

The code and data to reproduce all the analyses in this work are available in [https://github.com/greenelab/phenoplier](https://github.com/greenelab/phenoplier).


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>


## Acknowledgements

Figure 1 was created with BioRender.com.


## Supplementary material


### CRISPR-screen

![
**EVOS Fluorescent Microscope Image Capture.**
A. HepG2_lentiV2_Ctrl with no-viral transduction.
B. HepG2_lentiV2 with viral transduction.
<!--  -->
](images/crispr/figure1.png "EVOS Fluorescent Microscope Image Capture"){#fig:sup:crispr:fig1 width="80%"}


![
**Fluorescence-Activated Cell Sorting Gate Setting.**
A. HepG2_UnStained WT.
B. HepG2_lentiV2 with viral transduction.
<!--  -->
](images/crispr/figure2.png "Fluorescence-Activated Cell Sorting Gate Setting"){#fig:sup:crispr:fig2 width="80%"}


![
**Verification of sgRNA cassette and lentiV2 transgene.**
A. 20nt sgRNA cassette was verified in lentiV2 transduced genomic DNA population, 163 bp PCR product obtained, while WT HepG2 didn’t possess the cassette, thus, no PCR product.
B. lentiviral-specific transgene WPRE was verified in lentiV2 transduced genomic DNA population, while no transduced WT didn’t have the transgene, therefore, no 173 bp PCR product observed.
<!--  -->
](images/crispr/figure3.png "Verification of sgRNA cassette and lentiV2 transgene"){#fig:sup:crispr:fig3 width="80%"}


![
<!-- **XXX.** -->
<!--  -->
<!--  -->
](images/crispr/table1.png "Table 1"){#fig:sup:crispr:table1 width="80%"}


![
**Illumina library generation.**
A. Construct for generating illumina libraries.
B. Final illumina library from HS DNA ---showed a single ~285bp peak was generated.
](images/crispr/figure4.png "xxxx"){#fig:sup:crispr:fig4 width="80%"}


### LV603

<!-- LV603:multiplier_pathways:start -->
| Pathway                             | AUC   | FDR      |
|:------------------------------------|:------|:---------|
| IRIS Neutrophil-Resting             | 0.91  | 4.51e-35 |
| SVM Neutrophils                     | 0.98  | 1.43e-09 |
| PID IL8CXCR2 PATHWAY                | 0.81  | 7.04e-03 |
| SIG PIP3 SIGNALING IN B LYMPHOCYTES | 0.77  | 1.95e-02 |

Table: Pathways aligned to LV603 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv603}
<!-- LV603:multiplier_pathways:end -->

<!-- LV603:phenomexcan_traits_assocs:start -->
| Trait description                  | Sample size   | Cases   | FDR            |
|:-----------------------------------|:--------------|:--------|:---------------|
| Myeloid White Cell Count           | 173,480       |         | 3.63e&#8209;07 |
| Sum Basophil Neutrophil Count      | 173,480       |         | 4.07e&#8209;07 |
| Neutrophil Count                   | 173,480       |         | 4.17e&#8209;07 |
| Sum Neutrophil Eosinophil Count    | 173,480       |         | 4.72e&#8209;07 |
| Granulocyte Count                  | 173,480       |         | 5.16e&#8209;07 |
| White Blood Cell Count             | 173,480       |         | 2.67e&#8209;06 |
| Neutrophill count                  | 349,856       |         | 1.58e&#8209;05 |
| White blood cell (leukocyte) count | 350,470       |         | 2.06e&#8209;05 |

Table: Significant trait associations of LV603 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv603}
<!-- LV603:phenomexcan_traits_assocs:end -->

<!-- LV603:emerge_traits_assocs:start -->
| Phecode                     | Trait description   | Sample size   | Cases   | FDR   |
|:----------------------------|:--------------------|:--------------|:--------|:------|
| No significant associations |                     |               |         |       |

Table: Significant trait associations of LV603 in eMERGE. {#tbl:sup:emerge_assocs:lv603}
<!-- LV603:emerge_traits_assocs:end -->


### Gene modules enrichment for lipids gene-sets

<!-- lipids_gene_sets:modules_enriched_increase:start -->
| Gene module   | Lipids gene-set   | Leading edge      | p-value   |
|:--------------|:------------------|:------------------|:----------|
| **LV246**     | increase          | *DGAT2*, *ACACA*  | 0.0035    |
| LV702         | increase          | *ACACA*, *DGAT2*  | 0.0046    |
| **LV607**     | increase          | *ACACA*, *DGAT2*  | 0.0058    |
| LV890         | increase          | *ACACA*, *DGAT2*  | 0.0067    |
| **LV74**      | increase          | *MBTPS1*, *DGAT2* | 0.0078    |
| **LV865**     | increase          | *ACACA*, *DGAT2*  | 0.0092    |
| LV841         | increase          | *ACACA*, *DGAT2*  | 0.0096    |

Table: Gene modules (LVs) nominally enriched for the lipids-increasing gene-set from the CRISPR-screen (*P* < 0.01). LVs significantly aligned with pathways (FDR < 0.05) from the MultiPLIER models are shown in boldface. {#tbl:sup:lipids_crispr:modules_enriched_increase}
<!-- lipids_gene_sets:modules_enriched_increase:end -->


<!-- lipids_gene_sets:modules_enriched_decrease:start -->
| Gene module   | Lipids gene-set   | Leading edge       | p-value   |
|:--------------|:------------------|:-------------------|:----------|
| LV520         | decrease          | *FBXW7*, *TCF7L2*  | 0.0006    |
| LV801         | decrease          | *UBE2J2*, *TCF7L2* | 0.0022    |
| LV512         | decrease          | *FBXW7*, *TCF7L2*  | 0.0025    |
| **LV612**     | decrease          | *PTEN*, *FBXW7*    | 0.0036    |
| LV41          | decrease          | *PCYT2*, *TCF7L2*  | 0.0041    |
| **LV838**     | decrease          | *UBE2J2*, *TCF7L2* | 0.0070    |
| LV302         | decrease          | *TCF7L2*, *PTEN*   | 0.0083    |
| LV959         | decrease          | *TCF7L2*, *PTEN*   | 0.0092    |

Table: Gene modules (LVs) nominally enriched for the lipids-decreasing gene-set from the CRISPR-screen (*P* < 0.01). LVs significantly aligned with pathways (FDR < 0.05) from the MultiPLIER models are shown in boldface. {#tbl:sup:lipids_crispr:modules_enriched_decrease}
<!-- lipids_gene_sets:modules_enriched_decrease:end -->


### LV246

<!-- LV246:multiplier_pathways:start -->
| Pathway                                                        | AUC   | FDR      |
|:---------------------------------------------------------------|:------|:---------|
| REACTOME FATTY ACID TRIACYLGLYCEROL AND KETONE BODY METABOLISM | 0.89  | 3.97e-16 |
| REACTOME METABOLISM OF LIPIDS AND LIPOPROTEINS                 | 0.67  | 1.14e-08 |
| REACTOME TRIGLYCERIDE BIOSYNTHESIS                             | 0.86  | 6.52e-04 |
| KEGG PYRUVATE METABOLISM                                       | 0.82  | 2.66e-03 |
| KEGG PROPANOATE METABOLISM                                     | 0.83  | 4.27e-03 |

Table: Pathways aligned to LV246 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv246}
<!-- LV246:multiplier_pathways:end -->

<!-- LV246:phenomexcan_traits_assocs:start -->
| Trait description                                        | Sample size   | Cases   | FDR            |
|:---------------------------------------------------------|:--------------|:--------|:---------------|
| CH2DB NMR                                                | 24,154        |         | 1.05e&#8209;12 |
| High cholesterol (self-reported)                         | 361,141       | 43,957  | 7.78e&#8209;07 |
| Ankle spacing width                                      | 206,589       |         | 2.06e&#8209;05 |
| Ankle spacing width (right)                              | 114,614       |         | 9.03e&#8209;05 |
| HDL Cholesterol NMR                                      | 19,270        |         | 2.46e&#8209;04 |
| Cholesterol lowering medication                          | 193,148       | 24,247  | 2.54e&#8209;04 |
| Ankle spacing width (left)                               | 114,630       |         | 5.39e&#8209;04 |
| Fasting Glucose                                          | 46,186        |         | 1.90e&#8209;03 |
| Cholesterol lowering medication                          | 165,340       | 38,057  | 6.74e&#8209;03 |
| Pulse rate, automated reading                            | 340,162       |         | 8.61e&#8209;03 |
| Recent easy annoyance or irritability                    | 117,483       |         | 1.04e&#8209;02 |
| Treatment/medication code: simvastatin                   | 361,141       | 40,921  | 1.11e&#8209;02 |
| Pulse rate                                               | 118,850       |         | 1.19e&#8209;02 |
| Mean platelet (thrombocyte) volume                       | 350,470       |         | 1.37e&#8209;02 |
| Duration of moderate activity                            | 268,826       |         | 1.69e&#8209;02 |
| LDL Cholesterol NMR                                      | 13,527        |         | 1.94e&#8209;02 |
| Red blood cell (erythrocyte) distribution width          | 350,473       |         | 1.99e&#8209;02 |
| Intra-ocular pressure, corneal-compensated (right)       | 76,630        |         | 2.63e&#8209;02 |
| Heel bone mineral density (BMD) (right)                  | 114,552       |         | 2.74e&#8209;02 |
| Triglycerides NMR                                        | 21,559        |         | 3.47e&#8209;02 |
| Heel bone mineral density T-score, automated (right)     | 114,614       |         | 3.75e&#8209;02 |
| Heel quantitative ultrasound index, direct entry (right) | 114,614       |         | 3.75e&#8209;02 |
| Days/week of moderate physical activity 10+ minutes      | 343,943       |         | 4.85e&#8209;02 |
| Ischaemic heart disease (wide definition)                | 361,194       | 20,857  | 4.97e&#8209;02 |

Table: Significant trait associations of LV246 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv246}
<!-- LV246:phenomexcan_traits_assocs:end -->

<!-- LV246:emerge_traits_assocs:start -->
| Phecode   | Trait description          | Sample size   | Cases   | FDR            |
|:----------|:---------------------------|:--------------|:--------|:---------------|
| 276.41    | Acidosis                   | 41,838        | 1,526   | 2.40e&#8209;03 |
| 276.4     | Acid-base balance disorder | 42,005        | 1,693   | 2.97e&#8209;03 |

Table: Significant trait associations of LV246 in eMERGE. {#tbl:sup:emerge_assocs:lv246}
<!-- LV246:emerge_traits_assocs:end -->


### LV116

<!-- LV116:multiplier_pathways:start -->
| Pathway                                              | AUC   | FDR      |
|:-----------------------------------------------------|:------|:---------|
| REACTOME INTERFERON SIGNALING                        | 0.84  | 3.48e-09 |
| SVM Macrophages M1                                   | 0.92  | 2.09e-05 |
| REACTOME INTERFERON ALPHA BETA SIGNALING             | 0.94  | 3.36e-05 |
| REACTOME CYTOKINE SIGNALING IN IMMUNE SYSTEM         | 0.67  | 1.53e-04 |
| IRIS DendriticCell-LPSstimulated                     | 0.65  | 1.09e-03 |
| KEGG CYTOSOLIC DNA SENSING PATHWAY                   | 0.84  | 3.22e-03 |
| REACTOME NEGATIVE REGULATORS OF RIG I MDA5 SIGNALING | 0.81  | 1.61e-02 |

Table: Pathways aligned to LV116 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv116}
<!-- LV116:multiplier_pathways:end -->


### LV931

![
**Cell types for LV931.**
<!--  -->
](images/lvs_analysis/lv931/lv931-cell_types.svg "Cell types for LV931"){#fig:sup:lv931 width="80%"}


<!-- LV931:multiplier_pathways:start -->
| Pathway          | AUC   | FDR      |
|:-----------------|:------|:---------|
| MIPS SPLICEOSOME | 0.63  | 3.13e-02 |
| PID TGFBRPATHWAY | 0.71  | 3.99e-02 |

Table: Pathways aligned to LV931 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv931}
<!-- LV931:multiplier_pathways:end -->


### LV66

![
**Cell types for LV66.**
<!--  -->
](images/lvs_analysis/lv66/lv66-cell_types.svg "Cell types for LV66"){#fig:sup:lv66 width="80%"}

<!-- LV66:multiplier_pathways:start -->
| Pathway                                        | AUC   | FDR      |
|:-----------------------------------------------|:------|:---------|
| REACTOME METABOLISM OF LIPIDS AND LIPOPROTEINS | 0.62  | 3.12e-04 |

Table: Pathways aligned to LV66 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv66}
<!-- LV66:multiplier_pathways:end -->


### Agreement of consensus clustering partitions with the ensemble by number of clusters

![
**Final selected partitions for follow-up analysis.**
<!--  -->
From all consensus clustering partitions generated with $k$ from 2 to 60, we selected those with a median adjusted Rand index (ARI) with the ensemble members greater the 75th percentile.
](images/clustering/selected_best_partitions_by_k.svg "Consensus partitions agreement with ensemble"){#fig:sup:consensus_agreement width="80%"}



### Cluster-specific and general transcriptional processes associated with disease

![
**Cluster-specific and general transcriptional processes associated with disease using novel LVs.**
The plot shows a submatrix of $\hat{\mathbf{M}}$ for the main trait clusters at $k$=29, considering only LVs (rows) that are not aligned with any pathway.
Standardized values from -6 (lighter color) to 21 (darker color).
](images/clustering/global_clustermap-novel-plain.svg "Heatmap with novel gene modules and traits"){#fig:sup:clustering:novel:heatmap width="100%"}


### LV928

![
**Cell types for LV928.**
<!--  -->
](images/lvs_analysis/lv928/lv928-cell_types.svg "Cell types for LV928"){#fig:sup:lv928 width="80%"}

<!-- LV928:multiplier_pathways:start -->
| Pathway   | AUC   | FDR      |
|:----------|:------|:---------|
| DMAP ERY3 | 0.81  | 1.16e-24 |
| DMAP ERY4 | 0.78  | 2.49e-17 |

Table: Pathways aligned to LV928 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv928}
<!-- LV928:multiplier_pathways:end -->

<!-- LV928:phenomexcan_traits_assocs:start -->
| Trait description                               | Sample size   | Cases   | Partition / cluster   | FDR            |
|:------------------------------------------------|:--------------|:--------|:----------------------|:---------------|
| Mean sphered cell volume                        | 344,729       |         | 29 / 2                | 2.18e&#8209;46 |
| Mean reticulocyte volume                        | 344,728       |         | 29 / 2                | 4.08e&#8209;44 |
| Mean corpuscular volume                         | 350,473       |         | 29 / 2                | 5.57e&#8209;33 |
| Red blood cell (erythrocyte) distribution width | 350,473       |         | 29 / 23               | 7.62e&#8209;31 |
| Reticulocyte percentage                         | 344,728       |         | 29 / 4                | 2.12e&#8209;29 |
| Reticulocyte count                              | 344,729       |         | 29 / 4                | 6.88e&#8209;28 |
| Reticulocyte Count                              | 173,480       |         | 29 / 4                | 1.06e&#8209;23 |
| Mean corpuscular haemoglobin                    | 350,472       |         | 29 / 2                | 7.89e&#8209;23 |
| High light scatter reticulocyte count           | 344,729       |         | 29 / 4                | 3.05e&#8209;21 |
| Immature reticulocyte fraction                  | 344,728       |         | 29 / 4                | 5.04e&#8209;21 |
| High light scatter reticulocyte percentage      | 344,729       |         | 29 / 4                | 1.57e&#8209;16 |
| Red blood cell (erythrocyte) count              | 350,475       |         | 29 / 5                | 2.53e&#8209;16 |
| Red Blood Cell Count                            | 173,480       |         | 29 / 5                | 2.62e&#8209;09 |
| Haemoglobin concentration                       | 350,474       |         | 29 / 5                | 1.25e&#8209;03 |
| Haematocrit percentage                          | 350,475       |         | 29 / 5                | 3.77e&#8209;03 |

Table: Significant trait associations of LV928 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv928}
<!-- LV928:phenomexcan_traits_assocs:end -->

<!-- LV928:emerge_traits_assocs:start -->
| Phecode   | Trait description                                | Sample size   | Cases   | FDR            |
|:----------|:-------------------------------------------------|:--------------|:--------|:---------------|
| 250.24    | Type 2 diabetes with neurological manifestations | 43,236        | 2,963   | 1.44e&#8209;02 |
| 195       | Cancer, suspected or other                       | 50,040        | 2,250   | 2.42e&#8209;02 |
| 514.2     | Solitary pulmonary nodule                        | 50,389        | 2,270   | 4.65e&#8209;02 |

Table: Significant trait associations of LV928 in eMERGE. {#tbl:sup:emerge_assocs:lv928}
<!-- LV928:emerge_traits_assocs:end -->


### LV30

![
**Cell types for LV30.**
<!--  -->
](images/lvs_analysis/lv30/lv30-cell_types.svg "Cell types for LV30"){#fig:sup:lv30 width="80%"}

<!-- LV30:multiplier_pathways:start -->
| Pathway   | AUC   | FDR      |
|:----------|:------|:---------|
| DMAP ERY3 | 0.95  | 5.62e-52 |
| DMAP ERY4 | 0.98  | 5.28e-51 |
| DMAP ERY5 | 0.98  | 1.96e-49 |

Table: Pathways aligned to LV30 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv30}
<!-- LV30:multiplier_pathways:end -->

<!-- LV30:phenomexcan_traits_assocs:start -->
| Trait description                          | Sample size   | Cases   | Partition / cluster   | FDR            |
|:-------------------------------------------|:--------------|:--------|:----------------------|:---------------|
| Mean reticulocyte volume                   | 344,728       |         | 29 / 2                | 1.41e&#8209;51 |
| Immature reticulocyte fraction             | 344,728       |         | 29 / 4                | 5.79e&#8209;40 |
| Mean sphered cell volume                   | 344,729       |         | 29 / 2                | 3.26e&#8209;36 |
| Mean corpuscular volume                    | 350,473       |         | 29 / 2                | 3.18e&#8209;35 |
| Reticulocyte percentage                    | 344,728       |         | 29 / 4                | 1.41e&#8209;28 |
| Mean corpuscular haemoglobin               | 350,472       |         | 29 / 2                | 3.72e&#8209;28 |
| High light scatter reticulocyte count      | 344,729       |         | 29 / 4                | 8.20e&#8209;28 |
| Reticulocyte count                         | 344,729       |         | 29 / 4                | 2.13e&#8209;26 |
| Reticulocyte Count                         | 173,480       |         | 29 / 4                | 1.11e&#8209;24 |
| High light scatter reticulocyte percentage | 344,729       |         | 29 / 4                | 4.05e&#8209;22 |

Table: Significant trait associations of LV30 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv30}
<!-- LV30:phenomexcan_traits_assocs:end -->

<!-- LV30:emerge_traits_assocs:start -->
| Phecode                     | Trait description   | Sample size   | Cases   | FDR   |
|:----------------------------|:--------------------|:--------------|:--------|:------|
| No significant associations |                     |               |         |       |

Table: Significant trait associations of LV30 in eMERGE. {#tbl:sup:emerge_assocs:lv30}
<!-- LV30:emerge_traits_assocs:end -->


### LV730

![
**Cell types for LV730.**
<!--  -->
](images/lvs_analysis/lv730/lv730-cell_types.svg "Cell types for LV730"){#fig:sup:lv730 width="80%"}

<!-- LV730:multiplier_pathways:start -->
| Pathway    | AUC   | FDR      |
|:-----------|:------|:---------|
| DMAP MEGA2 | 0.82  | 2.64e-05 |

Table: Pathways aligned to LV730 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv730}
<!-- LV730:multiplier_pathways:end -->

<!-- LV730:phenomexcan_traits_assocs:start -->
| Trait description                  | Sample size   | Cases   | Partition / cluster   | FDR            |
|:-----------------------------------|:--------------|:--------|:----------------------|:---------------|
| Platelet distribution width        | 350,470       |         | 29 / 1                | 2.88e&#8209;13 |
| Mean platelet (thrombocyte) volume | 350,470       |         | 29 / 1                | 7.26e&#8209;13 |
| Platelet count                     | 350,474       |         | 29 / 1                | 1.24e&#8209;07 |
| Platelet Count                     | 173,480       |         | 29 / 1                | 1.21e&#8209;06 |
| Platelet crit                      | 350,471       |         | 29 / 1                | 1.38e&#8209;04 |

Table: Significant trait associations of LV730 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv730}
<!-- LV730:phenomexcan_traits_assocs:end -->

<!-- LV730:emerge_traits_assocs:start -->
| Phecode                     | Trait description   | Sample size   | Cases   | FDR   |
|:----------------------------|:--------------------|:--------------|:--------|:------|
| No significant associations |                     |               |         |       |

Table: Significant trait associations of LV730 in eMERGE. {#tbl:sup:emerge_assocs:lv730}
<!-- LV730:emerge_traits_assocs:end -->


### LV598

![
**Cell types for LV598.**
<!--  -->
](images/lvs_analysis/lv598/lv598-cell_types.svg "Cell types for LV598"){#fig:sup:lv598 width="80%"}

<!-- LV598:multiplier_pathways:start -->
| Pathway                     | AUC   | FDR      |
|:----------------------------|:------|:---------|
| PID SYNDECAN 1 PATHWAY      | 0.81  | 1.20e-02 |
| REACTOME COLLAGEN FORMATION | 0.77  | 1.89e-02 |

Table: Pathways aligned to LV598 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv598}
<!-- LV598:multiplier_pathways:end -->

<!-- LV598:phenomexcan_traits_assocs:start -->
| Trait description           | Sample size   | Cases   | Partition / cluster   | FDR            |
|:----------------------------|:--------------|:--------|:----------------------|:---------------|
| 6mm strong meridian (right) | 66,256        |         | 29 / 10               | 3.21e&#8209;07 |
| 6mm weak meridian (right)   | 66,256        |         | 29 / 10               | 2.04e&#8209;06 |
| 6mm strong meridian (left)  | 65,551        |         | 29 / 10               | 2.44e&#8209;06 |
| 3mm strong meridian (left)  | 75,398        |         | 29 / 10               | 2.53e&#8209;06 |
| 6mm weak meridian (left)    | 65,551        |         | 29 / 10               | 1.20e&#8209;05 |
| 3mm weak meridian (left)    | 75,398        |         | 29 / 10               | 1.58e&#8209;05 |
| 3mm strong meridian (right) | 75,410        |         | 29 / 10               | 2.95e&#8209;05 |
| 3mm weak meridian (right)   | 75,410        |         | 29 / 10               | 3.86e&#8209;05 |

Table: Significant trait associations of LV598 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv598}
<!-- LV598:phenomexcan_traits_assocs:end -->

<!-- LV598:emerge_traits_assocs:start -->
| Phecode                     | Trait description   | Sample size   | Cases   | FDR   |
|:----------------------------|:--------------------|:--------------|:--------|:------|
| No significant associations |                     |               |         |       |

Table: Significant trait associations of LV598 in eMERGE. {#tbl:sup:emerge_assocs:lv598}
<!-- LV598:emerge_traits_assocs:end -->


### LV844

![
**Cell types for LV844.**
](images/lvs_analysis/lv844/lv844-cell_types.svg "Cell types for LV844"){#fig:sup:lv844 width="80%"}

<!-- LV844:multiplier_pathways:start -->
| Pathway                                  | AUC   | FDR      |
|:-----------------------------------------|:------|:---------|
| KEGG ANTIGEN PROCESSING AND PRESENTATION | 0.80  | 1.35e-03 |

Table: Pathways aligned to LV844 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv844}
<!-- LV844:multiplier_pathways:end -->

<!-- LV844:phenomexcan_traits_assocs:start -->
| Trait description                                     | Sample size   | Cases   | Partition / cluster   | FDR            |
|:------------------------------------------------------|:--------------|:--------|:----------------------|:---------------|
| Rheumatoid Arthritis                                  | 80,799        | 19,234  | 29 / 26               | 1.20e&#8209;57 |
| malabsorption/coeliac disease (self-reported)         | 361,141       | 1,587   | 29 / 8                | 1.25e&#8209;43 |
| Coeliac disease                                       | 361,194       | 842     | 29 / 8                | 1.52e&#8209;41 |
| Intestinal malabsorption (ICD10 K90)                  | 361,194       | 922     | 29 / 8                | 5.28e&#8209;40 |
| Started insulin within one year diagnosis of diabetes | 16,415        | 1,999   | 29 / 13               | 7.77e&#8209;38 |
| Systemic Lupus Erythematosus                          | 23,210        | 7,219   | 29 / 26               | 6.45e&#8209;35 |
| Age diabetes diagnosed                                | 16,166        |         | 29 / 13               | 1.92e&#8209;34 |
| Never eat: Wheat products                             | 359,777       | 9,573   | 29 / 13               | 1.37e&#8209;31 |
| hyperthyroidism (self-reported)                       | 361,141       | 2,730   | 29 / 13               | 3.41e&#8209;30 |
| Medication: insulin product                           | 361,141       | 3,545   | 29 / 13               | 1.78e&#8209;25 |
| Insulin medication (females)                          | 193,148       | 1,476   | 29 / 13               | 2.79e&#8209;23 |
| Insulin medication (males)                            | 165,340       | 2,248   | 29 / 13               | 1.27e&#8209;20 |
| hypothyroidism (self-reported)                        | 361,141       | 17,574  | 29 / 13               | 3.35e&#8209;20 |
| Medication: levothyroxine sodium                      | 361,141       | 14,689  | 29 / 13               | 2.76e&#8209;19 |
| psoriasis (self-reported)                             | 361,141       | 4,192   | 29 / 13               | 6.74e&#8209;16 |

Table: Significant trait associations of LV844 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv844}
<!-- LV844:phenomexcan_traits_assocs:end -->

<!-- LV844:emerge_traits_assocs:start -->
| Phecode   | Trait description                                                                    | Sample size   | Cases   | FDR            |
|:----------|:-------------------------------------------------------------------------------------|:--------------|:--------|:---------------|
| 714.1     | Rheumatoid arthritis                                                                 | 49,453        | 2,541   | 1.53e&#8209;08 |
| 250.1     | Type 1 diabetes                                                                      | 42,723        | 2,450   | 3.85e&#8209;08 |
| 714       | Rheumatoid arthritis and other inflammatory polyarthropathies                        | 50,215        | 3,303   | 1.02e&#8209;06 |
| 440       | Atherosclerosis                                                                      | 47,471        | 4,993   | 6.73e&#8209;03 |
| 578.8     | Hemorrhage of rectum and anus                                                        | 47,545        | 1,991   | 6.73e&#8209;03 |
| 585.32    | End stage renal disease                                                              | 43,309        | 1,842   | 9.01e&#8209;03 |
| 440.2     | Atherosclerosis of the extremities                                                   | 45,524        | 3,046   | 1.09e&#8209;02 |
| 514.2     | Solitary pulmonary nodule                                                            | 50,389        | 2,270   | 1.39e&#8209;02 |
| 444       | Arterial embolism and thrombosis                                                     | 43,378        | 900     | 2.97e&#8209;02 |
| 440.22    | Atherosclerosis of native arteries of the extremities with intermittent claudication | 44,639        | 2,161   | 3.61e&#8209;02 |

Table: Significant trait associations of LV844 in eMERGE. {#tbl:sup:emerge_assocs:lv844}
<!-- LV844:emerge_traits_assocs:end -->


### LV155

![
**Cell types for LV155.**
<!--  -->
](images/lvs_analysis/lv155/lv155-cell_types.svg "Cell types for LV155"){#fig:sup:lv155 width="80%"}

<!-- LV155:multiplier_pathways:start -->
| Pathway                            | AUC   | FDR   |
|:-----------------------------------|:------|:------|
| No pathways significantly enriched |       |       |

Table: Pathways aligned to LV155 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv155}
<!-- LV155:multiplier_pathways:end -->

<!-- LV155:phenomexcan_traits_assocs:start -->
| Trait description                | Sample size   | Cases   | Partition / cluster   | FDR            |
|:---------------------------------|:--------------|:--------|:----------------------|:---------------|
| hypothyroidism (self-reported)   | 361,141       | 17,574  | 29 / 13               | 1.65e&#8209;03 |
| hyperthyroidism (self-reported)  | 361,141       | 2,730   | 29 / 13               | 1.03e&#8209;02 |
| Medication: levothyroxine sodium | 361,141       | 14,689  | 29 / 13               | 1.12e&#8209;02 |

Table: Significant trait associations of LV155 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv155}
<!-- LV155:phenomexcan_traits_assocs:end -->

<!-- LV155:emerge_traits_assocs:start -->
| Phecode   | Trait description       | Sample size   | Cases   | FDR            |
|:----------|:------------------------|:--------------|:--------|:---------------|
| 244.2     | Acquired hypothyroidism | 45,839        | 1,155   | 5.66e&#8209;02 |

Table: Trait associations of LV155 in eMERGE. {#tbl:sup:emerge_assocs:lv155}
<!-- LV155:emerge_traits_assocs:end -->


### LV57

![
**Cell types for LV57.**
](images/lvs_analysis/lv57/lv57-cell_types.svg "Cell types for LV57"){#fig:sup:lv57 width="80%"}

<!-- LV57:multiplier_pathways:start -->
| Pathway                                | AUC   | FDR      |
|:---------------------------------------|:------|:---------|
| KEGG T CELL RECEPTOR SIGNALING PATHWAY | 0.70  | 1.26e-03 |
| SVM T cells CD4 memory activated       | 0.79  | 2.59e-03 |
| IRIS CD4Tcell-Th2-restimulated12hour   | 0.78  | 7.57e-03 |
| KEGG ALLOGRAFT REJECTION               | 1.00  | 1.09e-02 |
| Custom Treg                            | 0.98  | 1.37e-02 |
| PID NFAT TFPATHWAY                     | 0.74  | 1.52e-02 |
| IRIS MemoryTcell-RO-activated          | 0.70  | 2.87e-02 |

Table: Pathways aligned to LV57 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv57}
<!-- LV57:multiplier_pathways:end -->

<!-- LV57:phenomexcan_traits_assocs:start -->
| Trait description                                     | Sample size   | Cases   | Partition / cluster   | FDR            |
|:------------------------------------------------------|:--------------|:--------|:----------------------|:---------------|
| hypothyroidism (self-reported)                        | 361,141       | 17,574  | 29 / 13               | 7.21e&#8209;25 |
| Medication: levothyroxine sodium                      | 361,141       | 14,689  | 29 / 13               | 3.71e&#8209;23 |
| hyperthyroidism (self-reported)                       | 361,141       | 2,730   | 29 / 13               | 8.93e&#8209;07 |
| Started insulin within one year diagnosis of diabetes | 16,415        | 1,999   | 29 / 13               | 6.60e&#8209;05 |
| Medication: insulin product                           | 361,141       | 3,545   | 29 / 13               | 5.20e&#8209;04 |
| Insulin medication (females)                          | 193,148       | 1,476   | 29 / 13               | 9.40e&#8209;04 |
| Insulin medication (males)                            | 165,340       | 2,248   | 29 / 13               | 3.63e&#8209;03 |

Table: Significant trait associations of LV57 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv57}
<!-- LV57:phenomexcan_traits_assocs:end -->

<!-- LV57:emerge_traits_assocs:start -->
| Phecode   | Trait description                                             | Sample size   | Cases   | FDR            |
|:----------|:--------------------------------------------------------------|:--------------|:--------|:---------------|
| 244       | Hypothyroidism                                                | 54,404        | 9,720   | 7.66e&#8209;09 |
| 244.4     | Hypothyroidism NOS                                            | 53,968        | 9,284   | 7.66e&#8209;09 |
| 279       | Disorders involving the immune mechanism                      | 56,771        | 3,309   | 1.07e&#8209;02 |
| 514.2     | Solitary pulmonary nodule                                     | 50,389        | 2,270   | 2.62e&#8209;02 |
| 714       | Rheumatoid arthritis and other inflammatory polyarthropathies | 50,215        | 3,303   | 3.77e&#8209;02 |

Table: Significant trait associations of LV57 in eMERGE. {#tbl:sup:emerge_assocs:lv57}
<!-- LV57:emerge_traits_assocs:end -->


### LV54

![
**Cell types for LV54.**
](images/lvs_analysis/lv54/lv54-cell_types.svg "Cell types for LV54"){#fig:sup:lv54 width="80%"}

<!-- LV54:multiplier_pathways:start -->
| Pathway                            | AUC   | FDR   |
|:-----------------------------------|:------|:------|
| No pathways significantly enriched |       |       |

Table: Pathways aligned to LV54 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv54}
<!-- LV54:multiplier_pathways:end -->

<!-- LV54:phenomexcan_traits_assocs:start -->
| Trait description                                     | Sample size   | Cases   | Partition / cluster   | FDR            |
|:------------------------------------------------------|:--------------|:--------|:----------------------|:---------------|
| Intestinal malabsorption (ICD10 K90)                  | 361,194       | 922     | 29 / 8                | 3.10e&#8209;25 |
| Coeliac disease                                       | 361,194       | 842     | 29 / 8                | 4.78e&#8209;25 |
| Never eat: Wheat products                             | 359,777       | 9,573   | 29 / 13               | 3.93e&#8209;23 |
| Systemic Lupus Erythematosus                          | 23,210        | 7,219   | 29 / 26               | 8.16e&#8209;23 |
| Started insulin within one year diagnosis of diabetes | 16,415        | 1,999   | 29 / 13               | 2.57e&#8209;20 |
| hyperthyroidism (self-reported)                       | 361,141       | 2,730   | 29 / 13               | 6.70e&#8209;19 |
| Medication: insulin product                           | 361,141       | 3,545   | 29 / 13               | 3.62e&#8209;18 |
| Age diabetes diagnosed                                | 16,166        |         | 29 / 13               | 9.20e&#8209;18 |
| malabsorption/coeliac disease (self-reported)         | 361,141       | 1,587   | 29 / 8                | 9.63e&#8209;15 |
| Insulin medication (males)                            | 165,340       | 2,248   | 29 / 13               | 6.01e&#8209;14 |
| psoriasis (self-reported)                             | 361,141       | 4,192   | 29 / 13               | 1.81e&#8209;13 |
| Rheumatoid Arthritis                                  | 80,799        | 19,234  | 29 / 26               | 2.17e&#8209;13 |
| Insulin medication (females)                          | 193,148       | 1,476   | 29 / 13               | 2.61e&#8209;12 |
| Medication: levothyroxine sodium                      | 361,141       | 14,689  | 29 / 13               | 4.25e&#8209;10 |
| hypothyroidism (self-reported)                        | 361,141       | 17,574  | 29 / 13               | 2.49e&#8209;08 |

Table: Significant trait associations of LV54 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv54}
<!-- LV54:phenomexcan_traits_assocs:end -->

<!-- LV54:emerge_traits_assocs:start -->
| Phecode   | Trait description                                             | Sample size   | Cases   | FDR            |
|:----------|:--------------------------------------------------------------|:--------------|:--------|:---------------|
| 250.1     | Type 1 diabetes                                               | 42,723        | 2,450   | 1.69e&#8209;13 |
| 244       | Hypothyroidism                                                | 54,404        | 9,720   | 1.01e&#8209;05 |
| 244.4     | Hypothyroidism NOS                                            | 53,968        | 9,284   | 1.01e&#8209;05 |
| 695       | Erythematous conditions                                       | 48,347        | 4,210   | 8.54e&#8209;05 |
| 714       | Rheumatoid arthritis and other inflammatory polyarthropathies | 50,215        | 3,303   | 6.58e&#8209;04 |
| 440       | Atherosclerosis                                               | 47,471        | 4,993   | 1.90e&#8209;03 |
| 585       | Renal failure                                                 | 51,437        | 9,970   | 7.10e&#8209;03 |
| 585.33    | Chronic Kidney Disease, Stage III                             | 46,279        | 4,812   | 7.49e&#8209;03 |
| 585.32    | End stage renal disease                                       | 43,309        | 1,842   | 7.49e&#8209;03 |
| 250.6     | Polyneuropathy in diabetes                                    | 41,948        | 1,675   | 8.55e&#8209;03 |
| 250       | Diabetes mellitus                                             | 52,531        | 12,258  | 1.02e&#8209;02 |
| 285.2     | Anemia of chronic disease                                     | 39,673        | 2,606   | 1.64e&#8209;02 |
| 502       | Postinflammatory pulmonary fibrosis                           | 42,396        | 1,723   | 1.77e&#8209;02 |
| 415.1     | Acute pulmonary heart disease                                 | 49,887        | 1,857   | 1.88e&#8209;02 |
| 285.21    | Anemia in chronic kidney disease                              | 38,616        | 1,549   | 2.53e&#8209;02 |
| 585.3     | Chronic renal failure [CKD]                                   | 49,204        | 7,737   | 2.62e&#8209;02 |
| 743       | Osteoporosis, osteopenia and pathological fracture            | 55,165        | 11,990  | 2.87e&#8209;02 |
| 415.11    | Pulmonary embolism and infarction, acute                      | 49,867        | 1,837   | 3.04e&#8209;02 |
| 577       | Diseases of pancreas                                          | 60,538        | 1,795   | 3.06e&#8209;02 |
| 585.1     | Acute renal failure                                           | 46,803        | 5,336   | 3.23e&#8209;02 |
| 195       | Cancer, suspected or other                                    | 50,040        | 2,250   | 3.27e&#8209;02 |
| 289.4     | Lymphadenitis                                                 | 47,564        | 3,078   | 3.67e&#8209;02 |
| 440.2     | Atherosclerosis of the extremities                            | 45,524        | 3,046   | 4.52e&#8209;02 |

Table: Significant trait associations of LV54 in eMERGE. {#tbl:sup:emerge_assocs:lv54}
<!-- LV54:emerge_traits_assocs:end -->


### LV847

![
**Cell types for LV847.**
](images/lvs_analysis/lv847/lv847-cell_types.svg "Cell types for LV847"){#fig:sup:lv847 width="80%"}

<!-- LV847:multiplier_pathways:start -->
| Pathway                           | AUC   | FDR      |
|:----------------------------------|:------|:---------|
| KEGG SYSTEMIC LUPUS ERYTHEMATOSUS | 0.74  | 1.86e-04 |
| REACTOME MEIOTIC RECOMBINATION    | 0.78  | 3.60e-04 |
| REACTOME RNA POL I TRANSCRIPTION  | 0.75  | 5.56e-04 |
| REACTOME AMYLOIDS                 | 0.76  | 2.17e-03 |

Table: Pathways aligned to LV847 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv847}
<!-- LV847:multiplier_pathways:end -->

<!-- LV847:phenomexcan_traits_assocs:start -->
| Trait description                                                                          | Sample size   | Cases   | Partition / cluster   | FDR            |
|:-------------------------------------------------------------------------------------------|:--------------|:--------|:----------------------|:---------------|
| Mean corpuscular haemoglobin                                                               | 350,472       |         | 29 / 2                | 7.34e&#8209;73 |
| Mean corpuscular volume                                                                    | 350,473       |         | 29 / 2                | 1.43e&#8209;50 |
| Blood pressure medication (females)                                                        | 193,148       | 33,519  | 29 / 17               | 1.38e&#8209;18 |
| Heart attack, angina, stroke or hypertension                                               | 360,420       | 253,565 | 29 / 17               | 2.92e&#8209;15 |
| hypertension                                                                               | 360,420       | 97,139  | 29 / 17               | 4.82e&#8209;14 |
| hypertension (self-reported)                                                               | 361,141       | 93,560  | 29 / 17               | 1.02e&#8209;13 |
| Medication: bendroflumethiazide                                                            | 361,141       | 20,196  | 29 / 17               | 1.06e&#8209;08 |
| Mean sphered cell volume                                                                   | 344,729       |         | 29 / 2                | 2.16e&#8209;08 |
| Blood pressure medication (males)                                                          | 165,340       | 40,987  | 29 / 17               | 1.14e&#8209;07 |
| Medication for cholesterol, blood pressure, diabetes, or take exogenous hormones (females) | 193,148       | 133,338 | 29 / 17               | 1.21e&#8209;06 |
| Diastolic blood pressure, automated reading                                                | 340,162       |         | 29 / 17               | 2.93e&#8209;06 |
| Medication for cholesterol, blood pressure or diabetes (males)                             | 165,340       | 110,372 | 29 / 17               | 5.01e&#8209;06 |
| Mean reticulocyte volume                                                                   | 344,728       |         | 29 / 2                | 8.38e&#8209;03 |

Table: Significant trait associations of LV847 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv847}
<!-- LV847:phenomexcan_traits_assocs:end -->

<!-- LV847:emerge_traits_assocs:start -->
| Phecode   | Trait description                                                                    | Sample size   | Cases   | FDR            |
|:----------|:-------------------------------------------------------------------------------------|:--------------|:--------|:---------------|
| 585.32    | End stage renal disease                                                              | 43,309        | 1,842   | 3.11e&#8209;08 |
| 443       | Peripheral vascular disease                                                          | 47,867        | 5,389   | 4.13e&#8209;06 |
| 442.1     | Aortic aneurysm                                                                      | 45,589        | 3,111   | 1.01e&#8209;05 |
| 411.3     | Angina pectoris                                                                      | 43,503        | 4,382   | 4.28e&#8209;05 |
| 440.2     | Atherosclerosis of the extremities                                                   | 45,524        | 3,046   | 6.57e&#8209;05 |
| 415.11    | Pulmonary embolism and infarction, acute                                             | 49,867        | 1,837   | 9.90e&#8209;05 |
| 416       | Cardiomegaly                                                                         | 53,289        | 5,259   | 1.34e&#8209;04 |
| 415.1     | Acute pulmonary heart disease                                                        | 49,887        | 1,857   | 1.49e&#8209;04 |
| 599.3     | Dysuria                                                                              | 42,858        | 3,581   | 1.74e&#8209;04 |
| 585       | Renal failure                                                                        | 51,437        | 9,970   | 3.90e&#8209;04 |
| 411       | Ischemic Heart Disease                                                               | 54,275        | 15,154  | 1.19e&#8209;03 |
| 531       | Peptic ulcer (excl. esophageal)                                                      | 59,472        | 1,561   | 2.26e&#8209;03 |
| 250.6     | Polyneuropathy in diabetes                                                           | 41,948        | 1,675   | 2.32e&#8209;03 |
| 443.9     | Peripheral vascular disease, unspecified                                             | 46,926        | 4,448   | 2.40e&#8209;03 |
| 519       | Other diseases of respiratory system, not elsewhere classified                       | 56,909        | 2,056   | 2.43e&#8209;03 |
| 401.2     | Hypertensive heart and/or renal disease                                              | 30,405        | 6,253   | 2.43e&#8209;03 |
| 411.8     | Other chronic ischemic heart disease, unspecified                                    | 44,123        | 5,002   | 2.71e&#8209;03 |
| 440.22    | Atherosclerosis of native arteries of the extremities with intermittent claudication | 44,639        | 2,161   | 2.97e&#8209;03 |
| 401.22    | Hypertensive chronic kidney disease                                                  | 28,944        | 4,792   | 5.61e&#8209;03 |
| 514       | Abnormal findings examination of lungs                                               | 54,668        | 6,549   | 6.96e&#8209;03 |
| 427.6     | Premature beats                                                                      | 31,575        | 2,453   | 1.27e&#8209;02 |
| 585.1     | Acute renal failure                                                                  | 46,803        | 5,336   | 1.39e&#8209;02 |
| 418       | Nonspecific chest pain                                                               | 51,082        | 17,765  | 1.39e&#8209;02 |
| 250.1     | Type 1 diabetes                                                                      | 42,723        | 2,450   | 1.44e&#8209;02 |
| 285.21    | Anemia in chronic kidney disease                                                     | 38,616        | 1,549   | 1.82e&#8209;02 |
| 368       | Visual disturbances                                                                  | 56,141        | 2,694   | 1.88e&#8209;02 |
| 427.5     | Arrhythmia (cardiac) NOS                                                             | 36,861        | 7,739   | 2.01e&#8209;02 |
| 687.1     | Rash and other nonspecific skin eruption                                             | 47,039        | 4,964   | 2.15e&#8209;02 |
| 185       | Cancer of prostate                                                                   | 52,630        | 2,815   | 2.31e&#8209;02 |
| 747       | Cardiac and circulatory congenital anomalies                                         | 59,494        | 2,167   | 2.47e&#8209;02 |
| 444       | Arterial embolism and thrombosis                                                     | 43,378        | 900     | 2.53e&#8209;02 |
| 585.3     | Chronic renal failure [CKD]                                                          | 49,204        | 7,737   | 2.53e&#8209;02 |
| 440       | Atherosclerosis                                                                      | 47,471        | 4,993   | 2.62e&#8209;02 |
| 591       | Urinary tract infection                                                              | 49,727        | 10,016  | 2.94e&#8209;02 |
| 411.1     | Unstable angina (intermediate coronary syndrome)                                     | 41,763        | 2,642   | 3.06e&#8209;02 |
| 285.2     | Anemia of chronic disease                                                            | 39,673        | 2,606   | 3.06e&#8209;02 |
| 274.1     | Gout                                                                                 | 59,252        | 3,394   | 3.23e&#8209;02 |
| 585.34    | Chronic Kidney Disease, Stage IV                                                     | 43,322        | 1,855   | 3.84e&#8209;02 |
| 452       | Other venous embolism and thrombosis                                                 | 40,476        | 3,816   | 4.49e&#8209;02 |
| 427.12    | Paroxysmal ventricular tachycardia                                                   | 31,154        | 2,032   | 4.52e&#8209;02 |

Table: Significant trait associations of LV847 in eMERGE. {#tbl:sup:emerge_assocs:lv847}
<!-- LV847:emerge_traits_assocs:end -->


### LV136

![
**Cell types for LV136.**
<!--  -->
Pulmonary microvascular endothelial cells were exposed to hypoxia for 24 hours or more [@url:https://www.ncbi.nlm.nih.gov/bioproject/PRJNA232177];
](images/lvs_analysis/lv136/lv136-cell_types.svg "Cell types for LV136"){#fig:sup:lv136 width="80%"}

<!-- LV136:multiplier_pathways:start -->
| Pathway                       | AUC   | FDR      |
|:------------------------------|:------|:---------|
| PID INTEGRIN1 PATHWAY         | 0.88  | 9.35e-06 |
| KEGG ECM RECEPTOR INTERACTION | 0.80  | 7.29e-05 |
| REACTOME COLLAGEN FORMATION   | 0.87  | 2.00e-04 |
| REACTOME MUSCLE CONTRACTION   | 0.75  | 1.49e-02 |

Table: Pathways aligned to LV136 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv136}
<!-- LV136:multiplier_pathways:end -->

<!-- LV136:phenomexcan_traits_assocs:start -->
| Trait description                                  | Sample size   | Cases   | Partition / cluster   | FDR            |
|:---------------------------------------------------|:--------------|:--------|:----------------------|:---------------|
| 3mm strong meridian (right)                        | 75,410        |         | 29 / 10               | 6.37e&#8209;11 |
| 6mm strong meridian (left)                         | 65,551        |         | 29 / 10               | 1.53e&#8209;09 |
| 6mm strong meridian (right)                        | 66,256        |         | 29 / 10               | 1.78e&#8209;09 |
| 3mm strong meridian (left)                         | 75,398        |         | 29 / 10               | 9.90e&#8209;09 |
| Coronary Artery Disease                            | 184,305       | 60,801  | 29 / 11               | 1.26e&#8209;08 |
| 3mm weak meridian (right)                          | 75,410        |         | 29 / 10               | 1.26e&#8209;08 |
| 6mm weak meridian (right)                          | 66,256        |         | 29 / 10               | 2.41e&#8209;08 |
| 3mm weak meridian (left)                           | 75,398        |         | 29 / 10               | 3.96e&#8209;08 |
| 6mm weak meridian (left)                           | 65,551        |         | 29 / 10               | 9.31e&#8209;08 |
| Coronary atherosclerosis                           | 361,194       | 14,334  | 29 / 14               | 3.04e&#8209;06 |
| Ischaemic heart disease (wide definition)          | 361,194       | 20,857  | 29 / 14               | 5.71e&#8209;06 |
| Heart attack                                       | 360,420       | 8,288   | 29 / 14               | 2.36e&#8209;04 |
| Myocardial infarction                              | 361,194       | 7,018   | 29 / 14               | 5.20e&#8209;04 |
| Acute myocardial infarction (ICD10 I21)            | 361,194       | 5,948   | 29 / 14               | 8.14e&#8209;04 |
| heart attack/myocardial infarction (self-reported) | 361,141       | 8,239   | 29 / 14               | 1.16e&#8209;03 |
| Major coronary heart disease event                 | 361,194       | 10,157  | 29 / 14               | 1.47e&#8209;02 |

Table: Significant trait associations of LV136 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv136}
<!-- LV136:phenomexcan_traits_assocs:end -->

<!-- LV136:emerge_traits_assocs:start -->
| Phecode   | Trait description            | Sample size   | Cases   | FDR            |
|:----------|:-----------------------------|:--------------|:--------|:---------------|
| 747.1     | Cardiac congenital anomalies | 59,198        | 1,871   | 1.57e&#8209;01 |
| 411.4     | Coronary atherosclerosis     | 52,836        | 13,715  | 1.60e&#8209;01 |

Table: Trait associations of LV136 in eMERGE. {#tbl:sup:emerge_assocs:lv136}
<!-- LV136:emerge_traits_assocs:end -->


### LV93

![
**Cell types for LV93.**
<!--  -->
](images/lvs_analysis/lv93/lv93-cell_types.svg "Cell types for LV93"){#fig:sup:lv93 width="80%"}

<!-- LV93:multiplier_pathways:start -->
| Pathway                            | AUC   | FDR   |
|:-----------------------------------|:------|:------|
| No pathways significantly enriched |       |       |

Table: Pathways aligned to LV93 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv93}
<!-- LV93:multiplier_pathways:end -->

<!-- LV93:phenomexcan_traits_assocs:start -->
| Trait description                          | Sample size   | Cases   | Partition / cluster   | FDR            |
|:-------------------------------------------|:--------------|:--------|:----------------------|:---------------|
| CH2DB NMR                                  | 24,154        |         | 29 / 16               | 5.91e&#8209;24 |
| Reticulocyte Count                         | 173,480       |         | 29 / 4                | 1.33e&#8209;14 |
| High light scatter reticulocyte count      | 344,729       |         | 29 / 4                | 2.52e&#8209;13 |
| Reticulocyte count                         | 344,729       |         | 29 / 4                | 1.35e&#8209;12 |
| Reticulocyte percentage                    | 344,728       |         | 29 / 4                | 4.93e&#8209;11 |
| High light scatter reticulocyte percentage | 344,729       |         | 29 / 4                | 2.18e&#8209;10 |
| Immature reticulocyte fraction             | 344,728       |         | 29 / 4                | 2.31e&#8209;08 |
| Chronotype                                 | 128,266       |         | 29 / 16               | 9.73e&#8209;04 |
| HDL Cholesterol NMR                        | 19,270        |         | 29 / 16               | 2.41e&#8209;03 |

Table: Significant trait associations of LV93 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv93}
<!-- LV93:phenomexcan_traits_assocs:end -->

<!-- LV93:emerge_traits_assocs:start -->
| Phecode   | Trait description                  | Sample size   | Cases   | FDR            |
|:----------|:-----------------------------------|:--------------|:--------|:---------------|
| 208       | Benign neoplasm of colon           | 55,694        | 8,597   | 1.39e&#8209;02 |
| 440.2     | Atherosclerosis of the extremities | 45,524        | 3,046   | 2.87e&#8209;02 |

Table: Significant trait associations of LV93 in eMERGE. {#tbl:sup:emerge_assocs:lv93}
<!-- LV93:emerge_traits_assocs:end -->


### LV206

![
**Cell types for LV206.**
<!--  -->
](images/lvs_analysis/lv206/lv206-cell_types.svg "Cell types for LV206"){#fig:sup:lv206 width="80%"}

<!-- LV206:multiplier_pathways:start -->
| Pathway                            | AUC   | FDR   |
|:-----------------------------------|:------|:------|
| No pathways significantly enriched |       |       |

Table: Pathways aligned to LV206 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv206}
<!-- LV206:multiplier_pathways:end -->

<!-- LV206:phenomexcan_traits_assocs:start -->
| Trait description   | Sample size   | Cases   | Partition / cluster   | FDR            |
|:--------------------|:--------------|:--------|:----------------------|:---------------|
| CH2DB NMR           | 24,154        |         | 29 / 16               | 5.04e&#8209;21 |
| HDL Cholesterol NMR | 19,270        |         | 29 / 16               | 5.20e&#8209;03 |

Table: Significant trait associations of LV206 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv206}
<!-- LV206:phenomexcan_traits_assocs:end -->

<!-- LV206:emerge_traits_assocs:start -->
| Phecode   | Trait description            | Sample size   | Cases   | FDR            |
|:----------|:-----------------------------|:--------------|:--------|:---------------|
| 458       | Hypotension                  | 51,341        | 4,432   | 3.06e&#8209;02 |
| 286.9     | Abnormal coagulation profile | 48,006        | 800     | 3.39e&#8209;02 |
| 458.9     | Hypotension NOS              | 50,150        | 3,241   | 3.58e&#8209;02 |
| 428.2     | Heart failure NOS            | 48,178        | 3,584   | 3.71e&#8209;02 |

Table: Significant trait associations of LV206 in eMERGE. {#tbl:sup:emerge_assocs:lv206}
<!-- LV206:emerge_traits_assocs:end -->


### LV260

![
**Cell types for LV260.**
<!--  -->
](images/lvs_analysis/lv260/lv260-cell_types.svg "Cell types for LV260"){#fig:sup:lv260 width="80%"}

<!-- LV260:multiplier_pathways:start -->
| Pathway                            | AUC   | FDR   |
|:-----------------------------------|:------|:------|
| No pathways significantly enriched |       |       |

Table: Pathways aligned to LV260 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv260}
<!-- LV260:multiplier_pathways:end -->

<!-- LV260:phenomexcan_traits_assocs:start -->
| Trait description   | Sample size   | Cases   | Partition / cluster   | FDR            |
|:--------------------|:--------------|:--------|:----------------------|:---------------|
| CH2DB NMR           | 24,154        |         | 29 / 16               | 4.35e&#8209;17 |
| HDL Cholesterol NMR | 19,270        |         | 29 / 16               | 1.88e&#8209;02 |

Table: Significant trait associations of LV260 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv260}
<!-- LV260:phenomexcan_traits_assocs:end -->

<!-- LV260:emerge_traits_assocs:start -->
| Phecode   | Trait description   | Sample size   | Cases   | FDR            |
|:----------|:--------------------|:--------------|:--------|:---------------|
| 427.6     | Premature beats     | 31,575        | 2,453   | 7.90e&#8209;02 |

Table: Trait associations of LV260 in eMERGE. {#tbl:sup:emerge_assocs:lv260}
<!-- LV260:emerge_traits_assocs:end -->


### LV21

![
**Cell types for LV21.**
<!--  -->
](images/lvs_analysis/lv21/lv21-cell_types.svg "Cell types for LV21"){#fig:sup:lv21 width="80%"}

<!-- LV21:multiplier_pathways:start -->
| Pathway                            | AUC   | FDR   |
|:-----------------------------------|:------|:------|
| No pathways significantly enriched |       |       |

Table: Pathways aligned to LV21 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv21}
<!-- LV21:multiplier_pathways:end -->

<!-- LV21:phenomexcan_traits_assocs:start -->
| Trait description   | Sample size   | Cases   | Partition / cluster   | FDR            |
|:--------------------|:--------------|:--------|:----------------------|:---------------|
| Alzheimers Disease  | 54,162        | 17,008  | 29 / 16               | 1.11e&#8209;19 |
| LDL Cholesterol NMR | 13,527        |         | 29 / 16               | 9.53e&#8209;05 |
| Triglycerides NMR   | 21,559        |         | 29 / 16               | 1.74e&#8209;02 |

Table: Significant trait associations of LV21 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv21}
<!-- LV21:phenomexcan_traits_assocs:end -->

<!-- LV21:emerge_traits_assocs:start -->
| Phecode   | Trait description        | Sample size   | Cases   | FDR            |
|:----------|:-------------------------|:--------------|:--------|:---------------|
| 573       | Other disorders of liver | 47,826        | 2,524   | 2.99e&#8209;02 |
| 577       | Diseases of pancreas     | 60,538        | 1,795   | 5.51e&#8209;02 |

Table: Trait associations of LV21 in eMERGE. {#tbl:sup:emerge_assocs:lv21}
<!-- LV21:emerge_traits_assocs:end -->


### LV5

![
**Cell types for LV5.**
<!--  -->
](images/lvs_analysis/lv5/lv5-cell_types.svg "Cell types for LV5"){#fig:sup:lv5 width="80%"}

<!-- LV5:multiplier_pathways:start -->
| Pathway                            | AUC   | FDR   |
|:-----------------------------------|:------|:------|
| No pathways significantly enriched |       |       |

Table: Pathways aligned to LV5 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv5}
<!-- LV5:multiplier_pathways:end -->

<!-- LV5:phenomexcan_traits_assocs:start -->
| Trait description                                             | Sample size   | Cases   | Partition / cluster   | FDR            |
|:--------------------------------------------------------------|:--------------|:--------|:----------------------|:---------------|
| LDL Cholesterol NMR                                           | 13,527        |         | 29 / 16               | 1.44e&#8209;04 |
| Triglycerides NMR                                             | 21,559        |         | 29 / 16               | 4.03e&#8209;04 |
| Alzheimers Disease                                            | 54,162        | 17,008  | 29 / 16               | 2.47e&#8209;03 |
| Ever had prolonged feelings of sadness or depression          | 117,763       | 64,374  | 29 / 27               | 6.92e&#8209;03 |
| Medication for depression                                     | 117,763       | 28,351  | 29 / 27               | 8.24e&#8209;03 |
| Recent feelings of depression                                 | 117,656       |         | 29 / 27               | 1.05e&#8209;02 |
| Ever contemplated self-harm                                   | 117,610       |         | 29 / 27               | 1.50e&#8209;02 |
| Recent lack of interest or pleasure in doing things           | 117,757       |         | 29 / 27               | 1.65e&#8209;02 |
| Amount of alcohol drunk on a typical drinking day             | 108,256       |         | 29 / 27               | 2.77e&#8209;02 |
| Ever sought or received professional help for mental distress | 117,677       | 46,020  | 29 / 27               | 3.08e&#8209;02 |
| General happiness                                             | 117,442       |         | 29 / 27               | 3.73e&#8209;02 |
| Depression (diagnosed by a professional)                      | 117,782       | 25,087  | 29 / 27               | 4.03e&#8209;02 |

Table: Significant trait associations of LV5 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv5}
<!-- LV5:phenomexcan_traits_assocs:end -->

<!-- LV5:emerge_traits_assocs:start -->
| Phecode   | Trait description          | Sample size   | Cases   | FDR            |
|:----------|:---------------------------|:--------------|:--------|:---------------|
| 241       | Nontoxic nodular goiter    | 47,842        | 3,158   | 1.92e&#8209;02 |
| 241.1     | Nontoxic uninodular goiter | 47,125        | 2,441   | 6.84e&#8209;02 |

Table: Trait associations of LV5 in eMERGE. {#tbl:sup:emerge_assocs:lv5}
<!-- LV5:emerge_traits_assocs:end -->


### LV434

![
**Cell types for LV434.**
HEK293 is a cell line derived from human embryonic kidney cells;
3T3 is a cell line derived from mouse embryonic fibroblasts.
](images/lvs_analysis/lv434/lv434-cell_types.svg "Cell types for LV434"){#fig:sup:lv434 width="80%"}

<!-- LV434:multiplier_pathways:start -->
| Pathway                            | AUC   | FDR   |
|:-----------------------------------|:------|:------|
| No pathways significantly enriched |       |       |

Table: Pathways aligned to LV434 from the MultiPLIER models. {#tbl:sup:multiplier_pathways:lv434}
<!-- LV434:multiplier_pathways:end -->

<!-- LV434:phenomexcan_traits_assocs:start -->
| Trait description                        | Sample size   | Cases   | Partition / cluster   | FDR            |
|:-----------------------------------------|:--------------|:--------|:----------------------|:---------------|
| Attention Deficit Hyperactivity Disorder | 53,293        | 19,099  | 29 / 21               | 5.62e&#8209;03 |

Table: Significant trait associations of LV434 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv434}
<!-- LV434:phenomexcan_traits_assocs:end -->

<!-- LV434:emerge_traits_assocs:start -->
| Phecode   | Trait description                | Sample size   | Cases   | FDR            |
|:----------|:---------------------------------|:--------------|:--------|:---------------|
| 722       | Intervertebral disc disorders    | 47,659        | 7,458   | 1.44e&#8209;02 |
| 721       | Spondylosis and allied disorders | 47,517        | 7,316   | 1.64e&#8209;02 |
| 250.4     | Abnormal glucose                 | 45,220        | 4,947   | 2.23e&#8209;02 |
| 721.1     | Spondylosis without myelopathy   | 47,315        | 7,114   | 2.66e&#8209;02 |
| 720       | Spinal stenosis                  | 44,807        | 4,606   | 3.99e&#8209;02 |

Table: Significant trait associations of LV434 in eMERGE. {#tbl:sup:emerge_assocs:lv434}
<!-- LV434:emerge_traits_assocs:end -->
