# Methods #4: Methods for unobserved confounding

`````{admonition} Executive summary
:class: info

Addressing unobserved confounding:
* Instrumental variables
* Regression discontinuity (RD)
* Interrupted time series (ITS)
* Difference in differences (DiD)
`````

## Addressing unobserved confounding

'The above methods rely on an assumption of no unmeasured confounding (ie, conditional exchangeability), which is often not plausible in observational study designs. The following methods attempt to address unmeasured confounding, subject to certain unprovable assumptions, by exploiting some assignment mechanism (akin to randomisation in an RCT) that determines exposure status but is thought to be unrelated to any unobserved confounders.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Instrumental variables

<mark>read this</mark> https://dimewiki.worldbank.org/Instrumental_Variables

An **intrumental variable (IV)** is a variable that **causes some variation in the exposure** that is **unrelated to the outcome**, except through the exposure.

Example: 'If a treatment is only performed at certain hospitals, a patient's distance from such a hospital may affect the probability that they receive this treatment (but doesn't affect whether they had the condition), and this distance can be used as an instrument'.

'**Mendelian randomisation** uses IV analysis with genetic variants as instruments. IV analysis estimates a local average treatment effect (LATE) among 'compliers' - indivudals whose exposure status is affected by the instrument. This group cannot be precisely identified, and the LATE may therefore sometimes be of limited practical or policy relevance'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Regression discontinuity (RD)

<mark>read this</mark> https://dimewiki.worldbank.org/Regression_Discontinuity

'RD methods can be used when the **exposure status** (wholly or partly) is determined by some **continuous variable exceeding some arbitrary threshold** (called the forcing variable).'

'If the relationship between the forcing variable and the outcome is otherwise continuous, any discontinuity or jump in the relationship can be attributed to the exposure.'

'RD estimates a LATE among the individuals who fall just above or just below the threshold. As with
IV analysis, bias can occur if the forcing variable is connected
to the outcome through a back-door path or any other pathway
besides the exposure.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Interrupted time series (ITS)

'ITS studies compare the **trend over time in a population-level outcome before and after an exposure** is introduced. Assuming that the trend would have been unchanged if the intervention was not introduced, a change in trend at the point of introduction (in terms of level and/or slope) can be attributed to the exposure.'

'ITS can be regarded as a special case of IV or RD, with time being the instrument or forcing variable. ITS addresses time-invariant confounding but can be biased if other events that influence the outcome happen at the same time as the exposure'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Difference in differences (DiD)

'DiD studies measure the **change in a population-level outcome before and after an intervention** is introduced, compared with a **comparison group where the intervention is never introduced**. This is similar to RD and ITS, but attempts to control for changing time trends, by using a comparison group to represent the counterfactual outcome trend in the exposed.'

'DiD also addresses time-invariant confounding but requires assuming that there would have been no difference in trend between the groups in the absence of the intervention (the ‘parallel trends’ assumption).' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)