---
author-meta:
- Milton Pividori
- Marylyn D. Ritchie
- Casey S. Greene
bibliography:
- content/manual-references.json
date-meta: '2021-04-11'
header-includes: '<!--

  Manubot generated metadata rendered from header-includes-template.html.

  Suggest improvements at https://github.com/manubot/manubot/blob/master/manubot/process/header-includes-template.html

  -->

  <meta name="dc.format" content="text/html" />

  <meta name="dc.title" content="Integrating transcriptome-wide association studies with gene co-expression patterns" />

  <meta name="citation_title" content="Integrating transcriptome-wide association studies with gene co-expression patterns" />

  <meta property="og:title" content="Integrating transcriptome-wide association studies with gene co-expression patterns" />

  <meta property="twitter:title" content="Integrating transcriptome-wide association studies with gene co-expression patterns" />

  <meta name="dc.date" content="2021-04-11" />

  <meta name="citation_publication_date" content="2021-04-11" />

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

  <link rel="alternate" type="text/html" href="https://greenelab.github.io/phenoplier_manuscript/v/c62c48b60dcf10cc250c95f4d99722dd3f4c7c85/" />

  <meta name="manubot_html_url_versioned" content="https://greenelab.github.io/phenoplier_manuscript/v/c62c48b60dcf10cc250c95f4d99722dd3f4c7c85/" />

  <meta name="manubot_pdf_url_versioned" content="https://greenelab.github.io/phenoplier_manuscript/v/c62c48b60dcf10cc250c95f4d99722dd3f4c7c85/manuscript.pdf" />

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
([permalink](https://greenelab.github.io/phenoplier_manuscript/v/c62c48b60dcf10cc250c95f4d99722dd3f4c7c85/))
was automatically generated
from [greenelab/phenoplier_manuscript@c62c48b](https://github.com/greenelab/phenoplier_manuscript/tree/c62c48b60dcf10cc250c95f4d99722dd3f4c7c85)
on April 11, 2021.
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

<!-- 

 -->
 

## Introduction

<!--
# Things to remember:

1. There is some introduction in the BDS conference abstract, and also in the one for the CSHL that we didn't submit.

# Important papers

- Predicting genotype-specific gene regulatory networks
https://www.biorxiv.org/content/10.1101/2021.01.18.427134v1?rss=1
I like the ideas mentioned in the abstract and introduction of this paper.

- Identification of therapeutic targets from genetic association studies using hierarchical component analysis
Highly related paper.
See notes here https://drive.google.com/file/d/1C-6OGDxo3lG4_1b33prplsZ22r5hwjkq/view
Cite this paper about GWAS component, gene modules, and S-PrediXcan.
Some limitations of this method:
1. They find co-expression modules in GTEx only, we do it across recount2.
1. They use weighted correlation network analysis (WGCNA) to find modules,
   which seems simple.  We use PLIER with prior knowledge.
1. This is how they find a module: ``The eigen-gene component was then computed
   as the first principal component of the expression matrix of co-expressed
   genes''
1. ``Among 44 tissues analyzed, we generally detected 213±89 co-expression
   modules in one tissue.''
-->


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
**b)** After the integration process, we found that neutrophil counts and other white blood cells (bottom) were ranked among the top 10 traits for an LV that was termed a neutrophil signature in the original MultiPLIER study.
Genes in this LV were found to be expressed in relevant cell types (top).
<!--  -->
PMBC: `Explain`{.red}; mDCs: `Explain`{.red}.
<!--  -->
](images/entire_process/entire_process.svg "PhenoPLIER
framework"){#fig:entire_process width="100%"}


(`This paragraph has probably too much detail about MultiPLIER`{.red})
<!--  -->
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
human traits.
Since the MultiPLIER models also provide the experimental conditions (such as cell types and tissues) in which genes in a module are concurringly expressed, our approach would also allow inferring the context in which the gene module affects a trait or disease.


In the original MultiPLIER study [@doi:10.1016/j.cels.2019.04.003], the authors
found an LV significantly associated with previously known neutrophil gene-sets
and highly correlated with neutrophil estimates from gene expression.
<!--  -->
We analyzed this LV using our approach (Figure @fig:entire_process b), and found that
1) neutrophil counts and other white blood cell traits from PhenomeXcan [@doi:10.1126/sciadv.aba2083] were ranked among the top 10 traits for this LV,
and 2) that the genes in this LV are expressed in neutrophil cells (see more details in the supplementary material).
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


### Genes causally involved in lipids accumulation are associated with relevant traits and tissues

We found 492 genes associated with lipids accumulation by using a genome-wide lentiviral pooled CRISPR-Cas9 library targeting 19,114 genes in the human genome (see Methods).
From these, we identified two high-confidence gene-sets that either caused a decrease (96 genes) or an increase (175 genes) of lipids.
Next, we used these two gene-sets to assess whether singe gene-trait associations in PhenomeXcan recapitulated lipids-related traits.
We show that our gene module-based approach is more robust to identify genetic associations with lipids-relevant traits, and that it can be used to contextualize these results by identifing tissue and cell type-specific gene-trait associations.


First, using these two gene-sets, we assessed the genes' effects on all 3,752 phenotypes in PhenomeXcan by adding their standardized effect sizes and obtaining a ranked list of traits.
The top associated traits for genes in the decreasing-lipids gene-set were highly relevant to lipid levels, such as hypertension, diastolic and systolic blood pressure, and vascular diseases.
Other associated traits included asthma and lung function.
We also performed the same operation for our gene module-based approach by considering 24 modules significantly enriched with the decreasing-lipids gene-set (Gene-set enrichment analysis, FDR < 0.05).
In this case, we also found highly lipids-relevant traits among the top 25, including hypertension, blood pressure, specific cardiometabolic diseases like atherosclerosis, and celiac disease.
This is particularly relevant because each of the 24 modules aggregated a specific weighted combination of almost 3,000 genes' effect sizes across all 3,752 traits.
Thus, aggregating the effects of this number of genes and obtaining top-ranked lipids-relevant traits is highly unlikely to happen by chance ($P < 0.001$, see Methods), suggesting that gene modules (discovered with an unsupervised method) represent functionally meaningful units.


![
**Tissues and traits associated with a gene module related to lipids metabolism (LV246).**
<!--  -->
**a)** Top cell types/tissues where genes in LV246 are expressed on.
Values in the $y$-axis come from matrix $\mathbf{B}$ in the MultiPLIER models (Figure @fig:entire_process a).
In the $x$-axis, cell types/tissues are sorted by the median value.
<!--  -->
**b)** Gene-trait associations (S-MultiXcan) and colocalization (fastENLOC) for the top traits in LV246.
The top 40 genes in LV246 are shown, sorted by their module weigth, from largest (top gene *SCD*) to smallest (gene *FAR2*).
<!--  -->
SGBS: Simpson Golabi Behmel Syndrome;
CH2DB: CH<sub>2</sub> groups to double bonds ratio;
NMR: nuclear magnetic resonance;
HDL: high-density lipoprotein.
<!--  -->
](images/lvs_analysis/lv246/lv246.svg "LV246 TWAS plot"){#fig:lv246 width="100%"}


When we considered the increasing-lipids set, genes and modules were associated with a more diverse set of traits, such as blood count tests, whole-body bioelectrical impedance measures, severe asthma, lung function, and rheumatoid arthritis.
Additionally, gene modules were also associated with blood lipids, arterial stiffness, intraocular pressure, handgrip strength, and celiac disease.
One gene module (LV246), significantly enriched with the increasing-lipids gene-set, was also associated with lipids metabolism and triglyceride biosynthesis pathways.
In Figure @fig:lv246 a, we used our module-based approach to show that LV246 genes are mainly co-expressed in adipose tissue, and to a less extent, liver cells (hepatocytes), which play key roles in coordinating and regulating lipids metabolism.
This LV was associated with blood lipids, hypercholesterolemia, cholesterol lowering medication, and family history of heart disease, among others (Figure @fig:lv246 b).
Two high-confidence genes from our CRISPR screening, *DGAT2* and *ACACA* (responsible for encoding important enzymes for triglycerides and fatty acid synthesis), accounted for most of the gene-set enrichment signal for LV246.
However, as it can be seen in Figure @fig:lv246 b, these two genes are not strongly associated with any of the top traits for this LV;
other members of this module, such as *SCD*, *LPL*, *FADS2*, *HMGCR* and *LDLR*, were instead significantly associated and colocalized with lipid-relevant traits.
This suggests that a module-based perspective can contextualize and reprioritize TWAS hits using modules of functionally related genes.


`Notes:`{.red}

::: {style="color: red"}
- Improve description of CRISPR analysis.
- Genes *DGAT2* and *ACACA* are part of the high-confidence set, not the merged one (combining high and medium confidence). We might want to distinguish between them in Methods.
- It would be good at some point to have an LV that does not match a pathway.
Otherwise, a reviewer could say "but this is similar to a method computing an association between pathways and traits, where is the novelty here?".
A potential candidate could be LV504, significantly enriched with the increasing-lipids gene-set, associated with medication for blood pressure, asthma, celiac disease, and rheumatoid arthritis.
Genes in this LV are expressed in skeletal muscle cells, intestinal subepithelial myofibroblasts, embryonic kidney cells, lung fibroblast cells, etc.
- We need to standardize the way we refer to our method (gene module-based approach, PhenoPLIER, etc).

Minor:

- Add -log10(p-value) in the legend of figure.
- Maybe make *DGAT2* and *ACACA* gene names bold in figure.
- It would be great to be able to say "this LV is _significantly associated_ with this trait". Some reviewers might want that.
Maybe we could use the Summary-MultiXcan approach to estimate the multivariate regression coefficients from individual genes associations, and get a p-value for the module-trait association.
This could be a future small project, maybe an application note.
One way to quickly compute a p-value is to use MAGMA gene-set analysis.
:::


### Clusters of traits in the gene module space are associated with relevant transcriptional processes

![
**Cluster analysis on traits from PhenomeXcan.**
<!--  -->
**a)** The projection of TWAS results for 3,752 traits to the latent
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
**b)** The clusters found by the consensus function are used as labels to train a decision tree classifier on the original input data, which detects the most important LVs that differentiate groups of traits.
<!--  -->
](images/clustering/clustering_design.svg "Cluster analysis on
traits"){#fig:clustering:design width="100%"}


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
(Figure @fig:clustering:design).
<!--  -->
An important property for a successful application of a consensus clustering
approach is the diversity of the ensemble, understood as the level of
disagreement between the base clustering solutions
[@doi:10.1016/j.ins.2016.04.027; @doi:10.1109/TPAMI.2011.84;
@doi:10.1016/j.patcog.2014.04.005].
A diverse set of solutions can be generated by using different data representations (such as dimensionality reduction methods or subsets of features), clustering algorithms with distinct assumptions ($k$-means, for instance, assumes hyperspherical clusters), and a varying set of algorithm's parameters (such as the number of clusters or the initial random seeds).
<!--  -->
In our approach, we performed cluster analysis using five different clustering
algorithms on three representations of the input data (the original data with
987 latent variables, its projection into the top 50 principal components, and
the embedding learned by UMAP [@arxiv:1802.03426] using 50 components) (see
Figure @fig:clustering:design a). The clustering methods used cover a wide range
of different assumptions on cluster shapes and a varying set of parameters such
as the number of clusters (from 2 to 60), the width of the Gaussian kernel in
spectral clustering, and other method-specific parameters (see the supplementary
material for more details).
<!--  -->
The process generated an ensemble with 4,428 clustering solutions for all
traits. This ensemble was used to derive a coassociation matrix between traits
by counting the number of times a pair of traits was clustered together.
A consensus function was applied on the coassociation matrix to derive a consolidated solution using the information in the ensemble.
For these final partitions, we did not select a specific number of clusters, but instead used a clustering tree [@doi:10.1093/gigascience/giy083] (Figure @fig:clustering:tree) to examine stable groups of traits at multiple resolutions.
<!--  -->
Finally, for the interpretation of the clusters, we trained a decision tree
classifier (a highly interpretable machine learning model) on the original
input data using the clusters found as labels. This approach allowed us to
quickly identify the most important gene modules for the groups of traits found.
<!--  -->
More details of the clustering process are available in the supplementary
material.


![
**Clustering tree using multiple resolutions for clusters of traits.**
<!--  -->
Clustering tree of traits partitions at different resolutions (from 5 to 26 clusters).
Each row represents a partition of the traits, and each circle is a cluster from that partition.
Arrows indicate how traits in one cluster move across clusters from different partitions.
Most of the clusters are preserved across different resolutions, showing a high stability even with independent runs of the clustering algorithm.
<!--  -->
BMR: basal metabolic rate;
WC: waist/hip circumference;
MCV: mean corpuscular volume;
MCH: mean corpuscular hemoglobin;
MRV: mean reticulocyte volume;
MRV: mean reticulocyte volume;
MSCV: mean sphered cell volume;
RDW: red cell (erythrocyte) distribution width;
RA: rheumatoid arthritis;
SLE: systemic lupus erythematosus;
<sup>a</sup> includes whole-body, arms and legs impedances;
<sup>b</sup> allergies refer to allergic rhinitis or atopic dermatitis;
<sup>c</sup> includes Alzheimer's disease, coronary artery disease, breast cancer, fasting blood glucose and insulin measurements, inflammatory bowel disease, and atopic dermatitis;
<sup>d</sup> includes erythrocyte count, hemoglobin concentration, and hematocrit percentage;
<sup>e</sup> includes reticulocyte count and percentage, immature reticulocyte fraction, and high light scatter reticulocytes count and percentage;
<sup>f</sup> includes platelet count, platelet crit, mean platelet volume, and platelet distribution width.
<sup>g</sup> includes diabetes, gout, arthrosis, and respiratory diseases (and related medications such as ramipril, allopurinol, lisinopril, and albuterol), and several environmental/behavioral factors such as intake of a range of common food/drink items including alcohol, time spent outdoors and watching TV, smoking and sleeping habits, early-life factors, education attainment, psychological and mental health, and health satisfaction.
<sup>h</sup> includes vascular problems such as angina, deep vein thrombosis (DVT), intraocular pressure, eye and mouth problems, hand-grip strength, several measurements of physical activity, jobs involving heavy physical work, transport type for commuting, intake of common vitamin/mineral supplements, and various types of body pain and medications for pain relief.
<sup>i</sup> age when diabetes was first diagnosed;
<sup>j</sup> includes neutrophil count, neutrophil+basophil count, neutrophil+eosinophil count, granulocyte count, leukocyte count, and myeloid cell count.
<!--  -->
](images/clustering/clustering_tree.svg "Clustering tree using the consensus solutions for traits"){#fig:clustering:tree width="100%"}


A clustering tree of the consensus solutions at different resolutions is shown in Figure @fig:clustering:tree.
For each $k$ (the number of clusters), the consensus partition that maximized the agreement with the ensemble was selected (see supplementary material).
Since it is expected that a subset of resolutions better represents the patterns among traits, we further filtered the consensus partitions by taking those with an agreement value higher than the 75th percentile, which included partitions from 5 to 26 clusters.


The clustering tree shows five clear branches that start at the top with different numerical labels (from left to right):
0) physical measures including anthropometric traits (with fat-free and fat mass measures in separate sub-branches) and eye measures (keratometry),
1) a "large" branch that includes most of the traits that start to be subdivided only at $k=16$ (with asthma, lipids, and nutrient intake clusters),
2) bone-densitometry measurements,
3) hematological assays on red blood cells and platelets, and
4) a "complex" branch including assays on white blood cells, skin and hair color, autoimmune disorders, and cardiovascular diseases (hypertension, heart problems, and other cardiovascular-related traits such hand-grip strength [@pmid:25982160], and environmental/behavioral factors such as physical activity and diet).
<!--  -->
All branches show relatively highly stable clusters, where the same traits are clustered together across different resolutions even with the consensus algorithm using random seeds at each level.
<!--  -->
The arrows between clusters of different resolutions show how traits move from one group to another, and this only happens between the "complex" branch and the rest, particularly with traits expected to be linked to several others, such as white blood cells, cardiovascular and autoimmune diseases, and other related factors.
(`(Be very careful with the following examples, they need to be extremely obvious/expected)`{.red})
For example, the arrow from cluster 14 at $k=16$ (heart problems and related traits) to cluster 15 at $k=22$ (lipids), indicate the move of coronary artery disease, fasting glucose and blood insulin measurement to the lipids clusters, which are highly related (`CITATION`{.red}).
<!-- Possible citations above:
- https://pubmed.ncbi.nlm.nih.gov/30694691/
- IMPORTANT: https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.118.034978
    This one has a couple of citations in the introduction
 -->
Another example is age when diabetes was first diagnosed that is moved from cluster 0 at $k=25$ to cluster 21 at $k=26$ (with autoimmune diseases such as hypo and hyperthyroidism), and intraocular pressure and eye problems from the same cluster to cluster 25 at $k=26$ (with traits related to hypertension and cardiovascular problems).
This movement of traits across highly-related clusters indicates the complexity of the relationships, where in these cases the algorithm finds meaningful but changing traits at different resolutions.


![
**Gene modules show specific and general transcriptional processes associated with different clusters of traits.**
<!--  -->
`(Early draft version; we need to improve the y-axis labels on the right)`{.red}
<!--  -->
The plot shows a submatrix of $\hat{\mathbf{M}}$ for the main trait clusters (from the bottom of the clustering tree in Figure @fig:clustering:tree), considering only gene modules (rows) that align well with at least one known pathway.
Labels on the right show the top two cell types and top two tissues where gene modules are expressed in.
Values range from -5 (lighter color) to 16 (darker color).
<!--  -->
](images/clustering/global_clustermap-cell_types.svg "Heatmap with gene modules and traits"){#fig:clustering:heatmap width="100%"}


Next, we analyzed which gene modules are driving these trait clusters.
For that, we trained decision tree classifiers on the input data (Figure @fig:clustering:design) using each cluster at $k=26$ (bottom of Figure @fig:clustering:tree) as labels.
This yielded for each cluster the top associated gene modules, where several of them were well-aligned to existing pathways, and other modules were "novel" and expressed in relevant tissues (`REVISE`{.red}).
Results are shown in Figure @fig:clustering:heatmap, where it can be seen that some modules are highly specific to certain types of traits, and others seem to be associated with a wide range of different traits and diseases, thus potentially involved in more general biological functions.
For example, modules such as LV928 and LV30, that are known to be related to early progenitors of the erythrocytes lineage [@doi:10.1016/j.cell.2011.01.004] (`DMAP_ERY` pathways in Supplementary Figure @fig:clustering:heatmap_pathways), are predominantly expressed in early differentiation stages of erythropoiesis, and strongly associated with different assays on red blood cells (erythrocytes and reticulocytes, including cell counts, mean volumes and distribution width).
On the other side, others are highly specific, such as LV730, expressed in thrombocytes, and exclusively associated with hemathological assays on platelets;
or LV598, whose genes are expressed in corneal endothelial cells, and are almost only related to keratometry measurements.
<!-- 
LV154 is also expressed in corneal endothelial cells and associated with keratometry, but not exclusively.
 -->

<!--
Autoimmune diseases are very similar, as it can be seen, but some modules show highly specific associations: for example, I THINK, thyroid-related disorders with LV155 (with genes expressed in thyroid)
-->



::: {style="color: red"}
- Maybe include Ben's question about why we expect these clustering results. My answer was more or less that far apart clusters are explained by more specific LVs to those traits, and the complex branch is more related to traits that are highly connected to all biological processes, where more subtle differences are captured only at higher resolutions.
:::


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

<!-- 
- the importance to invest more resources in finding gene co-expression patterns to increase the number of potential gene modules
- one disadvantage is that we have a limited amount of genes, only 6.000 out of 22k in phenomexcan;
more sophisticated methods for gene co-expression pattern discovery are needed to expand the implications of these analyses and cover more contexts.
- this limited amount of genes makes our approach biased to already known pathways and mechanisms
-->


## Conclusions

<!--
- these results suggest that more research is necessary to continue finding new gene modules/latent variables that capture relevant transcriptional processes that allows us to reprioritize genetic studies.
-->


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>


## Methods

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


### Top latent variables associated with neutrophils

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


### CRISPR-Cas9 screening

`Add details`{.red}


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

![
**Pathways associated with gene modules in Figure @fig:clustering:heatmap.**
<!--  -->
`(Early draft version; instead of this figure, we might want to just add a table with information about LVs)`{.red}
<!--  -->
This figure is equivalent to Figure @fig:clustering:heatmap but, instead of cell types, labels on the right show all the associated pathways for each latent variable.
<!--  -->
](images/clustering/global_clustermap-pathways.svg "Heatmap with gene modules and traits"){#fig:clustering:heatmap_pathways width="100%"}


### Drug-disease predictions

::: {style="color: red"}
- anti-correlation using dot product of s-predixcan on all tissues and lincs
:::


## Supplementary material
