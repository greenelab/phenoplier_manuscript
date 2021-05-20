---
author-meta:
- Milton Pividori
- Marylyn D. Ritchie
- Casey S. Greene
bibliography:
- content/manual-references.json
date-meta: '2021-05-20'
header-includes: '<!--

  Manubot generated metadata rendered from header-includes-template.html.

  Suggest improvements at https://github.com/manubot/manubot/blob/master/manubot/process/header-includes-template.html

  -->

  <meta name="dc.format" content="text/html" />

  <meta name="dc.title" content="Integrating transcriptome-wide association studies with gene co-expression patterns" />

  <meta name="citation_title" content="Integrating transcriptome-wide association studies with gene co-expression patterns" />

  <meta property="og:title" content="Integrating transcriptome-wide association studies with gene co-expression patterns" />

  <meta property="twitter:title" content="Integrating transcriptome-wide association studies with gene co-expression patterns" />

  <meta name="dc.date" content="2021-05-20" />

  <meta name="citation_publication_date" content="2021-05-20" />

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

  <meta name="citation_author" content="Marylyn D. Ritchie" />

  <meta name="citation_author_institution" content="Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA" />

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

  <link rel="alternate" type="text/html" href="https://greenelab.github.io/phenoplier_manuscript/v/908e6da275aa6396b6812e2a5b5fb06335dac67d/" />

  <meta name="manubot_html_url_versioned" content="https://greenelab.github.io/phenoplier_manuscript/v/908e6da275aa6396b6812e2a5b5fb06335dac67d/" />

  <meta name="manubot_pdf_url_versioned" content="https://greenelab.github.io/phenoplier_manuscript/v/908e6da275aa6396b6812e2a5b5fb06335dac67d/manuscript.pdf" />

  <meta property="og:type" content="article" />

  <meta property="twitter:card" content="summary_large_image" />

  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />

  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />

  <meta name="theme-color" content="#ad1457" />

  <!-- end Manubot generated metadata -->'
keywords:
- gene co-expression
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
([permalink](https://greenelab.github.io/phenoplier_manuscript/v/908e6da275aa6396b6812e2a5b5fb06335dac67d/))
was automatically generated
from [greenelab/phenoplier_manuscript@908e6da](https://github.com/greenelab/phenoplier_manuscript/tree/908e6da275aa6396b6812e2a5b5fb06335dac67d)
on May 20, 2021.
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
     Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA
     · Funded by The Gordon and Betty Moore Foundation GBMF 4552; The National Human Genome Research Institute (R01 HG010067)
  </small>

+ **Marylyn D. Ritchie**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon}
    [0000-0002-1208-1720](https://orcid.org/0000-0002-1208-1720)
    · ![Twitter icon](images/twitter.svg){.inline_icon}
    [MarylynRitchie](https://twitter.com/MarylynRitchie)<br>
  <small>
     Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA
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

Tissue specificity is a key feature of human disease and genes with tissue-specific expression are enriched for disease associations [@pmid:20624743; @pmid:14707169; @doi:10.1073/pnas.0810772105].
<!--  -->
Identifying the function of genes involves understanding the regulatory mechanisms that affect their expression across different tissues and cell types [@doi:10.1126/science.aaz1776; @doi:10.1038/s41586-020-2559-3; @doi:10.1038/s41576-019-0200-9].
<!--  -->
Large compendia describing key elements of regulatory DNA have been recently released or updated, which comprise chromatin-state annotations, high-resolution enhancers [@doi:10.1038/s41586-020-03145-z], DNase I hypersensitive sites maps [@doi:10.1038/s41586-020-2559-3], and the characterization of genetic effects on gene expression across different tissues [@doi:10.1126/science.aaz1776].
<!--  -->
The integration with genome-wide association studies (GWAS) on thousands of common diseases could dramatically improve the identification of these transcriptional mechanisms that, when dysregulated, often result in tissue- and cell lineage-specific pathology.


Owing to the readily available gene expression data across several tissues [@doi:10.1038/nbt.3838; @doi:10.1038/s41467-018-03751-6; @doi:10.1126/science.aaz1776; @doi:10.1186/s13040-020-00216-9], a popular approach to identify these biological processes is transcription-wide association studies (TWAS), which integrates expression quantitative trait loci (eQTL) data to provide a mechanistic interpretation for genome-wide association studies (GWAS).
<!--  -->
This is done by testing whether perturbations in gene regulatory mechanisms mediate the association between genetic variants and human diseases [@doi:10.1371/journal.pgen.1009482; @doi:10.1038/ng.3506; @doi:10.1371/journal.pgen.1007889; @doi:10.1038/ng.3367].
<!--  -->
However, TWAS has not been useful to detect tissue-specific effects [@doi:10.1016/j.ajhg.2017.01.031; @doi:10.1038/s41588-018-0081-4], since eQTLs are generally shared across tissues.
<!--  -->
Alternative statistical approaches that connect GWAS with gene expression data can infer disease-relevant tissues and cell types [@doi:10.1038/s41588-018-0081-4; @doi:10.1016/j.ajhg.2011.09.002; @doi:10.1093/bioinformatics/btu326; @doi:10.1038/ng.3598; @doi:10.1038/ncomms6890], but they generally apply enrichment analysis techniques that do not account for widespread gene correlations due to technical noise (i.e. "batch effects") [@doi:10.1038/nrg2825; @doi:10.1038/s41592-019-0456-1].
<!--  -->
In addition, they generally rely on small sets of expression data compared with the total RNA-seq samples available today [@doi:10.1038/s41467-018-03751-6; @doi:10.1038/nbt.3838].


Here we propose a polygenic method that maps gene associations from TWAS on >4,000 traits [@doi:10.1126/sciadv.aba2083] into a latent representation learned from public gene expression repositories on tens of thousands of RNA-seq human samples [@doi:10.1016/j.cels.2019.04.003; @doi:10.1038/nbt.3838].
<!--  -->
This low-dimensional space comprises latent variables representing gene modules with coordinated expression across different tissues and cell types.
We used a computational approach that can reduce technical noise by learning patterns that align to prior knowledge.
<!--  -->
When mapping gene-trait associations to this reduced expression space, we found that traits and diseases are associated with gene modules expressed in relevant cell types.
<!--  -->
Our approach is also more robust in finding meaningful module-trait associations even when individual genes involved in lipids metabolism do not reach genome-wide significance in lipids-related traits.
<!--  -->
We also show that our module-based approach is more accurate in predicting known drug-disease association than using single gene-traits associations, and that our approach could be also useful to study mechanisms of action of drugs.
<!--  -->
Finally, we performed cluster analysis on traits mapped to this latent representation, with clusters highly stable across different resolutions.
<!--  -->
We found common and specific transcriptional processes associated with autoimmune and cardiovascular diseases.

<!--
Some ideas I still have to think about/read more:

- From the tissue specificity review, I liked the idea that "disease-associated genes are typically expressed widely across tissues".
Maybe I can something like: "One approach to disentangle this complex transcriptional mechinery is to consider genes that are co-expressed across different cell types".

- Take a look at the Biology of Genomes abstract; there are some ideas there that I might consider to mention here. I left a paragraph below, a first version of this introduction.
 -->

<!--
Text changed from from the Biology of Genomes abstract that might be helpful:

Transcription-wide association studies (TWAS) provide a mechanistic interpretation of genome-wide association studies (GWAS) by testing whether perturbations in gene regulatory mechanisms mediate the association between genetic variants and human diseases [@doi:10.1371/journal.pgen.1009482; @doi:10.1038/ng.3506; @doi:10.1371/journal.pgen.1007889; @doi:10.1038/ng.3367].
TWAS methods integrate expression quantitative trait loci (eQTL) with GWAS to compute gene-level associations and prioritize potential therapeutic targets [@doi:10.1038/s41588-019-0385-z; @doi:10.1038/nn.4618].
Yet the typical TWAS approach looks at one gene at a time, missing the fact that genes act in concert to carry out different functions.
Methods that consider gene-sets of functionally related genes can have more power to detect associations even when individual genes are not genome-wide significant [@doi:10.1073/pnas.0506580102; @doi:10.1371/journal.pcbi.1004219; @doi:10.1158/0008-5472.CAN-09-4502; @doi:10.1038/nrg2884; @doi:10.1038/s41467-018-06022-6], however, they are typically confined to already known pathways and do not incorporate the effects of eQTLs in the transcriptome.

Another part:

Pathway analysis considers groups of functionally related genes when studying a phenotype of interest, and it has been shown that this gene-set-based approach can have more power to detect associations even when individual genes are not gnenome-wide significant [@doi:10.1158/0008-5472.CAN-09-4502; @doi:10.1038/nrg2884; @doi:].

-->

<!--
# Important papers

- Predicting genotype-specific gene regulatory networks
https://www.biorxiv.org/content/10.1101/2021.01.18.427134v1?rss=1
I like the ideas mentioned in the abstract and introduction of this paper.
-->

`Notes:`{.red}

::: {style="color: red"}
- We need to say more about the clustering of traits, and select a good example to summarize our results.
- I'm not including eMERGE replication here because I still have to work on that part.

Minor:

- I don't like much the idea of mentioning "module-trait associations", since that conveys the idea of a p-value, which we are not giving.
- Reviewers might ask for the sample sizes of GWAS.
Some of them, in PhenoPLIER, are really underpowered, with very few cases;
others are from large studies.
We should be careful when picking our examples in the Results section.
:::


## Results

<!--

Some papers that might be interesting:

https://www.nature.com/articles/s41591-020-01221-5
Air pollution linked to neurodegeneration markers

-->


### Framework for the integration of TWAS with gene co-expression patterns

![
**Schematic of the PhenoPLIER framework.**
<!--  -->
**a)** The integration process between gene co-expression patterns from MultiPLIER (top) and TWAS results from PhenomeXcan.
PhenoPLIER projects gene-based association results on more than 4,000 traits to a latent space learned from a recount2, a large gene expression compendium.
This generates matrix $\mathbf{\hat{M}}$, where each trait is now described by latent variables (LV) or gene modules.
<!--  -->
**b)** After the integration process, we found that neutrophil counts and other white blood cells (bottom) were ranked among the top 10 traits for an LV that was termed a neutrophil signature in the original MultiPLIER study.
Genes in this LV were found to be expressed in relevant cell types (top).
<!--  -->
PBMC: peripheral blood mononuclear cells;
mDCs: myeloid dendritic cells.
<!--  -->
](images/entire_process/entire_process.svg "PhenoPLIER framework"){#fig:entire_process width="100%"}


In Figure @fig:entire_process we show the main components of PhenoPLIER, our framework to integrate TWAS and gene co-expression patterns (see Methods for more details).
The framework combines TWAS results on thousands of phenotypes with gene co-expression patterns by projecting gene-trait associations on a latent gene expression representation.
Each of these latent variables (LVs), obtained with an unsupervised learning method, represents a gene-set or gene module, essentially a group of genes with coordinated expression patterns (i.e. they are expressed together in the same tissues and cell types).
Since genes in these modules vary together, we expect that they may also function together [@doi:10.1186/1471-2164-7-187; @doi:10.1186/s13059-019-1835-8].
Thus, the projection of TWAS results into this latent space might provide context for their interpretation.


For the gene-trait associations we used PhenomeXcan [@doi:10.1126/sciadv.aba2083], a massive TWAS resource on the UK Biobank [@doi:10.1038/s41586-018-0579-z] and other cohorts that provides results for 4,091 phenotypes, including different diseases and traits.
These results were projected to the low-dimensional gene expression representation learned by MultiPLIER using:

$$
\hat{\mathbf{M}} = (\mathbf{Z}^{\top} \mathbf{Z} + \lambda_{2} \mathbf{I})^{-1} \mathbf{Z}^{\top} \mathbf{M},
$$ {#eq:proj}

where $\mathbf{M}^{n \times t}$ is the gene-trait associations matrix from MultiXcan [@doi:10.1371/journal.pgen.1007889] (standardized effect sizes) for $n$ genes and $t$ traits,
$\mathbf{Z}^{n \times l}$ are the gene loadings with $l$ latent variables,
$\lambda_2$ is the regularization parameter used in the training step,
and $\hat{\mathbf{M}}^{l \times t}$ is finally the projection of $\mathbf{M}$ into the latent space: all traits in PhenomeXcan are now described by gene modules.
Since the MultiPLIER models also provide the experimental conditions (such as cell types and tissues, represented by matrix $\mathbf{B}$ in Figure @fig:entire_process a) in which genes in a module are concurringly expressed, our approach also allows inferring the context in which the gene module affects a trait or disease.


In the original MultiPLIER study, the authors found an LV significantly associated with previously known neutrophil gene-sets and highly correlated with neutrophil estimates from gene expression.
<!--  -->
We analyzed this LV using our approach (Figure @fig:entire_process b), and found that
1) neutrophil counts and other white blood cell traits from PhenomeXcan were ranked among the top 10 traits for this LV,
and 2) that the genes in this LV are expressed in neutrophil cells.
<!--  -->
These initial results strongly suggested that shared patterns exist in the gene expression space (which has no GTEx samples) and the TWAS space (with gene models trained using GTEx v8), and that the approach also allows inferring the context-specific effects of gene modules on complex traits.
<!--  -->
We will also show how the approach can aid translational efforts by mapping pharmacological perturbations to this latent space, enabling to observe which compounds affect the transcriptional activity of gene modules.


`Notes/questions:`{.red}

::: {style="color: red"}

Ideas/minor:

- In the figure, add a reference to the TWAS plot (genes x traits) for LV603.
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


### Our gene module-based approach more accurately predicts known disease therapeutics

We systematically evaluated our gene module-based approach from a translational perspective by assessing whether it could more accurately predict known treatments for disease.
For this, we used the transcriptional responses to small molecule perturbations profiled in LINCS L1000 [@doi:10.1016/j.cell.2017.10.049], which were further processed and mapped to DrubBank IDs [@doi:10.1093/nar/gkt1068; @doi:10.7554/eLife.26726; @doi:10.5281/zenodo.47223].
Based on the established drug repurposing strategy that looks for reversed transcriptome patterns between genes and drug-induced perturbations [@doi:10.1126/scitranslmed.3002648; @doi:10.1126/scitranslmed.3001318], we used a framework for prioritizing drug candidates that uses imputed transcriptomes from GWAS [@doi:10.1038/nn.4618].
For this, we computed a drug-disease score by anti-correlating the $z$-scores for a disease (from TWAS) and the $z$-scores for a drug (from LINCS) across sets of genes of different size (see Methods).
Therefore, a large score for a drug-disease pair indicates that a higher (lower) predicted expression of disease-associated genes are down (up)-regulated by the drug, thus predicting a potential treatment.
Similarly for the gene module approach, we estimated how pharmacological perturbations affected the gene module activity by projecting expression profiles of drugs into our latent representation (Equation @eq:proj).
We used a manually-curated gold standard of drug-disease medical indications [@doi:10.7554/eLife.26726; @doi:10.5281/zenodo.47664] across 53 diseases and 322 compounds to evaluate and compare the prediction performance.


![
**Drug-disease prediction performance for gene-based and module-based approaches.**
<!--  -->
The receiver operating characteristic (ROC) (left) and the precision-recall curves (right) for a gene-based and our module-based approach.
<!--  -->
AUC: area under the curve; AP: average precision.
<!--  -->
](images/drug_disease_prediction/roc_pr_curves.svg "ROC-PR curves for drug-disease prediction"){#fig:drug_disease:roc_pr width="100%"}


The ROC and precision-recall (PR) curves comparing both approaches are shown in Figure @fig:drug_disease:roc_pr.
Our proposed gene module-based method outperformed the gene-based one with an area under the curve of 0.632 and an average precision of 0.858.
<!--  -->
It is important to note that the gene-trait associations and drug-induced expression profiles projected into the latent space represent a compressed version of the entire set of results.
The prediction results show that this low-dimensional space captures biologically meaningful patterns that can better represent and link pathophysiological processes with the mechanisms of action of drugs.
In the following, with the aim to understand these results, we examined specific drug-disease pairs where both methods disagreed.


Nicotinic acid (niacin), a B vitamin widely used clinically to treat lipid disorders by exerting its effects on a number tissues, although not all its mechanisms have been documented [@doi:10.1016/j.amjcard.2008.02.029; @doi:10.1194/jlr.S092007].
This compound can increase high-density lipoprotein (HDL) by inhibiting an HDL catabolism receptor in liver.
Niacin also inhibits diacylglycerol acyltransferase–2 (DGAT2), which decrease production of low-density lipoproteins (LDL) by modulating triglyceride synthesis in hepatocytes, or by inhibiting adipocyte triglyceride lipolysis [@doi:10.1016/j.amjcard.2008.02.029].
Niacin was categorized in our gold standard as a disease-modifying indication for atherosclerosis (AT) and coronary artery disease (CAD), and not for pancreatitis.
For pancreatitis, both the gene-based and module-based methods assigned a negative score (below their averages), which agrees with the gold standard in that niacin does not therapeutically change the biology of this disease.
For AT and CAD, the module-based approach predicted niacin as a therapeutic drug by scoring them with 0.52 and 0.96 (above the mean), whereas the gene-based method assigned negative scores of -0.09 and -0.16 (below the mean), respectively.
To understand why the predictions by the module-based method were different, we obtained the LVs that positively contributed to the score by looking at large positive (negative) LV values for the disease and large negative (positive) LV values for the drug of interest.
Notably, LV246 (analyzed previously) was among the top 20 modules contributing to the prediction of niacin as a therapeutic drug for AT.
As shown in Figure @fig:lv246, this module is mainly expressed in adipose cells and hepatocytes, its top genes encode important enzymes involved in lipid biosynthesis, and several of them are significantly associated and colocalized with cardiovascular-related traits:
*SCD* (10q24.31) is associated with hypercholesterolemia (P=1.9e-5) and its GWAS and eQTL signals are fully colocalized (RCP=1.0);
*LPL* (8p21.3), which is known to be linked to different disorders of lipoprotein metabolism, is strongly associated with hypercholesterolemia (P=7.5e-17, RCP=0.26), and family history of heart disease (P=1.7e-5, RCP=0.22);
other genes associated with hypercholesterolemia in this module are
*FADS2* (11q12.2) (P=9.42e-5, RCP=0.623),
*HMGCR* (5q13.3) (P=1.3e-42, RCP=0.23),
and *LDLR* (19p13.2) (P=9.9e-136, RCP=0.41).


![
**Cell types where the top 10 modules contributing for niacin-atherosclerosis prediction are expressed.**
<!--  -->
Average module expression ($y$-axis) of different cell types ($x$-axis) across the top 10 latent variables/modules with a positive contribution for the niacin-AT prediction.
The figure shows a clear immune cells signature, driven mainly by the top 2 modules: LV116 and LV931 (see Supplementary Figures @fig:sup:lv116 and @fig:sup:lv931).
<!-- https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP045569 -->
PBMCs: peripheral blood mononuclear cells;
HSV: treated with herpes simplex virus;
<!-- https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP015670 -->
WNV: Infected with West Nile virus;
<!-- https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP062958 -->
IFNa: interferon-alpha treatment;
<!-- https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP039361 -->
HMDM: human peripheral blood mononuclear cell-derived macrophages;
IPSDM: human induced pluripotent stem cell-derived macrophages;
<!-- https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP015670 -->
](images/drug_disease_prediction/niacin-at-modules_cell_types.svg "Cell types of top modules for niacin-AT prediction"){#fig:drug_disease:niacin width="80%"}


The analysis of other niacin-AT-contributing modules revealed additional known mechanisms of action of niacin.
For example, GPR109A/HCAR2 is a G protein-coupled high-affinity niacin receptor in adipocytes and immune cells, including monocytes, macrophages, neutrophils and dendritic cells [@doi:10.1016/j.tips.2006.05.008; @doi:10.1038/sj.jid.5700586].
It was initially thought that the antiatherogenic effects of niacin were solely due to inhibition of lipolysis in adipose tissue.
However, it has been shown that nicotinic acid can reduce atherosclerosis progression independently of its antidyslipidemic activity through the activation of GPR109A in immune cells [@doi:10.1172/JCI41651], thus boosting anti-inflammatory processes and reversing cholesterol transport [@doi:10.1161/ATVBAHA.108.179283].
As shown in Figure @fig:drug_disease:niacin, this alternative mechanism for niacin could have been hypothesized by examining the cell types where modules positively contributing to the niacin-AT prediction are expressed.
Among these, we also found other potentially interesting modules that could represent mechanisms to explore, such as LV536 expressed in the bladder (Supplementary Figure @fig:sup:lv536) and LV885/LV840 expressed in kidneys (Supplementary Figures @fig:sup:lv885 and @fig:sup:lv840)


The projection of these two types of data into a common latent gene module-based representation could provide a more powerful framework for drug repositioning using data from genetic studies.
Additionally, our approach could be also helpful to better understand the mechanism of pharmacological effect of known or experimental drugs.
For example, one of the top modules affected by niacin (LV66, Supplementary Figure @fig:sup:lv66) is mainly expressed in ovarian granulosa cells.
This compound has been very recently considered as a potential therapeutic for ovarian diseases [@doi:10.1159/000495051; @doi:10.1071/RD20306], as it was found to promote follicle growth and inhibit granulosa cell apoptosis in animal models.
Our proposed approach could be helpful to generate novel hypothesis to evaluate potential mechanisms of action of different drugs.


`Notes/questions:`{.red}

::: {style="color: red"}
- The main problem with this current section is the quality of LINCS L1000 data.
It might be necessary to use Cmap build 02 also here, since there are some concerns about the LINCS imputation pipeline (https://think-lab.github.io/d/185/).
- It could be good to discuss cases where the gene-based approach performed better (there are several ones, even with cardiovascular diseases).
This could potentially show that for some drug-disease pairs, maybe the compound targets a few genes instead of being a broad-spectrum/multi-tissue/multi-cell-type one like niacin.
- It would be great to have an expert in cardiovascular diseases and lipid disorder to review this part.
- Is it clear the message in Figure @fig:drug_disease:niacin ?
An alternative is to just show the most interesting LVs instead of averaging all and showing the top cell types as it is now.

Ideas/minor:

- Maybe as part of the manuscript, we can provide the drug-predictions for all traits in PhenomeXcan for download.
- An interesting analysis could consist in keeping LVs aligned with pathways only; what happens with prediction performance? If it goes down, it means that among not-aligned LVs we have useful information to link diseases and drugs.
  It would be nice to be able to claim that.
:::


### Clusters of traits in the gene module space are associated with relevant transcriptional processes

![
**Cluster analysis on traits using the latent gene expression representation.**
<!--  -->
**a)** The projection of TWAS results on $n$=3,752 traits into the latent gene expression representation is the input data to the clustering process.
A linear (PCA) and non-linear (UMAP) dimensionality reduction techniques are applied to the input data, and the three data versions are processed by five different clustering algorithms.
These algorithms derive partitions from the data using different sets of parameters (such as the number of clusters), leading to an ensemble of 4,428 partitions.
Then, a distance matrix is derived by counting how many times a pair of traits were grouped in different clusters across the ensemble.
Finally, a consensus function is applied to the distance matrix to generate consolidated partitions with different number of clusters (from 2 to $\sqrt{n}\approx$ 60).
These final solutions are represented in the clustering tree (Figure @fig:clustering:tree).
<!--  -->
**b)** The clusters found by the consensus function are used as labels to train a decision tree classifier on the original input data, which detects the LVs that better differentiate groups of traits.
<!--  -->
](images/clustering/clustering_design.svg "Cluster analysis on traits"){#fig:clustering:design width="100%"}


The previous results suggest that $\hat{\mathbf{M}}$ represents a less noisy low-dimentional version of the data.
Thus, we conducted cluster analysis on $\hat{\mathbf{M}}$ to find groups of traits that are similarly affected by the same transcriptional processes.
To avoid using a single clustering algorithm (which implies using a single assumption about the structure of the data), we employed a consensus clustering approach where different methods with varying sets parameters were applied on the data, and later combined into a consolidated solution [@doi:10.1109/TPAMI.2005.237; @Strehl2002; @doi:10.1016/j.ins.2016.04.027] (Figure @fig:clustering:design).
Our clustering pipeline generated 15 final consensus clustering solutions with 5 to 29 clusters (Supplementary Figure @fig:sup:consensus_agreement).
Instead of selecting a specific number of clusters, we used a clustering tree [@doi:10.1093/gigascience/giy083] (Figure @fig:clustering:tree) to examine stable groups of traits across multiple resolutions.
<!--  -->
Finally, for the interpretation of the clusters, we trained a decision tree classifier (a highly interpretable machine learning model) on the input data $\hat{\mathbf{M}}$ using the clusters found as labels.
This allowed us to quickly identify the latent variables/gene modules that better differentiated the groups of traits found (see Methods).


![
**Clustering tree using multiple resolutions for clusters of traits.**
<!--  -->
Each row represents a partition/grouping of the traits, and each circle is a cluster from that partition, and the number of clusters go from 5 to 29.
Arrows indicate how traits in one cluster move across clusters from different partitions.
Most of the clusters are preserved across different resolutions, showing highly stable solutions even with independent runs of the clustering algorithm.
<!--  -->
MCV: mean corpuscular volume;
MCH: mean corpuscular hemoglobin;
MRV: mean reticulocyte volume;
MSCV: mean sphered cell volume;
RDW: red cell (erythrocyte) distribution width;
BMI: body mass index;
WC: waist circumference;
HC: hip circumference;
BMR: basal metabolic rate;
RA: rheumatoid arthritis;
SLE: systemic lupus erythematosus;
IBD: inflammatory bowel disease;
<!--  -->
*Descriptions of traits by cluster IDs (from left to right):*
12: also includes lymphocyte count and allergies such as allergic rhinitis or eczema;
4: includes reticulocyte count and percentage, immature reticulocyte fraction, and high light scatter reticulocytes count and percentage;
5: includes erythrocyte count, hemoglobin concentration, and hematocrit percentage;
18: also includes ankle spacing width;
1: includes platelet count, crit, mean volume, and distribution width;
13: diabetes refers to age when the diabetes was first diagnosed;
25: includes vascular problems such as angina, deep vein thrombosis (DVT), intraocular pressure, eye and mouth problems, pulse rate, hand-grip strength, several measurements of physical activity, jobs involving heavy physical work, types of transport used, intake of vitamin/mineral supplements, and various types of body pain and medications for pain relief;
21: also includes attention deficit hyperactivity disorder (ADHD), number of years of schooling completed, bone density, and intracranial volume measurement;
28: includes diabetes, gout, arthrosis, and respiratory diseases (and related medications such as ramipril, allopurinol, and lisinopril), urine assays, female-specific factors (age at menarche, menopause, first/last live birth), and several environmental/behavioral factors such as intake of a range of food/drink items including alcohol, time spent outdoors and watching TV, smoking and sleeping habits, early-life factors (breastfed as a baby, maternal smoking around birth), education attainment, psychological and mental health, and health satisfaction;
11: also includes fasting blood glucose and insulin measurement;
16: lipids include high and low-density lipoprotein cholesterol (HDL and LDL), triglycerides, and average number of methylene groups per a double bond;
14: includes myocardial infarction, coronary atherosclerosis, ischaemic heart disease (wide definition).
9: includes neutrophil count, neutrophil+basophil count, neutrophil+eosinophil count, granulocyte count, leukocyte count, and myeloid cell count.
<!--  -->
](images/clustering/clustering_tree.svg "Clustering tree on groups of traits"){#fig:clustering:tree width="100%"}


The clustering tree in Figure @fig:clustering:tree shows five clear branches that are shown at the top with different numerical labels (from left to right):
0) a "large" branch that includes most of the traits that start to be subdivided only at $k$=16 (with asthma, subjective well-being traits, and nutrient intake clusters),
1) heel bone-densitometry measurements,
2) hematological assays on red blood cells,
3) physical measures, including spirometry and body impedance, and anthropometric traits with fat-free and fat mass measures in separate sub-branches, and
4) a "complex" branch including keratometry measurements, assays on white blood cells and platelets, skin and hair color traits, autoimmune disorders (type 1 diabetes, psoriasis, hyper/hypothyroidism, rheumatoid arthritis, systemic lupus erythematosus, celiac disease), and cardiovascular diseases (hypertension, coronary artery disease, myocardial infraction, hypercholesterolemia, and other cardiovascular-related traits such hand-grip strength [@pmid:25982160], and environmental/behavioral factors such as physical activity and diet) (See Supplementary Files 1-5 for clustering results).
<!--  -->
All branches show relatively highly stable clusters, where the same traits are clustered together across different resolutions even with the consensus algorithm using random seeds at each level.
<!--  -->
The arrows between different clusters show how traits move from one group to another across different resolutions.
This mainly happens between clusters within the "complex" branch, and between clusters from the "large" branch to the "complex" branch.
This is expected, since the "complex" branch contains traits related to a wide range of different factors and thus are hard to categorize into a single cluster.


![
**Cluster-specific and general transcriptional processes.**
<!--  -->
The plot shows a submatrix of $\hat{\mathbf{M}}$ for the main trait clusters at $k$=29, considering only gene modules (rows) that align well with at least one known pathway.
<!-- Labels on the right show LV names and their main tissues/cell types where gene modules are expressed in. -->
Values are standardized from -5 (lighter color) to 16 (darker color).
<!--  -->
](images/clustering/global_clustermap-plain.svg "Heatmap with gene modules and traits"){#fig:clustering:heatmap width="100%"}


Next, we analyzed which gene modules are driving these clusters of traits.
For that, we trained decision tree classifiers on the input data (Figure @fig:clustering:design) using each cluster at $k$=29 (bottom of Figure @fig:clustering:tree) as labels (see Methods).
This yielded for each cluster the top gene modules, where several of them were well-aligned to existing pathways, and others were "novel" and expressed in relevant tissues.
We summarized this in Figure @fig:clustering:heatmap, where it can be seen that some modules are highly specific to certain types of traits, and others seem to be associated with a wide range of different traits and diseases, thus potentially involved in more general biological functions.
For example, modules such as LV928 and LV30 (Supplementary Figures @fig:sup:lv928 and @fig:sup:lv30), which are known to be related to early progenitors of the erythrocytes lineage [@doi:10.1016/j.cell.2011.01.004], are predominantly expressed in early differentiation stages of erythropoiesis, and strongly associated with different assays on red blood cells (erythrocytes and reticulocytes).
On the other side, others are highly specific, such as LV730, expressed in thrombocytes from different cancer samples (Supplementary Figures @fig:sup:lv730), and strongly associated with hemathological assays on platelets;
or LV598, whose genes are expressed in corneal endothelial cells (Supplementary Figures @fig:sup:lv598) and associated to keratometry measurements (FDR < 0.05; Supplementary Table @tbl:sup:phenomexcan_assocs:lv598).
<!-- 
LV154 is also expressed in corneal endothelial cells and associated with keratometry, but not exclusively.
 -->


The autoimmune diseases sub-branch also has significant gene modules associations expressed in relevant cell types.
<!--  -->
LV155 was strongly expressed in thyroid (Supplementary Figures @fig:sup:lv155), and significantly associated with hypothyroidism both in PhenomeXcan and eMERGE (FDR < 0.05; Supplementary Tables @tbl:sup:phenomexcan_assocs:lv155 and @tbl:sup:emerge_assocs:lv155).
<!--  -->
LV844 was the most strongly associated gene module with autoimmune disorders (FDR < 1e-15; Supplementary Tables @tbl:sup:phenomexcan_assocs:lv844 and @tbl:sup:emerge_assocs:lv844), and was expressed in a wide range of cell types, including blood, breast organoids, myeloma cells, lung fibroblasts, and different cell types from the brain (Supplementary Figures @fig:sup:lv844).
<!--  -->
Other important gene modules associated with autoimmunity in both PhenomeXcan and eMERGE are LV57 expressed in T cells (Supplementary Figure @fig:sup:lv57, and Supplementary Tables @tbl:sup:phenomexcan_assocs:lv57 and @tbl:sup:emerge_assocs:lv57), and LV54 expressed in different soft tissue tumors, breast, lung, pterygia and epithelial cells (Supplementary Figure @fig:sup:lv54, and Supplementary Tables @tbl:sup:phenomexcan_assocs:lv54 and @tbl:sup:emerge_assocs:lv54).


The cardiovascular sub-branch also exhibited significant associations, such as LV847 (Supplementary Figure @fig:sup:lv847) with blood pressure traits and hypertension (Supplementary Tables @tbl:sup:phenomexcan_assocs:lv847 and @tbl:sup:emerge_assocs:lv847), which was expressed in CD19 (B cells) (which are related to preeclampsia [@doi:10.1161/HYPERTENSIONAHA.111.188276]), Jurkcat cells (T lymphocyte cells), and cervical carcinoma cell lines (the uterus was previously reported to be linked to blood pressure through a potential hormonal pathway [@doi:10.1038/s41467-018-06022-6; @doi:10.1007/s11906-006-0080-1]).
<!--  -->
LV136 was aligned with known collagen formation and muscle contraction pathways, and it was associated to coronary artery disease, myocardial infarction and keratometry measurements (Supplementary Tables @tbl:sup:phenomexcan_assocs:lv136 and @tbl:sup:emerge_assocs:lv136), and expressed in a wide range of cell types, including fibroblasts, mesenchymal stem cells, osteoblasts, pancreatic stellate cells, cardiomyocytes, and adipocytes (Supplementary Figure @fig:sup:lv136).
<!--  -->
Lipids were clustered with chronotype and Alzheimer's disease, and were significantly associated with several modules expressed mainly in brain cell types, including LV93 (Supplementary Figure @fig:sup:lv93, and Supplementary Tables @tbl:sup:phenomexcan_assocs:lv93 and @tbl:sup:emerge_assocs:lv93), LV206 (Supplementary Figure @fig:sup:lv206, and Supplementary Tables @tbl:sup:phenomexcan_assocs:lv206 and @tbl:sup:emerge_assocs:lv206), and LV260 (Supplementary Figure @fig:sup:lv260, and Supplementary Tables @tbl:sup:phenomexcan_assocs:lv260 and @tbl:sup:emerge_assocs:lv260).
These modules were associated mainly with cardiovascular traits in eMERGE.


Within the cardiovascular sub-branch, we also found mental and neurodevelopmental disorders such as Alzheimer's disease, schizophrenia, and attention deficit hyperactivity disorder (ADHD).
These disorders were previously linked to the cardiovascular system [@pmid:12093424; @doi:10.1161/CIRCULATIONAHA.113.002065; @doi:10.1192/bjp.bp.117.202606; @doi:10.1161/CIRCRESAHA.118.313563], and share several risk factors, including hypertension, high cholesterol, obesity, smoking, among others [@doi:10.1186/s12916-014-0206-2; @doi:10.1111/j.1076-7460.2007.06696.x].
<!--  -->
In our results, however, these diseases were grouped by potentially shared transcriptional processes expressed in specific tissues/cell types.
<!--  -->
Alzheimer's disease, for example, was significantly associated with LV21 (FDR < 1e-18) and with LV5 (FDR < 0.01) (Supplementary Tables @tbl:sup:phenomexcan_assocs:lv21 and @tbl:sup:phenomexcan_assocs:lv5).
LV21 was strongly expressed in a variety of soft tissue sarcomas, monocytes/macrophages (including microglia from cortex samples), and aortic valves (Supplementary Figure @fig:sup:lv21);
as discussed previously, macrophages play a key role in the reverse cholesterol transport and thus atherogenesis [@doi:10.1093/qjmed/hci136].
LV5 was expressed in breast cancer and brain glioma samples, microglia (cortex), liver, and kidney, among other cell types (Supplementary Figure @fig:sup:lv5).
LV21 and LV5 were also strongly associated with lipids: LDL cholesterol (FDR < 0.001) and triglycerides (FDR < 0.05 and FDR < 0.001, respectively).
Additionally, LV5 was associated with depression traits from the UK Biobank.
<!--  -->
ADHD was the only significantly associated trait for LV434 (FDR < 0.01) (Supplementary Table @tbl:sup:phenomexcan_assocs:lv434), which was expressed in breast cancer and glioma cells, cerebral organoids, and several different cell populations from the brain: fetal neurons (replicating and quiescence), microglia, and astrocytes (Supplementary Figure @fig:sup:lv434).
<!-- 
https://link.springer.com/article/10.1007/s11060-019-03165-4
Clinical diagnosis of attention-deficit/hyperactivity disorder in survivors of pediatric brain tumors
    - very interesting
 -->
<!--  -->
Schizophrenia was not significantly associated with any gene module tested in our analysis.
<!--  -->
None of these LVs were aligned to prior pathways, which might represent potentially novel transcriptional processes affecting the cardiovascular and central nervous system.


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

### MultiPLIER and Pathway-level information extractor (PLIER)

MultiPLIER [@doi:10.1016/j.cels.2019.04.003] extracts patterns of co-expressed genes from recount2 [@doi:10.1038/nbt.3838], a large gene expression dataset.
The approach applies the pathway-level information extractor method (PLIER) [@doi:10.1038/s41592-019-0456-1], which performs unsupervised learning using prior knowledge (cannonical pathways) to reduce technical noise.
Via a matrix factorization approach, PLIER deconvolutes the gene expression data into a set of latent variables (LV), where each represents a gene module (i.e. a set of genes with coordinated expression patterns).
This reduced the data dimensionality into 987 latent variables.

Given a gene expression dataset $\mathbf{Y}^{n \times p}$ with $n$ genes and $p$ conditions and a prior knowledge matrix $\mathbf{C} \in \{0,1\}^{n \times m}$ for $m$ gene sets (so that $\mathbf{C}_{ij} = 1$ if gene $i$ belongs to gene set $j$), (e.g., gene sets from MSigDB [@doi:10.1016/j.cels.2015.12.004]), PLIER finds $\mathbf{U}$, $\mathbf{Z}$, and $\mathbf{B}$ minimizing

$$
||\mathbf{Y} - \mathbf{Z}\mathbf{B}||^{2}_{F} + \lambda_1 ||\mathbf{Z} - \mathbf{C}\mathbf{U}||^{2}_{F} + \lambda_2 ||\mathbf{B}||^{2}_{F} + \lambda_3 ||\mathbf{U}||_{L^1}
$$ {#eq:met:plier_func}

subject to $\mathbf{U}>0, \mathbf{Z}>0$;
$\mathbf{Z}^{n \times l}$ are the gene loadings with $l$ latent variables,
$\mathbf{B}^{l \times p}$ is the latent space for $p$ conditions,
$\mathbf{U}^{m \times l}$ specifies which of the $m$ prior-information gene sets in $\mathbf{C}$ are represented for each LV,
and $\lambda_i$ are different regularization parameters used in the training step.
<!--  -->
$\mathbf{Z}$ is a low-dimensional representation of the gene space where each LV aligns as much as possible to prior knowledge and it might represent a known or novel gene module (i.e., a meaningful biological pattern) or noise.


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

**NOT FINISHED**

We used the dot product of the S-PrediXcan $z$-score for each gene-disease pair, and the $z$-score for each gene-drug pair in LINCS L1000, multiplied by -1.

To obtain a drug-disease association for the gene module-mapped TWAS results, we first projected LINCS L1000 data into this latent representation using Equation (@eq:proj), thus leading to a matrix with the expression profiles of drugs mapped to latent variables.
This can be interpreted as the effects of compounds on gene modules activity.
Then, similarly as before, we anti-correlated gene module-traits scores and module expression profiles of drugs.


## Supplementary material


### Top latent variables associated with neutrophils

::: {style="color: red"}
**NOT FINISHED**

This section aims to show that the top LVs related to neutrophil counts are more correlated to neutrophil counts or esimates than expected by chance.
Probably I just need to add a proper caption for each figure, and reference them from the main text.
:::

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


### LV116 cell types

![
**Cell types for LV116.**
<!--  -->
](images/lvs_analysis/lv116/lv116-cell_types.png "Cell types for LV116"){#fig:sup:lv116 width="80%"}


### LV931 cell types

![
**Cell types for LV931.**
<!--  -->
](images/lvs_analysis/lv931/lv931-cell_types.png "Cell types for LV931"){#fig:sup:lv931 width="80%"}


### LV536 cell types

![
**Cell types for LV536.**
<!--  -->
FIXME: *transitional* here refers to bladder: https://trace.ncbi.nlm.nih.gov/Traces/sra/?study=SRP007947
<!--  -->
](images/lvs_analysis/lv536/lv536-cell_types.png "Cell types for LV536"){#fig:sup:lv536 width="80%"}


### LV885 cell types

![
**Cell types for LV885.**
<!--  -->
](images/lvs_analysis/lv885/lv885-tissues.png "Cell types for LV885"){#fig:sup:lv885 width="80%"}


### LV840 cell types

![
**Cell types for LV840.**
<!--  -->
](images/lvs_analysis/lv840/lv840-cell_types.png "Cell types for LV840"){#fig:sup:lv840 width="80%"}


### LV66 cell types

![
**Cell types for LV66.**
<!--  -->
](images/lvs_analysis/lv66/lv66-cell_types.png "Cell types for LV66"){#fig:sup:lv66 width="80%"}


### LV928

![
**Cell types for LV928.**
<!--  -->
](images/lvs_analysis/lv928/lv928-cell_types.svg "Cell types for LV928"){#fig:sup:lv928 width="80%"}


### LV30

![
**Cell types for LV30.**
<!--  -->
](images/lvs_analysis/lv30/lv30-cell_types.svg "Cell types for LV30"){#fig:sup:lv30 width="80%"}


### LV730

![
**Cell types for LV730.**
<!--  -->
](images/lvs_analysis/lv730/lv730-cell_types.svg "Cell types for LV730"){#fig:sup:lv730 width="80%"}


### LV598

![
**Cell types for LV598.**
<!--  -->
](images/lvs_analysis/lv598/lv598-cell_types.svg "Cell types for LV598"){#fig:sup:lv598 width="80%"}

<!-- LV598:phenomexcan_traits_assocs:start -->
| Trait description           | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:----------------------------|:--------------|:--------|:---------------------------|:---------------------|
| 6mm strong meridian (right) | 66,256        |         | 29 / 10                    | 4.13e-07             |
| 6mm weak meridian (right)   | 66,256        |         | 29 / 10                    | 2.63e-06             |
| 6mm strong meridian (left)  | 65,551        |         | 29 / 10                    | 3.13e-06             |
| 3mm strong meridian (left)  | 75,398        |         | 29 / 10                    | 3.24e-06             |
| 6mm weak meridian (left)    | 65,551        |         | 29 / 10                    | 1.53e-05             |
| 3mm weak meridian (left)    | 75,398        |         | 29 / 10                    | 2.00e-05             |
| 3mm strong meridian (right) | 75,410        |         | 29 / 10                    | 3.70e-05             |
| 3mm weak meridian (right)   | 75,410        |         | 29 / 10                    | 4.81e-05             |

Table: Significant trait associations of LV598 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv598}
<!-- LV598:phenomexcan_traits_assocs:end -->

<!-- DISABLED LV598:emerge_traits_assocs:start -->
<!-- DISABLED LV598:emerge_traits_assocs:end -->


### LV155

![
**Cell types for LV155.**
<!--  -->
](images/lvs_analysis/lv155/lv155-cell_types.svg "Cell types for LV155"){#fig:sup:lv155 width="80%"}

<!-- LV155:phenomexcan_traits_assocs:start -->
| Trait description                                                      | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:-----------------------------------------------------------------------|:--------------|:--------|:---------------------------|:---------------------|
| Non-cancer illness code, self-reported: hypothyroidism/myxoedema       | 361,141       | 17,574  | 29 / 13                    | 2.01e-03             |
| Non-cancer illness code, self-reported: hyperthyroidism/thyrotoxicosis | 361,141       | 2,730   | 29 / 13                    | 1.29e-02             |
| Treatment/medication code: levothyroxine sodium                        | 361,141       | 14,689  | 29 / 13                    | 1.41e-02             |

Table: Significant trait associations of LV155 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv155}
<!-- LV155:phenomexcan_traits_assocs:end -->

<!-- LV155:emerge_traits_assocs:start -->
| Phecode   | Trait description       | Sample size   | Cases   | p-value (adjusted)   |
|:----------|:------------------------|:--------------|:--------|:---------------------|
| 244.2     | Acquired hypothyroidism | 45,839        | 1,155   | 2.19e-02             |
| 427.9     | Palpitations            | 35,214        | 6,092   | 4.43e-02             |

Table: Significant trait associations of LV155 in eMERGE. {#tbl:sup:emerge_assocs:lv155}
<!-- LV155:emerge_traits_assocs:end -->


### LV844

![
**Cell types for LV844.**
<!--  -->
`Note`{.red} "Cell types from brain" come from [@doi:10.1073/pnas.1516645112], treated with different chemichals; I don't have enough information to separate cell types.
<!--  -->
](images/lvs_analysis/lv844/lv844-cell_types.svg "Cell types for LV844"){#fig:sup:lv844 width="80%"}

<!-- LV844:phenomexcan_traits_assocs:start -->
| Trait description                                                                         | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:------------------------------------------------------------------------------------------|:--------------|:--------|:---------------------------|:---------------------|
| Rheumatoid Arthritis                                                                      | 80,799        | 19,234  | 29 / 26                    | 4.27e-57             |
| Non-cancer illness code, self-reported: malabsorption/coeliac disease                     | 361,141       | 1,587   | 29 / 8                     | 4.83e-43             |
| Coeliac disease                                                                           | 361,194       | 842     | 29 / 8                     | 4.76e-41             |
| Diagnoses - main ICD10: K90 Intestinal malabsorption                                      | 361,194       | 922     | 29 / 8                     | 1.41e-39             |
| Started insulin within one year diagnosis of diabetes                                     | 16,415        | 1,999   | 29 / 13                    | 1.78e-37             |
| Systemic Lupus Erythematosus                                                              | 23,210        | 7,219   | 29 / 26                    | 1.41e-34             |
| Age diabetes diagnosed                                                                    | 16,166        |         | 29 / 13                    | 3.93e-34             |
| Never eat eggs, dairy, wheat, sugar: Wheat products                                       | 359,777       | 9,573   | 29 / 13                    | 2.78e-31             |
| Non-cancer illness code, self-reported: hyperthyroidism/thyrotoxicosis                    | 361,141       | 2,730   | 29 / 13                    | 6.08e-30             |
| Treatment/medication code: insulin product                                                | 361,141       | 3,545   | 29 / 13                    | 3.05e-25             |
| Medication for cholesterol, blood pressure, diabetes, or take exogenous hormones: Insulin | 193,148       | 1,476   | 29 / 13                    | 4.63e-23             |
| Medication for cholesterol, blood pressure or diabetes: Insulin                           | 165,340       | 2,248   | 29 / 13                    | 1.92e-20             |
| Non-cancer illness code, self-reported: hypothyroidism/myxoedema                          | 361,141       | 17,574  | 29 / 13                    | 4.96e-20             |
| Treatment/medication code: levothyroxine sodium                                           | 361,141       | 14,689  | 29 / 13                    | 4.01e-19             |
| Non-cancer illness code, self-reported: psoriasis                                         | 361,141       | 4,192   | 29 / 13                    | 9.28e-16             |

Table: Significant trait associations of LV844 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv844}
<!-- LV844:phenomexcan_traits_assocs:end -->

<!-- LV844:emerge_traits_assocs:start -->
| Phecode   | Trait description                                             | Sample size   | Cases   | p-value (adjusted)   |
|:----------|:--------------------------------------------------------------|:--------------|:--------|:---------------------|
| 714.1     | Rheumatoid arthritis                                          | 49,453        | 2,541   | 8.22e-09             |
| 250.1     | Type 1 diabetes                                               | 42,723        | 2,450   | 2.54e-08             |
| 714       | Rheumatoid arthritis and other inflammatory polyarthropathies | 50,215        | 3,303   | 5.06e-07             |
| 440       | Atherosclerosis                                               | 47,471        | 4,993   | 3.15e-03             |
| 578.8     | Hemorrhage of rectum and anus                                 | 47,545        | 1,991   | 3.15e-03             |
| 585.32    | End stage renal disease                                       | 43,309        | 1,842   | 4.38e-03             |
| 440.2     | Atherosclerosis of the extremities                            | 45,524        | 3,046   | 5.00e-03             |
| 514.2     | Solitary pulmonary nodule                                     | 50,389        | 2,270   | 6.16e-03             |
| 444       | Arterial embolism and thrombosis                              | 43,378        | 900     | 1.36e-02             |
| 558       | Noninfectious gastroenteritis                                 | 40,177        | 3,191   | 2.94e-02             |
| 747.11    | Cardiac shunt/ heart septal defect                            | 58,364        | 1,037   | 3.60e-02             |
| 585       | Renal failure                                                 | 51,437        | 9,970   | 3.87e-02             |
| 443.9     | Peripheral vascular disease, unspecified                      | 46,926        | 4,448   | 4.43e-02             |

Table: Significant trait associations of LV844 in eMERGE. {#tbl:sup:emerge_assocs:lv844}
<!-- LV844:emerge_traits_assocs:end -->


### LV57

![
**Cell types for LV57.**
<!--  -->
<!--  -->
](images/lvs_analysis/lv57/lv57-cell_types.svg "Cell types for LV57"){#fig:sup:lv57 width="80%"}

<!-- LV57:phenomexcan_traits_assocs:start -->
| Trait description                                                                         | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:------------------------------------------------------------------------------------------|:--------------|:--------|:---------------------------|:---------------------|
| Non-cancer illness code, self-reported: hypothyroidism/myxoedema                          | 361,141       | 17,574  | 29 / 13                    | 1.17e-24             |
| Treatment/medication code: levothyroxine sodium                                           | 361,141       | 14,689  | 29 / 13                    | 6.07e-23             |
| Non-cancer illness code, self-reported: hyperthyroidism/thyrotoxicosis                    | 361,141       | 2,730   | 29 / 13                    | 1.16e-06             |
| Started insulin within one year diagnosis of diabetes                                     | 16,415        | 1,999   | 29 / 13                    | 8.17e-05             |
| Treatment/medication code: insulin product                                                | 361,141       | 3,545   | 29 / 13                    | 6.33e-04             |
| Medication for cholesterol, blood pressure, diabetes, or take exogenous hormones: Insulin | 193,148       | 1,476   | 29 / 13                    | 1.13e-03             |
| Medication for cholesterol, blood pressure or diabetes: Insulin                           | 165,340       | 2,248   | 29 / 13                    | 4.50e-03             |

Table: Significant trait associations of LV57 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv57}
<!-- LV57:phenomexcan_traits_assocs:end -->

<!-- LV57:emerge_traits_assocs:start -->
| Phecode   | Trait description                                             | Sample size   | Cases   | p-value (adjusted)   |
|:----------|:--------------------------------------------------------------|:--------------|:--------|:---------------------|
| 244       | Hypothyroidism                                                | 54,404        | 9,720   | 3.97e-09             |
| 244.4     | Hypothyroidism NOS                                            | 53,968        | 9,284   | 3.97e-09             |
| 279       | Disorders involving the immune mechanism                      | 56,771        | 3,309   | 4.93e-03             |
| 514.2     | Solitary pulmonary nodule                                     | 50,389        | 2,270   | 1.19e-02             |
| 714       | Rheumatoid arthritis and other inflammatory polyarthropathies | 50,215        | 3,303   | 1.68e-02             |
| 452.2     | Deep vein thrombosis [DVT]                                    | 38,791        | 2,131   | 4.37e-02             |

Table: Significant trait associations of LV57 in eMERGE. {#tbl:sup:emerge_assocs:lv57}
<!-- LV57:emerge_traits_assocs:end -->


### LV54

![
**Cell types for LV54.**
<!--  -->
<!--  -->
](images/lvs_analysis/lv54/lv54-cell_types.svg "Cell types for LV54"){#fig:sup:lv54 width="80%"}

<!-- LV54:phenomexcan_traits_assocs:start -->
| Trait description                                                                         | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:------------------------------------------------------------------------------------------|:--------------|:--------|:---------------------------|:---------------------|
| Diagnoses - main ICD10: K90 Intestinal malabsorption                                      | 361,194       | 922     | 29 / 8                     | 5.09e-25             |
| Coeliac disease                                                                           | 361,194       | 842     | 29 / 8                     | 7.77e-25             |
| Never eat eggs, dairy, wheat, sugar: Wheat products                                       | 359,777       | 9,573   | 29 / 13                    | 6.33e-23             |
| Systemic Lupus Erythematosus                                                              | 23,210        | 7,219   | 29 / 26                    | 1.32e-22             |
| Started insulin within one year diagnosis of diabetes                                     | 16,415        | 1,999   | 29 / 13                    | 3.84e-20             |
| Non-cancer illness code, self-reported: hyperthyroidism/thyrotoxicosis                    | 361,141       | 2,730   | 29 / 13                    | 9.59e-19             |
| Treatment/medication code: insulin product                                                | 361,141       | 3,545   | 29 / 13                    | 5.07e-18             |
| Age diabetes diagnosed                                                                    | 16,166        |         | 29 / 13                    | 1.28e-17             |
| Non-cancer illness code, self-reported: malabsorption/coeliac disease                     | 361,141       | 1,587   | 29 / 8                     | 1.36e-14             |
| Medication for cholesterol, blood pressure or diabetes: Insulin                           | 165,340       | 2,248   | 29 / 13                    | 8.67e-14             |
| Non-cancer illness code, self-reported: psoriasis                                         | 361,141       | 4,192   | 29 / 13                    | 2.61e-13             |
| Rheumatoid Arthritis                                                                      | 80,799        | 19,234  | 29 / 26                    | 3.11e-13             |
| Medication for cholesterol, blood pressure, diabetes, or take exogenous hormones: Insulin | 193,148       | 1,476   | 29 / 13                    | 3.89e-12             |
| Treatment/medication code: levothyroxine sodium                                           | 361,141       | 14,689  | 29 / 13                    | 5.92e-10             |
| Non-cancer illness code, self-reported: hypothyroidism/myxoedema                          | 361,141       | 17,574  | 29 / 13                    | 3.31e-08             |

Table: Significant trait associations of LV54 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv54}
<!-- LV54:phenomexcan_traits_assocs:end -->

<!-- LV54:emerge_traits_assocs:start -->
| Phecode   | Trait description                                             | Sample size   | Cases   | p-value (adjusted)   |
|:----------|:--------------------------------------------------------------|:--------------|:--------|:---------------------|
| 250.1     | Type 1 diabetes                                               | 42,723        | 2,450   | 2.04e-13             |
| 244       | Hypothyroidism                                                | 54,404        | 9,720   | 5.10e-06             |
| 244.4     | Hypothyroidism NOS                                            | 53,968        | 9,284   | 5.37e-06             |
| 695       | Erythematous conditions                                       | 48,347        | 4,210   | 4.25e-05             |
| 714       | Rheumatoid arthritis and other inflammatory polyarthropathies | 50,215        | 3,303   | 3.06e-04             |
| 440       | Atherosclerosis                                               | 47,471        | 4,993   | 8.88e-04             |
| 585       | Renal failure                                                 | 51,437        | 9,970   | 3.40e-03             |
| 585.32    | End stage renal disease                                       | 43,309        | 1,842   | 3.64e-03             |
| 585.33    | Chronic Kidney Disease, Stage III                             | 46,279        | 4,812   | 3.64e-03             |
| 285.2     | Anemia of chronic disease                                     | 39,673        | 2,606   | 7.62e-03             |
| 415.1     | Acute pulmonary heart disease                                 | 49,887        | 1,857   | 8.67e-03             |
| 285.21    | Anemia in chronic kidney disease                              | 38,616        | 1,549   | 1.16e-02             |
| 743       | Osteoporosis, osteopenia and pathological fracture            | 55,165        | 11,990  | 1.31e-02             |
| 415.11    | Pulmonary embolism and infarction, acute                      | 49,867        | 1,837   | 1.39e-02             |
| 577       | Diseases of pancreas                                          | 60,538        | 1,795   | 1.42e-02             |
| 585.1     | Acute renal failure                                           | 46,803        | 5,336   | 1.51e-02             |
| 195       | Cancer, suspected or other                                    | 50,040        | 2,250   | 1.52e-02             |
| 440.2     | Atherosclerosis of the extremities                            | 45,524        | 3,046   | 1.89e-02             |
| 714.1     | Rheumatoid arthritis                                          | 49,453        | 2,541   | 3.18e-02             |
| 458.9     | Hypotension NOS                                               | 50,150        | 3,241   | 3.32e-02             |

Table: Significant trait associations of LV54 in eMERGE. {#tbl:sup:emerge_assocs:lv54}
<!-- LV54:emerge_traits_assocs:end -->


### LV847

![
**Cell types for LV847.**
<!--  -->
<!--  -->
](images/lvs_analysis/lv847/lv847-cell_types.svg "Cell types for LV847"){#fig:sup:lv847 width="80%"}

<!-- LV847:phenomexcan_traits_assocs:start -->
| Trait description                                                                                           | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:------------------------------------------------------------------------------------------------------------|:--------------|:--------|:---------------------------|:---------------------|
| Medication for cholesterol, blood pressure, diabetes, or take exogenous hormones: Blood pressure medication | 193,148       | 33,519  | 29 / 17                    | 1.95e-18             |
| Vascular/heart problems diagnosed by doctor: None of the above                                              | 360,420       | 253,565 | 29 / 17                    | 4.07e-15             |
| Vascular/heart problems diagnosed by doctor: High blood pressure                                            | 360,420       | 97,139  | 29 / 17                    | 6.99e-14             |
| Non-cancer illness code, self-reported: hypertension                                                        | 361,141       | 93,560  | 29 / 17                    | 1.48e-13             |
| Treatment/medication code: bendroflumethiazide                                                              | 361,141       | 20,196  | 29 / 17                    | 1.41e-08             |
| Medication for cholesterol, blood pressure or diabetes: Blood pressure medication                           | 165,340       | 40,987  | 29 / 17                    | 1.47e-07             |
| Medication for cholesterol, blood pressure, diabetes, or take exogenous hormones: None of the above         | 193,148       | 133,338 | 29 / 17                    | 1.55e-06             |
| Diastolic blood pressure, automated reading                                                                 | 340,162       |         | 29 / 17                    | 3.76e-06             |
| Medication for cholesterol, blood pressure or diabetes: None of the above                                   | 165,340       | 110,372 | 29 / 17                    | 6.36e-06             |

Table: Significant trait associations of LV847 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv847}
<!-- LV847:phenomexcan_traits_assocs:end -->

<!-- LV847:emerge_traits_assocs:start -->
| Phecode   | Trait description                                              | Sample size   | Cases   | p-value (adjusted)   |
|:----------|:---------------------------------------------------------------|:--------------|:--------|:---------------------|
| 585.32    | End stage renal disease                                        | 43,309        | 1,842   | 1.88e-08             |
| 442.1     | Aortic aneurysm                                                | 45,589        | 3,111   | 5.23e-06             |
| 411.3     | Angina pectoris                                                | 43,503        | 4,382   | 2.14e-05             |
| 415.11    | Pulmonary embolism and infarction, acute                       | 49,867        | 1,837   | 5.13e-05             |
| 416       | Cardiomegaly                                                   | 53,289        | 5,259   | 6.50e-05             |
| 415.1     | Acute pulmonary heart disease                                  | 49,887        | 1,857   | 7.28e-05             |
| 411       | Ischemic Heart Disease                                         | 54,275        | 15,154  | 5.49e-04             |
| 401.2     | Hypertensive heart and/or renal disease                        | 30,405        | 6,253   | 1.28e-03             |
| 519       | Other diseases of respiratory system, not elsewhere classified | 56,909        | 2,056   | 1.28e-03             |
| 411.8     | Other chronic ischemic heart disease, unspecified              | 44,123        | 5,002   | 1.42e-03             |
| 427.6     | Premature beats                                                | 31,575        | 2,453   | 5.65e-03             |
| 687.1     | Rash and other nonspecific skin eruption                       | 47,039        | 4,964   | 9.88e-03             |
| 185       | Cancer of prostate                                             | 52,630        | 2,815   | 1.03e-02             |
| 591       | Urinary tract infection                                        | 49,727        | 10,016  | 1.34e-02             |
| 442.11    | Abdominal aortic aneurysm                                      | 44,531        | 2,053   | 2.08e-02             |
| 427.21    | Atrial fibrillation                                            | 37,743        | 8,621   | 2.26e-02             |
| 389.1     | Sensorineural hearing loss                                     | 53,672        | 4,318   | 2.73e-02             |
| 427.2     | Atrial fibrillation and flutter                                | 37,934        | 8,812   | 4.50e-02             |

Table: Significant trait associations of LV847 in eMERGE. {#tbl:sup:emerge_assocs:lv847}
<!-- LV847:emerge_traits_assocs:end -->


### LV136

![
**Cell types for LV136.**
<!--  -->
Pulmonary microvascular endothelial cells were exposed to hypoxia for 24 hours or more [@url:https://www.ncbi.nlm.nih.gov/bioproject/PRJNA232177];
](images/lvs_analysis/lv136/lv136-cell_types.svg "Cell types for LV136"){#fig:sup:lv136 width="80%"}

<!-- LV136:phenomexcan_traits_assocs:start -->
| Trait description                                                          | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:---------------------------------------------------------------------------|:--------------|:--------|:---------------------------|:---------------------|
| 3mm strong meridian (right)                                                | 75,410        |         | 29 / 10                    | 9.19e-11             |
| 6mm strong meridian (left)                                                 | 65,551        |         | 29 / 10                    | 2.06e-09             |
| 6mm strong meridian (right)                                                | 66,256        |         | 29 / 10                    | 2.38e-09             |
| 3mm strong meridian (left)                                                 | 75,398        |         | 29 / 10                    | 1.34e-08             |
| 3mm weak meridian (right)                                                  | 75,410        |         | 29 / 10                    | 1.67e-08             |
| Coronary Artery Disease                                                    | 184,305       | 60,801  | 29 / 11                    | 1.67e-08             |
| 6mm weak meridian (right)                                                  | 66,256        |         | 29 / 10                    | 3.21e-08             |
| 3mm weak meridian (left)                                                   | 75,398        |         | 29 / 10                    | 5.20e-08             |
| 6mm weak meridian (left)                                                   | 65,551        |         | 29 / 10                    | 1.21e-07             |
| Coronary atherosclerosis                                                   | 361,194       | 14,334  | 29 / 14                    | 3.90e-06             |
| Ischaemic heart disease, wide definition                                   | 361,194       | 20,857  | 29 / 14                    | 7.22e-06             |
| Vascular/heart problems diagnosed by doctor: Heart attack                  | 360,420       | 8,288   | 29 / 14                    | 2.93e-04             |
| Myocardial infarction                                                      | 361,194       | 7,018   | 29 / 14                    | 6.33e-04             |
| Myocardial infarction, strict                                              | 361,194       | 7,018   | 29 / 14                    | 6.33e-04             |
| Diagnoses - main ICD10: I21 Acute myocardial infarction                    | 361,194       | 5,948   | 29 / 14                    | 9.92e-04             |
| Non-cancer illness code, self-reported: heart attack/myocardial infarction | 361,141       | 8,239   | 29 / 14                    | 1.40e-03             |
| Major coronary heart disease event excluding revascularizations            | 361,194       | 10,157  | 29 / 14                    | 1.85e-02             |
| Major coronary heart disease event                                         | 361,194       | 10,157  | 29 / 14                    | 1.85e-02             |
| Fasting Insulin                                                            | 38,238        |         | 29 / 11                    | 3.85e-02             |

Table: Significant trait associations of LV136 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv136}
<!-- LV136:phenomexcan_traits_assocs:end -->

<!-- LV136:emerge_traits_assocs:start -->
| Phecode   | Trait description            | Sample size   | Cases   | p-value (adjusted)   |
|:----------|:-----------------------------|:--------------|:--------|:---------------------|
| 747.1     | Cardiac congenital anomalies | 59,198        | 1,871   | 4.71e-02             |
| 411.4     | Coronary atherosclerosis     | 52,836        | 13,715  | 4.80e-02             |

Table: Significant trait associations of LV136 in eMERGE. {#tbl:sup:emerge_assocs:lv136}
<!-- LV136:emerge_traits_assocs:end -->


### LV93

![
**Cell types for LV93.**
<!--  -->
](images/lvs_analysis/lv93/lv93-cell_types.svg "Cell types for LV93"){#fig:sup:lv93 width="80%"}

<!-- LV93:phenomexcan_traits_assocs:start -->
| Trait description   | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:--------------------|:--------------|:--------|:---------------------------|:---------------------|
| CH2DB NMR           | 24,154        |         | 29 / 16                    | 9.61e-24             |
| Chronotype          | 128,266       |         | 29 / 16                    | 1.17e-03             |
| HDL Cholesterol NMR | 19,270        |         | 29 / 16                    | 2.99e-03             |

Table: Significant trait associations of LV93 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv93}
<!-- LV93:phenomexcan_traits_assocs:end -->

<!-- LV93:emerge_traits_assocs:start -->
| Phecode   | Trait description                  | Sample size   | Cases   | p-value (adjusted)   |
|:----------|:-----------------------------------|:--------------|:--------|:---------------------|
| 208       | Benign neoplasm of colon           | 55,694        | 8,597   | 6.21e-03             |
| 440.2     | Atherosclerosis of the extremities | 45,524        | 3,046   | 1.31e-02             |
| 444       | Arterial embolism and thrombosis   | 43,378        | 900     | 4.06e-02             |

Table: Significant trait associations of LV93 in eMERGE. {#tbl:sup:emerge_assocs:lv93}
<!-- LV93:emerge_traits_assocs:end -->


### LV206

![
**Cell types for LV206.**
<!--  -->
](images/lvs_analysis/lv206/lv206-cell_types.svg "Cell types for LV206"){#fig:sup:lv206 width="80%"}

<!-- LV206:phenomexcan_traits_assocs:start -->
| Trait description   | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:--------------------|:--------------|:--------|:---------------------------|:---------------------|
| CH2DB NMR           | 24,154        |         | 29 / 16                    | 7.67e-21             |
| HDL Cholesterol NMR | 19,270        |         | 29 / 16                    | 6.46e-03             |

Table: Significant trait associations of LV206 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv206}
<!-- LV206:phenomexcan_traits_assocs:end -->

<!-- LV206:emerge_traits_assocs:start -->
| Phecode   | Trait description            | Sample size   | Cases   | p-value (adjusted)   |
|:----------|:-----------------------------|:--------------|:--------|:---------------------|
| 458       | Hypotension                  | 51,341        | 4,432   | 1.41e-02             |
| 286.9     | Abnormal coagulation profile | 48,006        | 800     | 1.54e-02             |
| 458.9     | Hypotension NOS              | 50,150        | 3,241   | 1.58e-02             |
| 428.2     | Heart failure NOS            | 48,178        | 3,584   | 1.65e-02             |

Table: Significant trait associations of LV206 in eMERGE. {#tbl:sup:emerge_assocs:lv206}
<!-- LV206:emerge_traits_assocs:end -->


### LV260

![
**Cell types for LV260.**
<!--  -->
](images/lvs_analysis/lv260/lv260-cell_types.svg "Cell types for LV260"){#fig:sup:lv260 width="80%"}

<!-- LV260:phenomexcan_traits_assocs:start -->
| Trait description   | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:--------------------|:--------------|:--------|:---------------------------|:---------------------|
| CH2DB NMR           | 24,154        |         | 29 / 16                    | 5.96e-17             |
| HDL Cholesterol NMR | 19,270        |         | 29 / 16                    | 2.37e-02             |

Table: Significant trait associations of LV260 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv260}
<!-- LV260:phenomexcan_traits_assocs:end -->

<!-- LV260:emerge_traits_assocs:start -->
| Phecode   | Trait description   | Sample size   | Cases   | p-value (adjusted)   |
|:----------|:--------------------|:--------------|:--------|:---------------------|
| 427.6     | Premature beats     | 31,575        | 2,453   | 2.85e-02             |
| 426.3     | Bundle branch block | 31,827        | 2,705   | 4.80e-02             |

Table: Significant trait associations of LV260 in eMERGE. {#tbl:sup:emerge_assocs:lv260}
<!-- LV260:emerge_traits_assocs:end -->


### LV21

![
**Cell types for LV21.**
<!--  -->
](images/lvs_analysis/lv21/lv21-cell_types.svg "Cell types for LV21"){#fig:sup:lv21 width="80%"}

<!-- LV21:phenomexcan_traits_assocs:start -->
| Trait description   | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:--------------------|:--------------|:--------|:---------------------------|:---------------------|
| Alzheimers Disease  | 54,162        | 17,008  | 29 / 16                    | 1.64e-19             |
| LDL Cholesterol NMR | 13,527        |         | 29 / 16                    | 1.18e-04             |
| Triglycerides NMR   | 21,559        |         | 29 / 16                    | 2.19e-02             |

Table: Significant trait associations of LV21 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv21}
<!-- LV21:phenomexcan_traits_assocs:end -->

<!-- LV21:emerge_traits_assocs:start -->
| Phecode   | Trait description        | Sample size   | Cases   | p-value (adjusted)   |
|:----------|:-------------------------|:--------------|:--------|:---------------------|
| 573       | Other disorders of liver | 47,826        | 2,524   | 1.37e-02             |
| 577       | Diseases of pancreas     | 60,538        | 1,795   | 2.15e-02             |

Table: Significant trait associations of LV21 in eMERGE. {#tbl:sup:emerge_assocs:lv21}
<!-- LV21:emerge_traits_assocs:end -->


### LV5

![
**Cell types for LV5.**
<!--  -->
](images/lvs_analysis/lv5/lv5-cell_types.svg "Cell types for LV5"){#fig:sup:lv5 width="80%"}

<!-- LV5:phenomexcan_traits_assocs:start -->
| Trait description                                                                      | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:---------------------------------------------------------------------------------------|:--------------|:--------|:---------------------------|:---------------------|
| LDL Cholesterol NMR                                                                    | 13,527        |         | 29 / 16                    | 1.78e-04             |
| Triglycerides NMR                                                                      | 21,559        |         | 29 / 16                    | 5.00e-04             |
| Alzheimers Disease                                                                     | 54,162        | 17,008  | 29 / 16                    | 3.06e-03             |
| Ever had prolonged feelings of sadness or depression                                   | 117,763       | 64,374  | 29 / 27                    | 8.69e-03             |
| Substances taken for depression: Medication prescribed to you (for at least two weeks) | 117,763       | 28,351  | 29 / 27                    | 1.03e-02             |
| Recent feelings of depression                                                          | 117,656       |         | 29 / 27                    | 1.32e-02             |
| Ever contemplated self-harm                                                            | 117,610       |         | 29 / 27                    | 1.89e-02             |
| Recent lack of interest or pleasure in doing things                                    | 117,757       |         | 29 / 27                    | 2.08e-02             |
| Amount of alcohol drunk on a typical drinking day                                      | 108,256       |         | 29 / 27                    | 3.50e-02             |
| Ever sought or received professional help for mental distress                          | 117,677       | 46,020  | 29 / 27                    | 3.92e-02             |
| General happiness                                                                      | 117,442       |         | 29 / 27                    | 4.74e-02             |

Table: Significant trait associations of LV5 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv5}
<!-- LV5:phenomexcan_traits_assocs:end -->

<!-- LV5:emerge_traits_assocs:start -->
| Phecode   | Trait description            | Sample size   | Cases   | p-value (adjusted)   |
|:----------|:-----------------------------|:--------------|:--------|:---------------------|
| 241       | Nontoxic nodular goiter      | 47,842        | 3,158   | 8.98e-03             |
| 241.1     | Nontoxic uninodular goiter   | 47,125        | 2,441   | 2.57e-02             |
| 241.2     | Nontoxic multinodular goiter | 46,465        | 1,781   | 4.43e-02             |

Table: Significant trait associations of LV5 in eMERGE. {#tbl:sup:emerge_assocs:lv5}
<!-- LV5:emerge_traits_assocs:end -->


### LV434

![
**Cell types for LV434.**
<!--  -->
`FIXME:`{.red} create a section for all LVs and clarify how figures were generated, like:
The top samples in human breast cancer cells have larger LV values that were thresholded at 3.0 for visualization purposes.
<!--  -->
HEK293 is a cell line derived from human embryonic kidney cells;
3T3 is a cell line derived from mouse embryonic fibroblasts.
](images/lvs_analysis/lv434/lv434-cell_types.svg "Cell types for LV434"){#fig:sup:lv434 width="80%"}

<!-- LV434:phenomexcan_traits_assocs:start -->
| Trait description                        | Sample size   | Cases   | Partition/cluster number   | p-value (adjusted)   |
|:-----------------------------------------|:--------------|:--------|:---------------------------|:---------------------|
| Attention Deficit Hyperactivity Disorder | 53,293        | 19,099  | 29 / 21                    | 7.01e-03             |

Table: Significant trait associations of LV434 in PhenomeXcan. {#tbl:sup:phenomexcan_assocs:lv434}
<!-- LV434:phenomexcan_traits_assocs:end -->

<!-- LV434:emerge_traits_assocs:start -->
| Phecode   | Trait description                        | Sample size   | Cases   | p-value (adjusted)   |
|:----------|:-----------------------------------------|:--------------|:--------|:---------------------|
| 722       | Intervertebral disc disorders            | 47,659        | 7,458   | 6.65e-03             |
| 721       | Spondylosis and allied disorders         | 47,517        | 7,316   | 7.62e-03             |
| 250.4     | Abnormal glucose                         | 45,220        | 4,947   | 1.02e-02             |
| 721.1     | Spondylosis without myelopathy           | 47,315        | 7,114   | 1.22e-02             |
| 720       | Spinal stenosis                          | 44,807        | 4,606   | 1.74e-02             |
| 288       | Diseases of white blood cells            | 47,288        | 2,802   | 2.10e-02             |
| 796       | Elevated prostate specific antigen [PSA] | 51,990        | 2,175   | 3.09e-02             |
| 288.2     | Elevated white blood cell count          | 46,595        | 2,109   | 3.54e-02             |
| 079       | Viral infection                          | 46,991        | 1,934   | 4.19e-02             |

Table: Significant trait associations of LV434 in eMERGE. {#tbl:sup:emerge_assocs:lv434}
<!-- LV434:emerge_traits_assocs:end -->


### Agreement of consensus clustering partitions with the ensemble by number of clusters

![
**Final selected partitions for follow-up analysis.**
<!--  -->
From all consensus clustering partitions generated with $k$ from 2 to 60, we selected those with a median adjusted Rand index (ARI) with the ensemble members greater the 75th percentile.
](images/clustering/selected_best_partitions_by_k.svg "Consensus partitions agreement with ensemble"){#fig:sup:consensus_agreement width="80%"}
