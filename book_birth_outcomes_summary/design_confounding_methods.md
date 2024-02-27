# Methods for causal inference

## Randomised controlled trials (RCTs)

The gold standard method for inferring causality is randomisation - e.g. randomising patients to receive a treatment or not. This is because it removes confounding - it removes the common cause of the treatment and outcome, since the only cause of treatment was randomisation.

Randomisation makes treatment groups exchangeable. **Exchangeability** is when there are no confounders, so whatever treatment group each person was randomised too, we still would've seen the same outcomes in whichever were treated v.s. not, the groups are exchangeable.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

**Intention-to-treat analysis** is the preferred analysis strategy for RCTs. This means that the analysis includes all participants, all retained in the group to which they were allocated. However, this can be hard to achieve due to:
1. **Missing outcomes**
    * A "complete case" (or "available case") analysis only includes participants with no missing outcomes, and whilst only a few missing outcomes won't cause a problem, in half of trials more than 10% of randomised patients may have missing outcomes. Hence, exclusion will reduce the sample size, and may introduce bias if loss to follow-up is related to a patient's response to treatment.
    * Participants with missing outcomes can be included if their outcomes are imputed - but this requires strong assumptions. Common example is to use "last observation carried forward", but this may introduce bias and makes no allowance for uncertainty imputation.
2. **Non-adherence to protocol**
    * Examples include participants who didn't meet inclusion criteria (e.g. wrong diagnosis, too young), did not take all of the intended treatment, received a different treatment, or received no treatment
    * Intention-to-treat analysis ignores protocol deviations, including participants in their assigned groups regardless. Modified intention-to-treat (or 'per protocol analysis') is an analysis that excludes participants who didn't adequately adhere (e.g. minimum amount of intervention) - but this would need to be labelled as a non-randomised, observational comparison, and be aware that the exclusion of patients compromises randomisation.[[CONSORT]](https://www.bmj.com/content/340/bmj.c869)

These two problems can introduce **non-random selection effects** - i.e. randomisation isn't the only cause for treatment - hence introducing confounding (bias), and meaning that exchangeability would no longer holder - and hence why intention-to-treat is recommended (i.e. ignore protocol deviations).

The **Complier-Average Causal Effect (CACE) estimate** is the comparison of the average outcome of the compliers in the treatment arm compared with the average outcome of the comparable group of would-be compliers in the control arm. It is the intention-to-treat effect in the sub-group of participants who would always have complied with their treatment allocation, and is not subject to confounding.[[source]](https://hummedia.manchester.ac.uk/institutes/methods-manchester/docs/CausalInference.pdf)

## Stratification

Principal stratification was proposed by Frangakis and Rubin 2002.[[source]](https://doi.org/10.1111/j.0006-341X.2002.00021.x)

Stratification involves either:
* Restricting analysis to subset of study population with particular value of confounder, or
* Performing analysis in each stratum of confounder, then pooling effect estimates

This is represented by drawing box on DAG.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

It has typically been implemented in four different ways:
* Principal stratification as a partition of units by response type
* Principal stratification as an approximation to research questions concerning population averages (e.g. bounds and LATE analysis under non-compliance)
* Principal stratification as a genuine focus of a research question (e.g. censorship by death)
* Principal stratification as an intellectual restriction that confines its analysis to the assessment of strata-specific effects[[Pearl 2011]](https://ftp.cs.ucla.edu/pub/stat_ser/r382.pdf)

# ROUGH NOTES...

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

**Matching** - e.g. matching each person with treatment and confounder, with someone with treatment and not confounder, and with someone who did not have treatment or confounder. Analysis is restricted to matched people. As the treatment and no treatment groups are matched on confounder, if there is association, then not due to confounder, as adjusted for it. This can't be represented in DAG, because non-faithfulness - the association to a backdoor path is exactly cancelled by the matched subset.

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

## NOT suitable: Including all possible confounders

'Many analysts take the strategy of putting in **all possible confounders**. This can be bad news, because adjusting for **colliders and mediators can introduce bias**, as we’ll discuss shortly. Instead, we’ll look at **minimally sufficient adjustment sets**: sets of covariates that, when adjusted for, block all back-door paths, but include no more or no less than necessary. That means there can be many minimally sufficient sets, and if you remove even one variable from a given set, a back-door path will open.'[[source]](https://cran.r-project.org/web/packages/ggdag/vignettes/intro-to-dags.html)