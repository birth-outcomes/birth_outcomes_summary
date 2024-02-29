# Causal assumptions and estimands

## Causal assumptions

'Causal effects are impossible to measure directly, since they involve comparing unobserved counterfactual outcomes that would have happened under different circumstances. A causal effect is identifiable if it can be **estimated** using observable data, given certain **assumptions** about the data and the underlying causal relationships. Such identifying assumptions typically cannot be fully tested statistically but have to be justified based on theory and/or existing evidence about the real-world processes under study'.[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

These assumptions include:
* Exchangeability assumption
* Stable Unit Treatment Value Assumption (SUTVA), which combines
    * Non-interference assumption
    * Consistency assumption
* Positivity assumption
* Ignorability assumption

### Exchangeability assumption

'The **exchangeability** (or "no confounding") assumption requires that individuals who were exposed and unexposed have the same potential outcomes on average. This allows the observed outcomes in an unexposed group to be used as a proxy for the counterfactual (unobservable) outcomes in an exposed group. RCTs strive to achieve exchangeability by randomly assigning the exposure, while observational studies often rely on achieving conditional exchangeability (or ‘no unmeasured confounding’), which means that exchangeability holds after conditioning on some set of variables'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

### Stable Unit Treatment Value Assumption (SUTVA)

**SUTVA** is composed of two assumptions.

**(1) No interference between units** (or "**non-interference assumption**"). This assumption requires that an individuals potential outcomes do 'not depend on the exposure status of anyone else. This assumption can be violated by ‘spillover effects’ of some exposures (eg, **vaccination**), where an individual’s outcomes are affected by the exposure status of those around them. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

**(2) There is only one version of treatment** (or "**consistency assumption**").  This is also referred to as "no multiple versions of treatment" or "no hidden treatments". This means that you do not have a scenario where each treatment condition has more than one version, and thus each unit may have more than one potential outcome per treatment condition. Hence, to satisfy, you need to:
* Define each version as treatment, or
* Restrict treatments to a subset of versions, or
* Randomise versions and take average across versions, or
* Redefine causal effect, acknowledgeing that estimated effect is conditional on an unknown distribution of versions. [[Kimmell et al. 2021]](https://doi.org/10.1016/j.tree.2021.08.008)

In practice, it can be impossible to achieve perfect consistency, and so the focus is instead on whether these differences are small enough for the averaged estimate to be meaningful.[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

### Positivity assumption

**Positivity** means that, **for every set of values for X, treatment assignment was not deterministic**. If, for some values of X, treatment was deterministic, then **we would have no observed values of Y** for one of the treatment groups for those values of X. [[Coursera]](https://www.coursera.org/learn/crash-course-in-causality/lecture/f5LPB/causal-assumptions)

'When conditioning on other variables, positivity needs to hold for each combination of covariates. This means that for every combination of covariates, it is possible to be either exposed or unexposed. The combination of covariates where this assumption holds can be called the ‘**region of common support**’.'

Violations can be either:
* **Structural positivity violation** - if some combinations are impossible (eg, if a treatment is never prescribed when a particular contraindication is present)
* **Random positivity violation** - if combination is possible but is missing from the study sample by chance. The term ‘positivity’ may refer to both of these or only to structural positivity; the latter is usually more relevant in theoretical causal inference literature.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

### Ignorability assumption

**Ignorability** means that, given pre-treatment covariates X, treatment assignment is independent from the potential outcomes - i.e. **among people with the same values of X, we can think of treatment A being randomly assigned**. This is sometimes referred to as the 'no unmeasured confounders' assumption.

Example: Older people more likely to have treatment, and more likely to have outcome (hip fracture), so treatment assignment is not marginally independent from outcome - BUT within levels of age, treatment might be randomly assigned. [[Coursera]](https://www.coursera.org/learn/crash-course-in-causality/lecture/f5LPB/causal-assumptions)

## Causal effect estimands

'The size of a causal effect is the difference in the potential outcomes for a particular population given different counterfactual scenarios (eg, one where everyone is exposed vs one where everyone is unexposed). As with potential outcomes, causal effects cannot be observed at an individual level, so we rely instead on estimating average effects in groups of people. The outcome may be the mean of a continuous variable or the risk of a binary outcome. The scale of an effect measure can be either additive or multiplicative'... [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

| Causal effect measure | Outcome type | Scale |Example |
| --- | --- | --- | --- |
| **Causal mean difference** | Continuous | Additive | 'An average increase in systolic blood pressure by 10 mmHg' |
| **Causal mean ratio** | Continuous | Multiplicative | 'An average increase in systolic blood pressure by a factor of 1.1' or 'by 10%' |
| **Causal risk difference** | Binary | Additive | 'An average increase in the risk of stroke by 5%' |
| **Causal risk ratio** | Binary | Multiplicative | 'An average increase in the risk of stroke by a factor of 1.5'

[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

Depending on how the exposure if defined and what population is considered, 'several causal treatment effects can be distinguished'. It is important to specify which effect you are trying to estimate (i.e. **the causal estimand**), since these effects 'can differ substantially in terms of effect size, risk of bias, and interpretation'.[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

Possible causal treatment effects include:

| Causal treatment effect | Definition |
| --- | --- |
| **Average treatment effect (ATE)** | Difference between average outcome, when EVERYONE is exposed v.s. when NO-ONE is exposed |
| **Average treatment effect in the treated (ATT)** | ATE calculated only in sub-population of individuals who were actually exposed |
| **Average treatment effect in the untreated (ATU/ATUT)** | ATE calculated only in sub-population of individuals who were actually unexposed |
| **Intention-to-treat effect (ITT)** | Average effect of being assigned to (but not necessarilly receiving) the exposure |
| **Complier average causal effect (CACE) or local average treatment effect** | ATE calculated only among 'compliers' |

[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

It can be challenging to identify the appropriate causal estimand. However, specifying a **target trial** (i.e. hypothetical RCT you are trying to emulate), can help with figuring this out. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
