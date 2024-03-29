# Counterfactuals

`````{admonition} Executive summary
:class: info

The potential outcomes (or counterfactual) framework for causal inference states that we draw causal inference thought contrasting actual values and counterfactual values (if they had or had not received treatment/exposure). It is focused on all possible outcomes, and has specific notation you can use.

`````

## Introduction to the potential outcomes framework

To **define a causal effect**, we use the **potential outcomes framework** (also known as counterfactural or equivalent concepts approach[[source]](https://www.coursera.org/learn/crash-course-in-causality/lecture/Lgb6O/hypothetical-interventions) or Rubin or Neyman-Rubin causal model). This framework 'uses **mathematical notation** to describe **counterfactual outcomes** and can be used to describe the causal effect of an exposure on an outcome in statistical terms'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

This framework entails that:
* You can draw causal inferences when the distribution of observed outcomes in treated group equals in expectation the distribution if they had not ben treated - and because no-one can both receive and not receive treatment, 'causal inferences implicitly contrast actual values with counterfactual values'.
* Relating to older terminology, you can say that 'when exchangeability between those receiving and not receiving an intervention is obtained, the causal counterfactual can be estimated. When exchangeability (i.e., no confounding) is achieved, the contrast of actual outcomes among people who received the intervention in comparison with those who did not receive the intervention can provide the causal effect of the intervention' [[Glymour and Spiegelman 2017]](https://doi.org/10.2105%2FAJPH.2016.303539)

## Key terms

Some key terms in the potential outcomes framework:
* **Counterfactuals** are a comparison between what is and what might have been (e.g. treatment v.s. no treatment).
  * *For example, I know ingesting the poison killed John, because if John hadn't ingested the poison, I know he would have lived.* [No source]
  * 'The counterfactual outcomes of a specific individual can never be known, since we can never observe the same individual both exposed and unexposed under the same circumstances' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
* **Exposure (A)** = 'treatment, intervention or other variable that could have taken one of several counterfactual values'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
  * We are often focussed on **interventions** (i.e. variables that can be manipulated), as they fit well in the potential outcomes framework. Although other variables like age, race and gender can have causal effects, they do not fit as cleanly in the potential outcomes framework.[[source]](https://www.coursera.org/learn/crash-course-in-causality/lecture/Lgb6O/hypothetical-interventions) Rubin states that *"if you are not talking about an intervention, you can't talk about causality"* - i.e. we're defining causality using counterfactuals, which is about the counterfactual effects of the intervention[[source]](https://baselbiometrics.github.io/home/docs/trainings/20210202/1_Moffa.pdf)
* **Outcome (Y)**

## All possible outcomes for a binary exposure and outcome

'Potential outcomes refer to **all possible outcomes** that an individual could experience—both those which are observed (factual) and those which are not (counterfactual). Given a binary exposure and a binary outcome, the possible combinations of actual and counterfactual outcomes give rise to four causal types':
* '**‘Doomed’**: would have experienced the outcome regardless of exposure.'
* '**‘Causative’**: would have experienced the outcome if exposed, otherwise not.'
* '**‘Preventative’**: would have experienced the outcome if unexposed, otherwise not.'
* '**‘Immune’**: would not have experienced the outcome regardless of exposure status.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Notation
There are various notations used, but some examples are:
* Potential outcome if exposed (Y<sup>a=1</sup>) or not exposed (Y<sup>a=0</sup>)
* Expected value of continuous outcome (E(Y)) or probability of binary outcome(P(Y=1))
* Conditional expectation - expected value of Y given that another variable C is 1 (E(Y|C=1)) - i.e. expected values conditional on C / within levels of C / holding C constant. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
