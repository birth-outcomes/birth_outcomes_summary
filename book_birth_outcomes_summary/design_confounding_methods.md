# Methods to deal with confounding

<mark>Will need to integrate with the page on methods to account for treatment paradox</mark>

ROUGH NOTES...

## Randomisation

Randomise to receive treatment - removes common cause of treatment and outcome.

This is best method.

Although even in randomised trial, we can't randomise whether people adhere to their assigned treatment.

Randomisation makes groups exchangeable. **Exchangeability** is when there are no confounders, so whatever treatment group each person was randomised too, we still would've seen the same outcomes in whichever were treated v.s. not, the groups are exchangeable. You can also express exchangeability in the language of counterfactuals.
* In the RCT, 11% die in treatment group and 1% die in treatment group
* So in each group, the average counterfactual outcome under treatment is 0.11 and under no treatment is 0.01 - so, the distribution of the counterfactual outcomes (Y under treatment and Y under no treatment) is the same in the treated and untreated group - so the counterfactual outcomes are independent of the actual treatment

## Methods to block back door paths

**Stratification** - e.g. restrict analysis to subset of study population with particular value of confounder - or do analysis in each stratum of confounder, and then pool the effect estimates - and most sophisticated way of doing is regression analysis. This is represented by drawing box on DAG.

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
