# Methods #3: G-methods

`````{admonition} Executive summary
:class: info

G-methods:
* G-computation 
* Marginal structure models
* G-estimation

`````

## G-methods

G-methods are a family of methods that address intermediate confounding, or treatment-confounder feedback, which is when a confounder is affected by prior exposure status. They do so by taking the by 'taking the observed distribution of intermediate confounders (in the population as well as over time) into account, instead of holding them constant; in other words, they estimate marginal effects rather than conditional effects'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## G-computation 

'**G-computation** (or the parametric G-formula)  uses a statistical model (eg, a regression model) to predict the potential outcomes (with and without exposure) for each individual observation. This makes it possible to calculate treatment effects in a straightforward way, but relies on the statistical model being correctly specified.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Marginal structure models

'**Marginal structural models** aim to make the exposed and unexposed groups exchangeable in terms of confounders by weighting each observation (commonly using inverse probability of treatment weighting) so that the distribution of confounders is similar in both groups. An ATE can then be calculated by a simple comparison or unadjusted regression model.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## G-estimation

'**G-estimation** (using structural nested mean models) predicts the counterfactual outcome at each time point given no exposure from that point onwards, conditional on prior values of the exposure and confounders.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
