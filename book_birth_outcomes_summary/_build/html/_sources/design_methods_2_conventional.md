# Methods #2: Conventional approaches

`````{admonition} Executive summary
:class: info

Conventional methods:
* Stratification
* Matching
* Multivariable regression
* Inverse probability of treatment (or propensity score) weighting

`````

## Conventional approaches for causal effect estimation

The most common methods typically focus on conditioning on some set of common causes of the exposure and outcome.

In RCTs, you are controlling for **intercurrent events** (ICEs), which are defined 'a post-randomization event that “affect either interpretation or existence of the measurements associated with clinical questions of interest.”'. Examples include compliance to an assigned treatment, death before follow-up, treatment switching, etc.[[Lipkovich et al. 2022]](https://doi.org/10.1002/sim.9439)

### Stratification

Stratification or **principal stratification** is the **simplest** method to control confounding.[[Tripepi et al. 2010]](https://doi.org/10.1159/000319590) It is represented by drawing a box on the DAG.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

It was proposed by Frangakis and Rubin 2002.[[source]](https://doi.org/10.1111/j.0006-341X.2002.00021.x) It has gained popularity since the ICH E9 addendum on statistical principles for clinical trials, which listed it as a valid approach to ICEs.[[source]](https://cran.r-project.org/web/packages/PStrata/vignettes/PStrata_JSS.pdf) The use of stratification to adjust for confounding is so common that some investigators consider the terms 'stratification' and 'adjustment' synonymous. Whilst it can be used to adjust for confounding - but it can also be used to **identify effect modification**.[[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

Principal stratification involves partitioning participants into **principal strata** - i.e. particular values of a variable. 'Stratification necessarily results in multiple stratum-specific effect measures (one per stratum defined by the variables L). Each of them quantifies the average causal effect in a nonoverlapping subset of the population but, in general, none of them quantifies the average causal effect in the entire population.' Instead, they are **conditional effect measures**. [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

'Often, one of the principal strata is the focus of inference, but sometimes it is of interest to combine principal effects across several (or all) principal strata while accounting for a confounding effect of a post-randomization variable.'[[Lipkovich et al. 2022]](https://doi.org/10.1002/sim.9439) Hence, stratification involves either:
* **Restricting analysis to subset** of study population with particular value of confounder.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home) This type of stratification is referred to as **restriction**. When positivity fails for some strata of the population (i.e. impossible to get a certain exposure), restriction is used to limit causal inference to the strata where it does hold. [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)
* **Performing analysis in each stratum** of confounder.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home) For causal inference, stratification is simply applies restriction to several mutually exclusive subsets of the population, with exchangeability within each subset. [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)


#### Simple example

* Exposure: Birth order
* Outcome: Down syndrome
* Potential confounder: Maternal age

````{mermaid}
  flowchart LR;

    order("Birth order"):::white;
    down("Down syndrome"):::white;
    age("Maternal age"):::black;

    order -->|?| down;
    age --> order;
    age --> down;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

See figure:
* (a) Association of down syndrome with birth order and age groups seperately
* (b) Down syndrome cases stratified by birth order and maternal age

Can observe that crude association between birth order and Down syndrome was just due to maternal age (as in each age category, birth order did not affect down syndrome frequency, but in each birth order category, age did). [[Tripepi et al. 2010]](https://doi.org/10.1159/000319590)

![Tripepi et al. 2010 Figure 1](images/tripepi_2010_fig1.jpg)

#### Mantel-Haenszel Formula

The **Mantel-Haenszel formula** can be used to provide a pooled odds ratio across different strata. There are alternative methods (e.g. Woolf and inverse variance) but the Mantel-Haenszel method is generally the most robust.[[source]](https://www.statsdirect.co.uk/help/meta_analysis/mh.htm)

Key steps:
1. Calculate crude relative risks (RR) or odds ratio (OR) (i.e. **without stratifying**)
2. Stratify by confounding variable and calculate **stratum-specific** RR or OR
3. Assess whether effect estimates are roughly homogenous across strata and do not differ from that in the whole group
    * If they are **homogeneous**, this means there is **no confounding**, and you can calculate the overall adjusted RR or OR by the **Mantel-Haenszel formula**. The pooling estimate provides an **average** of the stratum-specific RRs or ORs with **weights proportional to the number of individuals** in each stratum.
    * If they are **heterogeneous** and we are interested in effect modification, stratum-specific effect estimates should be reported separately. [[Tripepi et al. 2010]](https://doi.org/10.1159/000319590)

#### Limitations of stratification

* Computes **conditional** effect measures (not average effect measures)
* Requires computation of effect measures in subsets of population defined by combining *all* variables required for conditional exchangeability[[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)
    * This can be laborious and demands a large sample **size** when there is more than one confounder.[[Tripepi et al. 2010]](https://doi.org/10.1159/000319590)
    * This is even if we're **not interested** in such effect modification. Solution: Stratification by something of interest (i.e. effect modifier) followed by IP weighting or standardisation (to adjust for confounding) allows you to deal with exchangeability (confounders) and effect modification (modifiers)
* **Noncollapsibility** of certain effect measures like the odds ratio [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)
* Requires **continuous** confounders to be **constrained** to a limited number of categories, which could generate **residual confounding** [[Tripepi et al. 2010]](https://doi.org/10.1159/000319590)

### Matching

**Matching** involves selecting a sample where exposed and unexposed groups have the same distribution of confounders.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home) We often start with the group with fewer individuals, and then use the other group to find matches. It does not have to be **one-to-one (matching pairs)** - it can be **one-to-many (matching sets)**. Matching is often based on a combination of confounders. [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

Matching can't be represented in DAG, because **non-faithfulness** - the association to a backdoor path is exactly cancelled by the matched subset.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

We make an assumption of conditional exchangeability given L (the confounder), meaning that matching results in '(unconditional) **exchangeability** of the treated and untreated in the matched population', and so we **directly compare** their outcomes. Matching ensures **positivity** since strata with only treated or untreated individuals are excluded. [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

#### Matching methods

Above describes **individual matching**, but you can also use **frequency matching**. For example, randomly selected individuals but ensuring 70% have L=1 (certain value of confounder), and then repeating for the other population. [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

There are a few approaches to matching, which include:
* **Propensity score matching** - matched based on propensity scores
* **Matched difference-in-differences** - perform matching then computed difference-in-differences - this controls for unobserved, time-invariant characteristics between the groups
* **Synthetic control method** - weight one group in a manner to it closely resembles the other group
Above, we are describing the **synthetic control method**. [[source]](https://dimewiki.worldbank.org/Matching)

#### Limitations of matching

* Requires extensive datasets to properly match, with detailed information on baseline characteristics, but this is not always available
* Assumes there are no unobserved characteristics between the matched groups. Possible solution: Matched difference-in-differences. [[source]](https://dimewiki.worldbank.org/Matching)
* Computes **conditional** effect measures (not average effect measures) - i.e. only for certain subset of population [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

### Multivariable regression

In **multivariable regression**, the confounders are **included as covariates**.

### Inverse probability of treatment (or propensity score) weighting

A **propensity score** is the 'probability of treatment assignment conditional on observed baseline characteristics'. It was defined by was Rosenbaum and Rubin (1983). It is a 'balancing score: conditional on the propensity score, the distribution of measured baseline covariates is similar between treated and untreated subjects'.[[Austin 2011]](https://doi.org/10.1080%2F00273171.2011.568786)

Four different propensity scores methods are used for removing the effects of confounding:
* **Propensity score matching**
* **Stratification on the propensity score**
* **Inverse probability of treatment weighting (IPTW) using the propensity score**
* **Covariate adjustment using the propensity score**[[Austin 2011]](https://doi.org/10.1080%2F00273171.2011.568786)

look at:
* https://www.liverpool.ac.uk/media/livacuk/schoolofmanagement/docs/Causal,Inference,with,Observational,Data,A,Tutorial,on,Propensity,Score,Analysis.pdf
* <mark>read this</mark> https://dimewiki.worldbank.org/Propensity_Score_Matching
* <mark>be clear about propensity score matching .v.s weighting v.s. anything else </mark>
