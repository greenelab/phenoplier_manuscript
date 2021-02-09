---
author-meta:
- Milton Pividori
- Marylyn D. Ritchie
- Casey S. Greene
bibliography:
- content/manual-references.json
date-meta: '2021-02-09'
header-includes: '<!--

  Manubot generated metadata rendered from header-includes-template.html.

  Suggest improvements at https://github.com/manubot/manubot/blob/master/manubot/process/header-includes-template.html

  -->

  <meta name="dc.format" content="text/html" />

  <meta name="dc.title" content="Integrating transcriptome-wide association studies with gene co-expression patterns" />

  <meta name="citation_title" content="Integrating transcriptome-wide association studies with gene co-expression patterns" />

  <meta property="og:title" content="Integrating transcriptome-wide association studies with gene co-expression patterns" />

  <meta property="twitter:title" content="Integrating transcriptome-wide association studies with gene co-expression patterns" />

  <meta name="dc.date" content="2021-02-09" />

  <meta name="citation_publication_date" content="2021-02-09" />

  <meta name="dc.language" content="en-US" />

  <meta name="citation_language" content="en-US" />

  <meta name="dc.relation.ispartof" content="Manubot" />

  <meta name="dc.publisher" content="Manubot" />

  <meta name="citation_journal_title" content="Manubot" />

  <meta name="citation_technical_report_institution" content="Manubot" />

  <meta name="citation_author" content="Milton Pividori" />

  <meta name="citation_author_institution" content="Department of Systems Pharmacology and Translational Therapeutics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA" />

  <meta name="citation_author_orcid" content="0000-0002-3035-4403" />

  <meta name="twitter:creator" content="@miltondp" />

  <meta name="citation_author" content="Marylyn D. Ritchie" />

  <meta name="citation_author_institution" content="Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA" />

  <meta name="citation_author_orcid" content="0000-0002-1208-1720" />

  <meta name="twitter:creator" content="@MarylynRitchie" />

  <meta name="citation_author" content="Casey S. Greene" />

  <meta name="citation_author_institution" content="Center for Health AI, University of Colorado School of Medicine, Aurora, CO, 80045, USA" />

  <meta name="citation_author_institution" content="Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine, Aurora, CO, 80045, USA" />

  <meta name="citation_author_orcid" content="0000-0001-8713-9213" />

  <meta name="twitter:creator" content="@GreeneScientist" />

  <link rel="canonical" href="https://greenelab.github.io/phenoplier_manuscript/" />

  <meta property="og:url" content="https://greenelab.github.io/phenoplier_manuscript/" />

  <meta property="twitter:url" content="https://greenelab.github.io/phenoplier_manuscript/" />

  <meta name="citation_fulltext_html_url" content="https://greenelab.github.io/phenoplier_manuscript/" />

  <meta name="citation_pdf_url" content="https://greenelab.github.io/phenoplier_manuscript/manuscript.pdf" />

  <link rel="alternate" type="application/pdf" href="https://greenelab.github.io/phenoplier_manuscript/manuscript.pdf" />

  <link rel="alternate" type="text/html" href="https://greenelab.github.io/phenoplier_manuscript/v/e24fd8104cafffab9158dd91c2128dbd6a7f7bcc/" />

  <meta name="manubot_html_url_versioned" content="https://greenelab.github.io/phenoplier_manuscript/v/e24fd8104cafffab9158dd91c2128dbd6a7f7bcc/" />

  <meta name="manubot_pdf_url_versioned" content="https://greenelab.github.io/phenoplier_manuscript/v/e24fd8104cafffab9158dd91c2128dbd6a7f7bcc/manuscript.pdf" />

  <meta property="og:type" content="article" />

  <meta property="twitter:card" content="summary_large_image" />

  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />

  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />

  <meta name="theme-color" content="#ad1457" />

  <!-- end Manubot generated metadata -->'
keywords:
- gene co-expression
- transfer learning
- MultiPLIER
- PhenomeXcan
- TWAS
lang: en-US
manubot-clear-requests-cache: false
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
title: Integrating transcriptome-wide association studies with gene co-expression patterns
...





[
<i class="fas fa-info-circle fa-lg"></i> **Draft manuscript**<br>
Text in <span style="color: red">red</span> or with <span class="red">red</span> background are internal comments
]{.banner .lightblue}


<small><em>
This manuscript
([permalink](https://greenelab.github.io/phenoplier_manuscript/v/e24fd8104cafffab9158dd91c2128dbd6a7f7bcc/))
was automatically generated
from [greenelab/phenoplier_manuscript@e24fd81](https://github.com/greenelab/phenoplier_manuscript/tree/e24fd8104cafffab9158dd91c2128dbd6a7f7bcc)
on February 9, 2021.
</em></small>

## Authors



+ **Milton Pividori**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon}
    [0000-0002-3035-4403](https://orcid.org/0000-0002-3035-4403)
    · ![GitHub icon](images/github.svg){.inline_icon}
    [miltondp](https://github.com/miltondp)
    · ![Twitter icon](images/twitter.svg){.inline_icon}
    [miltondp](https://twitter.com/miltondp)<br>
  <small>
     Department of Systems Pharmacology and Translational Therapeutics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA
     · Funded by The Gordon and Betty Moore Foundation GBMF 4552; The National Human Genome Research Institute (R01 HG010067)
  </small>

+ **Marylyn D. Ritchie**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon}
    [0000-0002-1208-1720](https://orcid.org/0000-0002-1208-1720)
    · ![Twitter icon](images/twitter.svg){.inline_icon}
    [MarylynRitchie](https://twitter.com/MarylynRitchie)<br>
  <small>
     Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA
  </small>

+ **Casey S. Greene**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon}
    [0000-0001-8713-9213](https://orcid.org/0000-0001-8713-9213)
    · ![GitHub icon](images/github.svg){.inline_icon}
    [cgreene](https://github.com/cgreene)
    · ![Twitter icon](images/twitter.svg){.inline_icon}
    [GreeneScientist](https://twitter.com/GreeneScientist)<br>
  <small>
     Center for Health AI, University of Colorado School of Medicine, Aurora, CO, 80045, USA; Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine, Aurora, CO, 80045, USA
     · Funded by The Gordon and Betty Moore Foundation (GBMF 4552); The National Human Genome Research Institute (R01 HG010067); The National Cancer Institute (R01 CA237170)
  </small>



## Abstract {.page_break_before}




## Results


### Integrating gene expression patterns with transcription-wide association studies

::: {style="color: red"}
Here we introduce our framework to perform the integration.

 1. Brief background on MultiPLIER and PhenomeXcan.
 1. Explanation of the framework depicted in Figure @fig:entire_process and its components.
 1. Description of initial set of results matching previous findings (neutrophil counts).
:::


![
**Schematic of the PhenoPLIER framework.**
<!--  -->
The integration process (middle) between MultiPLIER [@doi:10.1016/j.cels.2019.04.003] (top) and
PhenomeXcan [@doi:10.1101/833210] (bottom) outputs matrix $\mathbf{T}$. LV603 was previously
found to be strongly associated with neutrophil estimates when projecting a dataset of systemic
lupus erythematosus (SLE) whole blood (WB) into MultiPLIER. After integration, this LV is also
highly associated with blood count traits, with neutrophil counts at the top.
<!--  -->
](images/entire_process/entire_process.svg?sanitize=true "PhenoPLIER
framework"){#fig:entire_process height=5in}


### Projecting associations into a gene expression latent space reveals expected and novel trait clusters

::: {style="color: red"}
In this section, we already introduced some evidence that the proposal could work. The next step
(this section) is to cluster traits using the LVs as features.

1. Briefly explain idea of clustering traits using LVs.
1. Explain methods here, and then we see whether that should be moved elsewhere.
    1. Dimentionality reduction using UMAP.
    1. Spectral clustering approach.
    1. Stability measure to detect best number of clusters.
    1. Approach to interpret clusters by training a decision tree classifier.
1. We should have a set of expected results. For instance:
    1. Keratometry measurements are clustered together.
    1. Heel bone mineral density are also clustered together.
    1. See other clusters.
1. We should also include some "novel" clusters, or expected clusters with some novel traits in it.
    1. Lipids cluster? I'm working on this now.
1. Once we focus on a cluster, we provide an interpreation of why those traits are clustered
   together (which LVs are driving the association). Here we'll need to explain the method we might
   be using for this (decision trees on the original data). This could be a separate section.
:::


![
**Clustering of traits using matrix $\mathbf{T}^{\top}$.**
<!--  -->
Estimation of number of clusters using the consensus index method [@Vinh2010]. A spectral clustering
approach was used on matrix $\mathbf{T}^{\top}$ to group traits. The algorithm was run 100 times for
each $k$ value from 2 to 20, and the averaged adjusted Rand-index is reported in $y$-axis (top). A
partition with $k=13$ was obtained from $\mathbf{T}^{\top}$ (bottom), where ketatometry and heel
bone mineral density measurements clearly separate from the rest of traits. `Add svg version`{.red}
<!--  -->
](images/lvs_clustering/traits_clustering.png "Traits partition with k=13"){#fig:traits_clusters
height=5in}


![
**The top discriminating latent variables for the keratometry cluster.**
<!--  -->
For clustering interpretation, a decision tree classifier was trained using the original data
($\mathbf{T}^{\top}$), the keratometry cluster as positive class, and the rest of traits as
negative class. The top associated latent variable was LV136, followed by LV767 and LV612 (which
were detected by removing LV136 and LV767 from the training data, respectively).
<!--  -->
`Add svg version.`{.red}
<!--  -->
](images/lvs_clustering/traits_clustering_features.png "Features discriminating keratometry
cluster"){#fig:kera_features height=5.5in}


### Analysis of keratometry cluster reveals groups of genes associated with cardiovascular-related traits

::: {style="color: red"}
In this section, we build on our previous results to analyze a single or a couple of LVs. The idea
is to show raw MultiXcan/fastENLOC results and how individual genes in the module are associated
with the traits. Based on this, we could provide an interpretation (if possible) on how genes could
be affecting different and related traits/diseases.

These are some articles I found relating the trait categories in Figure @fig:lv136_traits (LV136).

1. Ocular problems and cardiovascular diseases:
    1. [(2017) The Relationship Between Cardiovascular Autonomic Dysfunction and Ocular Abnormality
       in Chinese T2DM](https://doi.org/10.1155/2017/7125760)
    1. [(2018) Looking into the eye of patients with chronic obstructive pulmonary disease: an
       opportunity for better microvascular profiling of these complex
       patients](https://doi.org/10.1111/aos.13765)
        1. This one also relates spirometry.
    1. [(2018) Residual Vision Activation and the Brain-Eye-Vascular Triad: Dysregulation,
       Plasticity and Restoration in Low Vision and Blindness - A
       Review](https://doi.org/10.3233/rnn-180880)
    1. [(2017) Evaluating Ocular Blood Flow](https://doi.org/10.4103/ijo.ijo_330_17)
1. Spirometry and CVD:
    1. [(2019) Mysterious link between the restrictive ventilatory impairment in spirometry and
       cardiovascular disease](https://doi.org/10.1016/j.resinv.2019.01.006)
    1. [(2018) Declining Lung Function and Cardiovascular
       Risk](https://doi.org/10.1016/j.jacc.2018.06.049)
    1. [(2018) Restrictive Spirometry and Cardiovascular Risk: Cause or
       Comorbidity?](https://doi.org/10.1513/AnnalsATS.201807-494ED)
    1. [(2011) Assessment of pulmonary function tests in cardiac
       patients](https://doi.org/10.1016/j.jsha.2011.01.003)
    1. It would be nice to see if the direction of effect of these genes are positive for CVD and
       negative for FEV1.
:::


![
**Traits and diseases associated with top genes in LV136.**
<!--  -->
Categories of the top 40 traits associated with genes in LV136 (left), and associations of traits
with the top 20 genes in LV136 (right): S-MultiXcan associations ($-\log_{10}(p\mathrm{-value})$,
thresholded at 10) are shown with gradients, whereas fastENLOC colocalization probabilities are
depicted with different circle sizes (only for $>5\mathrm{\%}$). Colors used for trait categories
are the same in both subfigures.
<!--  -->
](images/lvs_analysis/lv136/lv136_traits_multixcan_fastenloc.svg "Traits/diseases associated with
LV136 in PhenoPLIER"){#fig:lv136_traits}


![
**Cell types found in top five studies (recount2) associated with LV136.**
<!--  -->
Genes associated with LV136 are highly expressed in MSC, osteoblast and fibroblast when considering
all conditions for the given cell types in the top five studies in recount2.
<!--  -->
MSC: mesenchymal stem cells; iPSC: induced pluripotent stem cells; ESC: embryonic stem cells.
<!--  -->
`We should consider more studies maybe, not just the top 5.`{.red}
`Remove colors.`{.red}
<!--  -->
](images/lvs_analysis/lv136/lv136_cell_types.svg "Conditions associated with LV136 in
PhenoPLIER"){#fig:lv136_conditions height=3in}


### Clustering of LVs (gene modules) with similar trait associations

::: {style="color: red"}
I'm not sure if it's a good idea to include this, but I leave it here just in case.

The idea here is to cluster LVs by seeing how are they associated with different traits. So, taking
the keratometry cluster shown before as an example, here LV136, LV767, LV612 (and possibly others)
would be clustered together. The use case would be to start from a trait of interest and see the
cluster of LVs associated with it.
:::


### Drugs associated with gene modules

::: {style="color: red"}
This section includes the projection of Connectivity Map into the MultiPLIER space.
:::


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
