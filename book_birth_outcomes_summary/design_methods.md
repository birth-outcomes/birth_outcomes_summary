# Methods for causal effect estimation

`````{admonition} Executive summary
:class: info

Conventional methods:
* Stratification
* Matching
* Multivariable regression
* Inverse probability of treatment (or propensity score) weighting

G-methods:
* G-computation 
* Marginal structure models
* G-estimation

Addressing unobserved confounding:
* Instrumental variables
* Regression discontinuity (RD)
* Interrupted time series (ITS)
* Difference in differences (DiD)
`````

<mark> where does difference in differences fit in? </mark> https://dimewiki.worldbank.org/Difference-in-Difference

<mark>continue to use this textbook throughout</mark> https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/01/hernanrobins_WhatIf_2jan24.pdf

## Designing a study to estimate a causal effect from observational data

The gold standard method for inferring causality is randomisation - e.g. randomising patients to receive a treatment or not. This is because it removes confounding - it removes the common cause of the treatment and outcome, since the only cause of treatment was randomisation.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

When we are using **observational data**, there are a variety of possible methods for **causal effect estimation**. They all rely on assumptions (although those cannot always be tested).

When designing a study, you need to:
1. Clearly specify the **research question** in terms of a **causal estimand**
2. This allows you to **choose an appropriate method** for this estimand, and to carefully interrogate the influence of biases using **sensitivity and quantitative bias analysis**. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)


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

https://www.liverpool.ac.uk/media/livacuk/schoolofmanagement/docs/Causal,Inference,with,Observational,Data,A,Tutorial,on,Propensity,Score,Analysis.pdf

<mark>read this</mark> https://dimewiki.worldbank.org/Propensity_Score_Matching

<mark>be clear about propensity score matching .v.s weighting v.s. anything else </mark>

## G-methods

G-methods are a family of methods that address intermediate confounding, or treatment-confounder feedback, which is when a confounder is affected by prior exposure status. They do so by taking the by 'taking the observed distribution of intermediate confounders (in the population as well as over time) into account, instead of holding them constant; in other words, they estimate marginal effects rather than conditional effects'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

### G-computation 

'**G-computation** (or the parametric G-formula)  uses a statistical model (eg, a regression model) to predict the potential outcomes (with and without exposure) for each individual observation. This makes it possible to calculate treatment effects in a straightforward way, but relies on the statistical model being correctly specified.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

### Marginal structure models

'**Marginal structural models** aim to make the exposed and unexposed groups exchangeable in terms of confounders by weighting each observation (commonly using inverse probability of treatment weighting) so that the distribution of confounders is similar in both groups. An ATE can then be calculated by a simple comparison or unadjusted regression model.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

### G-estimation

'**G-estimation** (using structural nested mean models) predicts the counterfactual outcome at each time point given no exposure from that point onwards, conditional on prior values of the exposure and confounders.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Addressing unobserved confounding

'The above methods rely on an assumption of no unmeasured confounding (ie, conditional exchangeability), which is often not plausible in observational study designs. The following methods attempt to address unmeasured confounding, subject to certain unprovable assumptions, by exploiting some assignment mechanism (akin to randomisation in an RCT) that determines exposure status but is thought to be unrelated to any unobserved confounders.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

### Instrumental variables

<mark>read this</mark> https://dimewiki.worldbank.org/Instrumental_Variables

An **intrumental variable (IV)** is a variable that **causes some variation in the exposure** that is **unrelated to the outcome**, except through the exposure.

Example: 'If a treatment is only performed at certain hospitals, a patient's distance from such a hospital may affect the probability that they receive this treatment (but doesn't affect whether they had the condition), and this distance can be used as an instrument'.

'**Mendelian randomisation** uses IV analysis with genetic variants as instruments. IV analysis estimates a local average treatment effect (LATE) among 'compliers' - indivudals whose exposure status is affected by the instrument. This group cannot be precisely identified, and the LATE may therefore sometimes be of limited practical or policy relevance'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

### Regression discontinuity (RD)

<mark>read this</mark> https://dimewiki.worldbank.org/Regression_Discontinuity

'RD methods can be used when the **exposure status** (wholly or partly) is determined by some **continuous variable exceeding some arbitrary threshold** (called the forcing variable).'

'If the relationship between the forcing variable and the outcome is otherwise continuous, any discontinuity or jump in the relationship can be attributed to the exposure.'

'RD estimates a LATE among the individuals who fall just above or just below the threshold. As with
IV analysis, bias can occur if the forcing variable is connected
to the outcome through a back-door path or any other pathway
besides the exposure.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

### Interrupted time series (ITS)

'ITS studies compare the **trend over time in a population-level outcome before and after an exposure** is introduced. Assuming that the trend would have been unchanged if the intervention was not introduced, a change in trend at the point of introduction (in terms of level and/or slope) can be attributed to the exposure.'

'ITS can be regarded as a special case of IV or RD, with time being the instrument or forcing variable. ITS addresses time-invariant confounding but can be biased if other events that influence the outcome happen at the same time as the exposure'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

### Difference in differences (DiD)

'DiD studies measure the **change in a population-level outcome before and after an intervention** is introduced, compared with a **comparison group where the intervention is never introduced**. This is similar to RD and ITS, but attempts to control for changing time trends, by using a comparison group to represent the counterfactual outcome trend in the exposed.'

'DiD also addresses time-invariant confounding but requires assuming that there would have been no difference in trend between the groups in the absence of the intervention (the ‘parallel trends’ assumption).' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## What you shouldn't do: all possible confounders

'Many analysts take the strategy of putting in **all possible confounders**. This can be bad news, because adjusting for **colliders and mediators can introduce bias**, as we’ll discuss shortly. Instead, we’ll look at **minimally sufficient adjustment sets**: sets of covariates that, when adjusted for, block all back-door paths, but include no more or no less than necessary. That means there can be many minimally sufficient sets, and if you remove even one variable from a given set, a back-door path will open.'[[source]](https://cran.r-project.org/web/packages/ggdag/vignettes/intro-to-dags.html)

# ROUGH NOTES...

https://www.coursera.org/learn/crash-course-in-causality/lecture/xEcaf/stratification
* stratification - Essentially, you would stratify on important variables, and then average over the distribution of those variables which is also known as standardization. And then we're also going to talk about limitations with this standardization approach. And why it's something we normally can't do, and why we need additional causal inference methods.
* standardisation is the combination of conditioning and marginalising
* we're typically interested in a marginal causal effect, meaning when that does not involve conditioning on X
* standardisation involves stratifying and then averaging... obtaining a treatment effect within each stratum, and then pooling across stratum, where you're weighting by the probability of each stratum
* limitation is that there might be many confounders - so many X variables you need to control for, that you need to stratify by - and with so many combinations, it's likely that some would be empty (i.e. no people have that combination), meaning we can't do it

read this: https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/01/hernanrobins_WhatIf_2jan24.pdf

<mark>Will need to integrate with the page on methods to account for treatment paradox</mark>

Causal inference without models:
* Randomisation
* Standardisation
* Inverse probability weighting

Causal inference with models:
* Inverse probability weighting
* Marginal structural models
* Standardisation
* G-formula
* G-estimation
* OUtcome regression and propensity scores
* Instrumental variable estimation
* Causal survival analysis
* G-methods for time-varying treatments
* Target trial emulation
* Causal mediation

from their table of contents.. [[source]](https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/01/hernanrobins_WhatIf_2jan24.pdf)

## Methods to block back door paths

Sometimes construct **propensity score** (which is a function of the confounders) and then do stratification or matching based on the propensity score (rather than the confounders themselves).

G-METHOD: **Inverse probability weighting** - estimate probability of receiving treatment level actually received (and these probabilities witll be different depending on whether had confounder) - then compute inverse probability (1/probability) - then compute association between treatment and outcome, but each person is counted as many times as their inverse probability weight indicates.

* Person with heart disease treated with aspirin. Had a 50% chance of actually being treated with aspirin. Inverse probability weight 1/0.5 = 2.

Inverse probability weighting eliminates the backdoor through L.

G-METHOD: **Standardisation** - mathematically equivalent to inverse probability weighting - sometimes known as the **G-formula**

G-METHOD: **G-estimation**

What do all of these methods have in common?
* They require data on the confounders that block the backdoor path. If those data are available, then the choice of one of these methods over the others is often a matter of personal taste. Unless the treatment is time-varying -- then we have to go to G-methods. But if the data on the confounders are not available, then the method will not eliminate all the bias, and the magnitude of the residual bias will depend on how much of the backdoor path remains open.
* They require knowledge about the true causal DAG. If we don't know the true casual DAG, then we don't know the backdoor paths that we need to block.

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

## Methods that are alternatives to blocking backdoor paths

e.g. instrumental variable estimation

These methods are popular in economics, but often not general enough to adjust for confounding in many other settings (e.g. when treatment of interest changes over time) (as in time-varying treatments below).

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

## Others

Check if these are already covered or fit above:

Randomization to exposure, use of an instrumental variable, weighted regression via propensity scores, adjustment using multivariable regression, stratification on a confounder, conditioning enrollment on a confounder (restriction), and matching on a confounder.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

static-cWith expert knowledge on the underlying causal structure we can account for confounding in the study design (e.g. through restriction, matching, Mendelian randomization or instrumental variable 2 analysis) or in the data analysis.[6-8] The most used methods in causal inference are multivariable regression techniques, in which we can calculate the exposure effect conditional on the presence of confounding factors, though more complex analytic methods such as propensity score matching or inverse probability weighting are also employed.[2] Though generally not advisable, data-driven confounder selection may be employed in small datasets, under the condition that the data has been pre-processed to entail that covariates fed into the statistical selection method are only potential confounders and free of mediators.[[source]](https://static-content.springer.com/esm/art%3A10.1007%2Fs10654-021-00794-w/MediaObjects/10654_2021_794_MOESM1_ESM.pdf)

## SHAP

Look at some of the variets of SHAP that have been proposed...

asymmetric SHAP
* https://mkffl.github.io/2023/04/20/causal-shapley.html

causal SHAP
* https://towardsdatascience.com/casual-shap-values-a-possible-improvement-of-shap-values-4d4d62925b71
* https://arxiv.org/abs/2011.01625

## Additional: counterfactual prediction modelling

In the case of **counterfactual prediction modelling** (which answers ‘what if’ questions on prognosis related to interventions) **prediction and etiology intentionally collide**.[[Ramspek et al. 2021]](https://link.springer.com/article/10.1007/s10654-021-00794-w)

<mark>look into this</mark>

### When can prediction models answer causal questions?

As this example is from a simulation study where know true causal effects, we can plot the SHAP values from the prediction models v.s. the known true causal effects.

![Causal effects](images/shap_bugs_causal_vs_shap.png)

We can also add clustering to see the redundancy structure of the data as a dendrogram - 'when features merge together at the bottom (left) of the dendrogram it means that that the information those features contain about the outcome (renewal) is very redundant and the model could have used either feature. When features merge together at the top (right) of the dendrogram it means the information they contain about the outcome is independent from each other.'

![Redundancy](images/shap_bugs_redundancy.png)

**When can predictive models answer causal questions?** When the feature is independent of (a) other features in the model, and (b) unobserved confounders. Hence, it is not subject to bias from either unmeasured confounders or feature redundancy. Example: Economy
* Independent from other features in dendogram (no observed confounding)
* No unobserved confounding in causal digram

**When can they not be used? (1) When you have observed confounding.** Example: Ad Spend (no direct causal effect on retention, but correlated with Last upgrade and Monthly usage which do drive retention). 'Our predictive model identifies Ad Spend as the one of the best single predictors of retention because it captures so many of the true causal drivers through correlations. XGBoost imposes regularization, which is a fancy way of saying that it tries to choose the simplest possible model that still predicts well. If it could predict equally well using one feature rather than three, it will tend to do that to avoid overfitting.'

However, there are methods to deal with observed confounding, such as double/debiased machine learning model. This involves:
1. Train model to predict feature (Ad spend) using set of confounders (features not caused by Ad spend)
2. Train model to predict outcome (Did Renew) using that set of confounders
3. Train model to predict residual variation of outcome (the variation left after subtracting our prediction) using the residual variation of the causal feature of interest

'The intuition is that if Ad Spend causes renewal, then the part of Ad Spend that can’t be predicted by other confounding features should be correlated with the part of renewal that can’t be predicted by other confounding features.' There are packages like econML's LinearDML for this.

**When can they not be used? (2) When you have non-confounding redundancy.** 'This occurs when the feature we want causal effects for causally drives, or is driven by, another feature included in the model, but that other feature is not a confounder of our feature of interest.'

Example: Sales Calls directly impact retention, but also have an indirect effect on retention through Interactions. We can see this in the SHAP scatter plots above, which show how XGBoost underestimates the true causal effect of Sales Calls because most of that effect got put onto the Interactions feature.

'Non-confounding redundancy can be fixed in principle by removing the redundant variables from the model (see below). For example, if we removed Interactions from the model then we will capture the full effect of making a sales call on renewal probability. This removal is also important for double ML, since double ML will fail to capture indirect causal effects if you control for downstream features caused by the feature of interest. In this case double ML will only measure the “direct” effect that does not pass through the other feature. Double ML is however robust to controlling for upstream non-confounding redundancy (where the redundant feature causes the feature of interest), though this will reduce your statistical power to detect true effects. Unfortunately, we often don’t know the true causal graph so it can be hard to know when another feature is redundant with our feature of interest because of observed confounding vs. non-confounding redundancy. If it is because of confounding then we should control for that feature using a method like double ML, whereas if it is a downstream consequence then we should drop the feature from our model if we want full causal effects rather than only direct effects. Controlling for a feature we shouldn’t tends to hide or split up causal effects, while failing to control for a feature we should have controlled for tends to infer causal effects that do not exist. This generally makes controlling for a feature the safer option when you are uncertain.'

**When can they not be used? (3) When you have unobserved confounding.** 'The Discount and Bugs Reported features both suffer from unobserved confounding because not all important variables (e.g., Product Need and Bugs Faced) are measured in the data. Even though both features are relatively independent of all the other features in the model, there are important drivers that are unmeasured. In this case, both predictive models and causal models that require confounders to be observed, like double ML, will fail. This is why double ML estimates a large negative causal effect for the Discount feature even when controlling for all other observed features'

'Specialized causal tools based on the principals of instrumental variables, differences-in-differences, or regression discontinuities can sometimes exploit partial randomization even in cases where a full experiment is impossible. For example, instrumental variable techniques can be used to identify causal effects in cases where we cannot randomly assign a treatment, but we can randomly nudge some customers towards treatment, like sending an email encouraging them to explore a new product feature. Difference-in-difference approaches can be helpful when the introduction of new treatments is staggered across groups. Finally, regression discontinuity approaches are a good option when patterns of treatment exhibit sharp cut-offs (for example qualification for treatment based on a specific, measurable trait like revenue over $5,000 per month).'

[[source]](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/Be%20careful%20when%20interpreting%20predictive%20models%20in%20search%20of%20causal%20insights.html#)