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

  <link rel="alternate" type="text/html" href="https://greenelab.github.io/phenoplier_manuscript/v/8520e8669798beffeffa36a22c5874a5cda29fed/" />

  <meta name="manubot_html_url_versioned" content="https://greenelab.github.io/phenoplier_manuscript/v/8520e8669798beffeffa36a22c5874a5cda29fed/" />

  <meta name="manubot_pdf_url_versioned" content="https://greenelab.github.io/phenoplier_manuscript/v/8520e8669798beffeffa36a22c5874a5cda29fed/manuscript.pdf" />

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
Text in <span style="color: red">red</span>/<span class="red">red</span> are internal comments
]{.banner .lightblue}


<small><em>
This manuscript
([permalink](https://greenelab.github.io/phenoplier_manuscript/v/8520e8669798beffeffa36a22c5874a5cda29fed/))
was automatically generated
from [greenelab/phenoplier_manuscript@8520e86](https://github.com/greenelab/phenoplier_manuscript/tree/8520e8669798beffeffa36a22c5874a5cda29fed)
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

<!--

Some papers that might be interesting:

https://www.nature.com/articles/s41591-020-01221-5
Air pollution linked to neurodegeneration markers

-->


### PhenoPLIER integrates TWAS with gene co-expression patterns

![
**Schematic of the PhenoPLIER framework.**
<!--  -->
**a)** The integration process between gene co-expression patterns from
MultiPLIER [@doi:10.1016/j.cels.2019.04.003] (top) and TWAS results from
PhenomeXcan [@doi:10.1126/sciadv.aba2083]. PhenoPLIER projects gene-based
association results on \~4,000 traits to a latent space learned from a
large gene expression compendium (recount2 [@doi:10.1038/nbt.3838]). This
generates matrix $\mathbf{\hat{M}}$, where each trait is now described by
latent variables/gene modules.
<!--  -->
**b)** After the integration process, we found that neutrophil counts and other
white blood cells (bottom) were ranked among the top 10 traits for an LV that
was termed a neutrophil signature in the original MultiPLIER study. Genes in
this LV were found to be expressed in related cell types (top).
`Improve cell types/tissues figure`{.red}
<!--  -->
](images/entire_process/entire_process.svg "PhenoPLIER
framework"){#fig:entire_process width="100%"}


MultiPLIER [@doi:10.1016/j.cels.2019.04.003] is a recent computational strategy
that extracts patterns of co-expressed genes from large gene expression
datasets. The approach uses an unsupervised matrix factorization method that was
employed to extract latent variables from recount2 [@doi:10.1038/nbt.3838].
<!--  -->
The latent variables (LVs), essentially gene modules, then revealed biological
processes associated with disease severity in rare disease datasets that were
too small for effective model training. These gene sets aligned well with known
biological pathways and predicted cell type composition, even though the
approach was not explicitly designed for this goal.


Although the authors showed that certain patterns learned by MultiPLIER resemble
known biology, most of the LVs identified are completely unknown. Since genes in
these modules vary together in certain cell types and tissues, it's expected
that they may also function together [@doi:10.1186/1471-2164-7-187;
@doi:10.1186/s13059-019-1835-8].
<!--  -->
To test whether patterns in the expression space match those in the TWAS space,
we used PhenomeXcan [@doi:10.1126/sciadv.aba2083], a massive transcriptome-wide
association studies (TWAS) resource obtained from the UK Biobank
[@doi:10.1038/s41586-018-0579-z] and other cohorts (Figure @fig:entire_process
a). These results were projected to the low-dimensional gene representation
learned by MultiPLIER using:

$$\hat{\mathbf{M}} = (\mathbf{Z}^{\top} \mathbf{Z} + \lambda_{2} \mathbf{I})^{-1} \mathbf{Z}^{\top} \mathbf{M},$$ {#eq:proj}

where $\mathbf{M}^{n \times t}$ has gene-trait associations from MultiXcan
[@doi:10.1371/journal.pgen.1007889] (standardized effect sizes) for $n$ genes
and $t$ traits, $\mathbf{Z}^{n \times l}$ are the gene loadings with $l$ latent
variables, $\lambda_2$ is the regularization parameter used in the training
step, and $\hat{\mathbf{M}}^{l \times t}$ is finally the projection of
$\mathbf{M}$ into the latent space: all traits in PhenomeXcan are now described
by LVs, thus we can potentially infer the effects of gene modules on different
human traits. Since the MultiPLIER models also provide the conditions (such as
cell types and tissues) in which genes in a module are concurringly expressed,
our approach would also allow to infer the context in which the gene module
affects a trait or disease.


In the original MultiPLIER study [@doi:10.1016/j.cels.2019.04.003], the authors
found an LV significantly associated with previously known neutrophil gene-sets
and highly correlated with neutrophil estimates from gene expression.
<!--  -->
We analyzed this LV using our approach (Figure @fig:entire_process b), and found
that 1) neutrophil counts and other white blood cell traits from PhenomeXcan
[@doi:10.1126/sciadv.aba2083] were ranked among the top 10 traits for this LV,
and 2) that the genes in this LV are expressed in neuotrophil cells (see more
details in the supplementary material).
<!--  -->
These initial results strongly suggest that shared patterns exist in the gene
expression space (which has no GTEx samples) and the TWAS space (with gene
models trained using GTEx v8), and that the approach also allows to infer the
context-specific effects of gene modules on complex traits.
<!--  -->
We will also show how the approach can aid translational efforts by mapping
pharmacological perturbations to this latent space, enabling to observe which
compounds affect the transcriptional activity of gene modules.


::: {style="color: red"}
- Minor: LV603 is neutrophil-associated, but it is not significantly associated
  with other myeloid lineage cell types (see Figure S2A in MultiPLIER study).
  Maybe we can add a genes-traits figure of MultiXcan and fastENLOC results to
  see this better.
:::


### Clusters of traits in the gene module space are affected by shared transcriptional processes

![
**Cluster analysis on traits from PhenomeXcan.**
<!--  -->
**a)** The projection of TWAS results for 3,749 traits to the latent
representation learned from recount2 are the input data to the clustering
process. A linear (PCA) and non-linear (UMAP) dimensionality reduction
techniques are applied to the input data, and the three data versions are
processed by five different clustering algorithms. These algorithms derive
partitions from the data using different sets of parameters (such as the number
of clusters), leading to an ensemble of 4,428 partitions. A coassociation matrix
is derived by counting how many times a pair of traits were grouped together in
the ensemble. Finally, a consensus function is applied to the coassociation
matrix to generate consolidated partitions with different number of clusters.
These final solutions are represented in the clustering tree (Figure
@fig:clustering:tree).
<!--  -->
**b)** The clusters found by the consensus function are used as labels to train
a decision tree classifier on the original input data (latent representation),
which detects the most important LVs that differentiate groups of traits.
<!--  -->
](images/clustering/clustering_design.svg "Cluster analysis on
traits"){#fig:clusering:design width="100%"}


All traits in PhenomeXcan were projected into the latent space learned from
recount2 using Equation (@eq:proj). We conducted cluster analysis using this new
representation to find groups of traits that are similarly affected by the same
transcriptional processes.
<!--  -->
To avoid using a single clustering algorithm (which implies using a single
assumption about the structure of the data), we employed a consensus clustering
approach where different methods with varying sets parameters are applied on the
same data, and later combined into a consolidated solution
[@doi:10.1016/j.ins.2016.04.027; @doi:10.1109/TPAMI.2005.237; @Strehl2002]
(Figure @fig:clusering:design).
<!--  -->
An important property for a successful application of a consensus clustering
approach is the diversity of the ensemble, understood as the level of
disagreement between the base clustering solutions
[@doi:10.1016/j.ins.2016.04.027; @doi:10.1109/TPAMI.2011.84;
@doi:10.1016/j.patcog.2014.04.005]. A diverse set of solutions can be generated by
using different data representations (such as dimensionality reductions methods
or subsets of features), clustering algorithms with distinct assumptions
($k$-means, for instance, assumes hyperspherical clusters), and a varying set of
algorithm's parameters (such as the number of clusters or the initial random
seeds).
<!--  -->
In our approach, we performed cluster analysis using five different clustering
algorithms on three representations of the input data (the original data with
987 latent variables, its projection into the top 50 principal components, and
the embedding learned by UMAP [@arxiv:1802.03426] using 50 components) (see
Figure @fig:clusering:design a). The clustering methods used cover a wide range
of different assumptions on cluster shapes and a varying set of parameters such
as the number of clusters (from 2 to 60), the width of the Gaussian kernel in
spectral clustering, and other method-specific parameters (see the supplementary
material for more details).
<!--  -->
The process generated an ensemble with 4,428 clustering solutions for all
traits. This ensemble was used to derive a coassociation matrix between traits
by counting the number of times a pair of traits was clustered together.
Finally, a consensus function was applied on the coassociation matrix to derive
a consolidated solution using the information in the ensemble. For these final
partitions, we did not select a specific number of clusters, but instead used
a clustering tree [@doi:10.1093/gigascience/giy083] (Figure
@fig:clustering:tree) to examine how traits were grouped using multiple
resolutions.
<!--  -->
Finally, for the interpretation of the clusters, we trained a decision tree
classifier (a highly interpretable machine learning model) on the original
input data using the clusters found as labels. This approach allowed us to
quickly identify the most important gene modules for the groups of traits found.
<!--  -->
More details of the clustering process are available in the supplementary
material.


![
**Clustering tree using multiple resolutions.**
<!--  -->
Clustering tree of the consensus partitions at different resolutions (from 4 to
36 clusters). Each row represents a partition of the traits, and each circle is
a cluster from that partition where its size indicates the size of the cluster.
Arrows indicate how traits in one cluster move across clusters from different
resolutions.
<!--  -->
](images/clustering/clustering_tree.svg "Clustering tree using the
consensus solutions for traits"){#fig:clustering:tree width="100%"}


A clustering tree of the consensus solutions at different
resolutions is shown in Figure @fig:clustering:tree. For each $k$ (the number of
clusters), the consensus partition that maximized the agreement with the
ensemble was selected (see supplementary material). Since it is expected to find
a subset of resolutions that better represent the patterns among traits, we further
filtered the consensus partitions by taking those with an agreement value higher
than the median, which included partitions from 4 to 36 clusters.


The clusering tree shows four clear branches (from left to right):
bone-densitometry of heel and keratometry measurements (curvature of the corneal
surface), haematological assays on platelets and red blood cells, the
"complex" branch, and anthropometric traits.
<!--  -->
The complex branch includes stable clusters at different resolutions, such as 1)
white blood cell traits, 2) nutrients intake and diet-related, 3) cardiovascular
diseases (coronary artery disease, myocardial infarction, angina pectoris, among
others) and related medications, 4) mental health traits related to anxiety, 5)
asthma, allergic rhinitis, and atopic dermatitis, 6) schizophrenia, educational
outcomes and fluid intelligence score, 7) breath spirometry, 8) autoimmune
diseases (celiac disease, hypothyroidism, psoriasis, rheumatoid arthritis,
systemic lupus erythematosus, among others), 9) skin and hair color, and 10)
hypertension. In the following sections, we select some of these stable clusters
to analyze which transcriptional processes are specific to some groups of
traits.


#### Cardiovascular traits

::: {style="color: red"}
See if we are going to analyze this cluster.

The figures below include examples of the type of figure we can include here:

- Show the LVs that are distinct for this cluster (maybe a small decision tree
  for some of the clusters).
- For those LV, show which cell types/tissues are important (such as Figure
  @fig:lv136_conditions below).
- For some of these LVs, we can include the list of other traits also related
  and gene association results (such as Figure @fig:lv136_traits).
:::


![
**Cell types/tissues associated with genes in LV136.**
](images/lvs_analysis/lv136/lv136_cell_types.svg "Conditions associated with LV136 in
PhenoPLIER"){#fig:lv136_conditions width="50%"}


![
**Traits associated with genes in LV136.**
](images/lvs_analysis/lv136/lv136_traits_multixcan_fastenloc.svg "Traits/diseases associated with
LV136 in PhenoPLIER"){#fig:lv136_traits width="100%"}


#### Schizophrenia, educational attainment and intelligence

::: {style="color: red"}
See if we are going to analyze this cluster.
:::


#### Asthma and allergies

::: {style="color: red"}
See if we are going to analyze this cluster.
:::

<!-- ::: {style="color: red"}
Notes:

- this paper should be a good source to explain the asthma cluster:
https://www.nature.com/articles/ng.3985
::: -->


### Replication using Penn Medicine BioBank

::: {style="color: red"}
Maybe we can incorporate **Binglan's TWAS results on PMBB** and see if expected
traits-clusters are correctly predicted.
:::


<!-- #### Keratometry cluster reveals gene-sets associated with cardiovascular-related traits -->

<!-- 1. Ocular problems and cardiovascular diseases:
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
       negative for FEV1. -->


### PhenoPLIER improves drug-disease prediction

![
**Drug-disease prediction.**
<!--  -->
Explain.
<!--  -->
AUC: area under the curve; AP: average precision.
<!--  -->
](images/drug_disease_prediction/auc_pr.png "AUC-PR of drug-disease
associations"){#fig:drug_disease:auc_pr width="100%"}


We showed that the latent representation learned in a large gene expression data
set is helpful to link novel gene sets to complex diseases and the cell types
where they are expressed.
<!--  -->
We reasoned that this representation might be also useful to more
accurately predict the potential therapeutic effects of drugs. If the gene
patterns captured by MultiPLIER represent real and possibily unknown biological
pathways, then our approach might actually produce a more accurate estimation of
the effects of a perturbed molecular mechanisms on disease, and also how
pharmacological perturbations affect the process activity.
<!--  -->
This would, in addition to connecting gene modules with their context-specific
effects on complex traits, identify which compounds might provide an avenue to
alter a dysregulated process activity for therapeutical utility.


To test this hypothesis, we used a gold standard of drug-disease medical
indications [@doi:10.7554/eLife.26726; @doi:10.5281/zenodo.47664] to evaluate
and compare the prediction performance of both the original gene-disease
associations from PhenomeXcan, and its projection representing gene
module-disease associations.
<!--  -->
To test this, we used the transcriptional responses to small molecule
perturbations profiled in LINCS L1000 [@doi:10.1016/j.cell.2017.10.049], which
were further processed to obtain consensus signatures and map to DrubBank IDs
[@doi:10.1093/nar/gkt1068; @doi:10.7554/eLife.26726; @doi:10.5281/zenodo.47223].
<!--  -->
To compute a drug-disease score, we followed a similar procedure used previously
[@doi:10.1038/nn.4618] to anti-correlates gene-traits associations from TWAS and
expression profiles of drugs using their signed $z$-scores (see the
supplementary material). Here we used the dot product between gene-traits
$z$-scores and the consensus $z$-scores in LINCS L1000, which led to a score for
each drug-disease pair. (`Add more details?`{.red}).
<!--  -->
To obtain a drug-disease association for the gene module-mapped TWAS results, we
first projected LINCS L1000 data into this latent representation using Equation
(@eq:proj), thus leading to a matrix with the expression profiles of drugs
mapped to latent variables. This can be interpreted as the effects of compounds
on gene modules activity. Then, similarly as before, we anti-correlated gene
module-traits scores and module expression profiles of drugs.

`(Add number of drugs, diseases, and final number of mappings)`{.red}
<!--  -->
<!-- Both $\matr{D}$ and $\hat{\matr{D}}$ contain scores for 1170 drugs and 4091 traits,
which were further mapped to 56 unique Disease Ontology IDs. -->
<!--  -->
<!-- Then I assessed the performance of these two approaches using a manually curated list of
drug-disease associations~\autocite{Himmelstein2017, HimmelsteinPharmaDB2016}.
97 diseases and 601 compounds in PharmarcotherapyDB~\autocite{Himmelstein2017,
HimmelsteinPharmaDB2016},
which contains 755 disease-modifying therapies and 243
non-indications. After integrating this gold-standard list with the predictions, I
obtained 458 positive and 136 negative cases for evaluation.
-->


<!-- Finally, I obtained drug-disease predictions using both the original (gene-based) and
projected (gene module-based) associations: $\matr{D}=\matr{L}^{\top}\matr{M}$ and
$\hat{\matr{D}}=\hat{\matr{L}}^{\top}\hat{\matr{M}}$, respectively. -->
<!--  -->

The ROC and Precision-Recall (PR) curves comparing both approaches are shown in
Figure @fig:drug_disease:auc_pr. Notably, the gene module-based approach
proposed here clearly outperformed the gene-based one, with an area under the
curve (AUC) of 0.615 vs 0.573, and an average precision (AP) of 0.851 vs 0.841.
<!--  -->
This is particularly striking given that the projected TWAS results represent a
reduced or compressed version of the complete gene-based associations,
suggesting that a gene module perspective can be more informative, for instance,
for drug-repurposing scenarios using genetic studies.



::: {style="color: red"}
Another analysis here could be:

- Try the prediction again by keeping well-aligned LVs only. Do we get the same
  prediction performance?
:::

<!-- ::: {style="color: red"}
Papers to read:
- "SubtypeDrug: a software package for prioritization of candidate cancer
  subtype-specific drugs" https://doi.org/10.1093/bioinformatics/btab011 It
  might be interesting to see how the predict drug-disease associations when
  they say "evaluation of drug-disease reverse association"
::: -->


## Discussion


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>


## Supplementary material

### Pathway-level information extractor (PLIER)

MultiPLIER [@doi:10.1016/j.cels.2019.04.003], the computational strategy used in
this work, extracts patterns of co-expressed genes on large gene expression
datasets. MultiPLIER applies the pathway-level information extractor method
(PLIER) [@doi:10.1038/s41592-019-0456-1] to the recount2 data
[@doi:10.1038/nbt.3838], which performs unsupervised learning using prior
knowledge to reduce technical noise. Via a matrix factorization approach, PLIER
deconvolutes the gene expression data into a set of latent variables (LV) that
each represent a gene module (i.e. a set of genes with coordinated expression
patterns).

`COMPLETE`{.red}


### Top latent variables associated to neutrophils

![
**Correlation of neutrophil counts with top LVs associated with neutrophils traits.**
<!-- Description -->
](images/supplementary_material/lv603_neutrophils/neutrophils_top20_lvs.png "Top
20 LVs associated with neutrophils"){#fig:supp:neutrophils_top20lvs}

![
**Significance of neutrophil counts correlation.**
<!-- Description -->
](images/supplementary_material/lv603_neutrophils/significance_neutrophil.png "Significance of neutrophil counts
correlation"){#fig:supp:signif_neutrophils_counts height=3in}


### Consensus clustering of traits in PhenomeXcan

#### Dimensionality reduction

#### Ensemble creation: clustering algorithms and parameters

::: {style="color: red"}
- list of methods and its parameters
:::

#### Ensemble combination and consensus functions

::: {style="color: red"}
- evidence accumulation approach
- we also used a spectral clustering approach
- for each k, we picked the partition that maximized the agreement with the ensemble
- show figure where we select the ks that are greater than the median
:::


#### Clusters interpretation

::: {style="color: red"}
- we remove each LV and run the decision tree classifier again
:::


### Drug-disease predictions

::: {style="color: red"}
- anti-correlation using dot product of s-predixcan on all tissues and lincs
:::
