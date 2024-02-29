# Causal assumptions and estimands

# Causal assumptions

https://www.coursera.org/learn/crash-course-in-causality/lecture/f5LPB/causal-assumptions

Identifiability of causal effects requires making some untestable assupmtions - these are generally called causal assumptions. The most common are:
* Stable Unit Treatment Value Assumption (SUTVA)
* Consistency
* Ignorability
* Positivity

SUTVA involves two assumptions:
1. No interference - units do not interfere with each other... treatment assignment of one unit does not affect the outcome of another unit. Interference may also be called spillover or contagion.
2. One version of treatment

Consistency: The hypothetical/potential outcome under treatment is equal to the observed outcome of the actual treatment

Ignorability: Given pre-treatment covariates X, treatment assignment is independent from the potential outcomes - i.e. among people with the same values of X, we can think of treatment A being randomly assigned. This is sometimes referred to as the 'no unmeasured confounders' assumption.
* Example: Older people more likely to have treatment, and more likely to have outcome (hip fracture), so treatment assignment is not marginally independent from outcome - BUT within levels of age, treatment might be randomly assigned

Positivity: For every set of values for X, treatment assignment was not deterministic. If, for some values of X, treatment was deterministic, then we would have no observed values of Y for one of the treatment groups for those values of X.
* Variability in treatment assignment is important for identification

We can put these assumptions together to identify causal effects

## Causal effect estimands

https://baselbiometrics.github.io/home/docs/trainings/20210202/1_Moffa.pdf

Measures of causal effect - causal estimands

Dichotomous outcomes

The causal null hypothesis may be expressed in terms of:
* Causal risk difference
* Causal risk ratio
* Causal odds ratio

One way of expressing is with respect to outcome expected value. Average causal effect. In the presence of a causal effect, causal parameters will differ from the values characterising the causal null hypothesis, in a measure which quantifies the strength of the causal effect on different scales.

More generally, we may also define a causal effect in different sub-groups, e.g. within a sub-population with a certain level of covariate, or sub-population identified by the treated group.

https://www.coursera.org/learn/crash-course-in-causality/lecture/Qt0ic/causal-effects

Causal relative risk

Causal effect of treatment on the treated

Average causal effect in the subpopulation with the covariate
