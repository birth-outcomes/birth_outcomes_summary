# Causal estimands

`````{admonition} Executive summary
:class: info

Possible causal effect measures:
* Causal mean difference
* Causal mean ratio
* Causal risk difference
* Causal risk ratio

Possible causal effects - i.e. causal estimand - choice of which can be guided by thinking of target trial you are trying to emulate:
* Average treatment effect (ATE)
* Average treatment effect in the treated (ATT)
* Average treatment effect in the untreated (ATU/ATUT)
* Intention-to-treat effect (ITT)
* Complier average causal effect (CACE) or local average treatment effect

`````

## Causal effect estimands

'The size of a causal effect is the difference in the potential outcomes for a particular population given different counterfactual scenarios (eg, one where everyone is exposed vs one where everyone is unexposed). As with potential outcomes, causal effects cannot be observed at an individual level, so we rely instead on estimating average effects in groups of people. The outcome may be the mean of a continuous variable or the risk of a binary outcome. The scale of an effect measure can be either additive or multiplicative'... [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

| Causal effect measure | Outcome type | Scale |Example |
| --- | --- | --- | --- |
| **Causal mean difference** | Continuous | Additive | 'An average increase in systolic blood pressure by 10 mmHg' |
| **Causal mean ratio** | Continuous | Multiplicative | 'An average increase in systolic blood pressure by a factor of 1.1' or 'by 10%' |
| **Causal risk difference** | Binary | Additive | 'An average increase in the risk of stroke by 5%' |
| **Causal risk ratio** | Binary | Multiplicative | 'An average increase in the risk of stroke by a factor of 1.5'

[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

Depending on how the exposure if defined and what population is considered, 'several causal treatment effects can be distinguished'. It is important to specify which effect you are trying to estimate (i.e. **the causal estimand**), since these effects 'can differ substantially in terms of effect size, risk of bias, and interpretation'.

It can be challenging to identify the appropriate causal estimand. However, specifying a **target trial** (i.e. hypothetical RCT you are trying to emulate), can help with figuring this out. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

Possible causal treatment effects include:

| Causal treatment effect | Definition |
| --- | --- |
| **Average treatment effect (ATE)** | Difference between average outcome, when EVERYONE is exposed v.s. when NO-ONE is exposed |
| **Average treatment effect in the treated (ATT)** | ATE calculated only in sub-population of individuals who were actually exposed |
| **Average treatment effect in the untreated (ATU/ATUT)** | ATE calculated only in sub-population of individuals who were actually unexposed |
| **Intention-to-treat effect (ITT)** | Average effect of being assigned to (but not necessarilly receiving) the exposure |
| **Complier average causal effect (CACE) or local average treatment effect** | ATE calculated only among 'compliers' |

[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Intention-to-treat

**Intention-to-treat analysis** is the preferred analysis strategy for RCTs. This means that the analysis includes all participants, all retained in the group to which they were allocated.

However, this can be hard to achieve due to:
1. **Missing outcomes**
    * A "complete case" (or "available case") analysis only includes participants with no missing outcomes, and whilst only a few missing outcomes won't cause a problem, in half of trials more than 10% of randomised patients may have missing outcomes. Hence, exclusion will reduce the sample size, and may introduce bias if loss to follow-up is related to a patient's response to treatment.
    * Participants with missing outcomes can be included if their outcomes are imputed - but this requires strong assumptions. Common example is to use "last observation carried forward", but this may introduce bias and makes no allowance for uncertainty imputation.
2. **Non-adherence to protocol**
    * Examples include participants who didn't meet inclusion criteria (e.g. wrong diagnosis, too young), did not take all of the intended treatment, received a different treatment, or received no treatment
    * Intention-to-treat analysis ignores protocol deviations, including participants in their assigned groups regardless. Modified intention-to-treat (or 'per protocol analysis') is an analysis that excludes participants who didn't adequately adhere (e.g. minimum amount of intervention) - but this would need to be labelled as a non-randomised, observational comparison, and be aware that the exclusion of patients compromises randomisation.[[CONSORT]](https://www.bmj.com/content/340/bmj.c869)

These two problems can introduce **non-random selection effects** - i.e. randomisation isn't the only cause for treatment - hence introducing confounding (bias), and meaning that exchangeability would no longer holder - and hence why intention-to-treat is recommended (i.e. ignore protocol deviations).

The **Complier-Average Causal Effect (CACE) estimate** is the comparison of the average outcome of the compliers in the treatment arm compared with the average outcome of the comparable group of would-be compliers in the control arm. It is the intention-to-treat effect in the sub-group of participants who would always have complied with their treatment allocation, and is not subject to confounding.[[source]](https://hummedia.manchester.ac.uk/institutes/methods-manchester/docs/CausalInference.pdf)